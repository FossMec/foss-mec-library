#!/usr/bin/env python3
"""Validate the FOSS MEC Library source before mdBook builds it.

Standard library only. Checks, with file and line numbers where possible:

1. Every chapter listed in src/SUMMARY.md exists.
2. Local Markdown, HTML and reference-style links resolve to real files.
3. Root-relative links ("/assets/...") are rejected: the book is served from
   https://fossmec.github.io/foss-mec-library/.
4. Files under src/assets/materials use an allowed extension.
5. No file under src/ exceeds the 10 MiB upload policy.
6. Every material file is linked from at least one Markdown page.
7. Published pages do not contain the example.org placeholder.

Usage:
    python3 scripts/validate_content.py
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SUMMARY = SRC / "SUMMARY.md"

MAX_BYTES = 10 * 1024 * 1024  # 10 MiB, below GitHub's 25 MiB browser limit
ALLOWED_MATERIAL_EXTENSIONS = {
    ".md",
    ".pdf",
    ".pptx",
    ".docx",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".svg",
}
DANGEROUS_EXTENSIONS = {
    ".exe",
    ".msi",
    ".dmg",
    ".apk",
    ".iso",
    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",
    ".tgz",
    ".bz2",
    ".xz",
    ".sh",
    ".bash",
    ".bat",
    ".cmd",
    ".ps1",
    ".py",
    ".js",
    ".jar",
    ".bin",
}

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
MD_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)"
)
HTML_ATTR_RE = re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
REF_DEF_RE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?(?:\s+[\"'(].*)?$")
REF_USE_RE = re.compile(r"\[([^\]]*)\]\[([^\]]*)\]")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

errors: list[str] = []
warnings: list[str] = []
checked_links = 0


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def error(path: Path, line: int | None, message: str) -> None:
    location = rel(path)
    if line is not None:
        location = f"{location}:{line}"
    errors.append(f"{location}: {message}")


def warn(path: Path, line: int | None, message: str) -> None:
    location = rel(path)
    if line is not None:
        location = f"{location}:{line}"
    warnings.append(f"{location}: {message}")


def iter_markdown_lines(path: Path):
    """Yield (line_number, line) outside fenced code blocks."""
    inside = False
    fence_char = ""
    fence_len = 0
    text = path.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if not inside:
                inside = True
                fence_char = marker[0]
                fence_len = len(marker)
                continue
            if marker[0] == fence_char and len(marker) >= fence_len:
                inside = False
                fence_char = ""
                fence_len = 0
                continue
        if not inside:
            yield number, line


def strip_inline_code(line: str) -> str:
    return INLINE_CODE_RE.sub("", line)


def is_external(target: str) -> bool:
    if target.startswith("//"):
        return True
    return bool(SCHEME_RE.match(target))


def check_target(source: Path, number: int, target: str) -> None:
    """Validate one local link target; external and fragment links are ignored."""
    global checked_links

    target = target.strip()
    if not target or target.startswith("#") or is_external(target):
        return
    if "{{" in target or "{%" in target or "<" in target or ">" in target:
        return

    checked_links += 1
    parsed = urllib.parse.urlsplit(target)
    path_part = parsed.path
    if not path_part:
        return

    decoded = urllib.parse.unquote(path_part)
    if decoded.startswith("/"):
        error(
            source,
            number,
            f"root-relative link '{target}' breaks on project Pages; "
            "use a path relative to this file",
        )
        return

    candidate = (source.parent / decoded).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        error(source, number, f"link '{target}' resolves outside the repository")
        return

    if candidate.is_dir():
        if (candidate / "README.md").exists() or (candidate / "index.html").exists():
            return
        error(source, number, f"link '{target}' points to a directory without README.md")
        return

    if not candidate.exists():
        error(source, number, f"broken local link '{target}' (resolved to {rel(candidate)})")


def check_page_links(path: Path) -> set[Path]:
    """Check all local links on a page and return resolved local files."""
    referenced: set[Path] = set()
    definitions: dict[str, str] = {}
    uses: list[tuple[int, str]] = []

    for number, raw_line in iter_markdown_lines(path):
        line = strip_inline_code(raw_line)

        if "example.org" in line:
            error(
                path,
                number,
                "published pages must not contain the example.org placeholder",
            )

        ref_def = REF_DEF_RE.match(line)
        if ref_def:
            definitions[ref_def.group(1).strip().lower()] = ref_def.group(2)

        for match in REF_USE_RE.finditer(line):
            label = (match.group(2) or match.group(1)).strip().lower()
            if label:
                uses.append((number, label))

        for match in MD_LINK_RE.finditer(line):
            target = match.group(1)
            check_target(path, number, target)
            if not is_external(target) and not target.startswith("#"):
                parsed = urllib.parse.urlsplit(target)
                if parsed.path:
                    candidate = (path.parent / urllib.parse.unquote(parsed.path)).resolve()
                    referenced.add(candidate)

        for match in HTML_ATTR_RE.finditer(line):
            target = match.group(1)
            check_target(path, number, target)
            if not is_external(target) and not target.startswith("#"):
                parsed = urllib.parse.urlsplit(target)
                if parsed.path:
                    candidate = (path.parent / urllib.parse.unquote(parsed.path)).resolve()
                    referenced.add(candidate)

    for number, label in uses:
        if label not in definitions:
            error(path, number, f"reference-style link label '[{label}]' has no definition")

    for label, target in definitions.items():
        check_target(path, None, target)

    return referenced


def check_summary() -> set[Path]:
    if not SUMMARY.exists():
        errors.append(f"{rel(SUMMARY)}: file is missing")
        return set()

    chapters: set[Path] = set()
    duplicates: dict[Path, int] = {}

    for number, raw_line in iter_markdown_lines(SUMMARY):
        line = strip_inline_code(raw_line)
        for match in MD_LINK_RE.finditer(line):
            target = match.group(1)
            if is_external(target):
                error(SUMMARY, number, f"summary entry must be a local chapter, not '{target}'")
                continue
            parsed = urllib.parse.urlsplit(target)
            path_part = urllib.parse.unquote(parsed.path)
            if not path_part:
                continue
            if not path_part.endswith(".md"):
                error(SUMMARY, number, f"summary entry '{target}' is not a Markdown chapter")
                continue
            candidate = (SRC / path_part).resolve()
            if not candidate.exists():
                error(SUMMARY, number, f"missing chapter '{target}' (create {rel(candidate)})")
                continue
            chapters.add(candidate)
            duplicates[candidate] = duplicates.get(candidate, 0) + 1

    for chapter, count in duplicates.items():
        if count > 1:
            warn(SUMMARY, None, f"chapter '{rel(chapter)}' is listed {count} times")

    return chapters


def check_markdown_pages() -> set[Path]:
    referenced: set[Path] = set()
    for path in sorted(SRC.rglob("*.md")):
        if "assets" in path.parts or path.name == "SUMMARY.md":
            continue
        referenced |= check_page_links(path)
    return referenced


def check_summary_coverage(chapters: set[Path]) -> None:
    for path in sorted(SRC.rglob("*.md")):
        if "assets" in path.parts or path.name in {"404.md", "SUMMARY.md"}:
            continue
        if path not in chapters:
            warn(path, None, "Markdown page is not listed in src/SUMMARY.md")


def check_files(referenced: set[Path]) -> None:
    for path in sorted(SRC.rglob("*")):
        if not path.is_file():
            continue

        size = path.stat().st_size
        if size > MAX_BYTES:
            error(
                path,
                None,
                f"file is {size / (1024 * 1024):.1f} MiB; policy limit is 10 MiB",
            )

        suffix = path.suffix.lower()
        in_materials = "materials" in path.parts

        if in_materials and suffix not in ALLOWED_MATERIAL_EXTENSIONS:
            error(
                path,
                None,
                f"disallowed material extension '{suffix or '(none)'}'; "
                f"allowed: {', '.join(sorted(ALLOWED_MATERIAL_EXTENSIONS))}",
            )

        if suffix in DANGEROUS_EXTENSIONS:
            error(path, None, f"dangerous or unsupported file type '{suffix}'")

        if in_materials and path.name != "README.md":
            if path.resolve() not in referenced:
                error(
                    path,
                    None,
                    "material file is not linked from any Markdown page; "
                    "add a listing with title, description, author and licence",
                )


def main() -> int:
    if not SRC.is_dir():
        print("error: src/ directory not found", file=sys.stderr)
        return 1

    chapters = check_summary()
    check_summary_coverage(chapters)
    referenced = check_markdown_pages()
    check_files(referenced)

    for message in warnings:
        print(f"warning: {message}")
    for message in errors:
        print(f"error: {message}")

    if errors:
        print(
            f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s), "
            f"{checked_links} local link(s) checked.",
            file=sys.stderr,
        )
        return 1

    print(
        f"OK: {len(chapters)} chapter(s), {len(warnings)} warning(s), "
        f"{checked_links} local link(s) checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
