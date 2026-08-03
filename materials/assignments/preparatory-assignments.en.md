# Preparatory Course Assignment Pack

Version: 0.1.0  
Status: Official assignment draft  
Last updated: 2026-08-03  
Major change summary: Established four formative assignments, one integrated assignment, required evidence, AI boundaries, and remediation methods.  
Corresponding Chinese version: [前導課程作業包](preparatory-assignments.zh-TW.md)

## Document Purpose

For students, instructors, and teaching assistants in both preparatory tracks. Both tracks use the same core requirements, evidence, and passing standards; only deadlines, pacing, and language scaffolds may differ.

## Shared Assignment Rules

Every assignment must include:

1. Understanding or prediction before execution.
2. Program or modification result.
3. Self-created tests and expected results.
4. Actual results and comparison.
5. One explanation, trace, debugging, or requirement-change artifact.
6. An AI-use record when AI was used.

Correct output, successful compilation, passing OJ, or complete source code alone is insufficient for passing.

---

# Assignment 1: From Source Code to Execution

- Related material: Unit 1
- Requirement IDs: `X-01`, `X-02`, `X-04`
- Competency IDs: `PC-E01`, `PC-E03`, `PC-E04`
- Target maturity: L2–L4
- Acceptance tasks: `AT-04`, `AT-05`, `AT-07`, `AT-12`

## Task

Create a C program that prints three lines: your name, department or interest, and `I am learning C.`

## Required Evidence

- A source-to-output flow diagram.
- Expected output written before execution.
- Compile and run commands.
- One self-created compilation error, its classification, and correction explanation.
- Before-and-after results after modifying one line and recompiling.

## Passing Criteria

Explain the difference between compilation and execution, and support the correction with evidence.

## Remediation

Classify the stage of a new error example and explain live why source changes require recompilation.

---

# Assignment 2: Data and State Tracing

- Related material: Unit 2
- Requirement IDs: `CAP-D01` through `CAP-D04`
- Competency IDs: `PC-D01` through `PC-D05`
- Target maturity: L2–L4
- Acceptance tasks: `AT-03`, `AT-05`, `AT-06`, `AT-08`

## Task

Create a “purchase total calculator”: read unit price and quantity, then print the total.

## Required Evidence

- Input–process–output table.
- Variables, types, and reasons for their selection.
- At least three tests: normal, boundary, and necessary exceptional.
- One state-trace table.
- Requirement change: add a fixed shipping fee of 60; shipping is free when the total reaches 500.
- Updated tests and regression results.

## Constraint

Use only basic types, expressions, input/output, and necessary conditions; do not use arrays, functions, or advanced techniques.

## Passing Criteria

Type choices and tracing are reasonable, tests before and after modification are complete, and the first state change can be explained.

## Remediation

Trace instructor-provided values live and correct one format or type error.

---

# Assignment 3: Conditions and Loops

- Related material: Unit 3
- Requirement IDs: `CAP-C01` through `CAP-C04`
- Competency IDs: `PC-C01` through `PC-C07`
- Target maturity: L3–L4
- Acceptance tasks: `AT-03`, `AT-06`, `AT-07`, `AT-08`, `AT-12`

## Task

Create a “valid score statistics” program: repeatedly read scores; input `-1` ends the program. Accept only 0–100, then print the valid count and sum.

## Required Evidence

- The four loop elements.
- At least one iteration-by-iteration trace.
- Normal, boundary, and exceptional cases.
- Diagnosis of one instructor-provided off-by-one or infinite-loop defect.
- Requirement change: also print the average; when there is no valid score, print `No valid score`.

## Passing Criteria

Explain termination, valid-data checks, and update order; run regression tests after correcting the defect.

## Remediation

Trace a new input sequence live and identify each iteration state and the stopping reason.

---

# Assignment 4: Functions and Responsibility Decomposition

- Related material: Unit 4
- Requirement IDs: `CAP-F01` through `CAP-F04`
- Competency IDs: `PC-F01` through `PC-F05`
- Target maturity: L2–L4
- Acceptance tasks: `AT-04`, `AT-05`, `AT-06`, `AT-09`, `AT-12`

## Task

Refactor an instructor-provided program in which all work is inside `main` into at least two functions with clear responsibilities.

Suggested context: read three numbers, find the maximum, and print it.

## Required Evidence

- Explanation of responsibility problems before refactoring.
- Function-responsibility diagram and interfaces.
- Call trace.
- Identical test results before and after refactoring.
- Requirement change: also print the minimum.
- Compare two possible decompositions and justify the choice.

## Passing Criteria

Responsibilities are clear and independently testable, and the student can trace parameters and return values.

## Remediation

Decompose another oversized function or trace a new set of call data.

---

# Integrated Assignment: Small Score Reporter

- Related material: Units 1–4
- Requirement IDs: `EDU-01` through `EDU-04`, `X-01` through `X-06`
- Competency IDs: `PC-E`, `PC-D`, `PC-C`, `PC-F`, `PC-V`, `PC-A`, `PC-I`
- Target maturity: L3–L4
- Acceptance tasks: `AT-05` through `AT-12`

## Basic Requirements

Read three quiz scores and a passing threshold. Print:

- The average to one decimal place.
- `Pass` or `Try again`.
- The highest and lowest score.

Valid scores are 0–100. When any input is invalid, print `Invalid input` and stop.

## Required Development Cycle

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

## Required Evidence

1. Requirement-analysis table.
2. Data and function-responsibility diagram.
3. At least five tests including normal, threshold, boundary, and invalid cases.
4. Complete program.
5. One defect-diagnosis record.
6. Requirement change: remove the lowest score and recalculate the average.
7. Regression tests.
8. AI-use record or a “no AI used” declaration.
9. Micro-oral check.

## AI Review Task

The instructor provides one potentially incorrect AI suggestion. Students predict first, then compile, run, and test before accepting, modifying, or rejecting it with evidence.

## Not Permitted

- Arrays, pointers, dynamic memory, or advanced data structures as the core solution.
- Submitting AI-generated code that cannot be explained.
- Using one sample output as proof of correctness.

## Passing Criteria

- Program satisfies requirements and tests are trustworthy.
- Student explains data, control, and function responsibilities.
- Student modifies a requirement and performs regression verification.
- Student diagnoses one defect.
- Student explains how an AI suggestion was verified.

## Remediation

Remediation targets the missing capability rather than requiring indiscriminate resubmission:

- Weak tracing: live-trace a new input.
- Weak testing: add boundary and exceptional cases.
- Weak function understanding: modify an interface and explain it.
- Weak AI verification: review another incorrect suggestion.

---

# Submission Format

Submit one folder per assignment:

```text
assignment-x/
├── README.md          # understanding, predictions, tests, reflection, AI record
├── program.c          # program
└── evidence/          # trace tables, diagrams, or result screenshots
```

Equivalent formats are acceptable, but required evidence may not be omitted.

## Shared AI Use Rules

### Permitted

- Explain an error message already encountered.
- Add candidate tests after the student first proposes tests.
- Compare two student-proposed approaches.
- Suggest debugging hypotheses for student verification.

### Prohibited

- Request a complete answer before understanding and an initial approach.
- Let AI perform tracing, core decomposition, or the oral check.
- Submit code that cannot be explained, modified, or tested.

### Must Retain

- Understanding or approach before AI use.
- Self-created expected results and tests.
- Summary of AI suggestions.
- Verification method.
- Reason for accepting, modifying, or rejecting.

## Navigation

- [Materials Index](../README.en.md)
- [Shared Rubric](rubric.en.md)
- [AI Use Log Template](ai-use-log.en.md)
- [繁體中文版](preparatory-assignments.zh-TW.md)
