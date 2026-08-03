# C17 Examples and Defect Cases

Version: 0.1.0  
Status: Classroom verification draft  
Last updated: 2026-08-03  
Major change summary: Established directly compilable examples and intentionally defective cases for Preparatory Units 1–4.

## Purpose

These files support instructor demonstrations, student tracing, debugging, requirement modification, and regression testing.

Compile correct examples with:

```bash
gcc -std=c17 -Wall -Wextra -pedantic <file>.c -o <program>
```

Windows PowerShell runs the result with:

```powershell
.\<program>.exe
```

Linux and macOS run it with:

```bash
./<program>
```

Files under a `defects` directory are intentionally incorrect. Their purpose is prediction, diagnosis, correction, and regression—not copying a final answer.

## Units

- `unit-01`: source, compilation, execution, and stale executable behavior.
- `unit-02`: values, types, state, input/output, and integer division.
- `unit-03`: conditions, loops, boundaries, sentinels, and termination.
- `unit-04`: functions, responsibility decomposition, return values, and regression.

## Assessment Policy

Homework using these examples is not submitted or individually graded. Students keep their own versions, tests, traces, corrections, and AI-verification notes for classroom discussion and final-oral preparation.

## Navigation

- [Materials Index](../materials/README.en.md)
- [教材索引](../materials/README.zh-TW.md)
