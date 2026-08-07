# C17 Example Compile Manifest

Version: 0.1.0  
Status: Active verification manifest  
Last updated: 2026-08-07

## Purpose

This manifest defines expected translation, warning, and runtime treatment for source files under `examples/`. It prevents intentional defect cases from being mistaken for broken reference examples and prevents unsafe/nonterminating defect cases from being executed as ordinary CI tests.

Recommended baseline for ordinary native-host checks:

```bash
$CC -std=c17 -Wall -Wextra -pedantic <source.c> -o <program>
```

Run the manifest separately with the target GCC and Clang versions when both are supported. Exact diagnostic wording is not part of the acceptance criteria.

## Manifest

| Source | Category | Translation expectation | Runtime expectation | Automated treatment |
|---|---|---|---|---|
| `unit-01/hello.c` | correct | success, no required warning | prints `Hello, C!` | compile + run |
| `unit-01/defects/missing-semicolon.c` | intentional syntax/constraint defect | failure with diagnostic | no newly built program | compile and assert failure; do not run |
| `unit-02/average.c` | correct | success, no required warning | documented input contract and two-decimal average | compile + run test cases |
| `unit-02/defects/integer-division.c` | intentional logic defect | success | prints `Average: 2.00`; result is intentionally wrong for the intended real-number average | compile; optional controlled run; never treat output as correct solution |
| `unit-03/score-statistics.c` | correct | success, no required warning | documented sentinel/range behavior | compile + run test cases |
| `unit-03/defects/infinite-loop.c` | intentional termination defect | success | intentionally nonterminating | compile only in ordinary CI; never run without an explicit timeout |
| `unit-04/max-of-three.c` | correct | success, no required warning | documented maximum/input behavior | compile + run test cases |
| `unit-04/defects/missing-return.c` | intentional return-contract defect | compiler-dependent: translation may succeed and commonly warns with enabled warnings | using the call value after control reaches the closing brace has undefined behavior | compile for diagnostic observation only; do not execute in automated verification |

## Correct-Example Runtime Cases

### `unit-01/hello.c`

Expected stdout:

```text
Hello, C!
```

### `unit-02/average.c`

| stdin | stdout contains | expected process direction |
|---|---|---|
| `5 2` | `Average: 2.50` | success |
| `0 3` | `Average: 0.00` | success |
| `5 0` | `Count must be positive` | failure |
| `5 -2` | `Count must be positive` | failure |
| `x 2` | `Invalid input` | failure |

### `unit-03/score-statistics.c`

| stdin | stdout |
|---|---|
| `80 90 -1` | `Count: 2`, `Sum: 170`, `Average: 85.00` |
| `0 100 -1` | `Count: 2`, `Sum: 100`, `Average: 50.00` |
| `-1` | `No valid score` |
| `120 80 -1` | `Count: 1`, `Sum: 80`, `Average: 80.00` |

### `unit-04/max-of-three.c`

| stdin | stdout contains | expected process direction |
|---|---|---|
| `3 8 5` | `Maximum: 8` | success |
| `9 9 1` | `Maximum: 9` | success |
| `-3 -8 -5` | `Maximum: -3` | success |
| `x 8 5` | `Invalid input` | failure |

## Verification Record Template

When a compiler/environment is checked, record:

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| OS / environment | |
| Compiler | GCC / Clang / other |
| Compiler version | |
| Command flags | `-std=c17 -Wall -Wextra -pedantic` or documented equivalent |
| Correct examples | pass / findings |
| Intentional defects | matched manifest / findings |
| Runtime cases | pass / findings |
| Follow-up commit / issue | |

## Maintenance Rules

- Add every new executable C example or intentional defect to this manifest.
- A source file not classified here must not silently enter automated execution.
- Keep expected outputs synchronized with source code and bilingual test plans.
- Treat compiler diagnostic text as implementation-specific unless the C standard requires a diagnostic category, not an exact message.
- Do not execute examples with intentional undefined behavior or unbounded nontermination as ordinary CI tests.
