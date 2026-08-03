# C17 Example Tests and Incorrect AI Suggestions

Version: 0.1.0  
Status: Official teaching resource  
Last updated: 2026-08-03  
Corresponding Chinese version: [C17 範例測試與錯誤 AI 建議](TESTS-AND-AI.zh-TW.md)

## Document Purpose

For instructors and teaching assistants using `examples/`. Require prediction before compilation, execution, comparison, and explanation.

## Unit 1

### `unit-01/hello.c`

Expected output:

```text
Hello, C!
```

### `unit-01/defects/missing-semicolon.c`

Expected: compilation fails and the program does not run. Compiler wording may differ, but it should identify a missing `;` near `printf`.

Incorrect AI suggestion:

> This is a runtime error. Run the program first to see the complete message.

Reject it because compilation failure prevents a new executable from running.

## Unit 2

### `unit-02/average.c`

| Input | Expected Output |
|---|---|
| `5 2` | `Average: 2.50` |
| `0 3` | `Average: 0.00` |
| `5 0` | `Count must be positive` |

### `unit-02/defects/integer-division.c`

For input `5 2`, the incorrect result may be `2.00`. Integer division occurs before conversion to `double`.

Incorrect AI suggestion:

> Change the output format to `%.2f` and the result will become 2.50.

Reject it because formatting cannot repair an already completed integer division.

## Unit 3

### `unit-03/score-statistics.c`

| Input Sequence | Expected Result |
|---|---|
| `80 90 -1` | count 2, sum 170, average 85.00 |
| `0 100 -1` | count 2, sum 100, average 50.00 |
| `-1` | `No valid score` |
| `120 80 -1` | Ignore 120 and count only 80 |

### `unit-03/defects/infinite-loop.c`

Expected: the loop does not terminate because the control variable is not updated.

Incorrect AI suggestion:

> Replace `while` with `if` to fix it.

Students should identify that this changes the requirement and does not repair repeated execution with termination.

## Unit 4

### `unit-04/max-of-three.c`

| Input | Expected Output |
|---|---|
| `3 8 5` | `Maximum: 8` |
| `9 9 1` | `Maximum: 9` |
| `-3 -8 -5` | `Maximum: -3` |

### `unit-04/defects/missing-return.c`

Expected: the compiler should warn that a non-`void` function may not return a value; observed results are not trustworthy.

Incorrect AI suggestion:

> If the current test output is correct, there is no need to add `return`.

Reject it because the function contract requires every reachable path to provide a return value.

## Teaching Rules

- Defect files are not correct examples.
- Let students predict before revealing whether an AI suggestion is wrong.
- After correction, rerun normal, boundary, and necessary exceptional cases.
- Do not penalize a different reasonable solution.

## Navigation

- [Examples Index](README.md)
- [繁體中文版](TESTS-AND-AI.zh-TW.md)
