# Materials and Activity Resources

Version: 1.5.0  
Status: Current materials entry point; repository-wide Constitution 2.0 review in progress  
Last updated: 2026-08-06  
Major change summary: Reorganized entry points by primary audience, removed duplicated assessment policy and implied mandatory AI use, and clarified the status of prior review records.  
Corresponding Chinese version: [教材與活動資源](README.zh-TW.md)

## Document Purpose

This file is the navigation entry for `materials/`. It does not replace the assessment policy, Course Constitution, or material-writing standards.

Choose an entry point by role:

- Students: read preparatory and formal-course materials and use independent-homework and oral-preparation resources.
- Instructors: use delivery guides, classroom activities, participation-observation guidance, and rubrics.
- Authors and maintainers: use material templates, technical-validation records, and review records.

AI is optional by default in this course. Not using AI does not affect Unit completion, classroom participation, or assessment. When a material includes an AI activity, it must be clearly marked as a skippable optional extension. Core objectives and self-checks must not depend on AI.

## Student Entry Points

### Preparatory Course

| Unit | Traditional Chinese | English | Central focus |
|---|---|---|---|
| P-U01 | [程式如何從文字變成執行結果？](preparatory/unit-01-execution.zh-TW.md) | [How Does Program Text Become an Execution Result?](preparatory/unit-01-execution.en.md) | source code, compilation, executables, prediction, and error classification |
| P-U02 | [程式如何記住資料並改變狀態？](preparatory/unit-02-data-state.zh-TW.md) | [How Does a Program Remember Data and Change State?](preparatory/unit-02-data-state.en.md) | values, types, variables, state tracing, and input/output |
| P-U03 | [程式如何選擇與重複？](preparatory/unit-03-control-flow.zh-TW.md) | [How Does a Program Select and Repeat?](preparatory/unit-03-control-flow.en.md) | conditions, loops, termination, boundaries, and diagnosis |
| P-U04 | [如何把大問題拆成可理解的工作？](preparatory/unit-04-functions-integration.zh-TW.md) | [How Can a Large Problem Be Divided into Understandable Work?](preparatory/unit-04-functions-integration.en.md) | function responsibility, interfaces, testing, modification, and regression |

### Formal Course

- [正式課程學生教材索引](formal/README.zh-TW.md)
- [Formal Course Student Materials](formal/README.en.md)

The formal course includes F-U01 through F-U12 and covers representation and types, control flow, arrays, strings, call stacks, recursion, pointers, structures, dynamic memory, files, modular programming, testing and debugging, and integrated applications.

### Independent Homework and Oral Preparation

- [自主作業與口試準備包](assignments/preparatory-assignments.zh-TW.md)
- [Independent Homework and Oral Preparation Pack](assignments/preparatory-assignments.en.md)

Submission, grading, participation, and final-oral rules are defined only by the official learning and assessment policy:

- [學習與評量制度](../design/13-learning-assessment-policy.zh-TW.md)
- [Learning and Assessment Policy](../design/13-learning-assessment-policy.en.md)

## Instructor Entry Points

- [前導課程教師執行指引](instructor/session-guides.zh-TW.md)
- [Preparatory Course Instructor Implementation Guide](instructor/session-guides.en.md)
- [課堂參與與最終口試評分規準](assignments/rubric.zh-TW.md)
- [Classroom Participation and Final Oral Examination Rubric](assignments/rubric.en.md)
- [作業討論與課堂參與觀察指引](assignments/grading-guide.zh-TW.md)
- [Assignment Discussion and Participation Observation Guide](assignments/grading-guide.en.md)

Instructor documents carry pacing, homework discussion, misconceptions, representative errors, fallback activities, equitable participation modes, and assessment implementation. Student chapters should not contain instructor scheduling, grading administration, or answer-revealing prompts.

`preparatory/ASSESSMENT-NOTE.*` is a non-normative migration note for legacy wording. It is not policy and does not override the official assessment policy:

- [前導教材評量措辭遷移說明](preparatory/ASSESSMENT-NOTE.zh-TW.md)
- [Preparatory Assessment Wording Migration Note](preparatory/ASSESSMENT-NOTE.en.md)

## Author and Maintainer Entry Points

### Material Templates

- [單元教材模板](TEMPLATE.zh-TW.md)
- [Unit Material Template](TEMPLATE.en.md)

The template provides a suggested structure and a prepublication check. It does not replace Constitution 2.0, the official assessment policy, or instructional judgment for an individual Unit.

### Technical Validation

- [全 Unit 技術驗證報告](reviews/all-units-technical-validation.zh-TW.md)
- [All-Unit Technical Validation Report](reviews/all-units-technical-validation.en.md)
- [C17 Examples and Defect Cases](../examples/README.md)

Technical validation can confirm compilation, execution, test data, and known technical issues. It cannot by itself prove readability, instructional sequencing, or appropriate cognitive load.

### Review Records

The following files record reviews performed at particular times under particular constitutional baselines. When they conflict with Constitution 2.0 or the active repository-wide audit, the current baseline prevails:

- [前導教材憲法遵循審查](reviews/materials-constitution-review.zh-TW.md)
- [Preparatory Materials Constitution Review](reviews/materials-constitution-review.en.md)
- [P-U01 憲法遵循審查](reviews/pu01-constitution-review.zh-TW.md)
- [P-U01 Constitution Compliance Review](reviews/pu01-constitution-review.en.md)
- [全文件憲法遵循重審](reviews/all-documents-constitution-review.zh-TW.md)
- [Repository-Wide Constitution Compliance Review](reviews/all-documents-constitution-review.en.md)

Active repository-wide audit:

- [Constitution 2.0 全庫符合性審查](../reviews/repository-constitution-2-audit.zh-TW.md)
- [Repository-Wide Constitution 2.0 Compliance Audit](../reviews/repository-constitution-2-audit.en.md)

## Shared Principles for Student Materials

Student materials should select a structure appropriate to their teaching purpose. Every Unit is not required to reproduce an identical mechanical outline. Core principles include:

- State the core question, completion standard, and prerequisites clearly.
- Establish a problem, need, or mental model before introducing syntax.
- Use prediction, tracing, testing, debugging, and requirement modification when they serve the learning goal.
- Distinguish complete programs, fragments, pseudocode, and intentionally defective examples.
- Do not treat successful compilation, correct output, passing an OJ, or tool approval as sole evidence of capability.
- AI activities may appear only as clearly labeled, directly skippable optional extensions.
- Core completion standards and self-checks must not require AI use or AI records.
- Preserve substantive bilingual equivalence while allowing sentence structure and explanatory examples to differ for readability.

## Navigation

- [Back to Repository Home](../README.md)
- [Instructional Design Workspace](../design/README.en.md)
- [Course Constitution 2.0](../CONSTITUTION.en.md)
- [繁體中文版](README.zh-TW.md)
