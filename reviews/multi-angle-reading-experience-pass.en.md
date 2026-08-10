# Multi-Angle Student Reading Experience Review

Version: 1.0.0  
Status: Complete for this pass  
Last updated: 2026-08-10  
Corresponding Chinese version: [多角度學生閱讀體驗審查](multi-angle-reading-experience-pass.zh-TW.md)

## Purpose

This pass does not recheck only grammar, technical correctness, or file presence. It rereads the student path from different learner perspectives and focuses on whether:

- the tone guides understanding rather than sounding like commands, corrections, or a specification;
- a core concept has more than one meaningful entry point, such as a need, program, diagram, trace, counterexample, experiment, test, or requirement change;
- multiple angles actually complement one another instead of restating the same sentence;
- analogies are used only when they help and their limits remain clear;
- first-time C learners, students already familiar with an IDE, visual/trace-oriented learners, experiment-oriented learners, and students who understand tools best by diagnosing failures all have a plausible way into the material;
- Traditional Chinese and English preserve the same instructional angles and comparable tone.

## Overall conclusion

The student materials already have a strong multi-angle teaching foundation. They do not need to be mechanically rewritten into one repeated template. In particular, the middle and later Units often form a complementary path such as:

`need → minimal program → diagram/trace → boundary or failure → experiment/test → requirement change`

The clearest improvement opportunity in this pass was P-U00. The earlier version was technically clear but still led every beginner through essentially one author-selected understanding path. In practice, some students first understand the process through IDE controls, others through concrete files and terminal commands, and others only when they encounter the “I changed the source but still see the old output” problem.

P-U00 now explicitly supports three valid entry points:

```text
IDE-first
terminal / file-first
failure-first
```

All three converge on the same model:

```text
source → Build → executable → Run
```

Several imperative-sounding sentences were also softened so the chapter more often invites students to predict, choose the angle that currently makes sense, and map their own actions back onto the model.

## Unit-by-Unit multi-angle check

### P-U00

Angles include IDE Run experience, concrete source/build/executable artifacts, the stale-executable failure scenario, an IDE role diagram, Run/Debug breakpoint observation, and the distinction between Build success and requirement correctness.

Change in this pass: added IDE-first, terminal/file-first, and failure-first entries; added one bounded playback analogy for Run/Debug; softened several “do not...” constructions.

### P-U01

Angles include output prediction from source, sequential execution through `main`, observable `printf` effects, a trace table, `return` and reachability, build failure versus execution mismatch, and an ordering experiment.

Assessment: enough complementary angles. Direct instructions are generally followed by reasons or reproducible actions rather than governance-style language.

### P-U02

Angles include the intuitive conflict in `score = score + 5`, separating data/value/type/variable/state, state tables, external input entering program state, integer-division and format-mismatch surprises, and a requirement change that naturally motivates control flow.

Assessment: supports abstract, tracing-oriented, and experiment-oriented learners.

### P-U03

Angles include the score-cap requirement, boundary tables, an `if/else` flowchart, requirement-language-to-operator mapping, multi-branch ordering counterexamples, a four-question loop model, state tables, off-by-one cases, and nontermination.

Assessment: strong mix of program, diagram, table, and boundary reasoning.

### P-U04

Angles include the maintenance pain of an overloaded `main`, naming one responsibility, argument → parameter → return flow, a single-call trace, the “this function is responsible for ___” semantic check, interface reasoning, and requirement changes.

Assessment: functions are motivated from responsibility rather than introduced as a syntax list.

### F-U00

Angles include decomposing a familiar Run button, source versus executable artifacts, stale-executable diagnosis, IDE/compiler role separation, Build success versus requirement success, breakpoint observation, and explicit forward references to F-U10/F-U11.

Assessment: appropriate for formal-course students who have operated tools but may not have a precise tool model.

### F-U01

Angles include the `5 / 2` surprise, bit patterns and representation, LSB/MSB weights, operand-type data flow, format strings as type contracts, floating-point experiments, signed/unsigned boundary behavior, and defined-versus-undefined classification.

Assessment: abstract representation/type ideas have numeric, bit-level, I/O, and failure-based entries.

### F-U02

Angles include grade-classification tracing, boundary-value tables, `switch` for discrete options, nested-path tables, sentinel/EOF/invalid-input paths, and connection to test coverage.

Assessment: the Unit builds a path model rather than merely adding syntax.

### F-U03

Angles include the scaling pain of many separate variables, box diagrams, index/value separation, loop traces, out-of-bounds counterexamples, initialized-versus-addressable distinctions, multiple traversal tasks, and requirement changes.

Assessment: strong multi-angle treatment.

### F-U04

Angles include character-array versus text representation, the `"cat"` memory picture, character-array versus terminated-string contrast, capacity/visible-length/required-storage separation, `fgets` truncation, newline/EOF/overlong-line classification, and parser contracts.

Assessment: sufficient varied entry points for a high-cognitive-load topic.

### F-U05

Angles include per-call state from familiar function calls, nested call trees, the call-stack reasoning model, scope versus lifetime, countdown recursion, wrong-direction recursion, factorial descent/unwinding, and recursive string processing.

Assessment: recursion is supported through diagrams, mathematical expansion, failure direction, and a second data example.

### F-U06

Angles include recovering `scanf(..., &score)`, separating object/value/address, pointer diagrams, `&`/`*` operations, caller modification, NULL, lifetime/dangling pointers, aliasing, array conversion, pointer arithmetic, one-past, and a four-question safety check.

Assessment: one of the strongest multi-angle treatments of an abstract concept in the repository.

### F-U07

Angles include the data-organization problem of fields belonging to one student, struct tree diagrams, type versus object, field-validity rules, `.` and `->`, value versus pointer passing, and later copy/record-array consequences.

Assessment: `struct` grows from entity modeling rather than a syntax table.

### F-U08

Angles include fixed-array limitations, element count versus byte count, allocation lifecycle tracing, aliases surviving `free`, ownership via leak/double-free contrast, `realloc` growth, pointer-to-pointer caller-owner reasoning, and unchanged-on-failure contracts.

Assessment: supports learners oriented toward data structures, lifetimes, or API contracts.

### F-U09

Angles include process lifetime versus persistence, stream lifecycle, file mode as data policy, return-driven read loops versus the `feof` counterexample, EOF/format/I/O-error classification, complete-record handling with `fgets`, file format as protocol, transactional loading, and write/close failures.

Assessment: files are taught as a data journey rather than an API catalog.

### F-U10

Angles include change-cost pressure from an all-in-one `main.c`, interface versus implementation, header/source examples, failure contracts, include-dependency diagrams, compile → object → link flow, compile-versus-link errors, information hiding, and a second frontend as a module-boundary test.

Assessment: modularity has both a maintenance angle and a toolchain angle.

### F-U11

Angles include requirement-derived tests, boundary tables, failure versus root cause, debugging hypothesis loops, reproducible bug reports, regression testing, verification versus validation, incorrect test expectations, refactoring protection, and evidence-based code review.

Assessment: the idea of “trustworthiness” is built through multiple evidence layers.

### F-U12

Angles include observable requirements, data-model diagram and invariants, milestone-based implementation, ownership growth tracing, module boundaries, file protocols and transactional loading, delayed interactive input, layered testing, and a final multi-score requirement change that propagates through ownership/API/protocol/tests.

Assessment: despite high information density, the Unit uses milestones instead of dropping a specification all at once.

## Tone review

The materials often use phrases such as “predict first,” “classify first,” and “do not only...”. These have legitimate teaching value, but at high density they can accumulate into a corrective voice.

The principle for this pass is:

- keep warnings that genuinely prevent common misconceptions;
- prefer invitational language such as “try...”, “if this angle makes more sense...”, or “from another angle...” when precision is unchanged;
- do not make “do not memorize” a slogan without offering an actionable alternative;
- preserve technical precision while softening delivery;
- avoid flooding the course with everyday analogies that students might remember more strongly than the actual C rule.

P-U00 was revised accordingly in both languages. In the other Units, most directive wording is immediately paired with a reason, trace, experiment, or alternative strategy, so it does not currently justify a broad stylistic rewrite.

## Completion status

- P-U00–P-U04: multi-angle and tone review complete.
- F-U00–F-U12: multi-angle and tone review complete.
- Revised P-U00 Chinese/English pair: substantively aligned.
- Major abstract concepts have at least two genuinely different learning entries rather than definition restatement alone.
- No fixed pedagogical device is required in every Unit; the angle is chosen to fit the concept.
- No remaining reading barrier found in this pass requires a broad rewrite.
