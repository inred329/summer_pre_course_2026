# Materials and Activity Resources

Version: 1.2.0  
Status: Preparatory materials, assessment policy, and instructor implementation pack complete  
Last updated: 2026-08-03  
Major change summary: Added bilingual instructor implementation guidance and a material-assessment precedence rule, completing the directly teachable preparatory-course baseline.  
Corresponding Chinese version: [教材與活動資源](README.zh-TW.md)

## Document Purpose

This directory provides materials, activities, independent homework, classroom discussion, participation observation, AI-use records, instructor implementation, and final oral-exam preparation resources for both preparatory tracks.

Every official material must:

- Be reachable from the root README and this index.
- Be available in both Traditional Chinese and English.
- Cite requirement IDs, competency IDs, maturity targets, scope states, and acceptance tasks.
- Include reading, prediction, implementation, modification, testing, debugging, and explanation.
- State specific permitted, prohibited, and retained evidence for AI use.
- Never treat homework submission, roll call, or one successful output as capability evidence.

## Official Preparatory Materials

| Unit | Chinese Material | English Material | Core Delivery |
|---|---|---|---|
| 1 | [程式如何開始執行](preparatory/unit-01-execution.zh-TW.md) | [How a Program Begins to Run](preparatory/unit-01-execution.en.md) | Toolchain, minimal program, prediction, and error classification |
| 2 | [資料、型別與程式狀態](preparatory/unit-02-data-state.zh-TW.md) | [Data, Types, and Program State](preparatory/unit-02-data-state.en.md) | Values, types, state tracing, input/output, and requirement modification |
| 3 | [條件、迴圈與控制流程](preparatory/unit-03-control-flow.zh-TW.md) | [Conditions, Loops, and Control Flow](preparatory/unit-03-control-flow.en.md) | Paths, termination, boundary testing, and defect diagnosis |
| 4 | [函數、整合開發與 AI 驗證](preparatory/unit-04-functions-integration.zh-TW.md) | [Functions, Integrated Development, and AI Verification](preparatory/unit-04-functions-integration.en.md) | Function responsibility, integrated cycle, regression, and AI review |

The Chinese track delivers four sessions. The English track divides Unit 4 across Sessions 4 and 5. Core competencies, difficulty, and assessment standards are identical.

## Instructor Implementation Resources

- [前導課程教師執行指引](instructor/session-guides.zh-TW.md)
- [Preparatory Course Instructor Implementation Guide](instructor/session-guides.en.md)
- [前導教材評量制度補充規則](preparatory/ASSESSMENT-NOTE.zh-TW.md)
- [Preparatory Material Assessment Override](preparatory/ASSESSMENT-NOTE.en.md)

The instructor guide includes:

- Pacing for four Chinese sessions and five English sessions.
- Previous-homework discussion time in each class.
- Required error cases and incorrect AI suggestions.
- Participation-observation points.
- Fallback strategies for time shortage and tool failure.

When a unit still contains legacy wording such as submission, remediation, or micro-oral, the assessment override and `design/07` plus `design/13` take precedence.

## Independent Homework and Assessment Resources

- [自主作業與口試準備包](assignments/preparatory-assignments.zh-TW.md)
- [Independent Homework and Oral Preparation Pack](assignments/preparatory-assignments.en.md)
- [課堂參與與最終口試評分規準](assignments/rubric.zh-TW.md)
- [Classroom Participation and Final Oral Examination Rubric](assignments/rubric.en.md)
- [AI 使用紀錄模板](assignments/ai-use-log.zh-TW.md)
- [AI Use Log Template](assignments/ai-use-log.en.md)
- [作業討論與課堂參與觀察指引](assignments/grading-guide.zh-TW.md)
- [Assignment Discussion and Participation Observation Guide](assignments/grading-guide.en.md)

## Official Policy

- Homework is not submitted, graded, or individually marked.
- Each class begins with 15–25 minutes of previous-homework discussion.
- Roll call is not graded; attendance is not participation.
- Participation may be verbal, written, anonymous, program-based, or recorded through group work.
- One final one-on-one oral examination is the only summative assessment.
- Students keep homework and learning records for discussion and oral-exam preparation.

## Material Templates

- [單元教材模板](TEMPLATE.zh-TW.md)
- [Unit Material Template](TEMPLATE.en.md)

## Review Records

- [前導教材憲法遵循審查](reviews/materials-constitution-review.zh-TW.md)
- [Preparatory Materials Constitution Review](reviews/materials-constitution-review.en.md)

## Next Stage

- Create directly compilable C17 examples and defective programs for every unit.
- Verify GCC/Clang and Windows/Linux commands in the actual classroom environment.
- Create a bilingual-equivalent library of incorrect AI suggestions.
- Clean legacy assessment wording from each unit document.
- After later discussion, create the formal bilingual final one-on-one oral-examination content and procedure document.

## Navigation

- [Learning and Assessment Policy](../design/13-learning-assessment-policy.en.md)
- [Back to repository home](../README.md)
- [Instructional Design Workspace](../design/README.en.md)
- [繁體中文版](README.zh-TW.md)
