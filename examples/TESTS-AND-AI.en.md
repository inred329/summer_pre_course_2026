# C17 Example Test Plans and Optional Incorrect-Suggestion Review

Version: 0.2.0  
Status: Instructor resource  
Last updated: 2026-08-07  
Governance note: This resource does not create assessment or AI/tool-use requirements. The official learning and assessment policy remains authoritative.  
Corresponding Chinese version: [C17 範例測試計畫與選用錯誤建議審查](TESTS-AND-AI.zh-TW.md)

## Document Purpose

This resource helps instructors and teaching assistants verify the examples under `examples/` and plan prediction, tracing, diagnosis, correction, and regression activities.

Students should establish an expected result or technical hypothesis before observing a compiler/runtime result. AI-specific review is an optional extension only; the same core activity can be completed by reviewing a deliberately incorrect statement supplied by the instructor.

## Unit 1

### `unit-01/hello.c`

Expected output:

```text
Hello, C!
```

### `unit-01/defects/missing-semicolon.c`

Expected: C translation/build fails, so no newly built program should be executed. A conforming implementation must diagnose the constraint violation, but diagnostic wording and the reported source location can differ; do not require one exact “missing semicolon” message.

Optional incorrect-suggestion review:

> This is a runtime error. Run the newly built program first to see the complete message.

Reject the claim because the source does not successfully translate/build into the intended new program.

## Unit 2

### `unit-02/average.c`

Input contract: two decimal integers; `count` must be greater than zero.

| Input | Expected Output | Exit direction |
|---|---|---|
| `5 2` | `Average: 2.50` | success |
| `0 3` | `Average: 0.00` | success |
| `5 0` | `Count must be positive` | failure |
| `5 -2` | `Count must be positive` | failure |
| non-integer input | `Invalid input` | failure |

### `unit-02/defects/integer-division.c`

The program is expected to compile, but it prints `Average: 2.00` because integer division occurs before conversion to `double`.

Optional incorrect-suggestion review:

> Change only the output format to `%.2f` and the mathematical result will become 2.50.

Reject the claim: formatting changes presentation, not the already-computed integer-division result.

## Unit 3

### `unit-03/score-statistics.c`

Input contract: whitespace-separated decimal integers. `-1` is the sentinel; scores from 0 through 100 are accepted; other integer scores are ignored.

| Input Sequence | Expected Result |
|---|---|
| `80 90 -1` | count 2, sum 170, average 85.00 |
| `0 100 -1` | count 2, sum 100, average 50.00 |
| `-1` | `No valid score` |
| `120 80 -1` | ignore 120; count 1, sum 80, average 80.00 |

If a non-integer token is supplied, the current example stops scanning and reports the statistics accumulated so far. Treat that as part of the example's stated input contract rather than silently assuming recovery from malformed input.

### `unit-03/defects/infinite-loop.c`

Expected: the source compiles, but once executed the loop does not terminate because `value` is never updated. Prefer static tracing for the core diagnosis. If an instructor demonstrates execution, use an environment-level timeout or manual interruption; CI must not run this program without a timeout.

Optional incorrect-suggestion review:

> Replace `while` with `if` to fix it.

Reject the claim because it changes repeated-execution semantics rather than repairing progress toward the loop's termination condition.

## Unit 4

### `unit-04/max-of-three.c`

| Input | Expected Output |
|---|---|
| `3 8 5` | `Maximum: 8` |
| `9 9 1` | `Maximum: 9` |
| `-3 -8 -5` | `Maximum: -3` |
| malformed input | `Invalid input` |

### `unit-04/defects/missing-return.c`

The defect is reaching the closing `}` of a value-returning function without returning a value, while the caller uses the function-call result. Under C17, that execution has undefined behavior. Common compilers with warning options usually diagnose the suspicious control path, but this source is not a portable “must fail compilation” test and one exact warning is not required.

Do not execute this defect in automated verification as if its observed value were meaningful. The safe activity is to identify the contract violation, add the required return, and then test the corrected function.

Optional incorrect-suggestion review:

> If one observed run prints the expected maximum, there is no need to add `return`.

Reject the claim because one observation cannot justify behavior whose language-level preconditions have already been violated.

## Teaching Rules

- Files under `defects/` are intentionally wrong and must not be presented as correct reference solutions.
- Prediction and technical reasoning come before optional external-suggestion review.
- After a correction, rerun relevant normal, boundary, invalid, and failure cases.
- Do not penalize a different solution merely for being different when it satisfies the same contract and evidence expectations.
- Do not require AI use, AI logs, fixed prompts, or non-use declarations for these examples.

## Navigation

- [Examples Index](README.md)
- [Compile Manifest](COMPILE-MANIFEST.md)
- [繁體中文版](TESTS-AND-AI.zh-TW.md)
