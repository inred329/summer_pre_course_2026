# Student Reading Pass

Version: 2.0.0  
Last updated: 2026-08-09  
Corresponding Chinese version: [學生閱讀體驗審查](student-reading-pass.zh-TW.md)

## Purpose

Read every student-facing Unit from a learner's point of view and check opening motivation, concept timing, section transitions, whether examples actually support understanding, whether internal governance language intrudes on the reading path, Unit-to-Unit continuity, and substantive bilingual equivalence.

This pass does not repeat the Constitution/governance audit. Each student Unit is read from its first sentence through its final transition to verify that the material itself establishes the problem, model, examples, and next step without requiring learners to consult internal design or review documents to understand why a concept appears.

## Final Progress

| Unit | Chinese | English | Status | Main work |
|---|---|---|---|---|
| P-U01 | Complete | Complete | Complete | Replaced governance-style opening with one `hello.c` experiment connecting compilation, execution, defects, and change. |
| P-U02 | Complete | Complete | Complete | Used changing `score` state as the narrative spine and demoted next-Unit concepts to previews. |
| P-U03 | Complete | Complete | Complete | Continued directly from the 100-point-cap failure and built control flow through boundaries, state, and termination. |
| P-U04 | Complete | Complete | Complete | Established function calls and direct returns before output pointers and `NULL`. |
| F-U01 | Complete | Complete | Complete | Used the surprising `5 / 2` result to connect representation, type, formatting, approximation, boundaries, and undefined behavior. |
| F-U02 | Complete | Complete | Complete | Used “a value selects a path” to connect branches, boundaries, sentinel, EOF, invariant, and requirement change. |
| F-U03 | Complete | Complete | Complete | Created the need for arrays from retaining many values; unified index, length, initialization, and bounds; deferred the full pointer model. |
| F-U04 | Complete | Complete | Complete | Built one path from character array to `\0`, capacity, complete-line input, leftover input, and safe traversal; corrected the C explanation of a three-element `"cat"` initializer; avoided requiring the full pointer model before F-U06. |
| F-U05 | Complete | Complete | Complete | Entered from familiar calls and asked what state belongs to each call, then connected call frames, waiting relationships, scope/lifetime, recursion termination, result range, and iteration. |
| F-U06 | Complete | Complete | Complete | Recovered the address question from familiar `scanf(..., &score)` use and built object/value/address, dereference, `NULL`, lifetime, aliasing, array conversion, and one-past in sequence. |
| F-U07 | Complete | Complete | Complete | Created the need for `struct` from scattered fields belonging to one student, then connected type/object, initialization, `.`/`->`, string fields, structure copying, equality semantics, and arrays of structures. |
| F-U08 | Complete | Complete | Complete | Rewrote the Unit as fixed capacity → allocation lifetime → ownership → `realloc` growth → pointer-to-pointer → failure contract, adding an owner-pointer diagram and explicit explanation before `int **`. |
| F-U09 | Complete | Complete | Complete | Used “data must outlive this execution” to motivate streams, open modes, read results, complete records, file protocol, transactional loading, and write/close failure. |
| F-U10 | Complete | Complete | Complete | Motivated modules from the cost of keeping everything in one `main.c`, then connected interface/implementation, header/source, translation units, compile/link, and information hiding. |
| F-U11 | Complete | Complete | Complete | Gathered earlier boundary/failure tests into a requirement → expected result → test → debugging hypothesis → minimal fix → regression evidence chain while separating verification from validation. |
| F-U12 | Complete | Complete | Complete | Integrated Student, StudentList, ownership, files, modules, and tests through milestones; replaced the older specification-style English structure so it now follows the same integrated narrative as Chinese. |

## Major Reading Decisions

P-U01 through P-U04 were not missing core knowledge; their main problem was that openings and activities could read like material specifications. The revised sequence begins each Unit from an observable program phenomenon or a question left by the previous Unit, then introduces terminology only after the need exists. Output pointers, `NULL`, and unnecessary integer-limit machinery no longer interrupt the preparatory path.

F-U01 through F-U04 establish a continuous first-half formal-course chain: representation and type affect results → values select control paths → retaining many values motivates arrays → character arrays use `\0` to represent text. F-U04 also corrects the explanation of `char word[3] = "cat";`: C can initialize the three character elements, but no terminating `\0` fits, so the result is not a terminated C string suitable for ordinary string interfaces.

F-U05 through F-U07 deliberately place abstract terminology after an existing use. F-U05 starts from functions learners have already called and builds per-call state; F-U06 recovers the familiar `&score` and turns it into the address/pointer model; F-U07 introduces `->` only after structure members already have a concrete meaning. Call stack remains an execution-reasoning model, not a fixed physical memory layout guaranteed by the C standard.

F-U08 contained the clearest reading discontinuity in the second half of the formal course. The older sequence moved from a growable array directly to `append_value(int **values, ...)`, encouraging learners to treat pointer-to-pointer as another symbol pattern to memorize. The revised Unit first completes allocation lifetime, ownership, `realloc`, and alias invalidation, then answers “why `int **`?” explicitly: the caller-owned object being modified is itself an `int *` owner, so the function receives that pointer object's address, `&values`. Only then does it show an append implementation with an unchanged-on-failure contract.

F-U09 through F-U11 already had coherent student narratives and did not need rewriting merely to create changes. F-U09 follows one record through persistence and builds streams, protocols, and transactions; F-U10 motivates module boundaries from change cost and then distinguishes compile from link; F-U11 gathers testing habits from the previous ten Units into a reproducible, falsifiable, regression-protected evidence workflow.

F-U12 exposed a substantive bilingual mismatch rather than a sentence-level translation problem. The Chinese version had already become an incremental milestone narrative: requirements and observable evidence, StudentList invariant, minimal lifetime, add, fixed-data tests, ownership trace, modules, file protocol, interactive input, layered tests, and a final requirement change. The English version still used the older specification/capability-list structure. This pass rewrote the English version to follow the same teaching order while preserving the same failure contracts, transactional loading, nested-ownership consequences, and final requirement-change reasoning.

## Unit-to-Unit Reading Chain

The formal course now reads continuously as:

```text
representation/type
→ control paths
→ arrays
→ strings
→ function-call state/recursion
→ addresses/pointers
→ structures
→ dynamic allocation/ownership
→ file persistence
→ module boundaries
→ testing/debugging/evidence
→ integrated application
```

Each next Unit is motivated by a need or limitation already visible in the previous Unit rather than by an internal course-design document telling the learner what must come next.

## Completion Decision

The Student Reading Pass is complete for the current repository snapshot. P-U01 through P-U04 and F-U01 through F-U12 have all received end-to-end bilingual reading review. Major governance/specification tone, prematurely introduced concepts, narrative discontinuities, and substantive bilingual mismatches have been corrected. Each Unit now establishes its learning motivation, main model, practice, and transition from the student-facing material itself.

If teaching rehearsal, student feedback, or formal review later reveals a new comprehension barrier, it should be recorded as a new reading finding rather than reopening the completed repository-wide first pass.