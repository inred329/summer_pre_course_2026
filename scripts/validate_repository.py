#!/usr/bin/env python3
"""Repository-wide structural validation for Constitution 2.0 maintenance.

Mechanically checks:
- local Markdown links resolve;
- bilingual Markdown pairs exist and paired version metadata matches;
- obsolete Constitution 1.x references occur only in historical/audit records;
- ordinary C17 translation units compile with the selected compiler.

Intentional defect sources are not treated as ordinary reference programs. Their
specific expectations are documented in `examples/COMPILE-MANIFEST.md` and, for
validation fixtures, in `validation/run_validation.py`.

This script does not replace human review of substantive bilingual equivalence,
student readability, assessment policy, or technical pedagogy.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
VERSION_EN_RE = re.compile(r"^Version:\s*([^\s]+)", re.MULTILINE)
VERSION_ZH_RE = re.compile(r"^版本[：:]\s*([^\s]+)", re.MULTILINE)
OLD_CONSTITUTION_RE = re.compile(
    r"(?:Constitution\s+1\.[0-9]|Constitution[^\n]{0,30}1\.2\.0|憲法[^\n]{0,30}1\.2\.0)",
    re.IGNORECASE,
)
HISTORICAL_PREFIXES = (
    "design/12-constitution-compliance-review.",
    "reviews/repository-constitution-2-audit.",
)


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts and ".github" not in p.parts
    )


def strip_fenced_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def check_links(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    root_resolved = root.resolve()
    for path in files:
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip()
            lower = raw.lower()
            if lower.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            if raw.startswith("#"):
                continue

            target = raw.split(' "', 1)[0].split(" '", 1)[0]
            target = target.strip("<>").split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue

            if target.startswith("/"):
                resolved = (root / unquote(target.lstrip("/"))).resolve()
            else:
                resolved = (path.parent / unquote(target)).resolve()

            try:
                resolved.relative_to(root_resolved)
            except ValueError:
                errors.append(f"link escapes repository: {relative(path, root)} -> {raw}")
                continue

            if not resolved.exists():
                errors.append(f"broken link: {relative(path, root)} -> {raw}")
    return errors


def check_bilingual_pairs(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    file_set = set(files)
    for path in files:
        if path.name.endswith(".en.md"):
            peer = path.with_name(path.name.replace(".en.md", ".zh-TW.md"))
            if peer not in file_set:
                errors.append(f"missing zh-TW pair: {relative(path, root)}")
        elif path.name.endswith(".zh-TW.md"):
            peer = path.with_name(path.name.replace(".zh-TW.md", ".en.md"))
            if peer not in file_set:
                errors.append(f"missing en pair: {relative(path, root)}")
    return errors


def check_bilingual_versions(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for en in files:
        if not en.name.endswith(".en.md"):
            continue
        zh = en.with_name(en.name.replace(".en.md", ".zh-TW.md"))
        if not zh.exists():
            continue
        en_text = en.read_text(encoding="utf-8")
        zh_text = zh.read_text(encoding="utf-8")
        en_match = VERSION_EN_RE.search(en_text[:2500])
        zh_match = VERSION_ZH_RE.search(zh_text[:2500])
        if bool(en_match) != bool(zh_match):
            errors.append(
                f"version metadata presence differs: {relative(en, root)} / {relative(zh, root)}"
            )
        elif en_match and zh_match and en_match.group(1) != zh_match.group(1):
            errors.append(
                "version mismatch: "
                f"{relative(en, root)}={en_match.group(1)} / "
                f"{relative(zh, root)}={zh_match.group(1)}"
            )
    return errors


def check_old_constitution_references(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        rel = relative(path, root)
        if rel.startswith(HISTORICAL_PREFIXES):
            continue
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
        if OLD_CONSTITUTION_RE.search(text):
            errors.append(f"obsolete Constitution 1.x reference outside history/audit: {rel}")
    return errors


def is_intentional_defect(path: Path, root: Path) -> bool:
    rel_parts = path.relative_to(root).parts
    return "defects" in rel_parts or "expected_fail" in rel_parts


def c_translation_units(root: Path) -> list[Path]:
    return sorted(
        p
        for p in root.rglob("*.c")
        if ".git" not in p.parts
        and not any(part.startswith("build") for part in p.parts)
        and not is_intentional_defect(p, root)
    )


def compile_translation_units(root: Path, compiler: str) -> list[str]:
    errors: list[str] = []
    units = c_translation_units(root)
    if not units:
        return errors
    with tempfile.TemporaryDirectory(prefix="c17-objects-") as tmp:
        out_dir = Path(tmp)
        for index, source in enumerate(units):
            obj = out_dir / f"unit-{index}.o"
            cmd = [
                compiler,
                "-std=c17",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-Werror",
                "-c",
                str(source),
                "-o",
                str(obj),
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            if proc.returncode != 0:
                detail = (proc.stderr or proc.stdout).strip().replace("\n", " | ")
                errors.append(
                    f"{compiler} C17 compile failed: {relative(source, root)} :: {detail[:600]}"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--compiler", choices=("gcc", "clang"))
    parser.add_argument(
        "--skip-c",
        action="store_true",
        help="run document/navigation checks only",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    files = markdown_files(root)

    errors: list[str] = []
    errors.extend(check_links(root, files))
    errors.extend(check_bilingual_pairs(root, files))
    errors.extend(check_bilingual_versions(root, files))
    errors.extend(check_old_constitution_references(root, files))

    units: list[Path] = []
    if not args.skip_c:
        units = c_translation_units(root)
        compilers = [args.compiler] if args.compiler else ["gcc", "clang"]
        for compiler in compilers:
            try:
                proc = subprocess.run(
                    [compiler, "--version"], capture_output=True, text=True, check=False
                )
            except FileNotFoundError:
                errors.append(f"compiler not found: {compiler}")
                continue
            if proc.returncode != 0:
                errors.append(f"compiler is not runnable: {compiler}")
                continue
            errors.extend(compile_translation_units(root, compiler))

    if errors:
        print(f"repository validation failed with {len(errors)} issue(s):", file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        return 1

    c_summary: str | int = len(units) if not args.skip_c else "C checks skipped"
    print(
        f"repository validation passed: {len(files)} Markdown files, "
        f"{c_summary} ordinary C translation units"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
