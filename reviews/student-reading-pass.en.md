# Student Reading Pass

Version: 0.2.0  
Last updated: 2026-08-09  
Corresponding Chinese version: [學生閱讀體驗審查](student-reading-pass.zh-TW.md)

## Purpose

This record tracks the actual reading experience of student-facing materials. The pass is not primarily a governance or compliance review. Each Unit is read from beginning to end to see whether a student can follow its story, concepts, and activities without unnecessary friction.

Each Unit is checked for:

- whether the opening quickly establishes a useful question or motivation;
- whether concepts and terms appear when they are needed and have enough preparation;
- whether sections connect through a natural learning sequence;
- whether examples, defect cases, and exercises improve understanding instead of adding mechanical checklists;
- whether internal governance, assessment, or document-boundary language intrudes on the student reading path;
- whether the ending creates a natural bridge to the next Unit;
- whether the Chinese and English versions preserve the same learning path and technical meaning.

## Progress

| Unit | Chinese | English | Status | Main work |
|---|---|---|---|---|
| P-U01 Program execution path | Complete | Complete | First pass complete | Reworked the opening and transitions; reduced governance language; turned checklist-like activities into an experimental narrative; simplified the optional AI note; strengthened the edit → compile → run → observe thread; improved the bridge to the next Unit. |
| P-U02 Data, types, and state | Complete | Complete | First pass complete | Connected directly from P-U01; used changing `score` state as the narrative spine; framed `if` and `&score` as previews rather than prerequisites; removed the conceptual jump that asked students to implement the 100-point cap before learning conditions, and turned that failure into the bridge to P-U03. |
| P-U03 Control flow | Pending | Pending | Not started | — |
| P-U04 Functions and integration | Pending | Pending | Not started | — |
| F-U01–F-U12 | Pending | Pending | Not started | — |

## P-U01 Reading Observation

The original version was technically complete, but it opened with “Document Purpose and Completion Standard,” submission guidance, and AI policy before the student encountered the first programming question. Several later sections also used constraints, record-keeping suggestions, and test-table language that made the chapter feel closer to an operating specification than a continuous learning story.

After the first pass, P-U01 begins directly with the question of what actually happens after a C text file is saved. The chapter now keeps returning to the same `hello.c` experiment and connects prediction, real execution, deliberate defects, and requirement changes into one narrative. The Chinese and English versions preserve equivalent section order, questions, experiments, and closing transition.

## P-U02 Reading Observation

The original version also began with completion standards, record-keeping instructions, and AI policy before reaching the learner’s real question of how a running program keeps data. More importantly, it introduced `if` before control flow had been taught and later required students to implement a “maximum score of 100” rule, forcing them to use the next Unit’s central concept before it had been established.

After the first pass, P-U02 grows directly from P-U01’s fixed output into the question of what remains inside a running program. The statement `score = score + 5` now anchors value, type, variable, assignment, and state. The input example still keeps the safe success check, but clearly tells students that `if` and `&score` only need to be understood by purpose for now. The former immediate implementation of the 100-point cap is now an intentionally unresolved requirement: students see `98 + 5` produce `103`, which creates a natural need for “choosing different paths” and leads directly into P-U03.

## Completion Condition

The Student Reading Pass is complete only after P-U01–P-U04 and F-U01–F-U12 have all been read end to end, major reading barriers have been corrected, and students can understand the materials without relying on design, review, or other internal documents.