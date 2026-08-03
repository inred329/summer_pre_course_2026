# Course Delivery Map

Version: 0.1.0  
Status: Architecture draft  
Corresponding Chinese version: [課程交付地圖](08-delivery-map.zh-TW.md)

## Document Purpose

This document arranges the [Programming Competency Map](05-competency-map.en.md), [Course Scope Boundary](06-scope-boundary.en.md), and [Competency Acceptance Model](07-acceptance-model.en.md) into three connected delivery paths:

1. Chinese-taught preparatory course: four 3-hour sessions, totaling 12 hours.
2. English-taught preparatory course: five 2-hour sessions, totaling 10 hours.
3. Formal course: sixteen 3-hour weeks, totaling 48 hours.

This document answers when capabilities and evidence are delivered. It is not a lesson-plan sequence, slide outline, or textbook table of contents. Each delivery unit must still follow Need → Design Purpose → Language Logic → Syntax → Implementation → Verification.

## Constitutional Compliance

- Both preparatory tracks have the same core capabilities, maturity targets, and minimum evidence.
- The additional two hours in the Chinese-taught track must not create a higher core graduation standard.
- The preparatory course must not replace the formal course in advance.
- The formal course must raise maturity rather than repeat preparatory activities at the same level.
- Testing, debugging, explanation, and AI verification must run through every delivery unit.
- No unit may treat program completion or OJ success as sufficient evidence of learning.
- This document does not presume advanced data structures to be formal-course core content.

---

# 1. Delivery Design Unit

Each delivery unit includes at least:

```text
Capability groups
+ Target maturity
+ Core question
+ Main learning activities
+ Minimum acceptance evidence
+ Later dependencies
```

A unit title is a container for capability delivery, not a restriction that the capability may appear only once. Cross-cutting capabilities recur, while maturity and task complexity must increase.

---

# 2. Shared Preparatory Capability Baseline

At the end of either preparatory track, students must meet the same minimum baseline:

| Capability group | Shared minimum target | Minimum evidence |
|---|---:|---|
| PC-E Program Translation and Execution | L2–L4 | Process explanation, minimal build, error classification |
| PC-D Data and State | L2–L4 | State tracing, basic input-process-output, requirement modification |
| PC-C Flow and Control | L2–L3 | Condition and loop tracing, termination explanation |
| PC-F Functions and Abstraction | L1–L3 | Function-purpose explanation, call reading, simple decomposition |
| PC-M Memory Model | L1–L2 | Visual distinction among value, location, and address |
| PC-O Data Organization | L1–L2 | Recognition of the purposes of sequence, index, string, and record |
| PC-V Testing, Debugging, and Verification | L2–L4 | Expected results, boundary cases, initial debugging record |
| PC-A AI-Assisted Learning | L2–L4 | AI-suggestion verification and decision record |
| PC-I Integrated Cycle | L3 | One small understand-modify-test-reflect cycle |

The minimum preparatory evidence package follows `07-acceptance-model`:

1. Explanation of a small program's execution process.
2. Condition or loop trace.
3. Simple requirement modification and retest.
4. Error classification and initial debugging.
5. AI-suggestion verification record.

---

# 3. Chinese-Taught Preparatory Delivery Path

The Chinese-taught track has four 3-hour sessions. Longer sessions support complete activity cycles and in-class acceptance; they do not raise the core standard.

## Session 1: How a Program Begins to Execute

### Core Question

> How does C source code become executable behavior, and how does program state begin to change?

### Main Capabilities

- `PC-E01`, `PC-E03`, `PC-E04`
- `PC-D01`, `PC-D03`
- `PC-V01`, `PC-V02`

### Target Maturity

- Toolchain and error stages: L2
- Minimal build: L4
- Variable-state tracing: L2–L3

### Activity Cycle

```text
Predict minimal-program behavior
→ Build and compile
→ Compare expected and actual results
→ Introduce one compile error
→ Classify the error stage
→ Draw source-to-execution flow
```

### Minimum Evidence

- `AT-04` toolchain diagram
- `AT-05` minimal implementation
- `AT-07` compile-error classification
- `AT-12` micro oral check

## Session 2: Data, Conditions, and State Change

### Core Question

> How does a program represent data and choose its next action from current state?

### Main Capabilities

- `PC-D02` through `PC-D05`
- `PC-C01` through `PC-C03`
- `PC-V01`, `PC-V03`

### Target Maturity

- Types and expressions: L2–L3
- Condition tracing: L3
- Basic input-process-output: L4

### Activity Cycle

```text
Requirement statement
→ Select a data representation
→ Derive condition results manually
→ Implement input-process-output
→ Verify normal and boundary cases
→ Modify one condition requirement
```

### Minimum Evidence

- `AT-03` condition and state trace
- `AT-05` minimal implementation
- `AT-06` requirement modification
- `AT-08` test cases

## Session 3: Repetition, Termination, and Function Responsibility

### Core Question

> How can a program repeat work reliably, and how can responsibility be decomposed as a problem grows?

### Main Capabilities

- `PC-C04` through `PC-C06`
- `PC-F01` through `PC-F03`
- `PC-V02`, `PC-V04`

### Target Maturity

- Loop model and tracing: L3
- Function purpose and interface: L2–L3
- Initial debugging: L3–L4

### Activity Cycle

```text
Define initial state, condition, update, and termination
→ Trace the loop step by step
→ Diagnose an off-by-one or infinite-loop fault
→ Extract one responsibility into a function
→ Create caller-side tests
```

### Minimum Evidence

- `AT-03` loop trace
- `AT-07` loop-fault diagnosis
- `AT-04` function-responsibility diagram
- `AT-05` small-function implementation

## Session 4: Integration, Modification, and AI Verification

### Core Question

> For a small requirement, how can a learner complete the full cycle of understanding, implementation, testing, modification, debugging, and AI verification?

### Main Capabilities

- `PC-I01`
- `PC-A01` through `PC-A05`
- `PC-V01` through `PC-V05`
- Integration of earlier capabilities

### Target Maturity

- Integrated cycle: L3
- AI-suggestion verification: L4
- Requirement modification and regression testing: L4

### Activity Cycle

```text
Understand the requirement independently
→ Propose an initial approach
→ Establish expected results
→ Complete a minimal implementation
→ Ask AI a specific question
→ Verify the AI suggestion
→ Change the requirement
→ Run regression tests
→ Explain acceptance or rejection
```

### Minimum Evidence

- `AT-06` requirement modification
- `AT-08` test design
- `AT-11` AI-suggestion review
- `AT-12` micro oral check

---

# 4. English-Taught Preparatory Delivery Path

The English-taught track has five 2-hour sessions. It uses the same core standard as the Chinese-taught track but divides longer cycles into smaller units to control language and cognitive load.

## Session 1: Execution and First Program

Main capabilities: `PC-E01`, `PC-E04`, `PC-V01`.  
Minimum evidence: toolchain explanation, minimal build, expected-versus-actual comparison.

## Session 2: Data, Types, and Program State

Main capabilities: `PC-D01` through `PC-D04`.  
Minimum evidence: variable-state table, expression trace, basic input-process-output.

## Session 3: Conditions and Repetition

Main capabilities: `PC-C01` through `PC-C06`.  
Minimum evidence: condition trace, four loop elements, boundary case, and fault diagnosis.

## Session 4: Functions and Decomposition

Main capabilities: `PC-F01` through `PC-F03`, `PC-V03`.  
Minimum evidence: responsibility-decomposition diagram, small function, caller-side tests, requirement modification.

## Session 5: Integrated Cycle and AI Verification

Main capabilities: `PC-I01`, `PC-A01` through `PC-A05`, `PC-V01` through `PC-V05`.  
Minimum evidence: complete small cycle, AI-verification record, regression testing, and micro oral check.

## Chinese and English Pacing Alignment

| Shared delivery | Chinese-taught track | English-taught track |
|---|---|---|
| Toolchain and minimal program | Session 1 | Session 1 |
| Data, state, and basic operations | Sessions 1–2 | Session 2 |
| Conditions and loops | Sessions 2–3 | Session 3 |
| Functions and decomposition | Session 3 | Session 4 |
| Integration, modification, testing, and AI verification | Session 4 | Session 5 |

The additional two hours in the Chinese-taught track should be used first for:

- More live tracing and oral sampling.
- Remedial practice and fault diagnosis.
- A second modification and regression cycle.
- Additional Chinese explanation and visual modeling.

They must not create core capabilities required only of the Chinese-taught students.

---

# 5. Formal 16-Week Delivery Path

The formal course is not a topic list. It consists of five stages that raise capability maturity.

## Stage A: Stabilizing Shared Models (Weeks 1–3)

| Week | Main delivery | Target maturity | Main evidence |
|---|---|---:|---|
| 1 | Toolchain, execution model, and preparatory diagnosis | L2–L4 | AT-01, AT-03, AT-07 |
| 2 | Types, expressions, conversions, and I/O | L3–L5 | AT-03, AT-05, AT-08 |
| 3 | Conditions, loops, and combined control | L4–L5 | AT-06, AT-07, AT-12 |

This stage does not reteach the preparatory course. It uses new contexts, fault cases, and requirement changes to raise students toward implementation and diagnosis.

## Stage B: Functions and Modularization (Weeks 4–6)

| Week | Main delivery | Target maturity | Main evidence |
|---|---|---:|---|
| 4 | Function interfaces, parameters, return values, and call tracing | L3–L5 | AT-03, AT-04, AT-05 |
| 5 | Problem decomposition, single responsibility, and testable design | L4–L6 | AT-06, AT-09, AT-12 |
| 6 | Scope, lifetime, basic recursion, and integration check | L3–L5 | AT-03, AT-07, AT-09 |

## Stage C: Memory Model (Weeks 7–10)

| Week | Main delivery | Target maturity | Main evidence |
|---|---|---:|---|
| 7 | Value, location, address, address-of, and dereference | L3–L5 | AT-04, AT-03, AT-05 |
| 8 | Pointer aliasing, functions, and memory state | L4–L5 | AT-03, AT-07, AT-12 |
| 9 | Sequences, indexing, contiguous layout, and strings | L4–L5 | AT-05, AT-08, AT-07 |
| 10 | Automatic/dynamic storage, allocation, release, and common faults | L4–L5 | AT-05, AT-07, AT-08 |

This stage focuses on C memory semantics and does not use advanced data structures as the teaching vehicle.

## Stage D: Data Organization and Maintainable Programs (Weeks 11–13)

| Week | Main delivery | Target maturity | Main evidence |
|---|---|---:|---|
| 11 | Records, structures, and data models | L4–L5 | AT-04, AT-05, AT-06 |
| 12 | Searching, updating, and basic rearrangement of sequences and records | L4–L5 | AT-05, AT-08, AT-09 |
| 13 | Multi-file organization, interfaces, regression testing, and maintenance | L4–L6 | AT-06, AT-07, AT-09 |

## Stage E: Integration, Transfer, and Acceptance (Weeks 14–16)

| Week | Main delivery | Target maturity | Main evidence |
|---|---|---:|---|
| 14 | AI-code review, injected faults, and systematic debugging | L5–L6 | AT-07, AT-11, AT-12 |
| 15 | Integrated requirement change, regression verification, and transfer | L5–L6 | AT-06, AT-08, AT-10 |
| 16 | Integrated capability acceptance, explanation, and reflection | L5–L6 | Complete evidence package, micro oral check, transfer explanation |

---

# 6. Continuous Delivery of Cross-Cutting Capabilities

## Testing and Debugging

- Establish expected results before the first implementation.
- Every topic includes at least one normal and one boundary case.
- Every stage includes at least one defect-diagnosis task.
- Every correction requires regression verification.

## AI-Assisted Learning

AI is not concentrated in one week. Every stage includes at least one of:

- Verify an AI concept explanation.
- Review AI-generated code or tests.
- Compare an AI approach with a student approach.
- Experimentally test an AI debugging hypothesis.

Week 14 is integrated AI acceptance, not the first introduction to AI.

## Visual Models and Oral Explanation

- Execution, state, control flow, function calls, and memory concepts require reconstructable visual models.
- Every major stage includes at least one short oral explanation or live sampling activity.
- Visuals must support reasoning rather than serve as decoration.

---

# 7. Pacing Adjustment Rules

When the course falls behind, use this priority order:

1. Preserve core capabilities and minimum evidence.
2. Preserve tracing, testing, debugging, and explanation.
3. Reduce the number of exercises or context complexity.
4. Reclassify extension content as demonstration or resources.
5. Never compensate by skipping acceptance, compressing AI verification, or adding advanced topics.

When students progress faster, the course may:

- Add requirement changes and fault diagnosis.
- Increase unfamiliarity of new contexts.
- Compare implementations and language representations.
- Improve evidence quality rather than expand into advanced data structures.

---

# 8. Delivery Map Completion Criteria

After this document is established, later design must be able to:

- Trace every preparatory unit and formal week to capability IDs, maturity levels, and acceptance tasks.
- Demonstrate that both preparatory tracks have the same core standard.
- Explain how the formal course continues rather than repeats the preparatory course.
- Show how testing, debugging, explanation, and AI verification run through the full course.
- Prevent schedule pressure from reducing learning to syntax, output, or unplanned advanced data structures.

The next document is the [Risk Register](09-risk-register.en.md), which will identify risks in pacing, cognitive load, bilingual equivalence, AI dependency, and acceptance execution.

## Navigation

- [Previous: Competency Acceptance Model](07-acceptance-model.en.md)
- [Back to Instructional Design Workspace](README.en.md)
- [繁體中文版](08-delivery-map.zh-TW.md)
