# Student Material Outlines for 16 Units

Version: 0.2.0  
Status: Revisable planning and traceability model  
Last updated: 2026-08-07  
Governance note: This document plans student-material structure. It does not create grading, completion, AI/tool-use, or submission policy. The Constitution, official learning/assessment policy, design standards, and current student materials take precedence.  
Corresponding Chinese version: [16 個 Unit 的學生教材大綱](17-student-material-outlines.zh-TW.md)

## Document Purpose

This document translates the [Concept-Driven Unit Map](16-unit-map.en.md) into maintainable outlines for the 4 preparatory Units and 12 formal-course Units. It is a planning model, not the authoritative student material itself.

Each outline should support independent reading and normally include:

> Core Question → Prediction → Visual/Execution Model → Concept and C Mapping → Trace/Implementation → Error Diagnosis → Testing/Modification → Core Reflection → Summary

The exact section count may vary when a different structure improves readability. Core evidence must remain available without AI or another external assistant.

## Constitution 2.0 Alignment

- AI and other external assistance are optional by default.
- No outline requires an AI conversation, fixed prompt, saved transcript, AI-use record, or non-use declaration.
- A core reflection asks the learner to explain the central relationship in their own words and support it with code, a trace, a diagram, tests, or other evidence. It may be completed without an external tool.
- Optional external-assistance extensions, when offered, are directly skippable and require verification only when the learner actually adopts an external suggestion.
- Concrete C/toolchain claims must state relevant technical contracts and must distinguish language guarantees from implementation-specific behavior.
- The Chinese and English outlines use the same Unit IDs, core questions, technical depth, and evidence direction.

## Shared Authoring Requirements

Every completed student Unit should make the following visible where relevant:

1. what the learner should predict before observing a result;
2. the input/state/control/lifetime/stream/module contract needed to reason correctly;
3. at least one reproducible defect or failure case;
4. normal, boundary, invalid, or failure tests appropriate to the topic;
5. a requirement change or modification task;
6. what evidence supports confidence and what remains uncertain;
7. a directly accessible core completion path that does not depend on optional external tools.

---

# Preparatory Course

## P-U01 — How Does Program Text Become an Execution Result?

Core question: **How does human-readable program text become behavior that a computer can execute in the specified environment?**

Outline focus:

- problem, requirement, algorithm/design, source code, translation/build, diagnostic, executable/loadable representation, execution, output;
- minimal `main`, `stdio`, return status, and validated build/run commands;
- prediction before execution and diagnosis of a translation/build defect;
- explicit distinction between the conceptual build-responsibility model and the target toolchain's actual exposed stages/artifacts.

Core evidence: prediction, build/run observation, diagnostic classification, source change plus rebuild, and explanation of the observed source-to-execution chain.

Core reflection: Explain the relationship among source code, translation/build, the target program representation, execution, and observable evidence.

---

## P-U02 — How Does a Program Remember Data and Change State?

Core question: **How does a program preserve current data and produce a new state after each execution step?**

Outline focus:

- data, value, type, object/name, initialization, assignment, expression, evaluation, input/output, state change;
- state tables and expected results before execution;
- basic type/range/format assumptions and input-state boundaries;
- diagnosis of uninitialized, conversion, input, or format mistakes only through safe, well-specified examples.

Core evidence: stepwise state trace, predicted expression result, corrected defect, and a small requirement modification with retest.

Core reflection: Explain how value, type, named object, expression evaluation, and state change connect.

---

## P-U03 — How Does a Program Select and Repeat?

Core question: **When different situations require different actions, or one action must repeat, how does a program determine the next step?**

Outline focus:

- sequence, condition, selection, repetition, loop state, update, boundary, termination/nontermination;
- `if`/`else`, `while`, `for`, and carefully scoped transfer statements;
- branch prediction, iteration traces, off-by-one cases, and termination reasoning;
- regression verification after a changed boundary or requirement.

Core evidence: path trace, loop-state table, boundary tests, diagnosis of nontermination/off-by-one, and verified correction.

Core reflection: Explain how condition, state update, repetition, boundary, and termination work together.

---

## P-U04 — How Can a Large Problem Be Divided into Understandable Work?

Core question: **When a program grows longer, how can responsibilities be separated so each part can be understood, tested, and modified?**

Outline focus:

- decomposition, responsibility, function, interface, parameter, argument, return value, call;
- caller/callee state and basic function contracts;
- normal/boundary tests for small functions;
- comparing alternative decompositions and changing one requirement without rewriting unrelated responsibilities.

Core evidence: responsibility statement, call trace, tested function, decomposition comparison, and requirement modification.

Core reflection: Explain how responsibility, interface, parameter, argument, return value, and test evidence connect.

---

# Formal Course

## F-U01 — Why Do Representation, Type, and Operations Affect Results?

Core question: **Why can the same mathematical idea or source expression produce different program behavior because of representation, type, and conversion?**

Outline focus: integer ranges, bit/byte concepts, signed/unsigned boundaries, character representation, floating approximation, conversions, and formatted I/O. Separate portable C guarantees from implementation-defined or implementation-specific observations.

Core evidence: predicted results, boundary experiments appropriate to the target implementation, conversion/format defect diagnosis, and explanation of representation limits.

Core reflection: Explain how representation, type, conversion, and operation rules constrain observable results.

---

## F-U02 — How Can Reliable Multi-Branch and Repetitive Flows Be Built?

Core question: **When conditions, boundaries, and repetition rules become complex, how can correctness still be demonstrated?**

Outline focus: multi-way selection, nested control, sentinels, invariants, path coverage, compound conditions, and regression after control-flow changes.

Core evidence: path table/diagram, invariant or loop-state explanation, boundary/sentinel tests, diagnosed logic defect, and verified correction.

Core reflection: Explain how path coverage, loop condition, boundary, sentinel, and invariant provide complementary evidence.

---

## F-U03 — How Does Data Form an Ordered Collection?

Core question: **When multiple related values must be stored and processed together, how are they organized, located, and traversed safely?**

Outline focus: arrays, indexes, length/capacity, contiguous element layout, traversal, function-parameter array behavior, and out-of-bounds risk.

Core evidence: index/layout diagram, traversal trace, valid/invalid boundary cases, safe diagnosis of an indexing defect, and retest after a size change.

Core reflection: Explain how array layout, index, valid bounds, and iteration interact.

---

## F-U04 — How Is Text Represented and Processed as Data?

Core question: **How does C represent text, and how can a program know the valid content and capacity boundaries?**

Outline focus: `char` arrays, null termination, string literals, capacity versus length, `fgets`, input newline/state, selected string functions, and buffer boundaries.

Core evidence: character-array/string diagram, capacity/termination tests, diagnosis of malformed or truncated input handling, and corrected implementation with retest.

Core reflection: Explain why not every `char` array is a valid C string and why capacity and termination are separate concerns.

---

## F-U05 — What State Exists During Nested and Recursive Function Calls?

Core question: **During nested or recursive calls, how can parameters, local objects, return points, scope, and lifetime be reasoned about without assuming one physical runtime representation?**

Outline focus: activation model, scope, lifetime, automatic storage duration, nested calls, recursion, termination/base cases, and resource implications. A call-stack diagram may be used as an implementation/teaching model but must not be presented as a C-language guarantee.

Core evidence: activation/lifetime trace, scope-versus-lifetime comparison, recursion trace, and diagnosis of nontermination or invalid lifetime reasoning.

Core reflection: Explain the difference among scope, object lifetime, activation state, and a target implementation's possible call-stack visualization.

---

## F-U06 — How Can Data Be Accessed Indirectly Through Pointer Values?

Core question: **How can a pointer value designate an object, and under what preconditions is indirect access valid?**

Outline focus: objects, addresses, pointer types/values, null pointer, dereference preconditions, aliasing, pointer parameters, lifetime, bounds, and limited array relationships.

Core evidence: object-pointer diagram, aliasing trace, valid/invalid precondition classification, pointer-parameter modification, and safe diagnosis of null/dangling/out-of-bounds risks.

Core reflection: Explain how pointer value/type, designated object, lifetime, bounds, and dereference preconditions connect.

---

## F-U07 — How Can One Data Object Contain Different Fields?

Core question: **When one entity contains several different kinds of data, how can those fields be represented and manipulated as one meaningful record?**

Outline focus: requirements-to-fields, `struct` types/objects, member access, initialization, assignment, passing, nested structures, layout caveats, and record validity.

Core evidence: record design from requirements, member updates, function interaction, invalid-data tests, and comparison of two data designs.

Core reflection: Explain the difference among a structure type, a structure object, its members, and the interface responsibility around that record.

---

## F-U08 — How Does a Program Manage Storage Whose Size or Lifetime Is Decided at Runtime?

Core question: **When required storage cannot be fixed in advance, how can allocation, resizing, ownership/release responsibility, failure, and lifetime be handled safely?**

Outline focus: `malloc`, `calloc`, `realloc`, `free`, size arithmetic, allocation failure, failure-preserving resize patterns, ownership/release responsibility, dangling use, leaks, and double release.

Core evidence: allocation/use/release diagram, size/bounds reasoning, explicit failure path, ownership explanation, safe resize implementation, and regression after a capacity change.

Core reflection: Explain how allocation success, pointer ownership, lifetime, resizing, and release responsibility connect.

---

## F-U09 — How Does a Program Interact with Files and Persistent Data?

Core question: **When data is read from or written to an external file, how can the program distinguish valid data, end of input, and failure while preserving resource state?**

Outline focus: pathname/file versus opened stream, `FILE *`, open/read/write/close results, end-of-input indications, stream error state, text format/protocol, and transactional/failure-preserving loading where appropriate.

Core evidence: state/error trace, open/read/write failure cases, persisted-data verification, resource-closure reasoning, and corrected format/error handling.

Core reflection: Explain the difference among pathname/file, opened stream, end-of-input indication, and error state.

---

## F-U10 — How Can a Program Be Divided into Independently Maintainable Modules?

Core question: **How can interface and implementation be separated so program parts can be changed and built with explicit dependencies?**

Outline focus: headers/source files, declarations/definitions, include guards, translation units, target-toolchain build steps, linkage where applicable, dependency tracing, and compile-versus-link evidence.

Core evidence: interface/implementation split, dependency graph, target-toolchain build, diagnosis of declaration/definition/linkage defects, and replacement of an implementation behind a stable interface.

Core reflection: Explain how interface, implementation, translation unit, dependency, and linkage/build evidence differ.

---

## F-U11 — How Can Programs Be Tested, Diagnosed, and Improved Systematically?

Core question: **What evidence beyond one correct output is needed before a program or technical claim can be trusted?**

Outline focus: expected results, normal/boundary/invalid/failure tests, reproducibility, symptom/cause/hypothesis, debugging, verification, validation, regression, refactoring, evidence quality, and confidence limits.

Core evidence: expected-results-first test design, reproduced defect, tested hypothesis, correction, regression, and comparison of evidence strength.

Core reflection: Explain the differences and relationships among testing, verification, validation, debugging, and regression verification.

---

## F-U12 — How Can a Program Integrate Concepts Across the Course?

Core question: **How can requirements, data, control, functions, memory/lifetime, interaction, and engineering evidence be integrated into one maintainable program?**

Outline focus: requirement contracts, decomposition, data/control/module design, incremental implementation, failure handling, testing, modification, validation, maintenance, and explanation of trade-offs.

Core evidence: end-to-end traceability from requirement to implementation/test evidence, a changed requirement, a diagnosed defect or failure path, regression verification, and explanation of remaining limits.

Core reflection: Explain how requirements, design, implementation, tests, failure handling, and maintenance evidence form one development cycle.

---

## Optional External-Assistance Extension Pattern

A Unit may optionally add a short extension after the core path, for example:

1. the learner states their own current reasoning or expected result;
2. the learner optionally obtains an external suggestion;
3. the learner identifies a claim worth checking;
4. the learner verifies it with code, tests, diagnostics, reliable references, tracing, or another reproducible method;
5. the learner accepts, modifies, or rejects the suggestion.

This pattern is never a universal requirement. No fixed prompt, complete conversation log, before/after artifact, AI summary, or non-use declaration is required unless a specific approved activity or integrity rule explicitly says otherwise.

## Maintenance Rules

When changing this planning model:

- update the Chinese/English pair together;
- preserve Unit IDs and the current Unit Map's core questions/evidence direction;
- compare proposed outline changes with the actual current student materials before claiming implementation is complete;
- do not duplicate official assessment policy;
- keep optional external assistance directly skippable;
- verify concrete technical claims against the specified C standard/toolchain/environment;
- record substantive governance findings in the active Constitution 2.0 audit.

## Related Documents

- [Concept-Driven Unit Map](16-unit-map.en.md)
- [Programming Concept Registry](15-programming-concept-registry.en.md)
- [Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Formal Student Materials](../materials/formal/README.en.md)
- [Preparatory Student Materials](../materials/preparatory/)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](17-student-material-outlines.zh-TW.md)
