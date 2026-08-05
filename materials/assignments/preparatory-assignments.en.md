# Preparatory Independent Assignment and Oral Preparation Pack

Version: 0.3.0  
Status: Official learning-task baseline  
Last updated: 2026-08-05  
Major change summary: Retains unsubmitted, ungraded assignments while removing mandatory AI-use records, no-AI declarations, and a separate required AI-review task.  
Corresponding Chinese version: [前導課程自主作業與口試準備包](preparatory-assignments.zh-TW.md)

## Document Purpose

For students, instructors, and teaching assistants in both preparatory tracks. Both tracks use the same core tasks and capability standards; only pacing and language scaffolds may differ.

## Assignment Policy

- Every assignment should be completed, but it is not submitted and receives no direct grade.
- Students keep their programs, tests, traces, errors, and modifications.
- The next class discusses the previous assignment. Students may ask questions, share errors, compare solutions, or join class debugging.
- These assignments and learning records may be used as preparation for the final one-to-one oral examination.
- Instructors do not mark every assignment and do not deduct points for non-submission; students demonstrate capability through participation and the final oral examination.

Students should retain:

1. Understanding or prediction before execution.
2. Program or modification result.
3. Self-created tests and expected results.
4. Actual results and comparison.
5. One trace, debugging, or requirement-change record.
6. One remaining uncertainty to bring to the next class.
7. When AI was used, an optional brief note of any suggestion and verification result that helps later review; this is not a completion requirement.

Correct output, successful compilation, passing OJ, or complete source code alone does not establish capability.

---

# Assignment 1: From Source Code to Execution

- Related material: P-U01
- Competency IDs: `PC-E01`, `PC-E03`, `PC-E04`
- Target maturity: L2–L4

## Task

Create a C program that prints three lines: your name, department or interest, and `I am learning C.`

## Suggested Records

- A source-to-output flow diagram.
- Expected output written before execution.
- Compile and run commands.
- One self-created compilation error, its classification, and correction explanation.
- Before-and-after results after modifying one line and recompiling.
- One question to raise in the next class.

## Possible Next-Class Discussion

- How are compilation and execution different?
- Why must a source change be recompiled?
- Does the location named by an error message always identify the root cause?

---

# Assignment 2: Data and State Tracing

- Related material: P-U02
- Competency IDs: `PC-D01` through `PC-D05`
- Target maturity: L2–L4

## Task

Create a purchase-total calculator: read unit price and quantity, then print the total.

## Suggested Records

- Input–process–output table.
- Variables, types, and reasons for their selection.
- At least three tests: normal, boundary, and necessary exceptional.
- One state-trace table.
- Requirement change: add a fixed shipping fee of 60; shipping is free when the total reaches 500.
- Updated tests and regression results.
- One unresolved question about types or state.

## Constraint

Use only basic types, expressions, input/output, and necessary conditions; do not use arrays, functions, or advanced techniques.

---

# Assignment 3: Conditions and Loops

- Related material: P-U03
- Competency IDs: `PC-C01` through `PC-C07`
- Target maturity: L3–L4

## Task

Create a valid-score statistics program: repeatedly read scores; input `-1` ends the program. Accept only 0–100, then print the valid count and sum.

## Suggested Records

- The four loop elements.
- At least one iteration-by-iteration trace.
- Normal, boundary, and exceptional cases.
- One off-by-one or infinite-loop defect and its diagnosis record.
- Requirement change: also print the average; when there is no valid score, print `No valid score`.
- Regression tests after the correction.
- One loop question to bring to class.

---

# Assignment 4: Functions and Responsibility Decomposition

- Related material: P-U04
- Competency IDs: `PC-F01` through `PC-F05`
- Target maturity: L2–L4

## Task

Refactor a program in which all work is inside `main` into at least two functions with clear responsibilities.

Suggested context: read three numbers, find the maximum, and print it.

## Suggested Records

- Explanation of responsibility problems before refactoring.
- Function-responsibility diagram and interfaces.
- Call trace.
- Identical test results before and after refactoring.
- Requirement change: also print the minimum.
- Two possible decompositions and the reason for choosing one.
- One uncertainty about function design.

---

# Integrated Assignment: Small Score Reporter

- Related material: P-U01 through P-U04
- Competency IDs: `PC-E`, `PC-D`, `PC-C`, `PC-F`, `PC-V`, `PC-I`
- Target maturity: L3–L4

## Basic Requirements

Read three quiz scores and a passing threshold. Print:

- The average to one decimal place.
- `Pass` or `Try again`.
- The highest and lowest score.

Valid scores are 0–100. When any input is invalid, print `Invalid input` and stop.

## Permitted Core-Solution Scope

- Use three separate score variables, basic types, conditions, functions, and necessary expressions.
- Removing the lowest score and recalculating the average can be completed by subtracting the minimum from the sum of three scores and dividing by 2.
- Arrays or any untaught data structure are neither required nor encouraged.

## Suggested Development Cycle

```text
Understand requirements
→ Inputs, outputs, rules, and constraints
→ Responsibility decomposition
→ Expected results and tests
→ Minimal implementation
→ Execute and compare
→ Diagnose a defect
→ Modify a requirement
→ Regression verification
→ Explain and reflect
```

## Suggested Records

1. Requirement-analysis table.
2. Data and function-responsibility diagram.
3. At least five tests including normal, threshold, boundary, and invalid cases.
4. Complete program.
5. One defect-diagnosis record.
6. Requirement change: remove the lowest score and recalculate the average.
7. Regression tests.
8. A self-question list for final oral preparation.

## Optional AI Concept Conversation

Students may explain their function decomposition, testing strategy, or error cause to AI and notice whether the conversation exposes anything still unclear. This is optional, and no conversation must be saved or submitted. When an AI response conflicts with code or test results, reproducible evidence should guide judgment.

## Not Permitted

- Arrays, pointers, dynamic memory, or advanced data structures as the core solution.
- Keeping a complete external answer that the student cannot explain, modify, or test as oral-examination preparation.
- Using one sample output as proof of correctness.

---

# Independent Storage

No upload or submission is required. A suggested student folder is:

```text
assignment-x/
├── README.md          # understanding, predictions, tests, questions, and reflection
├── program.c          # program
└── evidence/          # trace tables, diagrams, or result records
```

Equivalent storage is acceptable as long as the student can find, read, modify, and explain the work during class discussion and the final oral examination.

## Shared AI Principles

- AI is not an assignment completion requirement, and routine use is not required.
- After forming an initial understanding, students may ask AI to explain an error, add candidate tests, or compare already-proposed approaches.
- AI should not replace tracing, core decomposition, testing, or final oral answers.
- Any AI suggestion still requires judgment through code, tests, compiler behavior, and reproducible results.

## Navigation

- [Learning and Assessment Policy](../../design/13-learning-assessment-policy.en.md)
- [Materials Index](../README.en.md)
- [Classroom Participation and Final Oral Examination Rubric](rubric.en.md)
- [繁體中文版](preparatory-assignments.zh-TW.md)
