#!/usr/bin/env python3
"""Public documentation guard for links, structure, and high-risk content.

The script deliberately uses only the Python standard library so contributors
can run the same checks locally and in GitHub Actions without installing a
documentation toolchain. It is a guardrail, not a substitute for technical and
security review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_ONE = re.compile(r"^#\s+\S", re.MULTILINE)
FENCE = re.compile(r"^\s*```", re.MULTILINE)
SECRET_PATTERNS = {
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "connection password": re.compile(
        r"(?i)(?:password|pwd)\s*=\s*[^<{$\s][^;\s]{5,}"
    ),
    "secret assignment": re.compile(
        r'(?i)"(?:secretaccesskey|clientsecret|apikey|authToken)"\s*:\s*"(?!<|\$\{|\{\{)[^\"]+"'
    ),
    "private IPv4": re.compile(
        r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b"
    ),
    "AWS account ARN": re.compile(r"arn:aws[a-z-]*:[^:\s]*:[^:\s]*:\d{12}:[^\s]+"),
    "AWS account ID": re.compile(r"(?<![\d-])\d{12}(?![\d-])"),
    "AWS instance ID": re.compile(r"\bi-[0-9a-f]{8,17}\b"),
    "presigned AWS URL": re.compile(r"(?i)[?&]X-Amz-(?:Credential|Signature)="),
    "bearer token": re.compile(r"(?i)\bAuthorization\s*:\s*Bearer\s+(?!<|\$\{|\{\{)[A-Za-z0-9._~+/=-]{20,}"),
}

REQUIRED_PATHS = (
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/README.md",
    "docs/further-reading.md",
    "docs/architecture/README.md",
    "docs/architecture/system-context.md",
    "docs/architecture/capability-status.md",
    "docs/architecture/runtime-boundaries-and-certification.md",
    "docs/architecture/tenancy-and-country-cells.md",
    "docs/architecture/entity-identification.md",
    "docs/architecture/geospatial.md",
    "docs/architecture/financial-systems.md",
    "docs/architecture/rider-driver-safety.md",
    "docs/architecture/jurisdictional-compliance.md",
    "docs/architecture/rental-marketplace.md",
    "docs/architecture/scaling-and-capacity.md",
    "docs/quality/README.md",
    "docs/quality/testing-and-verification.md",
    "docs/runbooks/README.md",
    "docs/runbooks/_template.md",
    "docs/runbooks/dispatching.md",
    "docs/runbooks/jwt-key-rotation.md",
    "docs/runbooks/schema-alignment.md",
    "docs/runbooks/wallet-reconciliation.md",
    "docs/adr/README.md",
    "docs/adr/000-template.md",
    "docs/adr/001-country-cell-sharding.md",
    "docs/adr/002-uuidv7-identifiers.md",
    "docs/adr/003-valkey-geospatial-state.md",
    "docs/adr/004-osrm-map-matching.md",
    "docs/adr/005-eventbridge-sqs-outbox.md",
    "docs/adr/006-private-object-storage.md",
    "docs/adr/007-asymmetric-jwt-signing.md",
    "docs/adr/008-double-entry-wallet-accounting.md",
    "docs/adr/009-mysql-scripts-not-ef-migrations.md",
    "docs/adr/010-flutter-feature-repositories.md",
    "docs/third-party/README.md",
    "docs/third-party/sbom.md",
    "docs/third-party/kilodrive-public-direct.cdx.json",
    "docs/third-party/kilodrive-public-direct.cdx.json.sha256",
)

RUNBOOK_METADATA_FIELDS = (
    "Owner",
    "Status",
    "Last exercised",
    "Related architecture",
)

LEGACY_TOP_LEVEL_DIRECTORIES = (
    "architecture",
    "aws",
    "database",
    "governance",
    "integrations",
    "runbooks",
    "security",
    "third-party",
)


def has_case_exact_path(path: Path) -> bool:
    """Return false when a link only works on a case-insensitive filesystem."""

    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return False
    cursor = ROOT
    for part in relative.parts:
        try:
            names = {child.name for child in cursor.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        cursor /= part
    return True


def relative_link_errors(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>\"")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = unquote(target.split("#", 1)[0])
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link target: {target}")
        elif not has_case_exact_path(resolved):
            errors.append(
                f"{path.relative_to(ROOT)}: link target case does not match disk: {target}"
            )
    return errors


def markdown_quality_errors(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(ROOT)
    if not text.strip():
        errors.append(f"{relative}: empty Markdown file")
        return errors
    if not HEADING_ONE.search(text):
        errors.append(f"{relative}: missing level-one title")
    if "\ufffd" in text:
        errors.append(f"{relative}: contains Unicode replacement character U+FFFD")
    if "\x00" in text:
        errors.append(f"{relative}: contains a NUL character")
    if len(FENCE.findall(text)) % 2:
        errors.append(f"{relative}: unclosed fenced code block")
    for number, line in enumerate(text.splitlines(), start=1):
        if line.rstrip() != line:
            errors.append(f"{relative}:{number}: trailing whitespace")
    return errors


def adr_errors(path: Path, text: str) -> list[str]:
    relative = path.relative_to(ROOT)
    if path.parent.name != "adr" or not re.match(r"\d{3}-.+\.md$", path.name):
        return []
    if path.name == "000-template.md":
        return []
    errors: list[str] = []
    for field in ("Status", "Date"):
        if not re.search(rf"^- \*\*{field}:\*\*\s+\S", text, re.MULTILINE):
            errors.append(f"{relative}: ADR is missing **{field}:** metadata")
    for heading in ("Context", "Decision", "Consequences", "Validation"):
        if not re.search(rf"^##\s+{re.escape(heading)}\b", text, re.MULTILINE):
            errors.append(f"{relative}: ADR is missing '{heading}' section")
    return errors


def runbook_errors(path: Path, text: str) -> list[str]:
    """Require ownership and exercise metadata on executable runbooks."""

    if path.parent.name != "runbooks" or path.name in {"README.md", "_template.md"}:
        return []
    relative = path.relative_to(ROOT)
    errors: list[str] = []
    for field in RUNBOOK_METADATA_FIELDS:
        if not re.search(rf"^- \*\*{re.escape(field)}:\*\*\s+\S", text, re.MULTILINE):
            errors.append(f"{relative}: runbook is missing **{field}:** metadata")
    return errors


def main() -> int:
    errors: list[str] = []
    for required in REQUIRED_PATHS:
        if not (ROOT / required).is_file():
            errors.append(f"missing required documentation file: {required}")
    for legacy in LEGACY_TOP_LEVEL_DIRECTORIES:
        if (ROOT / legacy).exists():
            errors.append(
                f"legacy top-level documentation directory remains: {legacy}/ "
                "(move it under docs/)"
            )
    files = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    )
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            if path.suffix.lower() in {".md", ".json", ".yml", ".yaml", ".py"}:
                errors.append(f"{path.relative_to(ROOT)}: is not valid UTF-8 text")
            continue
        for name, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: possible {name}")
        if path.suffix.lower() == ".md":
            errors.extend(relative_link_errors(path, text))
            errors.extend(markdown_quality_errors(path, text))
            errors.extend(adr_errors(path, text))
            errors.extend(runbook_errors(path, text))

    if errors:
        print("Documentation audit failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    markdown_files = [path for path in files if path.suffix.lower() == ".md"]
    word_count = sum(
        len(path.read_text(encoding="utf-8").split()) for path in markdown_files
    )
    print(
        "Documentation audit passed for "
        f"{len(files)} public files ({len(markdown_files)} Markdown, "
        f"approximately {word_count:,} words)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
