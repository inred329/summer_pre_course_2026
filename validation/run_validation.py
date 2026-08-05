#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "validation" / "fixtures"
FLAGS = ["-std=c17", "-Wall", "-Wextra", "-Wformat=2", "-pedantic", "-Werror"]


def run(cmd: list[str], *, input_text: str = "", cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        check=False,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compile_and_run(compiler: str, source: Path, input_text: str, expected_out: str, expected_code: int = 0) -> None:
    with tempfile.TemporaryDirectory() as temp:
        exe = Path(temp) / source.stem
        built = run([compiler, *FLAGS, str(source), "-lm", "-o", str(exe)])
        require(built.returncode == 0, f"{source.name} failed to compile:\n{built.stderr}")
        executed = run([str(exe)], input_text=input_text)
        require(executed.returncode == expected_code, f"{source.name} exit {executed.returncode}, expected {expected_code}\n{executed.stderr}")
        require(executed.stdout == expected_out, f"{source.name} output mismatch\nexpected: {expected_out!r}\nactual:   {executed.stdout!r}")


def expect_compile_failure(compiler: str, source: Path) -> None:
    with tempfile.TemporaryDirectory() as temp:
        exe = Path(temp) / source.stem
        built = run([compiler, *FLAGS, str(source), "-o", str(exe)])
        require(built.returncode != 0, f"{source.name} unexpectedly compiled successfully")


def compile_module(compiler: str) -> None:
    module_dir = FIXTURES / "module"
    with tempfile.TemporaryDirectory() as temp:
        temp_path = Path(temp)
        main_o = temp_path / "main.o"
        score_o = temp_path / "score.o"
        exe = temp_path / "report"
        for source, output in [(module_dir / "main.c", main_o), (module_dir / "score.c", score_o)]:
            built = run([compiler, *FLAGS, "-I", str(module_dir), "-c", str(source), "-o", str(output)])
            require(built.returncode == 0, f"module compile failed for {source.name}:\n{built.stderr}")
        linked = run([compiler, str(main_o), str(score_o), "-o", str(exe)])
        require(linked.returncode == 0, f"module link failed:\n{linked.stderr}")
        executed = run([str(exe)])
        require(executed.returncode == 0, f"module program failed: {executed.stderr}")
        require(executed.stdout == "85.0\nPass\n", f"module output mismatch: {executed.stdout!r}")


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
        ("p_u04.c", "", "85\n", 0),
        ("f_u01.c", "", "0.30000000000000004\nclose enough\n", 0),
        ("f_u02.c", "10\n20\n-1\n", "Sum: 30\n", 0),
        ("f_u02.c", "10\nx\n", "Invalid input\n", 1),
        ("f_u03.c", "", "92\n", 0),
        ("f_u04.c", "Amy\n", "Hello, Amy\n", 0),
        ("f_u04.c", "1234567890123456789012345\n", "Input too long\n", 1),
        ("f_u05.c", "4\n", "24\n", 0),
        ("f_u05.c", "-1\n", "Invalid or overflow\n", 1),
        ("f_u06.c", "", "85\n", 0),
        ("f_u07.c", "", "Amy 1001 90.0\n", 0),
        ("f_u08.c", "3\n", "0 10 20\n", 0),
        ("f_u08.c", "x\n", "Invalid input\n", 1),
        ("f_u09.c", "", "80\n", 0),
        ("f_u11.c", "", "all tests passed\n", 0),
        ("f_u12.c", "", "2 records\nAverage: 85.0\n", 0),
    ]

    for filename, input_text, expected_out, expected_code in cases:
        compile_and_run(compiler, FIXTURES / filename, input_text, expected_out, expected_code)

    compile_module(compiler)

    for filename in ["bad_format.c", "bad_struct_compare.c", "bad_pointer_member.c"]:
        expect_compile_failure(compiler, FIXTURES / "expected_fail" / filename)

    print(f"technical validation passed with {compiler}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
