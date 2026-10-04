"""Heading anchors shared by generated navigation and the repository link audit."""

import html
import re


def without_fences(text: str) -> str:
    result, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            result.append("")
        else:
            result.append(line if fence is None else "")
    return "\n".join(result)


def heading_id(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = html.unescape(re.sub(r"<[^>]*>", "", text)).lower()
    return re.sub(r"[^\w\s-]", "", text).replace(" ", "-")


def anchors(text: str) -> set[str]:
    result: set[str] = set()
    text = without_fences(text)
    for value in re.findall(r'\b(?:id|name)=[\"\x27]([^\"\x27]+)[\"\x27]', text):
        result.add(value)
    for match in re.finditer(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", text, re.M):
        base = heading_id(match[1])
        slug, suffix = base, 0
        while slug in result:
            suffix += 1
            slug = f"{base}-{suffix}"
        result.add(slug)
    return result
