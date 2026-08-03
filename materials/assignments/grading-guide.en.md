# Preparatory Grading Guide for Instructors and TAs

Version: 0.1.0  
Status: Official instructor draft  
Last updated: 2026-08-03  
Major change summary: Established assignment-evidence review, micro-oral checks, fair judgment, and remediation procedures.  
Corresponding Chinese version: [前導課程教師與助教批改指引](grading-guide.zh-TW.md)

## Document Purpose

For instructors and teaching assistants to grade assignments, provide formative feedback, conduct micro-oral checks, and run remediation consistently. Program output or automated-test results alone are insufficient.

## 1. Grading Sequence

1. Confirm requirements, competencies, scope, and required evidence.
2. Read the student's pre-execution understanding, predictions, and tests.
3. Check whether the program satisfies the specification and current scope.
4. Compare tracing, expected results, and actual behavior for consistency.
5. Review requirement modification, defect diagnosis, and regression testing.
6. When AI was used, review transparency and technical verification.
7. Sample core capability with one to three micro-oral questions.
8. Decide pass, conditional pass, remediation, or not passed according to the missing capability.

## 2. Prohibited Shortcuts

- Looking only at whether the program compiles.
- Looking only at OJ or test pass rate.
- Deducting marks solely because the program differs from a model answer.
- Lowering programming-capability judgment because English expression is not fluent.
- Automatically failing any AI use, or failing to review AI use at all.
- Letting a total score conceal a core gap such as inability to explain, lack of tests, or lack of regression verification.

## 3. Micro-Oral Principles

- Use the student's own program but change an input, threshold, or requirement.
- Ask questions such as “What is the next state?”, “Why is this test important?”, or “What changes here affect elsewhere?”
- Do not require memorized syntax definitions.
- AI may not answer live.
- Usually limit the check to 2–5 minutes.

## 4. Remediation Mapping

| Gap | Remediation |
|---|---|
| Execution model | Classify a new error and draw the toolchain |
| State understanding | Live-trace new values |
| Condition / loop | Locate and correct a boundary or termination defect |
| Function understanding | Modify an interface and trace parameters and return values |
| Insufficient testing | Add normal, boundary, and necessary exceptional cases |
| Insufficient debugging | Reproduce, hypothesize, verify, correct, and regress |
| Insufficient AI verification | Review a new incorrect suggestion with evidence |

Remediation targets the missing capability rather than requiring indiscriminate resubmission of the entire assignment.

## 5. Bilingual Fairness

- Both tracks use the same rubric, competency IDs, and passing standards.
- The English-taught track may use terminology cards, sentence scaffolds, and additional reading time.
- The Chinese-taught track's additional time supports tracing, remediation, diagnosis, and acceptance rather than additional core requirements.
- Technical understanding may be expressed through diagrams, tables, traces, or concise language; verbal polish is not technical maturity.

## 6. Tool Failure

When tools fail:

1. Record the environment problem.
2. Switch to a fallback environment.
3. Preserve prediction, tracing, testing, and explanation activities.
4. Do not directly judge capability as missing merely because the original device could not run the program.

## 7. AI-Use Judgment

Valid AI use includes:

- Understanding and approach before AI use.
- Tests created by the student first.
- Summary of the AI suggestion.
- A reproducible verification method.
- Reason for accepting, modifying, or rejecting.

When code is correct but the student cannot explain AI-influenced parts, arrange oral and requirement-change remediation rather than replacing evidence with a guess about intent.

## 8. Pre-Release Grade Check

- [ ] Both understanding-oriented and action-oriented evidence were reviewed.
- [ ] Output, compilation, or OJ was not used alone.
- [ ] Reasonable alternative solutions were allowed.
- [ ] Remediation directly maps to the missing capability.
- [ ] Standards are equivalent across language tracks.
- [ ] AI use was judged through transparency and verification.
- [ ] Student safety, dignity, and fairness were prioritized.

## Navigation

- [Assignment Pack](preparatory-assignments.en.md)
- [Shared Rubric](rubric.en.md)
- [繁體中文版](grading-guide.zh-TW.md)
