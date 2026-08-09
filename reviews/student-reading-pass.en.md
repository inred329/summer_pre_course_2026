# Student Reading Pass

Version: 1.2.0  
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
| F-U05 | Complete | Complete | First pass complete | Entered from familiar function calls and asked what state belongs to each call, then connected call frames, waiting relationships, scope/lifetime, recursion termination, result range, and iteration; kept call stack as a reasoning model rather than a mandated physical layout. |
| F-U06 | Complete | Complete | First pass complete | Recovered the address question from familiar `scanf(..., &score)` use and built object/value/address, dereference, `NULL`, lifetime, aliasing, array conversion, and one-past in sequence. |
| F-U07 | Complete | Complete | First pass complete | Created the need for `struct` from scattered fields belonging to one student, then connected type/object, initialization, `.`/`->`, string fields, structure copying, equality semantics, and arrays of structures. |
| F-U08 | Complete | Complete | First pass complete | Rewrote the Unit as fixed capacity → allocation lifetime → ownership → `realloc` growth → pointer-to-pointer → failure contract, adding an owner-pointer diagram and explicit explanation before `int **`. |
| F-U09–F-U12 | Pending | Pending | Not started | — |

## Important Reading Decisions in This Batch

The original F-U04 topics were individually useful, but a learner arriving from arrays first met specification-style completion language and then had to absorb `fgets`, newline removal, truncation, string-library calls, and pointer semantics in quick succession. The revised Unit begins directly from F-U03's character-array model and asks one question first: “How does text know where it ends?” Capacity, terminator, complete logical line, leftover input, and traversal then appear as consequences of that question.

The explanation of `char word[3] = "cat";` was also corrected. In C, this can initialize three character elements, but no element remains for the terminating `\0`; the result is therefore not a reliable C string. That is different from saying that a compiler must reject the declaration.

The `read_line` and string-comparison sections now avoid requiring the learner to understand the complete pointer model. Array-parameter adjustment, array-expression conversion, and pointer details are explicitly deferred to F-U06. The end of F-U04 uses the function calls already seen throughout the course to create the motivation for F-U05's call-stack and recursion model.

After an end-to-end reading, F-U05 did not require another large structural rewrite. It already opens from familiar calls such as `sum_array`, `max_array`, `strlen`, and `strcmp`, asks where unfinished work and per-call state live, and then uses `square` and nested calls to establish that every call owns distinct execution state. Scope/lifetime, recursion, base cases, progress toward termination, factorial, and string recursion arrive only after that concrete call model, so learners are not asked to memorize abstract terms before seeing why they matter.

F-U06 likewise did not need a structural rewrite. It begins from `scanf("%d", &score)`, a form students have used repeatedly, and upgrades `&score` from “write it this way for now” into an explicit address model. `*p`, pointer parameters, `NULL`, dangling pointers, aliasing, and the array/pointer relationship then appear as consequences of that model. One-past is introduced only after first-element addresses and pointer arithmetic have a concrete diagram.

F-U07 also maintains a natural learner path. It first shows the data-model problem created when one student's name, ID, and average are scattered, then separates a `struct` type from an actual object before introducing `.`, `typedef`, `->`, and value/pointer passing. Earlier rules for string capacity, pointer lifetime, and array bounds are reused inside the new record model instead of being replaced by a second set of rules. The chapter closes by asking what changes when the record count becomes a runtime decision, which leads directly into F-U08.

F-U08 contained a real reading discontinuity: the growable-list discussion was followed by `append_value(int **values, ...)`, which made pointer-to-pointer syntax appear before learners had a reason for the extra level. The Unit has therefore been rewritten around one continuous path: fixed capacity, byte-size calculation, allocate/use/free, ownership, `realloc`, alias invalidation, growth invariants, and only then a dedicated section answering “why `int **`?”. The revised explanation draws `append_value` parameter → caller's owner pointer → dynamic allocation and states the rule in F-U06 terms: the caller-owned object being modified is itself an `int *`, so the function receives that pointer object's address, `&values`. Only after that model is clear does the Unit show an append implementation with an unchanged-on-failure contract.

## Completion Condition

The Student Reading Pass is complete only after P-U01–P-U04 and F-U01–F-U12 have all been read end to end, major reading barriers have been corrected, and students can understand the material without depending on internal design or review documents.