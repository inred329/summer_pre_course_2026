# Materials and Activity Resources

Version: 1.4.0  
Status: Complete bilingual student materials for 16 Units with constitution and technical validation completed  
Last updated: 2026-08-05  
Major change summary: Completed bilingual technical validation across all 16 Units, corrected confirmed C17 and navigation defects, and added the all-Unit validation report.  
Corresponding Chinese version: [教材與活動資源](README.zh-TW.md)

## Document Purpose

This directory provides bilingual student materials for the preparatory and formal courses, together with independent homework, classroom-discussion, instructor-delivery, assessment, and maintenance resources.

Student materials center independent reading, prediction, implementation, tracing, testing, debugging, modification, and explanation. AI appears only as a brief concept-conversation audience at the end of each Unit; fixed prompts, mandatory conversation logs, and treating AI responses as evidence are not required.

## Official Preparatory Materials

| Unit | Traditional Chinese | English | Central focus |
|---|---|---|---|
| P-U01 | [程式如何從文字變成執行結果？](preparatory/unit-01-execution.zh-TW.md) | [How Does Program Text Become an Execution Result?](preparatory/unit-01-execution.en.md) | source code, compilation, executables, prediction, and error classification |
| P-U02 | [程式如何記住資料並改變狀態？](preparatory/unit-02-data-state.zh-TW.md) | [How Does a Program Remember Data and Change State?](preparatory/unit-02-data-state.en.md) | values, types, variables, state tracing, and input/output |
| P-U03 | [程式如何選擇與重複？](preparatory/unit-03-control-flow.zh-TW.md) | [How Does a Program Select and Repeat?](preparatory/unit-03-control-flow.en.md) | conditions, loops, termination, boundaries, and diagnosis |
| P-U04 | [如何把大問題拆成可理解的工作？](preparatory/unit-04-functions-integration.zh-TW.md) | [How Can a Large Problem Be Divided into Understandable Work?](preparatory/unit-04-functions-integration.en.md) | function responsibility, interfaces, testing, modification, and regression |

## Formal-Course Materials

- [正式課程學生教材](formal/README.zh-TW.md)
- [Formal Course Student Materials](formal/README.en.md)

The formal course contains F-U01 through F-U12 and covers representation and types, control flow, arrays, strings, call stacks, recursion, pointers, structures, dynamic memory, files, modular programming, testing and debugging, and integrated applications.

## Shared Standard for Student Materials

Every official Unit should include:

- document purpose and completion standard
- core question, learning objectives, and prerequisite Concepts
- appropriate prediction or reasoning activity
- visual model
- core Concepts and a minimal example
- execution, state, or memory tracing
- a reproducible, diagnosable, and correctable error case
- guided practice, independent practice, testing, and requirement modification
- a brief concept explanation to AI
- a reminder that AI responses still require judgment through programs, tests, and reproducible results
- self-check, summary, and forward/back navigation

Independent activities in student materials are not submitted, graded, or individually marked. Students may keep predictions, programs, errors, and corrections for classroom discussion and review.

## Instructor Implementation Resources

- [前導課程教師執行指引](instructor/session-guides.zh-TW.md)
- [Preparatory Course Instructor Implementation Guide](instructor/session-guides.en.md)
- [前導教材評量制度補充規則](preparatory/ASSESSMENT-NOTE.zh-TW.md)
- [Preparatory Material Assessment Override](preparatory/ASSESSMENT-NOTE.en.md)

Instructor guides carry pacing, homework discussion, participation observation, fallback strategies, and representative error cases. Student chapters do not carry instructor scheduling or grading administration.

## Independent Homework and Assessment Resources

- [自主作業與口試準備包](assignments/preparatory-assignments.zh-TW.md)
- [Independent Homework and Oral Preparation Pack](assignments/preparatory-assignments.en.md)
- [課堂參與與最終口試評分規準](assignments/rubric.zh-TW.md)
- [Classroom Participation and Final Oral Examination Rubric](assignments/rubric.en.md)
- [作業討論與課堂參與觀察指引](assignments/grading-guide.zh-TW.md)
- [Assignment Discussion and Participation Observation Guide](assignments/grading-guide.en.md)

The existing AI-use log template remains an optional extension resource. It is not a completion requirement for every Unit and students are not required to use it routinely.

## Official Policy

- Independent homework may follow each class but is not submitted, graded, or individually marked.
- The next class reserves 15–25 minutes to discuss previous homework, errors, tests, and alternative solutions.
- Roll call is not graded; attendance is not participation.
- Participation may be shown verbally, in writing, through anonymous questions, program operation, tracing, testing, or group records.
- The official grade consists only of classroom participation and one final one-on-one oral examination.
- Students keep homework and learning records for discussion and oral-examination preparation.

## Material Templates

- [單元教材模板](TEMPLATE.zh-TW.md)
- [Unit Material Template](TEMPLATE.en.md)

## Review Records

- [前導教材憲法遵循審查](reviews/materials-constitution-review.zh-TW.md)
- [Preparatory Materials Constitution Review](reviews/materials-constitution-review.en.md)
- [P-U01 憲法遵循審查](reviews/pu01-constitution-review.zh-TW.md)
- [P-U01 Constitution Compliance Review](reviews/pu01-constitution-review.en.md)
- [全文件憲法遵循重審](reviews/all-documents-constitution-review.zh-TW.md)
- [Repository-Wide Constitution Compliance Review](reviews/all-documents-constitution-review.en.md)
- [全 Unit 技術驗證報告](reviews/all-units-technical-validation.zh-TW.md)
- [All-Unit Technical Validation Report](reviews/all-units-technical-validation.en.md)

## Technical Validation Status

The current technical review stage is complete for all 16 Units. The validation report records C17 contracts, input and boundary behavior, intentional-error classification, bilingual equivalence, and navigation corrections.

Continuous improvements may later add automated Markdown code extraction, CI compilation, link checking, and classroom-toolchain smoke tests. These are maintenance enhancements rather than unresolved document defects.

## Next Stage

- Conduct a final human review of teaching depth and cognitive load.
- Divide the validated Units into actual Lessons and course weeks.
- Build optional CI checks for code blocks, bilingual pairs, and links.
- Pilot the materials in the target classroom environments and record teaching adjustments.

## Navigation

- [Learning and Assessment Policy](../design/13-learning-assessment-policy.en.md)
- [Back to repository home](../README.md)
- [Instructional Design Workspace](../design/README.en.md)
- [繁體中文版](README.zh-TW.md)
