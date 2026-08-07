# Concept-Driven Unit Map

Version: 0.2.1  
Status: Active design standard  
Governance note: This standard defines Unit identifiers, core questions, concept composition, and core evidence direction. It does not define grading, weekly pacing, or mandatory tool use.  
Corresponding Chinese version: [Concept 驅動的 Unit Map](16-unit-map.zh-TW.md)

## Document Purpose

This document composes stable Concepts from the Concept Tree and Concept Registry into teachable, readable, and traceable Units for the preparatory and connected formal C course.

A Unit consists of:

1. one student-understandable core question;
2. one coherent primary Concept chain or cluster;
3. a controlled number of newly introduced Concepts;
4. existing Concepts that are deepened or reused;
5. at least one prediction, tracing, testing, debugging, modification, or verification activity;
6. concrete C mappings whose technical boundaries are explicit;
7. a core completion/evidence direction independent of optional external tools.

A Unit is not automatically one class meeting or one week. Delivery slices are planned separately.

## Constitution 2.0 Alignment

- Unit structure is derived from concepts, dependencies, scope, and capability evidence rather than syntax chapter order alone.
- Student-facing materials may be longer or shorter than this skeleton but must preserve the core question, technical contracts, and capability direction.
- AI and other external assistance are optional by default. No Unit requires an AI conversation, AI explanation, AI log, fixed prompt, or non-use declaration for core completion.
- If optional external assistance is actually used, the learner remains responsible for understanding and technically verifying any adopted result.
- Concrete toolchain/runtime claims must identify the target environment and must not present common implementation models as C-language guarantees.

## Composition Markers

- `N`: Concept introduced in this Unit.
- `D`: Concept deepened in this Unit.
- `R`: Concept reused in this Unit.
- `P`: Preparatory-course scope.
- `F`: Formal-course scope.
- `X`: Optional/conditional external-assistance activity; never part of universal completion.

---

# Preparatory-Course Units

## P-U01 — How Does Program Text Become an Execution Result?

Core question: **How does human-readable program text become behavior that a computer can execute in the specified environment?**

Primary Concept chain:

```text
CT-C01 Problem
→ CT-C02 Requirement
→ CT-C03 Algorithm / Design Procedure
→ CT-C04 Program
→ CT-C05 Source Code
→ CT-C06 C Translation
→ CT-C07 C Implementation / Compiler Tool
→ CT-C08 Executable / Loadable Program Representation
→ CT-C09 Execution
→ CT-X02 Output
→ CT-E01 Expected Result / Property
→ CT-E04 Verification
```

Concept use:

- `N`: Problem, Requirement, Program, Source Code, C Translation, C Implementation/Compiler Tool, Executable/Loadable Representation, Execution, Output, Expected Result/Property, Diagnostic
- `D`: Algorithm/Design Procedure
- `R`: none

C mapping and technical boundary:

- minimal `main` program;
- `#include <stdio.h>`, `printf`, and return status;
- the actual GCC/Clang or other specified build command for the course environment;
- observed diagnostics and produced artifacts;
- explicit note that preprocessing/compilation/code generation/assembly/linking may be exposed differently by different implementations.

Core evidence:

- predict output before execution;
- distinguish source text, translation/build, produced program representation, and execution;
- reproduce and diagnose one translation/build error;
- explain why editing source does not change an already-built program until it is rebuilt;
- compare expected and actual evidence.

---

## P-U02 — How Does a Program Represent Data and Change State?

Core question: **How does a program represent current data and produce a new state after each relevant execution step?**

Primary chain:

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-M04 Object / Storage
→ CT-S01 State
→ CT-S03 Variable / Named Object
→ CT-S06 Initialization
→ CT-S07 Assignment
→ CT-S02 State Change
→ CT-I07 Expression
→ CT-I09 Evaluation
→ CT-E12 Trace
```

Concept use:

- `N`: Data, Value, Type, Object/Storage, State, Variable/Named Object, Initialization, Assignment, State Change, Expression, Evaluation, Trace
- `D`: Expected Result/Property, Output
- `R`: Program, Execution

C mapping:

- `int`, `double`, `char`;
- declaration and initialization;
- assignment and arithmetic expressions;
- basic standard input/output with format/type matching;
- introductory integer-division and conversion observations.

Core evidence:

- build state tables;
- trace old/new values line by line;
- predict expression results before running;
- identify invalid/uninitialized-state assumptions and input/format problems;
- compare integer and floating behavior only within clearly stated value ranges.

---

## P-U03 — How Does a Program Select and Repeat Reliably?

Core question: **When different situations require different actions, or work must repeat, how does a program decide the next step and know when to stop?**

Primary chain:

```text
CT-F01 Sequence
→ CT-F02 Condition
→ CT-F03 Selection / Decision
→ CT-F05 Repetition
→ CT-F06 Iteration
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Nontermination
→ CT-E03 Testing
→ CT-E10 Regression Verification
```

Concept use:

- `N`: Sequence, Condition, Selection/Decision, Repetition, Iteration, Loop Condition, Boundary, Nontermination
- `D`: Expression, Evaluation, State Change, Update, Testing
- `R`: Input, Output, Expected Result/Property

C mapping:

- relational/logical operators;
- `if`, `else`, `while`, `for`;
- `break`/`continue` only where they support the stated control purpose;
- counters, accumulators, and sentinel/end conditions.

Core evidence:

- predict branch paths;
- trace loop state iteration by iteration;
- compare boundary choices such as `<` vs `<=`;
- diagnose nontermination and off-by-one defects;
- change a requirement and rerun relevant regression checks.

---

## P-U04 — How Can a Larger Problem Be Divided into Understandable Work?

Core question: **When a program grows, how can responsibilities be separated so each part can be understood, tested, and modified?**

Primary chain:

```text
CT-A01 Decomposition
→ CT-A02 Responsibility
→ CT-A03 Function
→ CT-A04 Interface
→ CT-A06 Parameter
→ CT-A07 Argument
→ CT-A08 Return Value
→ CT-A09 Call
→ CT-E02 Test Case
→ CT-E03 Testing
→ CT-E04 Verification
```

Concept use:

- `N`: Decomposition, Responsibility, Function, Interface, Parameter, Argument, Return Value, Call
- `D`: Test Case, Testing, Verification, Requirement
- `R`: State, Selection, Repetition, Expected Result/Property

C mapping:

- function declaration/prototype, definition, and call;
- parameters and return values;
- local objects and basic scope;
- small integrated program with caller-side tests.

Core evidence:

- state a one-sentence function responsibility;
- predict arguments, parameters, and return values;
- trace relevant state before/during/after a call;
- design normal, boundary, invalid, or failure cases as appropriate;
- compare alternative decompositions and modify a requirement.

Optional `X` extension: if a learner chooses to consult AI or another assistant, verify any adopted suggestion using the same core testing/trace evidence. Skipping the extension changes no core completion requirement.

---

# Formal-Course Units

The formal course deepens preparatory Concepts rather than resetting them. Student-facing formal materials F-U01–F-U12 are the implementation of these Unit skeletons and may contain additional verified detail.

## F-U01 — Why Do Representation, Type, and Operations Affect Results?

Core question: **Why can the same mathematical idea produce different program results because of representation, type, and operation rules?**

Primary Concepts: CT-I03 Representation, CT-I04 Type, CT-I08 Operator, CT-I09 Evaluation, CT-I10 Conversion, CT-X04 Format, CT-E01 Expected Result/Property.

C mapping:

- integer ranges using `<limits.h>` rather than assumed bit widths;
- binary examples with explicitly stated widths when used;
- MSB/LSB as representation-position concepts only when the representation is specified;
- floating-point approximation and `<float.h>`/target observations;
- character representation and conversions;
- formatted I/O with correct specifiers.

Core evidence:

- predict type/conversion outcomes inside stated contracts;
- distinguish mathematical expectation from representable-domain behavior;
- test boundary values and formatting assumptions;
- identify where a claim is standard-guaranteed versus implementation-specific.

---

## F-U02 — How Can Complex Control Flow Remain Explainable and Testable?

Core question: **When conditions, boundaries, and repetition become more complex, what evidence supports correctness?**

Primary Concepts: CT-F03 Selection, CT-F05 Repetition, CT-F09 Sentinel/End Condition, CT-F10 Nested Control, CT-S11 Invariant, CT-E03 Testing, CT-E10 Regression Verification.

C mapping: `switch`, nested control, compound conditions, sentinel/end-condition loops, loop invariants as reasoning tools.

Core evidence: draw/trace paths, identify missing/overlapping cases, state an appropriate invariant, test boundaries, and reverify after requirement changes.

---

## F-U03 — How Does Data Form an Ordered Collection?

Core question: **When multiple related values must be stored and processed together, how are they organized, indexed, and kept within valid bounds?**

Primary Concepts: CT-I11 Collection, CT-M04 Object/Storage, CT-M05 Layout, CT-F08 Boundary, CT-F06 Iteration, CT-M15 Memory Safety; Composite CT-K01 Array.

C mapping: one-dimensional arrays, indexes, explicit length/capacity contracts, traversal, arrays passed to functions, introductory multidimensional arrays when in scope.

Core evidence: trace element/index relationships, test valid and invalid bounds, diagnose out-of-bounds/off-by-one defects, modify length/capacity requirements, and reverify.

---

## F-U04 — How Is Text Represented and Processed as C Data?

Core question: **How does C represent a string, how is its end determined, and what capacity/boundary conditions make operations valid?**

Primary Concepts: CT-I03 Representation, CT-K01 Array, CT-K02 String, CT-F09 Sentinel/End Condition, CT-X05 Buffer, CT-X04 Format, CT-M15 Memory Safety.

C mapping: `char` arrays, null terminator, string literals, `fgets`, selected `<string.h>` functions, explicit capacity/length contracts.

Core evidence: distinguish character arrays from valid strings, trace terminator/capacity state, test input boundaries, diagnose unterminated/insufficient-buffer cases, and account for byte-vs-character limits when discussing multibyte encodings.

---

## F-U05 — How Does a Function Call Create Temporary Execution State?

Core question: **During nested or recursive calls, how do parameters, local objects, control return, scope, and lifetime relate?**

Primary Concepts: CT-A09 Call, CT-A10 Activation Model, CT-S09 Scope, CT-S10 Lifetime, CT-M10 Storage Duration, CT-M11 Automatic Storage, CT-A11 Recursion.

C mapping: automatic local objects, nested calls, recursion, base/termination conditions.

Core evidence:

- trace an implementation-neutral activation model;
- distinguish scope from lifetime;
- reason about recursive progress/termination;
- diagnose invalid returned addresses or nonterminating recursion;
- relate a physical call stack/stack overflow only to the target implementation when that model is actually used.

---

## F-U06 — How Can Data Be Accessed Indirectly Through Pointers?

Core question: **How can a pointer designate another object, and what conditions make indirect access valid?**

Primary Concepts: CT-M03 Address, CT-M06 Pointer, CT-M07 Indirection/Dereference, CT-M08 Aliasing, CT-M09 Null Pointer, CT-S10 Lifetime, CT-M15 Memory Safety.

C mapping: `&`, `*`, pointer parameters, null pointer values, array/pointer relationships and limited pointer arithmetic within valid array-object rules.

Core evidence: draw pointer/object relationships, predict alias effects, identify dereference preconditions, and diagnose null, dangling, one-past misuse, and invalid access.

---

## F-U07 — How Can One Entity Contain Different Fields?

Core question: **When one entity contains several different kinds of data, how can those fields be modeled as one meaningful record?**

Primary Concepts: CT-I11 Collection, CT-M04 Object/Storage, CT-M05 Layout, CT-I04 Type, CT-A04 Interface; Composite CT-K03 Structure/Record.

C mapping: `struct`, member access, initialization/assignment, pointers to structures, nested structures, arrays of structures, `typedef` where it improves interface clarity.

Core evidence: derive fields from requirements, compare separate variables vs a record, distinguish semantic fields from implementation padding/layout, modify structures through clear interfaces, and test validity constraints.

---

## F-U08 — How Does a Program Manage Storage Whose Size or Lifetime Is Decided at Runtime?

Core question: **How can storage be acquired, resized, owned, and released safely when requirements are not fixed at translation time?**

Primary Concepts: CT-M13 Allocated Storage/Dynamic Allocation, CT-M14 Ownership/Release Responsibility, CT-S10 Lifetime, CT-M06 Pointer, CT-M15 Memory Safety.

C mapping: `malloc`, `calloc`, `realloc`, `free`, overflow-safe size reasoning, allocation failure, leak/dangling/double-free prevention.

Core evidence: draw allocate-use-resize-release paths, preserve the original allocation on `realloc` failure, identify ownership/release responsibility, test failure paths, and diagnose lifetime errors.

---

## F-U09 — How Does a Program Interact with Files and Persistent Data?

Core question: **When data must persist beyond one execution, how does a program read/write it while distinguishing normal end-of-input from errors and malformed data?**

Primary Concepts: CT-X03 Stream, CT-X06 File, CT-X07 End of Input, CT-X04 Format, CT-X05 Buffer, CT-X10 Protocol, CT-X08 Error State; Composite CT-K04 File I/O.

C mapping: `FILE *`, `fopen`, `fclose`, text I/O, return-value checks, `feof`/`ferror` only according to API semantics, transactional loading where partial failure matters.

Core evidence: check open/read/write/close states, distinguish EOF from error, test malformed/missing data, preserve invariants on failed load, and verify persisted results.

---

## F-U10 — How Can a Program Be Divided into Independently Maintainable Modules?

Core question: **How can interface and implementation be separated so program parts can be understood, translated, linked, tested, and replaced with controlled dependencies?**

Primary Concepts: CT-A12 Module, CT-A04 Interface, CT-A05 Implementation, CT-C06 C Translation, CT-A02 Responsibility, CT-E14 Documentation; Composite CT-K05 Modular Programming.

C mapping: `.h`/`.c`, declarations vs definitions, include guards, direct standard-library dependencies, separate translation, linkage where applicable, compile-vs-link diagnostics.

Core evidence: design an interface, split a source file, build all required translation units, diagnose declaration/definition/link errors, and replace an implementation without changing a valid client contract.

---

## F-U11 — How Can Programs Be Tested, Diagnosed, and Improved Systematically?

Core question: **What evidence beyond one correct output is needed before a program or technical claim should be trusted?**

Primary Concepts: CT-E01 Expected Result/Property, CT-E02 Test Case, CT-E03 Testing, CT-E04 Verification, CT-E05 Validation, CT-E06 Debugging, CT-E10 Regression Verification, CT-E11 Code Reading, CT-E13 Refactoring, CT-E17 Evidence, CT-E18 Judgment.

C mapping/activity: test tables/harnesses, diagnostics, defect reproduction and narrowing, behavior-preserving refactoring, compiler warnings and other tools where appropriate.

Core evidence: define expectations first, design normal/boundary/invalid/failure cases, narrow a fault through evidence, perform regression verification, and explain the limits of resulting confidence.

Optional `X` extension: when external assistance is actually used, apply CT-E16/19/20 conditionally and verify adopted claims. No external-assistance artifact is required from non-users.

---

## F-U12 — How Can Concepts Across the Course Be Integrated into One Verifiable Program?

Core question: **How can requirements, data, control, functions, memory/lifetime, interaction, modules, and verification be integrated without losing clear responsibilities or evidence?**

Primary Concepts: CT-C02 Requirement, CT-C03 Algorithm/Design, CT-A01 Decomposition, CT-A12 Module, CT-X10 Protocol, CT-E03 Testing, CT-E05 Validation, CT-E10 Regression Verification, CT-E18 Judgment.

This Unit introduces little new syntax. It integrates existing capabilities through requirement clarification, architecture/data-flow decisions, incremental implementation, failure handling, change impact, testing, diagnosis, and explanation.

Core evidence:

- convert requirements into observable behavior and technical contracts;
- design data/control/module responsibilities;
- build a minimal working slice incrementally;
- create and run relevant normal/boundary/invalid/failure/regression cases;
- handle a changed requirement without breaking unaffected behavior;
- explain design decisions, assumptions, limitations, and verification evidence.

---

## Relationship Between Units and Delivery

A Unit is a capability/concept skeleton, not a fixed class meeting.

- The Chinese preparatory track may deliver a Unit in one longer block.
- The English preparatory track may use more delivery slices and language scaffolds.
- Formal Units may span more than one week depending on the approved delivery plan.
- A delivery slice may adapt examples and pacing but may not silently change the Unit's core question, technical standard, or core evidence expectation.

## Unit Set

Current approved skeleton:

- Preparatory course: P-U01 through P-U04.
- Formal course: F-U01 through F-U12.
- Total: 16 Unit identifiers.

This count is a maintained design decision rather than a constitutional constant. Any merge/split requires updates to Concept Registry references, scope/competency traceability, material paths, both language versions, and the active audit.

## Maintenance Rules

1. Keep both language versions substantively equivalent.
2. Keep Unit identifiers stable unless a documented migration is performed.
3. Check Concept Registry dependencies and competency/scope standards when changing core Unit content.
4. Keep AI/external-assistance activities directly skippable unless an explicitly approved conditional activity targets tool judgment itself.
5. Verify concrete C/toolchain/runtime statements against the stated standard and target environment.
6. Ensure corresponding student materials remain readable, technically testable, and free of stale Unit requirements.
7. Record substantive changes in the repository-wide active audit.

## Related Documents

- [Programming Concept Tree](14-programming-concept-tree.en.md)
- [Programming Concept Registry](15-programming-concept-registry.en.md)
- [Programming Competency Map](05-competency-map.en.md)
- [Course Scope Boundary](06-scope-boundary.en.md)
- [Course Delivery Map](08-delivery-map.en.md)
- [Formal Materials Index](../materials/formal/README.en.md)
- [Preparatory Materials Index](../materials/preparatory/README.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](16-unit-map.zh-TW.md)
