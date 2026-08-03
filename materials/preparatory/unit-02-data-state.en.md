# Preparatory Unit 2: Data, Types, and Program State

Version: 0.1.0  
Status: Teaching draft  
Last updated: 2026-08-03  
Major change summary: Established complete material for values, types, variables, expressions, input/output, state tracing, and requirement modification.  
Corresponding Chinese version: [前導單元 2：資料、型別與程式狀態](unit-02-data-state.zh-TW.md)

## Document Purpose

For direct use by instructors, teaching assistants, and students. The Chinese preparatory track uses it across the latter part of Session 1 and Session 2; the English preparatory track uses it in Session 2.

## Basic Information

- Requirement IDs: `CAP-D01` through `CAP-D04`, `X-02`, `X-03`, `X-04`
- Competency IDs: `PC-D01` through `PC-D05`, `PC-V01`, `PC-V03`
- Target maturity: L2–L4
- Scope state: `SB-C`
- Acceptance tasks: `AT-02`, `AT-03`, `AT-05`, `AT-06`, `AT-08`, `AT-12`
- Risk IDs: `R-02`, `R-05`, `R-09`
- Estimated time: Chinese 150–180 minutes; English 120 minutes

## 1. Learning Objectives

Students can:

1. Distinguish a value, type, variable name, and current value.
2. Trace state changes caused by declaration, initialization, assignment, and expression evaluation.
3. Select `int` or `double` according to data meaning.
4. Build a basic input–process–output program.
5. Modify one requirement and update expected results and tests.

## 2. Prerequisites

- Build, compile, and run a minimal C program.
- Write expected output before execution.
- Distinguish compilation problems from incorrect results.

Students who lack these capabilities complete Unit 1 remediation rather than copying a complete program.

## 3. Tools and Environment

- GCC or Clang with C17 support.
- Compile with: `gcc -std=c17 -Wall -Wextra -pedantic score.c -o score`
- Fallback: an instructor-tested online C compiler.

## 4. Information Priority

### Must Understand

- A variable name is not the value itself.
- A type constrains representation and operations.
- Assignment changes program state.
- Input is an assumption, and output must be checked against an expected result.

### Must Complete

- One state-trace table.
- One input–process–output program.
- One diagnosis of a type or expression error.
- One requirement modification with regression testing.

### May Be Deferred

- Bit-level representation, complete overflow taxonomy, complex casts, and a full undefined-behavior taxonomy.

## 5. Core Question

> How does a program remember data, change data, and let us verify that the new result is reasonable?

## 6. Visual Model

```mermaid
flowchart LR
    I[Input] --> V[Variable]
    V --> E[Expression]
    E --> A[Assignment]
    A --> S[New State]
    S --> O[Output]
    X[Expected Result] --> C{Compare}
    O --> C
```

Verification method: calculate first, then run. When results differ, locate the first state that differs.

## 7. Core Concepts

- Value: actual data, such as `80`.
- Type: representation and permitted operations, such as `int` or `double`.
- Variable: a name used to refer to current data state.
- Initialization: assigning an initial value during declaration.
- Assignment: writing a new result into a variable.
- Expression: values, variables, and operators combined to produce a result.

## 8. Minimal Executable Example

```c
#include <stdio.h>

int main(void) {
    int score = 80;
    score = score + 5;
    printf("%d\n", score);
    return 0;
}
```

Expected output:

```text
85
```

## 9. State Trace

| Step | Statement | `score` Before | Evaluated Result | `score` After |
|---|---|---:|---:|---:|
| 1 | `int score = 80;` | does not exist | 80 | 80 |
| 2 | `score = score + 5;` | 80 | 85 | 85 |
| 3 | `printf(...)` | 85 | 85 | 85 |

Prediction question: What roles do the `score` on the right and the `score` on the left play?

## 10. Input–Process–Output Example

```c
#include <stdio.h>

int main(void) {
    int score;
    scanf("%d", &score);
    score = score + 5;
    printf("Adjusted score: %d\n", score);
    return 0;
}
```

Normal case: input `80`, expected `Adjusted score: 85`.  
Boundary case: input `0`, expected `Adjusted score: 5`.

In this unit, treat `&score` only as the form required for `scanf` to write into the variable; pointer semantics are intentionally deferred.

## 11. Common Errors

### Integer Division

```c
int total = 5;
int count = 2;
double average = total / count;
```

The result may be `2.0`, not `2.5`. Trace operand types first, then change it to:

```c
double average = (double) total / count;
```

Students must explain the reason rather than merely replacing the code with an AI suggestion.

### Format and Type Mismatch

Using `%d` for a `double` or `%lf` to read an `int` is incorrect. Verify with compiler warnings, observed behavior, and the type table.

## 12. Guided Practice

Build a “temperature plus one” program: read an integer temperature, add one, and print it. Submit:

1. An input–process–output table.
2. Two expected results.
3. The program and actual results.
4. One sentence explaining the state change.

## 13. Independent Practice

### Score Adjuster

Read an original score and bonus, then print the adjusted score.

- Input: two integers.
- Output: `Final score: <value>`.
- Constraint: use meaningful variable names and define three tests first.
- Required evidence: state table, program, test table, and oral explanation.

Alternative reasonable solutions are permitted.

## 14. Requirement Modification

Add this rule: “The adjusted score may not exceed 100.” Students must:

1. Identify the affected processing step.
2. Update expected results and add a case above 100.
3. Modify the program.
4. Re-run prior cases.
5. Explain why the original tests were insufficient.

## 15. AI Use Rules

Permitted: after completing a first version, ask AI for potentially missing tests or for help interpreting a compiler warning.  
Prohibited: request a complete answer before producing a state table and initial approach; submit code that cannot be explained.  
Must retain: pre-AI approach, self-created tests, suggestion summary, verification method, and reason for accepting or rejecting it.

## 16. Acceptance and Remediation

- Understanding evidence: `EV-TR + EV-EX`.
- Action evidence: `EV-IM + EV-TE + EV-MO`.
- Pass: state tracing matches the program, type selection can be explained, and the requirement change is completed.
- Remediation: trace a new set of values live, or correct one type error and explain why.

Micro-oral questions:

1. What is the value of `score` before and after assignment?
2. Why are `5 / 2` and `5.0 / 2` different?
3. Which new test matters most after the requirement change?

## 17. Instructor and TA Guidance

- Require hand calculation before execution.
- Do not expand `scanf` address syntax into a pointer lesson.
- When time is short, retain state tracing, the type error, and requirement modification; reduce exercise count.
- Successful output alone does not establish L4.

## 18. Unit Summary

This unit establishes the model that program execution changes state. The next unit uses conditions and repetition to decide how state changes.

## Navigation

- [Materials Index](../README.en.md)
- [繁體中文版](unit-02-data-state.zh-TW.md)
