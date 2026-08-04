# Preparatory Course Instructor Implementation Guide

Version: 0.2.0  
Status: Official implementation draft  
Last updated: 2026-08-05  
Major change summary: Retains the shared four-session Chinese and five-session English delivery flow while making incorrect AI suggestions optional verification material rather than a fixed AI-verification segment or required student record.  
Corresponding Chinese version: [前導課程教師執行指引](session-guides.zh-TW.md)

## Document Purpose

For instructors and teaching assistants delivering the preparatory course. This document carries pacing, homework discussion, participation observation, representative errors, and fallback strategies. It does not define the complete final-oral procedure and does not place instructor administration back into student chapters.

## Shared Class Cycle

Except for the first class, each session should ordinarily follow:

```text
Previous-homework discussion for 15–25 minutes
→ Core question
→ Visual model and prediction before execution
→ Minimal executable example
→ Guided modification, testing, and debugging
→ Class synthesis
→ Next independent homework
```

Homework is not submitted or graded. Students keep their programs, tests, traces, errors, and modifications. Routine AI use and saved AI conversations are not required.

## Role of AI in Instructor Delivery

- AI is not a separate course topic and does not receive a fixed time block.
- When useful, an instructor may use one plausible but incorrect AI suggestion as an ordinary error case.
- The same cycle applies: predict first, then verify through code, compiler behavior, tracing, or testing.
- Not using AI does not affect participation or assessment.
- Students are not required to provide AI-use logs, no-AI declarations, or fixed-format reflections.

## Participation Observation

Observable participation includes:

- Raising a concrete question or explaining an obstacle.
- Answering, revising, or extending reasoning.
- Participating in tracing, testing, debugging, or solution comparison.
- Sharing an error the student made.
- Proposing normal, boundary, or exceptional tests.
- Participating through writing, anonymous questions, program operation, or group records.

Attendance, roll call, speaking frequency, and response speed must not replace participation judgment.

---

# Chinese Track: Four Sessions

## Session 1: Execution Model and First Program (180 minutes)

### Core Question

> How does human-readable C source code become behavior that the computer actually runs?

### Suggested Timing

| Time | Activity |
|---:|---|
| 0–20 | Course policy: no roll-call grading, no homework submission, participation and final oral |
| 20–45 | Source code, compiler, executable, and execution diagram |
| 45–70 | Predict and run the minimal program |
| 70–90 | Diagnose a missing-semicolon compilation error |
| 90–100 | Break |
| 100–130 | Modify source without recompiling experiment |
| 130–160 | Values, variables, and first state trace |
| 160–175 | Student operation and error sharing |
| 175–180 | Assign independent Homework 1 |

### Required Error Cases

- Missing semicolon causes compilation failure.
- Source is modified while the old executable is run.
- “Compilation succeeded” is mistaken for “the program ran and is correct.”

### Optional External-Suggestion Case

> “After editing a `.c` file, running the existing `.exe` automatically uses the latest source code.”

Whether the suggestion came from AI, a search result, or a peer, students predict first and verify through source modification, running the old executable, and recompiling.

### If Time Is Short

Preserve the toolchain, prediction, missing-semicolon case, and recompilation experiment; shorten open-ended practice.

## Session 2: Data, Types, and State (180 minutes)

### Previous-Homework Discussion

Prioritize:

- Compilation versus execution.
- Why source changes require recompilation.
- Errors created by students.

### Core Question

> How does a program retain and change data, and how can we verify that the result is reasonable?

### Suggested Timing

| Time | Activity |
|---:|---|
| 0–25 | Homework 1 discussion and anonymous error case |
| 25–55 | Values, types, variables, initialization, and assignment |
| 55–85 | State traces and manual calculation |
| 85–95 | Break |
| 95–125 | `scanf`, processing, and output |
| 125–150 | Integer division and format/type errors |
| 150–170 | Requirement modification and regression testing |
| 170–180 | Assign independent Homework 2 |

### Required Error Case

```c
int total = 5;
int count = 2;
double average = total / count;
```

Also prepare a mismatch between `%d` or `%lf` and the variable type.

### Optional External-Suggestion Case

> “When the variable on the left is `double`, integer division on the right always preserves the fractional part.”

Require manual prediction, then compare `5 / 2` with `5.0 / 2` through execution.

## Session 3: Conditions, Loops, and Termination (180 minutes)

### Previous-Homework Discussion

Prioritize:

- Type selection.
- The first mismatch between a trace and program behavior.
- Tests for a free-shipping requirement change.

### Core Question

> How does a program choose a path and repeat work reliably?

### Suggested Timing

| Time | Activity |
|---:|---|
| 0–25 | Homework 2 discussion |
| 25–55 | Condition and path model |
| 55–85 | Boundary cases and condition ordering |
| 85–95 | Break |
| 95–125 | Four loop elements and iteration trace |
| 125–150 | Diagnose off-by-one and infinite-loop defects |
| 150–170 | Modify and test the valid-score statistics program |
| 170–180 | Assign independent Homework 3 |

### Required Error Cases

- `=` is used where comparison is intended.
- `<` is used instead of `<=` at a boundary.
- The loop control variable is not updated.
- The sentinel value is incorrectly included in statistics.

### Optional External-Suggestion Case

> “A loop that contains `break` can never become infinite.”

Students construct a counterexample in which the `break` statement is unreachable.

## Session 4: Functions, Responsibility Decomposition, and Integration (180 minutes)

### Previous-Homework Discussion

Prioritize:

- Termination condition and update order.
- Off-by-one defects.
- Handling zero valid records.

### Core Question

> How can a small requirement be decomposed, implemented, tested, modified, and supported with trustworthy evidence?

### Suggested Timing

| Time | Activity |
|---:|---|
| 0–25 | Homework 3 discussion |
| 25–55 | Function responsibility and interface diagram |
| 55–85 | Trace calls, parameters, and return values |
| 85–95 | Break |
| 95–130 | Refactor an oversized `main` |
| 130–160 | Integrated task, requirement modification, and regression testing |
| 160–175 | Compare decomposition approaches or diagnose one external suggestion |
| 175–180 | Organize homework and final-oral preparation principles |

### Required Error Cases

- A non-`void` function has no `return`.
- The caller ignores a return value.
- The function name does not match its responsibility.
- Only the new behavior is tested after modification; prior behavior is not regressed.

### Optional External-Suggestion Case

> “Changing every variable into a global variable makes function decomposition simpler and is therefore the best solution for beginners.”

Students compare the traceability and testability of global state with parameters and return values.

---

# English Track: Five-Session Pacing

- Session 1: Execution model and first program.
- Session 2: Data, types, and program state.
- Session 3: Conditions, loops, and termination.
- Session 4: Functions and responsibility decomposition.
- Session 5: Integrated cycle, requirement modification, regression testing, and learning organization.

Each English session is 120 minutes. Except for Session 1, reserve 15–20 minutes for discussing the previous homework. Terminology cards, sentence scaffolds, written responses, and pair discussion may be used without changing the core tasks or standards.

## Fallback Environment

- An instructor-tested GCC or Clang C17 environment.
- When personal equipment is unavailable, use instructor equipment, paired operation, or paper tracing.
- Tool failure must not be treated directly as non-participation or missing capability.

## Instructor Record After Class

Record only:

- Main misconceptions from the session.
- Effective error cases.
- Common student obstacles.
- Questions to continue next class.
- Overall participation patterns and a small amount of representative evidence.

Do not create per-session roll-call scores, fixed AI-use logs, or point totals for each spoken contribution.

## Navigation

- [Materials Index](../README.en.md)
- [Assignment Discussion and Participation Observation Guide](../assignments/grading-guide.en.md)
- [繁體中文版](session-guides.zh-TW.md)
