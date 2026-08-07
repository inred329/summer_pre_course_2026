#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

# Constitution 1.x references are intentionally retained only where an old review
# is explicitly historicalized, where the active audit records migration history,
# or where the governance index identifies an old review as historical.
FORMER_CONSTITUTION_ALLOWED = {
    Path("design/12-constitution-compliance-review.en.md"),
    Path("design/12-constitution-compliance-review.zh-TW.md"),
    Path("design/README.en.md"),
    Path("design/README.zh-TW.md"),
    Path("materials/reviews/materials-constitution-review.en.md"),
    Path("materials/reviews/materials-constitution-review.zh-TW.md"),
    Path("reviews/constitution-maturity-review.en.md"),
    Path("reviews/constitution-maturity-review.zh-TW.md"),
    Path("reviews/repository-constitution-2-audit.en.md"),
    Path("reviews/repository-constitution-2-audit.zh-TW.md"),
}

ENTRYPOINTS = {
    Path("README.md"),
    Path("CONSTITUTION.en.md"),
    Path("CONSTITUTION.zh-TW.md"),
    Path("design/README.en.md"),
    Path("design/README.zh-TW.md"),
    Path("materials/README.en.md"),
    Path("materials/README.zh-TW.md"),
    Path("materials/preparatory/README.en.md"),
    Path("materials/preparatory/README.zh-TW.md"),
    Path("materials/formal/README.en.md"),
    Path("materials/formal/README.zh-TW.md"),
    Path("examples/README.md"),
    Path("validation/README.md"),
}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
FORMER_CONSTITUTION_RE = re.compile(
    r"(?:Constitution|憲法)[^\n]{0,60}?\b1\.\d+(?:\.\d+)?\b",
    re.IGNORECASE,
)
VERSION_EN_RE = re.compile(r"^Version:\s*([^\s]+)", re.MULTILINE)
VERSION_ZH_RE = re.compile(r"^版本：\s*([^\s]+)", re.MULTILINE)


def relative(path: Path) -> Path:
    return path.relative_to(ROOT)


def markdown_files() -> list[Path]:
    ignored = {".git", ".github"}
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in ignored for part in path.relative_to(ROOT).parts)
    )


def strip_fenced_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def normalize_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if not target:
        return None

    if " \"" in target or " '" in target:
        target = target.split(" ", 1)[0]

    target = target.strip("<>")
    lower = target.lower()
    if lower.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None
    if target.startswith("#"):
        return None

    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not target:
        return None

    if target.startswith("/"):
        resolved = ROOT / target.lstrip("/")
    else:
        resolved = source.parent / target

    try:
        return resolved.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return Path("__OUTSIDE_REPOSITORY__") / target


def check_bilingual_pairs(files: list[Path]) -> list[str]:
    errors: list[str] = []
    rel_files = {relative(path) for path in files}

    for rel in sorted(rel_files):
        name = rel.name
        counterpart: Path | None = None
        if name.endswith(".en.md"):
            counterpart = rel.with_name(name[:-6] + ".zh-TW.md")
        elif name.endswith(".zh-TW.md"):
            counterpart = rel.with_name(name[:-9] + ".en.md")

        if counterpart is not None and counterpart not in rel_files:
            errors.append(f"missing bilingual counterpart: {rel} -> {counterpart}")

    checked: set[tuple[Path, Path]] = set()
    for rel in sorted(rel_files):
        if not rel.name.endswith(".en.md"):
            continue
        zh = rel.with_name(rel.name[:-6] + ".zh-TW.md")
        if zh not in rel_files:
            continue
        pair = (rel, zh)
        if pair in checked:
            continue
        checked.add(pair)

        en_text = (ROOT / rel).read_text(encoding="utf-8")
        zh_text = (ROOT / zh).read_text(encoding="utf-8")
        en_version = VERSION_EN_RE.search(en_text)
        zh_version = VERSION_ZH_RE.search(zh_text)
        if bool(en_version) != bool(zh_version):
            errors.append(f"version metadata present in only one language: {rel} <-> {zh}")
        elif en_version and zh_version and en_version.group(1) != zh_version.group(1):
            errors.append(
                f"bilingual version mismatch: {rel}={en_version.group(1)}; "
                f"{zh}={zh_version.group(1)}"
            )

    return errors


def check_internal_links(files: list[Path]) -> tuple[list[str], dict[Path, int]]:
    errors: list[str] = []
    incoming: dict[Path, int] = {relative(path): 0 for path in files}

    for source in files:
        rel_source = relative(source)
        text = strip_fenced_code(source.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            target_rel = normalize_link_target(source, raw)
            if target_rel is None:
                continue
            target_abs = ROOT / target_rel
            if not target_abs.exists():
                errors.append(f"broken internal link: {rel_source} -> {raw}")
                continue
            if target_abs.is_file() and target_abs.suffix.lower() == ".md":
                incoming[target_rel] = incoming.get(target_rel, 0) + 1

    return errors, incoming


def check_former_constitution(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        rel = relative(path)
        if rel in FORMER_CONSTITUTION_ALLOWED:
            continue
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
        for match in FORMER_CONSTITUTION_RE.finditer(text):
            snippet = " ".join(match.group(0).split())
            errors.append(f"former-Constitution reference outside historical/audit record: {rel}: {snippet}")
    return errors


def orphan_candidates(files: list[Path], incoming: dict[Path, int]) -> list[Path]:
    candidates: list[Path] = []
    for path in files:
        rel = relative(path)
        if rel in ENTRYPOINTS:
            continue
        if rel.name.startswith("README"):
            continue
        if incoming.get(rel, 0) == 0:
            candidates.append(rel)
    return candidates


def main() -> int:
    files = markdown_files()
    errors: list[str] = []

    errors.extend(check_bilingual_pairs(files))
    link_errors, incoming = check_internal_links(files)
    errors.extend(link_errors)
    errors.extend(check_former_constitution(files))

    candidates = orphan_candidates(files, incoming)

    print(f"checked {len(files)} Markdown files")
    if candidates:
        print("orphan/unreferenced candidates (informational; not a failure):")
        for path in candidates:
            print(f"  - {path}")
    else:
        print("no orphan/unreferenced Markdown candidates found")

    if errors:
        print("material validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("material navigation/bilingual/former-Constitution validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
