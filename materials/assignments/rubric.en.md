# Classroom Participation and Final Oral Examination Rubric

Version: 0.2.0  
Status: Official grading baseline  
Last updated: 2026-08-03  
Major change summary: Replaced per-assignment grading with classroom participation and one final one-to-one oral examination.  
Corresponding Chinese version: [課堂參與與最終口試評分規準](rubric.zh-TW.md)

## Document Purpose

For instructors and teaching assistants evaluating classroom participation and the final one-to-one oral examination. Assignments are not submitted or graded; they serve as formative learning, classroom-discussion, and final-examination materials.

## 1. Grade Structure

| Component | Suggested Weight | Role |
|---|---:|---|
| Classroom participation | 20–30% | Ongoing formative engagement |
| Final one-to-one oral examination | 70–80% | Sole summative capability assessment |

The announced percentage may vary, but the final oral examination must remain the primary source of the grade.

---

# 2. Classroom Participation Rubric

Participation is not attendance, speaking frequency, or a reward only for extroverted students.

## Observable Evidence

- Raising a concrete question or obstacle.
- Responding to an instructor or peer.
- Participating in tracing, testing, debugging, or comparison activities.
- Sharing an error and the reason for its correction.
- Proposing a test case.
- Revising earlier reasoning.
- Helping a peer understand without doing the work for them.
- Participating through writing, code operation, anonymous questions, or short reflection.

## Four Performance Levels

| Level | Criterion |
|---|---|
| 4 Consistent engagement | Regularly contributes concrete questions, reasoning, tests, error analysis, or correction evidence and supports understanding. |
| 3 Effective engagement | Shows observable participation across multiple activities and can raise or respond to specific content. |
| 2 Occasional engagement | Participates sometimes, but evidence is passive, fragmented, or inconsistent. |
| 1 Insufficient evidence | Little observable learning participation; presence alone is not participation. |

Instructors should judge the overall pattern across multiple classes rather than mechanically counting comments.

---

# 3. Final One-to-One Oral Examination Rubric

The student's own assignments, programs, tests, errors, and learning records are the primary examination materials.

## Dimensions

| Dimension | Suggested Weight | Main Evidence |
|---|---:|---|
| Requirement understanding and program reading | 20% | Identifies inputs, outputs, rules, data, and major structure |
| Execution tracing and mental model | 20% | Traces state, control paths, or function calls step by step |
| Live modification and implementation | 20% | Modifies a small requirement and explains the impact |
| Testing, debugging, and regression verification | 25% | Creates tests, locates errors, verifies corrections, and checks prior behavior |
| Explanation, reflection, and AI judgment | 15% | Answers follow-ups and explains trade-offs and AI verification |

## Four Performance Levels

### Requirement Understanding and Program Reading

- 4: Clearly identifies the problem, data, control, and responsibilities and explains design reasons and limits.
- 3: Correctly explains the main requirement and structure with minor prompting.
- 2: Describes only part of the behavior and has incomplete understanding of data or responsibility.
- 1: Cannot explain the program or mainly relies on memorization.

### Execution Tracing and Mental Model

- 4: Trace is complete and consistent with the program and identifies key transitions and possible faults.
- 3: Main trace is correct with minor corrections.
- 2: Gives only final output or frequently contradicts actual execution.
- 1: Cannot trace execution.

### Live Modification and Implementation

- 4: Identifies affected parts, completes the change, and preserves readability.
- 3: Completes the core change with occasional prompting.
- 2: Mainly relies on trial and error and often breaks prior behavior.
- 1: Cannot modify the work or can only copy an external answer.

### Testing, Debugging, and Regression Verification

- 4: Independently creates normal, boundary, and necessary exceptional tests, diagnoses with evidence, and completes regression verification.
- 3: Creates reasonable tests and completes basic diagnosis and regression checks.
- 2: Tests only one case or provides a correction without evidence.
- 1: Replaces verification with successful execution or an AI judgment.

### Explanation, Reflection, and AI Judgment

- 4: Answers follow-ups clearly and explains limitations, trade-offs, and evidence used to verify AI suggestions.
- 3: Explains core decisions and how AI was used.
- 2: Explanation is fragmented and cannot clearly separate personal judgment from AI suggestions.
- 1: Cannot explain the work or uses “AI said so” as the reason.

## Core Capability Thresholds

A total score may not hide a core capability gap. The oral examination may not be passed directly when any of the following applies:

- Cannot explain the core program.
- Cannot complete any small requirement change.
- Cannot independently create at least one valid test.
- Trace clearly contradicts actual program behavior.
- AI was used but its suggestion cannot be explained or verified.

Remediation or reassessment procedures will be defined when the detailed oral-examination process is finalized.

## Fairness Principles

- Do not deduct marks because a reasonable solution differs from the example.
- Both language tracks use the same capability criteria.
- Language-expression errors affect evaluation only when they prevent technical understanding.
- Tool failure requires a fallback environment or equivalent oral, paper, and code evidence.
- Participation supports multiple expression modes and does not reward extroversion alone.

## Navigation

- [Learning and Assessment Policy](../../design/13-learning-assessment-policy.en.md)
- [Assignment Pack](preparatory-assignments.en.md)
- [繁體中文版](rubric.zh-TW.md)
