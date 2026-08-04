# Assignment Discussion and Participation Observation Guide

Version: 0.3.0  
Status: Official instructor implementation baseline  
Last updated: 2026-08-05  
Major change summary: Retains assignment discussion and inclusive participation observation while making AI examples optional external-suggestion cases rather than required evidence in every Unit or final-oral preparation.  
Corresponding Chinese version: [作業討論與課堂參與觀察指引](grading-guide.zh-TW.md)

## Document Purpose

For instructors and teaching assistants to facilitate discussion of the previous assignment, observe classroom participation, provide formative feedback, and prepare students for the final oral examination. Assignments are not submitted, graded, or marked one by one.

## 1. Assignment Discussion at the Start of Class

Ordinarily reserve 15–25 minutes:

1. Invite students to raise obstacles, errors, or alternative solutions.
2. Select one or two representative issues for class tracing.
3. Require prediction before execution or inspection.
4. Compare expected and actual behavior.
5. Guide with follow-up questions rather than posting a complete answer.
6. After correction, create tests and run regression verification.
7. Summarize the principle that transfers into the new Unit.

When no student volunteers a question, use an anonymous error case, common defect, optional incorrect external suggestion, or two reasonable alternatives to begin discussion.

## 2. Instructor Questioning

Prefer questions such as:

- What did you expect?
- What actually happened?
- Where is the first inconsistency?
- What does this variable represent?
- What happens with a boundary input?
- Which tests are affected by this change?
- How do you know the correction did not break prior behavior?
- Which assumption in this external suggestion needs verification?

Avoid immediately giving a complete corrected version or relying on memorized syntax definitions.

## 3. Participation Observation

Participation evidence includes:

- Raising a concrete question or describing an obstacle.
- Answering or revising reasoning.
- Participating in tracing, testing, debugging, or comparison.
- Sharing an error the student made.
- Proposing a test case.
- Helping a peer without doing the work for them.
- Using writing, code operation, anonymous questions, or short reflection.

Do not judge participation through:

- Presence alone.
- A speaking-frequency ranking.
- Rewarding only the fastest responders.
- Treating silence as proof of no learning.

Record the overall pattern across multiple classes with brief observation codes or notes; do not assign points for every comment.

## 4. Deliberately Designed Opportunities to Make Mistakes

Prepare at least:

- One syntax or compilation error.
- One logic, boundary, or termination error.
- One small requirement change.

When useful, add one plausible but incorrect external suggestion. Its source may be AI, a search result, a documentation misreading, or a peer claim; it is not required in every Unit.

Use errors to practice reproduction, hypothesis, verification, correction, and regression rather than to shame students.

## 5. No Single-Answer Policy

Instructors may prepare reference solutions, but class learning should emphasize:

- Deriving solutions.
- Comparing multiple reasonable forms.
- Discussing trade-offs.
- Verifying through tests.

Do not reject a solution merely because it differs from the example when it satisfies the requirement, current scope, safety, and readability.

## 6. Bilingual and Participation Fairness

- Both tracks use the same capability and participation standards.
- The English-taught track may use terminology cards, sentence scaffolds, more reading time, and written responses.
- Additional time in the Chinese-taught track supports more tracing, discussion, and remediation rather than higher requirements.
- Introverted students may participate through anonymous questions, written traces, group activity, or code operation.
- Technical understanding matters more than verbal polish.

## 7. Tool Failure

When tools fail:

1. Record the environment problem.
2. Switch to a fallback environment.
3. Preserve prediction, tracing, testing, and explanation.
4. Use paper tracing, instructor equipment, or peer screen sharing.
5. Do not treat equipment failure as non-participation or missing capability.

## 8. External Suggestions and AI Use

- AI is not a fixed activity and is not a participation or assignment completion requirement.
- When a student used AI or another external suggestion, instructors may ask what the original understanding was, how the suggestion was verified, and why it was accepted or rejected.
- Do not automatically deduct for AI use, and do not require a declaration from students who did not use it.
- Correct output does not replace understanding, testing, and evidence-based judgment.

## 9. Final Oral Preparation

Near the end of the course, remind students to organize:

- Their assignments and different versions.
- Representative errors and corrections.
- Test and regression records.
- Concepts that remained uncertain or were later revised.
- When relevant, one optional example of an external suggestion they verified or rejected.

Instructors may demonstrate the kinds of capabilities the oral examination will use, while detailed content and procedure are defined separately.

## 10. Pre-Grade Check

- [ ] Participation was not calculated from attendance or speaking count.
- [ ] Multiple participation modes were available.
- [ ] Each class ordinarily preserved previous-assignment discussion time.
- [ ] Assignments were neither individually graded nor required for submission.
- [ ] The final oral examination remained the main grade source.
- [ ] Standards were equivalent across language tracks.
- [ ] AI was not required; when used, judgment focused on understanding and verification.
- [ ] Student safety, dignity, and fairness were prioritized.

## Navigation

- [Learning and Assessment Policy](../../design/13-learning-assessment-policy.en.md)
- [Independent Assignment and Oral Preparation Pack](preparatory-assignments.en.md)
- [Classroom Participation and Final Oral Examination Rubric](rubric.en.md)
- [繁體中文版](grading-guide.zh-TW.md)
