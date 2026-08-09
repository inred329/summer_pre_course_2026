# Student Reading Pass

Version: 0.5.0  
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
| P-U03 Control flow | Complete | Complete | First pass complete | Connected directly to P-U02's unresolved `98 + 5 = 103` case and used the 100-point cap to motivate `if`; turned conditions, boundaries, branch order, input checks, and loops into one control-flow narrative; reframed off-by-one, nontermination, and practice around reasoning about state. |
| P-U04 Functions and integration | Complete | Complete | First pass complete | Continued directly from P-U03's “everything in `main`” problem; introduced functions through simple parameters, arguments, calls, and return values before interface contracts; removed premature pointer-output/`NULL`/`INT_MAX` machinery from the core path; used bounded score examples and a score reporter to connect responsibility separation, direct function tests, requirement changes, and the transition to F-U01. |
| F-U01 Representation, types, and operations | Complete | Complete | First pass complete | Continued directly from the `int`/`double` work in P-U04; used the surprising result of `double result = 5 / 2` to create motivation; connected value, representation, type, format contracts, floating-point approximation, and integer boundaries into one “how data is interpreted” narrative; reframed defect cases through a defined-vs-undefined diagnostic model; integrated the ideas in a representation/division reporter and bridged to F-U02. |
| F-U02–F-U12 | Pending | Pending | Not started | — |

## P-U01 Reading Observation

The original version was technically complete, but it opened with “Document Purpose and Completion Standard,” submission guidance, and AI policy before the student encountered the first programming question. Several later sections also used constraints, record-keeping suggestions, and test-table language that made the chapter feel closer to an operating specification than a continuous learning story.

After the first pass, P-U01 begins directly with the question of what actually happens after a C text file is saved. The chapter now keeps returning to the same `hello.c` experiment and connects prediction, real execution, deliberate defects, and requirement changes into one narrative. The Chinese and English versions preserve equivalent section order, questions, experiments, and closing transition.

## P-U02 Reading Observation

The original version also began with completion standards, record-keeping instructions, and AI policy before reaching the learner’s real question of how a running program keeps data. More importantly, it introduced `if` before control flow had been taught and later required students to implement a “maximum score of 100” rule, forcing them to use the next Unit’s central concept before it had been established.

After the first pass, P-U02 grows directly from P-U01’s fixed output into the question of what remains inside a running program. The statement `score = score + 5` now anchors value, type, variable, assignment, and state. The input example still keeps the safe success check, but clearly tells students that `if` and `&score` only need to be understood by purpose for now. The former immediate implementation of the 100-point cap is now an intentionally unresolved requirement: students see `98 + 5` produce `103`, which creates a natural need for “choosing different paths” and leads directly into P-U03.

## P-U03 Reading Observation

The original version again placed purpose, completion, record-keeping, and AI-policy language before the first control-flow problem. Although the technical topics were present, conditions, operators, loop elements, defect cases, and exercises appeared mostly as parallel sections rather than as a continuation of the unresolved 100-point-cap problem at the end of P-U02. That made the chapter easier to read as a new list of syntax than as the next step in one learning story.

After the first pass, P-U03 begins directly with the failed `98 + 5 = 103` requirement and uses `if (final_score > 100)` to solve a problem the learner already has reason to understand. Values 99, 100, and 101 then establish boundary reasoning before the chapter expands to `else`, comparisons and logical combinations, successful-input checks, and branch ordering. Loops are introduced from the repeated need to add 1 through 5 and repeatedly return to state, condition, work, and update. Off-by-one and infinite-loop cases are now diagnosed through “which iteration disappeared?” and “does the controlling state move toward termination?” The closing section creates the next need naturally: once every responsibility is placed inside `main`, the program becomes harder to read, change, and verify, leading into P-U04.

## P-U04 Reading Observation

The original version had a strong responsibility-separation goal, but the first full function example immediately required `int *result`, `NULL`, `INT_MAX`, `INT_MIN`, signed-overflow checks, status returns, and output-through-pointer behavior. Those are valuable formal-course topics, but at this point the preparatory sequence had not yet established pointers or integer-boundary machinery. As a result, the reader had to absorb several advanced interface ideas before the simpler question “what is a function call and where does its result go?” had been made comfortable. The chapter also began with document-purpose and completion language instead of continuing the problem created at the end of P-U03.

After the first pass, P-U04 begins exactly where P-U03 stops: `main` can now store, choose, and repeat, but becomes difficult to read when every responsibility stays inside it. `max_of_two` establishes function name, parameters, arguments, call flow, and a direct return value with one small trace. Interface contracts are then introduced through deliberately bounded score inputs, so the text can discuss caller guarantees without forcing pointer outputs or overflow-preservation machinery into the preparatory core. A three-score reporter becomes the integration story: input and validation stay visible in `main`, while average calculation and pass/fail judgment become separately named and directly testable functions. The chapter closes by showing that the preparatory sequence is complete and creating the next formal-course question: the `int`, `double`, arithmetic, and input operations already used all depend on deeper representation and boundary rules, leading naturally into F-U01.

## F-U01 Reading Observation

The original version already covered bits, MSB/LSB, types, integer division, floating-point approximation, overflow, characters, and format mismatch correctly, but the reading path still followed a specification-like structure: “Purpose and Completion Standard → Core Question → capability list → parallel topic sections → error cases → exercises.” A learner arriving from P-U04 first met completion language and abstract outcomes instead of immediately seeing why familiar `int` and `double` operations were worth revisiting. Format mismatch, floating-point comparison, and signed overflow also appeared as separate facts rather than as parts of a shared model for distinguishing “defined behavior that does not match the requirement” from “behavior the language no longer defines.”

After the first pass, F-U01 connects directly to P-U04 and opens with the concrete surprise that `double result = 5 / 2;` produces `2.0`. The learner gets a question first, then follows one sequence: “value → representation → type → operation timing → format contract → approximation → boundaries.” MSB and LSB are introduced first through unsigned binary position and weight so the learner does not prematurely memorize “MSB means sign bit.” `printf` formats are brought into the type-contract story instead of appearing only as an isolated defect. The floating-point section explicitly separates “calculated approximations usually need requirement-driven tolerances” from exact sentinels such as a deliberately entered `0.0`, avoiding the oversimplified rule “never use `==` with floating point.” Integer boundaries establish the safe order “check first, then operate,” and the chapter collects signed overflow, unsigned modular arithmetic, integer division, and format mismatch into a defined-vs-undefined diagnostic table. A final `unsigned int`/`double` reporter integrates input formats, decimal/hexadecimal presentation, division, zero-divisor handling, and boundary tests before handing the reader naturally to F-U02, where several conditions and states begin to interact.

## Completion Condition

The Student Reading Pass is complete only after P-U01–P-U04 and F-U01–F-U12 have all been read end to end, major reading barriers have been corrected, and students can understand the materials without relying on design, review, or other internal documents.