#!/usr/bin/env python3
"""Validate the native-adapter handbook and generate an unclaimed test matrix.

The public architecture checkout does not contain the private product source.
Pass --source-root locally to compare the captured source snapshot and paths.
CI still checks the snapshot, documentation metadata and generated matrix for
internal contradictions; it cannot assert that a different repository moved.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "docs/architecture/native-source-snapshot.json"
INVENTORY_PATH = ROOT / "docs/architecture/native-adapter-inventory.json"
MATRIX_PATH = ROOT / "docs/quality/native-platform-certification-matrix.csv"
CAPABILITY_FIELDS = (
    "id", "operation", "app", "dart", "ios", "android", "callback", "api",
    "scope", "permission", "journal", "recovery", "diagnostic", "tests",
    "status", "evidence",
)
MATRIX_COLUMNS = (
    "capability", "platform", "lifecycle", "provider_environment",
    "signed_artifact", "status", "evidence", "reason",
)
LIFECYCLES = ("foreground", "background", "terminated", "reinstall")
INDEX_LINKS = {
    "README.md": ("docs/architecture/native-platform-handbook.md",),
    "docs/architecture/README.md": (
        "native-platform-handbook.md",
        "native-os-integrations.md",
        "google-play-billing-native-adapter.md",
    ),
    "docs/runbooks/README.md": (
        "native-device-integrations.md",
        "google-play-billing-recovery.md",
    ),
    "docs/quality/README.md": ("native-platform-certification-matrix.md",),
}


def source_version(path: Path) -> str:
    match = re.search(r"(?m)^version:\s*(\S+)", path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"missing Flutter version: {path}")
    return match.group(1)


def source_schema_version(path: Path) -> str:
    match = re.search(
        r'CurrentVersion\s*=\s*"([^"]+)"', path.read_text(encoding="utf-8")
    )
    if not match:
        raise ValueError(f"missing schema contract: {path}")
    return match.group(1)


def matrix_text(inventory: dict) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=MATRIX_COLUMNS, lineterminator="\n")
    writer.writeheader()
    for item in inventory["capabilities"]:
        for platform in ("ios", "android"):
            if item[platform].lower().startswith("not applicable"):
                continue
            provider_environments = (
                ("sandbox", "production")
                if item["id"] in {"apple-storekit", "google-play-billing"}
                else ("test-or-staging", "production")
                if item["id"] in {"push-registration-and-presentation", "trip-rtc-and-native-call"}
                else ("not-applicable",)
            )
            for lifecycle in LIFECYCLES:
                for provider_environment in provider_environments:
                    writer.writerow(
                        {
                            "capability": item["id"],
                            "platform": platform,
                            "lifecycle": lifecycle,
                            "provider_environment": provider_environment,
                            "signed_artifact": "not recorded for current source snapshot",
                            "status": "untested",
                            "evidence": "../current-baseline.md",
                            "reason": "This documentation pass did not execute an exact signed artifact/provider scenario.",
                        }
                    )
    return output.getvalue()


def validate(source_root: Path | None, write: bool) -> list[str]:
    errors: list[str] = []
    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    if inventory.get("sourceSnapshot") != SNAPSHOT_PATH.name:
        errors.append("inventory source snapshot link differs from owned snapshot")
    if not re.fullmatch(r"[0-9a-f]{40}", snapshot["productSourceRevision"]):
        errors.append("product source revision is not a full Git commit")
    if not re.fullmatch(r"[0-9a-f]{64}", snapshot["privateOpenApiSha256"]):
        errors.append("private OpenAPI hash is malformed")
    ids: set[str] = set()
    for index, item in enumerate(inventory["capabilities"]):
        missing = [field for field in CAPABILITY_FIELDS if not str(item.get(field, "")).strip()]
        if missing:
            errors.append(f"inventory row {index} missing: {', '.join(missing)}")
            continue
        if item["id"] in ids:
            errors.append(f"duplicate capability: {item['id']}")
        ids.add(item["id"])
        if "certified" in item["status"].lower() and "uncertified" not in item["status"].lower():
            errors.append(f"inventory row {item['id']} claims certification without exact artifact")
        if not (ROOT / "docs/architecture" / item["evidence"].split("/")[-1]).exists():
            errors.append(f"inventory row {item['id']} has missing architecture evidence")
        if source_root:
            for field in ("dart", "tests"):
                for raw_path in item[field].split(";"):
                    path = raw_path.strip()
                    if path.startswith(("src/", "tests/")) and not (source_root / path).exists():
                        errors.append(f"{item['id']}: {field} path missing in product source: {path}")

    baseline = (ROOT / "docs/current-baseline.md").read_text(encoding="utf-8")
    for key in ("consumerVersion", "systemAdminVersion", "schemaContract", "productSourceRevision"):
        if snapshot[key] not in baseline:
            errors.append(f"current baseline does not contain source-derived {key}")
    for page in (
        "docs/architecture/native-platform-handbook.md",
        "docs/architecture/native-os-integrations.md",
        "docs/architecture/google-play-billing-native-adapter.md",
        "docs/quality/native-platform-certification-matrix.md",
    ):
        text = (ROOT / page).read_text(encoding="utf-8") if (ROOT / page).exists() else ""
        for label in ("Owner:", "Last verified:", "Environment:", "Evidence:"):
            if label not in text:
                errors.append(f"{page} missing {label}")

    for index, targets in INDEX_LINKS.items():
        text = (ROOT / index).read_text(encoding="utf-8")
        for target in targets:
            if f"]({target})" not in text:
                errors.append(f"{index} does not link native handbook page {target}")

    for page in (
        "docs/architecture/native-platform-handbook.md",
        "docs/architecture/native-os-integrations.md",
        "docs/architecture/google-play-billing-native-adapter.md",
        "docs/architecture/native-adapters-and-store-billing.md",
        "docs/architecture/notification-delivery-lifecycle.md",
        "docs/architecture/documents-media-voice.md",
        "docs/architecture/mobile-session-and-device-lifecycle.md",
    ):
        text = (ROOT / page).read_text(encoding="utf-8")
        for pattern in (
            r"(?i)push (?:delivery|acceptance) (?:proves|guarantees) (?:device|user) (?:receipt|delivery)",
            r"(?i)(?:storekit|play billing) (?:callback|purchase update) (?:grants|authorizes) (?:membership|entitlement)",
            r"(?i)(?:gps fix|map marker) (?:proves|authorizes) (?:arrival|trip completion)",
        ):
            if re.search(pattern, text):
                errors.append(f"{page} contains a contradictory authority claim: {pattern}")

    expected = matrix_text(inventory)
    if write:
        MATRIX_PATH.write_text(expected, encoding="utf-8", newline="")
    elif not MATRIX_PATH.exists() or MATRIX_PATH.read_text(encoding="utf-8") != expected:
        errors.append("native platform certification matrix drift; run native_handbook.py --write")

    if source_root:
        comparisons = {
            "consumerVersion": source_version(source_root / "src/client/mobile/pubspec.yaml"),
            "systemAdminVersion": source_version(source_root / "src/client/system_admin/pubspec.yaml"),
            "schemaContract": source_schema_version(
                source_root / "src/server/KiloDrive.Api/Data/SchemaContract.cs"
            ),
            "privateOpenApiSha256": hashlib.sha256(
                (source_root / "docs/contracts/openapi/kilodrive-v1.json").read_bytes()
            ).hexdigest(),
            "productSourceRevision": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=source_root, text=True
            ).strip(),
        }
        for key, value in comparisons.items():
            if snapshot[key] != value:
                errors.append(f"captured {key} differs from current product source")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--write", action="store_true", help="regenerate the unclaimed matrix")
    args = parser.parse_args()
    errors = validate(args.source_root, args.write)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Native handbook inventory, source snapshot and matrix: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
