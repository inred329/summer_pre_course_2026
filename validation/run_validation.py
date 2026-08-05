#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "validation" / "fixtures"
FLAGS = ["-std=c17", "-Wall", "-Wextra", "-Wformat=2", "-pedantic", "-Werror"]


def run(cmd: list[str], *, input_text: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compile_and_run(
    compiler: str,
    source: Path,
    input_text: str,
    expected_out: str,
    expected_code: int = 0,
) -> None:
    with tempfile.TemporaryDirectory() as temp:
        exe = Path(temp) / source.stem
        built = run([compiler, *FLAGS, str(source), "-lm", "-o", str(exe)])
        require(built.returncode == 0, f"{source.name} failed to compile:\n{built.stderr}")
        executed = run([str(exe)], input_text=input_text)
        require(
            executed.returncode == expected_code,
            f"{source.name} exit {executed.returncode}, expected {expected_code}\n{executed.stderr}",
        )
        require(
            executed.stdout == expected_out,
            f"{source.name} output mismatch\nexpected: {expected_out!r}\nactual:   {executed.stdout!r}",
        )


def expect_compile_failure(compiler: str, source: Path) -> None:
    with tempfile.TemporaryDirectory() as temp:
        exe = Path(temp) / source.stem
        built = run([compiler, *FLAGS, str(source), "-o", str(exe)])
        require(built.returncode != 0, f"{source.name} unexpectedly compiled successfully")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compiler", required=True)
    args = parser.parse_args()
    compiler = args.compiler

    cases = [
        ("p_u01.c", "", "Hello, C!\n", 0),
        ("p_u02.c", "80\n", "Adjusted score: 85\n", 0),
        ("p_u02.c", "hello\n", "Invalid input\n", 1),
        ("p_u03.c", "60\n", "Pass\n", 0),
        ("p_u03.c", "x\n", "Invalid input\n", 1),
        ("all_remaining_units.c", "", "all unit contracts passed\n", 0),
    ]

    for filename, input_text, expected_out, expected_code in cases:
        compile_and_run(compiler, FIXTURES / filename, input_text, expected_out, expected_code)

    for filename in ["bad_format.c", "bad_struct_compare.c", "bad_pointer_member.c"]:
        expect_compile_failure(compiler, FIXTURES / "expected_fail" / filename)

    print(f"technical validation passed with {compiler}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
