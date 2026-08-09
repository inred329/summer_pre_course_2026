# Student Reading Pass

Version: 0.8.0  
Last updated: 2026-08-09  
Corresponding Chinese version: [學生閱讀體驗審查](student-reading-pass.zh-TW.md)

## Purpose

Read every student-facing Unit from a learner's point of view and check opening motivation, concept timing, section transitions, whether examples actually support understanding, whether internal governance language intrudes on the reading path, Unit-to-Unit continuity, and substantive bilingual equivalence.

## Progress

| Unit | Chinese | English | Status | Main work |
|---|---|---|---|---|
| P-U01 | Complete | Complete | First pass complete | Replaced governance-style opening with one `hello.c` experiment connecting compilation, execution, defects, and change. |
| P-U02 | Complete | Complete | First pass complete | Used changing `score` state as the narrative spine and demoted next-Unit concepts to previews. |
| P-U03 | Complete | Complete | First pass complete | Continued directly from the 100-point-cap failure and built control flow through boundaries, state, and termination. |
| P-U04 | Complete | Complete | First pass complete | Established function calls and direct returns before output pointers and `NULL`. |
| F-U01 | Complete | Complete | First pass complete | Used the surprising `5 / 2` result to connect representation, type, formatting, approximation, boundaries, and undefined behavior. |
| F-U02 | Complete | Complete | First pass complete | Used “a value selects a path” to connect branches, boundaries, sentinel, EOF, invariant, and requirement change. |
| F-U03 | Complete | Complete | First pass complete | Created the need for arrays from retaining many values; unified index, length, initialization, and bounds; deferred the full pointer model. |
| F-U04 | Complete | Complete | First pass complete | Built one path from character array to `\0`, capacity, complete-line input, leftover input, and safe traversal; corrected the C explanation of a three-element `"cat"` initializer; avoided requiring the full pointer model before F-U06. |
| F-U05–F-U12 | Pending | Pending | Not started | — |

## Important Reading Decisions in This Batch

The original F-U04 topics were individually useful, but a learner arriving from arrays first met specification-style completion language and then had to absorb `fgets`, newline removal, truncation, string-library calls, and pointer semantics in quick succession. The revised Unit begins directly from F-U03's character-array model and asks one question first: “How does text know where it ends?” Capacity, terminator, complete logical line, leftover input, and traversal then appear as consequences of that question.

The explanation of `char word[3] = "cat";` was also corrected. In C, this can initialize three character elements, but no element remains for the terminating `\0`; the result is therefore not a reliable C string. That is different from saying that a compiler must reject the declaration.

The `read_line` and string-comparison sections now avoid requiring the learner to understand the complete pointer model. Array-parameter adjustment, array-expression conversion, and pointer details are explicitly deferred to F-U06. The end of F-U04 uses the function calls already seen throughout the course to create the motivation for F-U05's call-stack and recursion model.

## Completion Condition

The Student Reading Pass is complete only after P-U01–P-U04 and F-U01–F-U12 have all been read end to end, major reading barriers have been corrected, and students can understand the material without depending on internal design or review documents.
