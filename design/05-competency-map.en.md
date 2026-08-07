# Programming Competency Map

Version: 0.2.1  
Status: Active design standard  
Governance note: This standard defines competency identifiers and evidence expectations; the Constitution and official learning/assessment policy remain authoritative for governance, grading, and tool-use rules  
Corresponding Chinese version: [程式設計能力地圖](05-competency-map.zh-TW.md)

## Document Purpose

This document converts the [Programming Domain Model](03-programming-domain-model.en.md) and [Programming Language Knowledge Dependency Graph](04-programming-language-knowledge-graph.en.md) into observable, teachable, and assessable programming capabilities.

- The domain model describes concepts and relationships.
- The knowledge dependency graph describes prerequisite and supporting relationships.
- This competency map defines what students should be able to do.

This document is not a weekly schedule or grading rubric. Scope, acceptance, delivery, materials, and assessment implementations may reference the competency identifiers here, but grading and AI/tool policy are governed by the official learning and assessment policy.

## Constitution 2.0 Alignment

- Capability cannot be established by successful execution or passed tests alone.
- Capability statements must be concrete, observable, and technically verifiable.
- Both language versions use the same identifiers, maturity meanings, substantive targets, status, and version.
- Testing, debugging, explanation, modification, and verification remain core evidence sources.
- AI and other external tools are optional by default. No core competency requires AI use or an AI-use record.
- When a learner actually adopts external assistance, conditional evidence may examine whether the adopted result was understood and technically verified.
- This standard does not preselect advanced data structures as core C-course capabilities.

---

# 1. Competency Maturity Model

```mermaid
flowchart LR
    L1[L1 Recognize] --> L2[L2 Explain]
    L2 --> L3[L3 Trace]
    L3 --> L4[L4 Implement]
    L4 --> L5[L5 Diagnose]
    L5 --> L6[L6 Transfer]
```

| Level | Name | Observable behavior |
|---|---|---|
| L0 | Not established | Cannot yet recognize or use the capability reliably without guessing or imitation. |
| L1 | Recognize | Identifies a concept, syntax element, datum, state, or relevant execution/translation responsibility in an example. |
| L2 | Explain | Explains in their own words why the concept exists, its logic, boundaries, and role. |
| L3 | Trace | Predicts relevant execution, data state, control flow, memory/lifetime state, or build evidence step by step. |
| L4 | Implement | Selects and correctly applies the capability to complete a scoped task. |
| L5 | Diagnose | Designs tests, locates faults, explains causes, handles relevant failure conditions, and makes justified modifications. |
| L6 | Transfer | Recognizes and adapts the same reasoning in a new context, larger problem, or another language/toolchain. |

Important capabilities should normally use more than one kind of evidence, including explanation or tracing and implementation, modification, testing, or diagnosis as appropriate.

---

# 2. Shared Learning Evidence

| Evidence code | Type | What the student demonstrates |
|---|---|---|
| EV-EX | Explanation | Explains requirements, design purpose, language logic, assumptions, and program behavior in their own words. |
| EV-VI | Visual representation | Draws and interprets flow, state, memory/lifetime, function-call, data-organization, or build-responsibility models. |
| EV-TR | Trace | Records relevant values, control paths, calls, object/lifetime changes, or other state transitions step by step. |
| EV-IM | Implementation | Completes a program or fragment that satisfies the current scope and stated technical contract. |
| EV-MO | Modification | Changes an existing program for a changed requirement and explains affected behavior and tests. |
| EV-TE | Testing | Defines expected behavior and creates normal, boundary, invalid, and failure cases when relevant. |
| EV-DE | Debugging | Reproduces a problem, narrows scope, forms and tests hypotheses, explains the correction, and performs regression verification. |
| EV-CO | Comparison | Compares forms, solutions, diagnostics, references, or tool outputs and explains trade-offs. |
| EV-AI | Conditional external-assistance judgment | Only when AI or another external assistant was actually used, explains the adopted suggestion, verification evidence, limitations, and accept/modify/reject decision. |
| EV-RE | Reflection and transfer | Explains how the capability applies to a new problem, later topic, environment, or language. |

No official assessment may use only EV-IM, automated-test success, tool approval, or one correct output as its sole evidence. EV-AI is never required merely to prove that a student used or did not use AI.

---

# 3. Competency Groups

## PC-E: Program Translation and Execution

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-E01 | Explain that C source text is translated by an implementation before CPU-level execution, and distinguish conceptual responsibilities such as preprocessing behavior, translation/compilation, optional object generation/linking, loading/startup, and execution without claiming every implementation exposes the same physical pipeline. | None | L2 | L3 | EV-EX, EV-VI |
| PC-E02 | Compare the specified toolchain's actual commands, inputs, outputs, and diagnostics with the conceptual build-responsibility model. | PC-E01 | L1 | L3 | EV-EX, EV-CO |
| PC-E03 | Use diagnostics or observed behavior to classify a problem at an appropriate level such as source/translation, linkage when applicable, startup/runtime, or program logic. | PC-E01, PC-V02 | L2 | L5 | EV-DE, EV-EX |
| PC-E04 | Create, build, and run a minimal C program in the specified environment and explain the commands, artifacts, and evidence actually observed. | PC-E01 | L4 | L5 | EV-IM, EV-EX, EV-DE |

## PC-D: Data and State

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-D01 | Distinguish a value, type, object/variable name, current value, and storage/lifetime concept. | PC-E01 | L2 | L4 | EV-EX, EV-VI |
| PC-D02 | Select an appropriate basic type from data meaning and explain relevant range, precision, conversion, or operation constraints. | PC-D01 | L2 | L5 | EV-EX, EV-CO, EV-IM |
| PC-D03 | Trace state changes caused by declaration, initialization, assignment, and expression evaluation. | PC-D01, PC-D02 | L3 | L5 | EV-TR, EV-VI, EV-DE |
| PC-D04 | Build and interpret arithmetic, comparison, and logical expressions while handling precedence, conversions, and relevant undefined or implementation-dependent boundaries. | PC-D02, PC-D03 | L3 | L5 | EV-TR, EV-IM, EV-DE |
| PC-D05 | Design an input-process-output flow and verify input assumptions, error states, and output reasonableness. | PC-D01 through PC-D04 | L4 | L5 | EV-IM, EV-TE, EV-EX |
| PC-D06 | Explain scope and lifetime and diagnose errors caused by confusing name visibility with object validity. | PC-F02, PC-M01 | L1 | L5 | EV-VI, EV-DE, EV-EX |

## PC-C: Flow and Control

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-C01 | Trace actions in execution order and explain causal state changes. | PC-D03 | L3 | L5 | EV-TR, EV-EX |
| PC-C02 | Convert a requirement into an evaluable condition and predict a selection path. | PC-D04, PC-C01 | L3 | L5 | EV-VI, EV-TR, EV-IM |
| PC-C03 | Compare one-way, two-way, and multi-way selection and choose an appropriate form. | PC-C02 | L2 | L5 | EV-CO, EV-IM, EV-MO |
| PC-C04 | Define initial state, continuation condition, update, and termination for a repetition problem. | PC-D03, PC-C02 | L3 | L5 | EV-VI, EV-TR, EV-IM |
| PC-C05 | Use loops for counting, accumulation, searching, or item-by-item processing and explain each iteration. | PC-C04 | L3 | L5 | EV-TR, EV-IM, EV-TE |
| PC-C06 | Diagnose non-termination, boundary errors, and off-by-one defects. | PC-C04, PC-V02 | L2 | L5 | EV-DE, EV-TE, EV-EX |
| PC-C07 | Combine conditions, loops, and nested control for more complex problems while preserving readable state reasoning. | PC-C02 through PC-C06 | L1 | L5 | EV-VI, EV-IM, EV-MO |

## PC-F: Functions and Abstraction

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-F01 | Identify separable responsibilities in a requirement and explain that functions are not merely a way to shorten code. | PC-D05, PC-C03 | L2 | L5 | EV-EX, EV-VI |
| PC-F02 | Distinguish function declaration, definition, call, parameter, return value, and interface contract. | PC-F01 | L2 | L4 | EV-EX, EV-CO, EV-IM |
| PC-F03 | Design small functions with explicit inputs, outputs, preconditions, and caller-side tests. | PC-F02, PC-V01 | L3 | L5 | EV-IM, EV-TE, EV-EX |
| PC-F04 | Trace nested calls, arguments/parameters, local objects, return points, and lifetimes using an implementation-neutral activation model; relate this to a call stack only when the target environment uses that model. | PC-F02, PC-D06 | L1 | L5 | EV-VI, EV-TR |
| PC-F05 | Decompose a larger problem into low-coupling, single-responsibility, independently testable functions/modules. | PC-F03, PC-C07 | L1 | L6 | EV-VI, EV-IM, EV-CO, EV-RE |
| PC-F06 | Identify suitable and unsuitable uses of recursion and trace base and recursive cases, including termination and resource implications. | PC-F04, PC-C04 | L0 | L4 | EV-VI, EV-TR, EV-CO |

## PC-M: Memory Model

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-M01 | Distinguish names, values, objects, storage, addresses, and lifetime. | PC-D01 | L1 | L4 | EV-VI, EV-EX |
| PC-M02 | Explain pointer types and values and correctly use address-of and dereference only when validity and operation preconditions hold. | PC-M01, PC-D02 | L0 | L5 | EV-VI, EV-TR, EV-IM |
| PC-M03 | Trace aliasing and explain which object or storage region a modification affects. | PC-M02, PC-D03 | L0 | L5 | EV-VI, EV-TR, EV-DE |
| PC-M04 | Explain array contiguity, indexing, pointer relationships, valid bounds, and one-past limitations where relevant. | PC-M02, PC-O01 | L0 | L5 | EV-VI, EV-TR, EV-DE |
| PC-M05 | Compare automatic and allocated storage duration and explain that stack/heap diagrams are teaching and implementation models rather than C-language guarantees. | PC-F04, PC-M01 | L0 | L4 | EV-VI, EV-CO, EV-EX |
| PC-M06 | Allocate, resize when required, and release dynamic storage while handling size arithmetic, allocation failure, ownership, and lifetime responsibility. | PC-M02, PC-M05, PC-V02 | L0 | L5 | EV-IM, EV-TE, EV-DE |
| PC-M07 | Diagnose null/invalid pointers, dangling pointers, out-of-bounds access, double release, use-after-release, and memory leaks using evidence appropriate to the target environment. | PC-M03, PC-M04, PC-M06 | L0 | L5 | EV-DE, EV-VI, EV-TE |

## PC-O: Data Organization

This group focuses on sequences, strings, records, and general data operations. It does not preselect advanced data structures as formal-course core content.

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-O01 | Use indexes to represent and process a homogeneous sequence while respecting valid bounds and tracing element state. | PC-C05, PC-D02 | L1 | L5 | EV-VI, EV-TR, EV-IM |
| PC-O02 | Treat a C string as a character array whose valid string representation depends on a terminating null character, and handle capacity, length, bounds, and input limitations. | PC-O01, PC-C05 | L0 | L5 | EV-VI, EV-IM, EV-DE |
| PC-O03 | Use a structure to group fields describing one entity into a record. | PC-D02, PC-F01 | L0 | L5 | EV-VI, EV-IM, EV-EX |
| PC-O04 | Use sequences or records to organize multiple items and design search, update, and basic rearrangement operations. | PC-O01, PC-O03, PC-C05 | L0 | L5 | EV-IM, EV-TE, EV-MO |
| PC-O05 | Compare basic search or rearrangement approaches, trace data changes, and explain suitable contexts. | PC-O01, PC-C05, PC-V01 | L0 | L5 | EV-TR, EV-CO, EV-IM |
| PC-O06 | Explain that data organization is a design choice involving data, relationships, and permitted operations rather than merely syntax. | PC-O01, PC-O03, PC-F01 | L0 | L4 | EV-EX, EV-VI, EV-RE |

## PC-V: Testing, Debugging, and Verification

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-V01 | State expected results or properties before execution and compare them with observed evidence. | PC-E04, PC-D03 | L3 | L6 | EV-TE, EV-TR, EV-EX |
| PC-V02 | Distinguish translation/build, linkage when applicable, runtime/precondition, logic, boundary, and requirement errors using appropriate evidence. | PC-E03, PC-V01 | L2 | L5 | EV-DE, EV-CO |
| PC-V03 | Create normal, boundary, invalid, and failure cases when relevant and explain why each case matters. | PC-V01, related capability | L2 | L6 | EV-TE, EV-EX |
| PC-V04 | Reproduce a problem, narrow its scope, form a testable hypothesis, and locate the cause. | PC-V02, PC-V03 | L2 | L6 | EV-DE, EV-TR |
| PC-V05 | Run regression checks after a correction and explain the limits of the resulting confidence. | PC-V04 | L1 | L6 | EV-DE, EV-TE, EV-EX |

## PC-A: Conditional External-Assistance Judgment

This group is optional and conditional. It does not define universal preparatory or formal-course maturity targets. It applies only when a learner actually uses AI or another external assistant, or when an explicitly approved activity makes tool judgment itself the learning objective.

| Competency ID | The student can... | Main prerequisites | Universal target | Conditional evidence |
|---|---|---|---|---|
| PC-A01 | State their own understanding, available evidence, and point of difficulty before relying on an external suggestion. | Relevant topic capability | None | EV-AI, EV-EX |
| PC-A02 | Ask for a bounded explanation, hint, comparison, or testing perspective without treating the result as authoritative. | PC-A01 | None | EV-AI, EV-RE |
| PC-A03 | Verify adopted external suggestions through programs, tests, compiler diagnostics, reliable references, tracing, or other reproducible evidence. | PC-V03, related capability | None | EV-AI, EV-TE, EV-DE |
| PC-A04 | Explain why an external suggestion was accepted, modified, or rejected. | PC-A03 | None | EV-AI, EV-EX |
| PC-A05 | Identify unsupported syntax/features, incorrect assumptions, undefined behavior, unsafe boundaries, or unnecessary complexity in external suggestions. | PC-A03, PC-V02 | None | EV-AI, EV-DE, EV-CO |
| PC-A06 | Provide only the tool-use record or attribution required by a specific activity, integrity rule, or assessment condition; no non-use declaration is required. | PC-A01 through PC-A04 | None | EV-AI only when applicable |

## PC-I: Integrated Development Cycle

| Competency ID | The student can... | Main prerequisites | Preparatory target | Formal-course target | Evidence |
|---|---|---|---|---|---|
| PC-I01 | Complete a small development cycle covering requirement understanding, an appropriate model, data/control design, minimal implementation, testing, debugging, modification, and reflection. Optional external assistance may be used but is not a prerequisite. | PC-D, PC-C, PC-F, PC-V | L3 | L6 | EV-VI, EV-IM, EV-MO, EV-TE, EV-DE, EV-RE; EV-AI only if applicable |

## Usage Principles

1. This competency map is an active design standard for competency identifiers and evidence expectations; it does not assign weeks or define grading percentages.
2. The scope document defines maturity boundaries between preparatory and formal courses.
3. A new core capability must be traceable to programming concepts and dependencies, not merely to a current tool trend.
4. Topic breadth must not reduce testing, debugging, explanation, modification, or verification expectations.
5. Optional AI/external-assistance capabilities must not be included as universal prerequisites, completion gates, maturity targets, or required evidence.
6. Any future inclusion of advanced data structures requires separate justification covering requirements, prerequisites, time, and evidence.
7. Implementation-specific claims must identify and verify the relevant compiler, standard mode, operating environment, or runtime model when those details matter.

## Related Documents

- [Programming Language Knowledge Dependency Graph](04-programming-language-knowledge-graph.en.md)
- [Course Scope Boundary](06-scope-boundary.en.md)
- [Acceptance Model](07-acceptance-model.en.md)
- [Official Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](05-competency-map.zh-TW.md)
