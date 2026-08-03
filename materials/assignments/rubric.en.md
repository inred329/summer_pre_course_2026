# Shared Preparatory Assignment Rubric

Version: 0.1.0  
Status: Official grading draft  
Last updated: 2026-08-03  
Major change summary: Established the shared capability-oriented grading and remediation baseline for all preparatory assignments.  
Corresponding Chinese version: [前導課程共用評分規準](rubric.zh-TW.md)

## Document Purpose

For instructors and teaching assistants assessing preparatory assignments. Grading centers on capability and evidence rather than one-time program success or similarity to a model solution.

## Grading Dimensions

| Dimension | Weight | Main Evidence |
|---|---:|---|
| Requirement understanding and prediction | 20% | Requirement analysis, expected results, flow or responsibility diagram |
| Correct implementation within current scope | 25% | Program, compilation, and execution results |
| Tracing, testing, and verification | 25% | State tables, normal/boundary/exceptional cases, expected-versus-actual comparison |
| Modification, debugging, and regression verification | 20% | Defect record, requirement change, regression tests |
| Explanation, reflection, and AI judgment | 10% | Oral check, reflection, AI-use record |

A total score may not conceal a core capability gap. Any of the following requires remediation even when the numerical total is sufficient:

- Cannot explain the core program.
- Trace contradicts program behavior.
- No self-created expected result or test.
- No regression testing after a requirement change.
- AI was used but its suggestion cannot be explained or verified.

## Four Performance Levels

| Level | Description |
|---|---|
| 4 Consistently Achieved | Evidence is complete and mutually consistent; the work can be explained, modified, and verified. |
| 3 Achieved | Core requirements are met; small non-core omissions do not undermine capability. |
| 2 Partially Achieved | A program or some evidence exists, but understanding, tracing, testing, or modification has a major gap. |
| 1 Not Established | Work mainly depends on guessing, imitation, or a complete answer and lacks trustworthy evidence. |

## Dimension Criteria

### Requirement Understanding and Prediction

- 4: Clearly identifies inputs, outputs, rules, and constraints; expected results are correct and include boundaries.
- 3: Main requirements and predictions are correct with only small omissions.
- 2: Describes part of the requirement, but predictions are incomplete or written after execution.
- 1: Cannot explain the requirement or infers reasoning from the final answer.

### Correct Implementation

- 4: Satisfies the specification, current scope, and readability expectations and can explain the main structure.
- 3: Main behavior is correct with minor non-core issues.
- 2: Only part of the behavior works or only one sample succeeds.
- 1: Does not run, clearly exceeds scope, or cannot be explained by the student.

### Tracing, Testing, and Verification

- 4: Trace matches the program; tests include normal, boundary, and necessary exceptional cases; trustworthiness can be explained.
- 3: Reasonable trace and multiple test categories with small omissions.
- 2: Only a few samples or an incorrect trace.
- 1: Only output or OJ success is shown.

### Modification, Debugging, and Regression

- 4: Locates problems with evidence, explains the correction, and performs complete regression testing.
- 3: Completes the change and basic regression testing, but diagnostic explanation is weaker.
- 2: Primarily uses trial-and-error and does not fully check prior behavior.
- 1: Merely replaces the work with a version supplied by another person or AI.

### Explanation, Reflection, and AI Judgment

- 4: Answers follow-up questions and clearly explains limitations and evidence behind AI decisions.
- 3: Explains core behavior and main decisions.
- 2: Explanation is fragmented; AI record is pasted without verification or is incomplete.
- 1: Cannot explain the submitted work.

## Decision

- Pass: every core dimension is at least level 3 and no mandatory-remediation condition applies.
- Conditional pass: a non-core omission can be completed by a specified deadline.
- Remediation: one or a small number of capability gaps require a targeted task.
- Not passed: multiple core capabilities are missing, or student understanding and verification cannot be established.

## Fairness Principles

- Do not deduct marks solely because a reasonable solution differs from the example.
- Both language tracks use the same criteria.
- Language-expression errors affect capability judgment only when they prevent technical understanding.
- Tool failure does not directly lower learning evaluation; use a fallback environment or equivalent evidence.

## Navigation

- [Assignment Pack](preparatory-assignments.en.md)
- [繁體中文版](rubric.zh-TW.md)
