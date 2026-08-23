#!/usr/bin/env python3
"""Public documentation guard: relative links and high-risk secret patterns."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
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
}


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
    return errors


def main() -> int:
    errors: list[str] = []
    files = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    )
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: possible {name}")
        if path.suffix.lower() == ".md":
            errors.extend(relative_link_errors(path, text))

    if errors:
        print("Documentation audit failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Documentation audit passed for {len(files)} public files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
