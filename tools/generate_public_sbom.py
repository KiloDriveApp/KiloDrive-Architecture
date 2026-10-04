#!/usr/bin/env python3
"""Generate or verify KiloDrive's sanitized public direct-dependency SBOM.

The authoritative release SBOM is produced with signed artifacts and includes
transitive/native components. This public baseline intentionally contains only
reviewed direct/override package coordinates and no private repository, build-host, or
infrastructure metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACT = ROOT / "docs" / "third-party" / "kilodrive-public-direct.cdx.json"
DEFAULT_SIDECAR = DEFAULT_ARTIFACT.with_suffix(DEFAULT_ARTIFACT.suffix + ".sha256")
GENERATOR_VERSION = "1.1.0"
NAMESPACE = uuid.UUID("b86be7d7-d95e-5d65-bdce-e07ac860dfc7")
# Explicitly reviewed source-controlled forks; no arbitrary local paths or Git URLs.
REVIEWED_VENDORED_PACKAGES = {"flutter_callkit_incoming", "in_app_purchase_android", "riverpod"}


def reviewed_text(source_root: Path, relative: str) -> str:
    """Never attribute modified dependency metadata to the committed baseline."""
    committed = subprocess.check_output(["git", "show", f"HEAD:{relative}"], cwd=source_root).decode("utf-8-sig")
    working = (source_root / relative).read_text(encoding="utf-8-sig")
    if committed.replace("\r\n", "\n") != working.replace("\r\n", "\n"):
        raise ValueError(f"Dependency input differs from the source commit: {relative}")
    return committed.replace("\r\n", "\n")


def normalize_nuget_version(version: str) -> str:
    """Collapse an exact NuGet range such as [1.3.1] to its package version."""

    value = version.strip()
    exact = re.fullmatch(r"\[\s*([^,\[\]()]+?)\s*\]", value)
    return exact.group(1) if exact else value


def parse_dotnet(source_root: Path) -> list[dict[str, str]]:
    props_path = source_root / "Directory.Packages.props"
    if not props_path.is_file():
        raise ValueError("Directory.Packages.props was not found under source root")

    props = ET.fromstring(reviewed_text(source_root, "Directory.Packages.props"))
    versions = {
        node.attrib["Include"]: node.attrib["Version"]
        for node in props.findall(".//PackageVersion")
    }
    references: dict[str, set[str]] = {}
    tracked = subprocess.check_output(["git", "ls-files", "--", "*.csproj"], cwd=source_root, text=True).splitlines()
    for relative in tracked:
        if not relative.startswith(("src/", "tests/", "tools/")):
            continue
        try:
            root = ET.fromstring(reviewed_text(source_root, relative))
        except ET.ParseError as error:
            raise ValueError(f"cannot parse project metadata: {relative}") from error
        for node in root.findall(".//PackageReference"):
            if node.attrib.get("Version") or node.attrib.get("VersionOverride"):
                raise ValueError(f"Explicit package-version override needs review: {relative}")
            name = node.attrib.get("Include") or node.attrib.get("Update")
            if name:
                references.setdefault(name, set()).add(relative)

    components: list[dict[str, str]] = []
    for name, projects in sorted(references.items(), key=lambda item: item[0].lower()):
        version = versions.get(name)
        if not version:
            raise ValueError(f"direct NuGet package has no central version: {name}")
        version = normalize_nuget_version(version)
        test_only = all(path.lower().startswith("tests/") for path in projects)
        components.append(
            {
                "ecosystem": "nuget",
                "name": name,
                "version": version,
                "scope": "test" if test_only else "runtime",
                "owners": ",".join(sorted({"tests" if p.startswith("tests/") else "tools" if p.startswith("tools/") else "server" for p in projects})),
            }
        )
    return components


def parse_flutter(source_root: Path, app: str = "mobile") -> tuple[str, list[dict[str, str]]]:
    mobile = source_root / "src" / "client" / app
    lock_path = mobile / "pubspec.lock"
    pubspec_path = mobile / "pubspec.yaml"
    if not lock_path.is_file() or not pubspec_path.is_file():
        raise ValueError("Flutter pubspec.yaml/pubspec.lock was not found")

    version_match = re.search(
        r"^version:\s*([^\s#]+)", reviewed_text(source_root, pubspec_path.relative_to(source_root).as_posix()), re.MULTILINE
    )
    if not version_match:
        raise ValueError("Flutter application version is missing")

    text = reviewed_text(source_root, lock_path.relative_to(source_root).as_posix())
    package_blocks = re.finditer(
        r"(?ms)^  (?P<name>[a-zA-Z0-9_]+):\n(?P<body>.*?)(?=^  [a-zA-Z0-9_]+:\n|\Z)",
        text,
    )
    components: list[dict[str, str]] = []
    for match in package_blocks:
        body = match.group("body")
        dependency = re.search(r'^    dependency:\s*"?([^"\n]+)"?', body, re.MULTILINE)
        resolved = re.search(r'^    version:\s*"?([^"\n]+)"?', body, re.MULTILINE)
        source = re.search(r"^    source:\s*([^\n]+)", body, re.MULTILINE)
        if not dependency or not resolved:
            continue
        # Flutter SDK libraries carry a synthetic 0.0.0 package version and are
        # recorded as the pinned toolchain/framework in release evidence rather
        # than mislabelled as packages from pub.dev.
        if source and source.group(1).strip() == "sdk":
            continue
        dependency_kind = dependency.group(1).strip()
        if dependency_kind not in {"direct main", "direct dev", "direct overridden"}:
            continue
        origin = source.group(1).strip() if source else ""
        if origin == "path" and match.group("name") in REVIEWED_VENDORED_PACKAGES:
            expected_path = f"third_party/{match.group('name')}"
            declared = re.search(r'^      path:\s*"?([^"\n]+)"?', body, re.M)
            if not declared or declared[1].strip() != expected_path:
                raise ValueError("Vendored package location differs from the reviewed policy")
            reviewed_text(source_root, f"src/client/{app}/{expected_path}/pubspec.yaml")
            origin = "reviewed-source-fork"
        elif origin != "hosted":
            raise ValueError(f"Non-hosted direct package requires publication review: {match.group('name')}")
        components.append(
            {
                "ecosystem": "pub",
                "name": match.group("name"),
                "version": resolved.group(1).strip(),
                "scope": {"direct main": "runtime", "direct dev": "development", "direct overridden": "explicit-override"}[dependency_kind],
                "owners": "consumer" if app == "mobile" else "system-admin",
                "origin": origin,
                "declaration": dependency_kind,
            }
        )
    return version_match.group(1), sorted(components, key=lambda item: item["name"])


def component_record(item: dict[str, str]) -> dict[str, object]:
    ecosystem = item["ecosystem"]
    name = item["name"]
    version = item["version"]
    coordinate = "generic/kilodrive-vendored" if item.get("origin") == "reviewed-source-fork" else ecosystem
    purl = f"pkg:{coordinate}/{quote(name, safe='._-')}@{quote(version, safe='.+_-')}"
    return {
        "type": "library",
        "bom-ref": purl,
        "name": name,
        "version": version,
        "purl": purl,
        "properties": [
            {"name": "kilodrive:ecosystem", "value": ecosystem},
            {"name": "kilodrive:direct-scope", "value": item["scope"]},
            {"name": "kilodrive:owners", "value": item["owners"]},
            {"name": "kilodrive:origin", "value": item.get("origin", "registry")},
            {"name": "kilodrive:declaration", "value": item.get("declaration", "direct")},
            {"name": "kilodrive:license-status", "value": "review-in-release-evidence"},
        ],
    }


def build_bom(source_root: Path, timestamp: str) -> dict[str, object]:
    parsed_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    if parsed_time.tzinfo is None:
        raise ValueError("timestamp must include UTC offset or Z")
    timestamp_utc = parsed_time.astimezone(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )

    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source_root, text=True).strip()
    mobile_version, flutter = parse_flutter(source_root)
    admin_version, admin_flutter = parse_flutter(source_root, "system_admin")
    direct = merge_components(parse_dotnet(source_root) + flutter + admin_flutter)
    direct.sort(key=lambda item: (item["ecosystem"], item["name"].lower(), item["version"]))
    records = [component_record(item) for item in direct]
    identity = "\n".join(record["bom-ref"] for record in records)
    serial = uuid.uuid5(NAMESPACE, f"{commit}\n{mobile_version}\n{admin_version}\n{identity}")
    root_ref = f"pkg:generic/kilodrive-public-baseline@{quote(mobile_version, safe='.+_-')}"
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source_root, text=True).strip() != commit:
        raise ValueError("Source revision changed during SBOM generation")

    return {
        "$schema": "https://cyclonedx.org/schema/bom-1.6.schema.json",
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{serial}",
        "version": 1,
        "metadata": {
            "timestamp": timestamp_utc,
            "tools": {
                "components": [
                    {
                        "type": "application",
                        "name": "KiloDrive public SBOM generator",
                        "version": GENERATOR_VERSION,
                    }
                ]
            },
            "component": {
                "type": "application",
                "bom-ref": root_ref,
                "name": "KiloDrive public architecture baseline",
                "version": mobile_version,
                "properties": [
                    {"name": "kilodrive:inventory-depth", "value": "direct-and-explicit-overrides"},
                    {"name": "kilodrive:source-commit", "value": commit},
                    {"name": "kilodrive:consumer-version", "value": mobile_version},
                    {"name": "kilodrive:system-admin-version", "value": admin_version},
                    {"name": "kilodrive:distribution", "value": "sanitized-public-baseline"},
                    {
                        "name": "kilodrive:authoritative-release-sbom",
                        "value": "false",
                    },
                ],
            },
        },
        "components": records,
        "dependencies": [
            {"ref": root_ref, "dependsOn": [record["bom-ref"] for record in records]}
        ],
    }


def merge_components(items: list[dict[str, str]]) -> list[dict[str, str]]:
    """Deduplicate identical coordinates without hiding app-specific versions."""
    merged: dict[tuple, dict] = {}
    for item in items:
        key = (item["ecosystem"], item["name"], item["version"], item.get("origin", "registry"))
        if key not in merged:
            merged[key] = dict(item)
        else:
            for field in ("owners", "scope", "declaration"):
                if field not in item:
                    continue
                merged[key][field] = ",".join(sorted(set(merged[key][field].split(",")) | set(item[field].split(","))))
    return list(merged.values())


def canonical_bytes(bom: dict[str, object]) -> bytes:
    return (json.dumps(bom, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def write_artifact(bom: dict[str, object], artifact: Path, sidecar: Path) -> None:
    data = canonical_bytes(bom)
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    sidecar.write_text(f"{digest}  {artifact.name}\n", encoding="utf-8", newline="\n")
    (artifact.parent / "direct-packages.md").write_bytes(render_inventory(bom))


def render_inventory(bom: dict) -> bytes:
    metadata = bom["metadata"]
    root = {p["name"]: p["value"] for p in metadata["component"]["properties"]}
    lines = ["# Reviewed direct packages and explicit overrides", "", "[Dependency guide](README.md) · [SBOM scope](sbom.md)", "",
             f"Consumer **{root['kilodrive:consumer-version']}**; System Admin **{root['kilodrive:system-admin-version']}**.",
             f"Source commit: `{root['kilodrive:source-commit']}`.",
             f"Generated at `{metadata['timestamp']}` from committed dependency inputs.", "",
             "Each row is one package coordinate. Different versions or origins remain separate;",
             "owner labels show which source applications/projects directly select it. A reviewed",
             "source fork is not the unmodified upstream package. SDK, transitive and resolved",
             "native graphs remain outside this public baseline, as do release license/advisory decisions.", "",
             "| Package | Version | Ecosystem | Owners | Scope | Origin |", "| --- | --- | --- | --- | --- | --- |"]
    for item in bom["components"]:
        p = {v["name"]: v["value"] for v in item["properties"]}
        lines.append(f"| `{item['name']}` | `{item['version']}` | {p['kilodrive:ecosystem']} | {p['kilodrive:owners']} | {p['kilodrive:direct-scope']} | {p['kilodrive:origin']} |")
    lines.extend(["", "Generated from the [public CycloneDX artifact](kilodrive-public-direct.cdx.json).",
                  "Run the generator to update this table; CI rejects a stale table or checksum.", ""])
    return "\n".join(lines).encode("utf-8")


def validate_bom(bom: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if bom.get("bomFormat") != "CycloneDX" or bom.get("specVersion") != "1.6":
        errors.append("artifact must be CycloneDX 1.6")
    metadata = bom.get("metadata")
    if not isinstance(metadata, dict) or not isinstance(metadata.get("component"), dict):
        errors.append("artifact is missing root component metadata")
    else:
        properties = {p["name"]: p["value"] for p in metadata["component"].get("properties", [])}
        if not re.fullmatch(r"[0-9a-f]{40}", properties.get("kilodrive:source-commit", "")):
            errors.append("artifact must record its source commit")
        for key in ("consumer", "system-admin"):
            if not properties.get(f"kilodrive:{key}-version"):
                errors.append(f"artifact must record the {key} source version")
    components = bom.get("components")
    if not isinstance(components, list) or not components:
        errors.append("artifact has no components")
        return errors
    refs: set[str] = set()
    ecosystems: set[str] = set()
    owners: set[str] = set()
    for index, component in enumerate(components):
        if not isinstance(component, dict):
            errors.append(f"component {index} is not an object")
            continue
        for field in ("bom-ref", "name", "version", "purl"):
            if not isinstance(component.get(field), str) or not component[field]:
                errors.append(f"component {index} is missing {field}")
        ref = component.get("bom-ref")
        properties = {p["name"]: p["value"] for p in component.get("properties", [])}
        owners.update(properties.get("kilodrive:owners", "").split(","))
        if isinstance(ref, str):
            if ref in refs:
                errors.append(f"duplicate component reference: {ref}")
            refs.add(ref)
            if ref.startswith("pkg:nuget/"):
                ecosystems.add("nuget")
            if ref.startswith("pkg:pub/"):
                ecosystems.add("pub")
    if ecosystems != {"nuget", "pub"}:
        errors.append("public baseline must contain NuGet and Pub components")
    if not {"consumer", "system-admin", "server"}.issubset(owners):
        errors.append("public baseline must cover server, consumer and System Admin owners")
    root_ref = metadata.get("component", {}).get("bom-ref") if isinstance(metadata, dict) else None
    for dependency in bom.get("dependencies", []):
        if dependency.get("ref") not in refs | {root_ref}:
            errors.append("dependency graph contains an unknown parent")
        if set(dependency.get("dependsOn", [])) - refs:
            errors.append("dependency graph contains an unknown component")
    serialized = json.dumps(bom)
    forbidden = ("AKIA", "BEGIN PRIVATE KEY", "Password=", "SecretAccessKey")
    for value in forbidden:
        if value.lower() in serialized.lower():
            errors.append(f"artifact contains forbidden sensitive pattern: {value}")
    return errors


def verify_artifact(artifact: Path, sidecar: Path) -> list[str]:
    errors: list[str] = []
    if not artifact.is_file() or not sidecar.is_file():
        return ["SBOM artifact or SHA-256 sidecar is missing"]
    try:
        bom = json.loads(artifact.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        return [f"SBOM is not valid UTF-8 JSON: {error}"]
    errors.extend(validate_bom(bom))
    inventory = artifact.parent / "direct-packages.md"
    if not errors and (not inventory.exists() or inventory.read_bytes() != render_inventory(bom)):
        errors.append("human-readable dependency inventory is missing or stale")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    sidecar_parts = sidecar.read_text(encoding="utf-8").strip().split()
    if len(sidecar_parts) != 2 or sidecar_parts[0] != digest or sidecar_parts[1] != artifact.name:
        errors.append("SBOM SHA-256 sidecar does not match artifact")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--generate", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--timestamp", default=datetime.now(timezone.utc).isoformat())
    parser.add_argument("--artifact", type=Path, default=DEFAULT_ARTIFACT)
    parser.add_argument("--sidecar", type=Path, default=DEFAULT_SIDECAR)
    args = parser.parse_args()

    if args.generate:
        if args.source_root is None:
            parser.error("--generate requires --source-root")
        bom = build_bom(args.source_root.resolve(), args.timestamp)
        errors = validate_bom(bom)
        if errors:
            print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
            return 1
        write_artifact(bom, args.artifact, args.sidecar)

    errors = verify_artifact(args.artifact, args.sidecar)
    if errors:
        print("Public SBOM verification failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    bom = json.loads(args.artifact.read_text(encoding="utf-8"))
    print(
        f"Public CycloneDX baseline verified: {len(bom['components'])} direct/override components; "
        f"SHA-256 sidecar matches."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
