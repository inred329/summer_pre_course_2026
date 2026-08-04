# Programming Concept Registry

Version: 0.1.0  
Status: Concept identification and dependency draft  
Last updated: 2026-08-04  
Corresponding Chinese version: [程式設計 Concept Registry](15-programming-concept-registry.zh-TW.md)

## Document Purpose

This document assigns stable IDs, primary dependencies, course scope, and suggested maturity targets to the core concepts in the Concept Tree. The Concept Tree answers “Which concepts exist?” This Registry answers “How is each concept tracked, depended on, and composed?”

This document does not yet define Units directly. A Unit should be composed from concepts that share a meaningful learning question and a coherent dependency path.

## ID Rules

| Domain | Prefix |
|---|---|
| Computation | `CT-C` |
| Information | `CT-I` |
| State | `CT-S` |
| Control Flow | `CT-F` |
| Abstraction | `CT-A` |
| Memory | `CT-M` |
| Interaction | `CT-X` |
| Engineering | `CT-E` |
| Composite Concept | `CT-K` |

Scope markers:

- `P-C`: preparatory-course core
- `P-F`: preparatory-course foundation
- `F-C`: formal-course core
- `F-A`: formal-course advanced or deferred

Maturity levels:

- `L1`: recognize
- `L2`: complete with guidance
- `L3`: independently handle familiar situations
- `L4`: apply under modified requirements or in a new context
- `L5`: compare, explain, and evaluate multiple approaches

## Computation

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-C01 | Problem | — | P-C | L3 |
| CT-C02 | Requirement | CT-C01 | P-C | L3 |
| CT-C03 | Algorithm | CT-C01, CT-C02 | P-C | L3 |
| CT-C04 | Program | CT-C03 | P-C | L3 |
| CT-C05 | Source Code | CT-C04 | P-C | L3 |
| CT-C06 | Translation | CT-C05 | P-C | L2 |
| CT-C07 | Compiler | CT-C06 | P-C | L2 |
| CT-C08 | Executable | CT-C06, CT-C07 | P-C | L2 |
| CT-C09 | Execution | CT-C08 | P-C | L3 |
| CT-C10 | Process | CT-C09 | P-F | L1 |
| CT-C11 | Termination | CT-C09 | P-C | L2 |

## Information

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-I01 | Data | CT-C04 | P-C | L3 |
| CT-I02 | Value | CT-I01 | P-C | L3 |
| CT-I03 | Representation | CT-I01, CT-I02 | P-F | L2 |
| CT-I04 | Type | CT-I02, CT-I03 | P-C | L3 |
| CT-I05 | Identifier | CT-C05 | P-C | L3 |
| CT-I06 | Constant | CT-I02, CT-I04 | P-C | L2 |
| CT-I07 | Expression | CT-I02, CT-I04, CT-I05 | P-C | L3 |
| CT-I08 | Operator | CT-I07 | P-C | L3 |
| CT-I09 | Evaluation | CT-I07, CT-I08 | P-C | L3 |
| CT-I10 | Conversion | CT-I03, CT-I04, CT-I09 | P-F | L2 |
| CT-I11 | Collection | CT-I01, CT-I04 | F-C | L3 |

## State

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-S01 | State | CT-C09, CT-I02 | P-C | L3 |
| CT-S02 | State Change | CT-S01, CT-I09 | P-C | L3 |
| CT-S03 | Variable | CT-I04, CT-I05, CT-S01 | P-C | L3 |
| CT-S04 | Declaration | CT-I04, CT-I05 | P-C | L3 |
| CT-S05 | Definition | CT-S04 | P-F | L2 |
| CT-S06 | Initialization | CT-S03, CT-S04 | P-C | L3 |
| CT-S07 | Assignment | CT-S02, CT-S03, CT-I07 | P-C | L3 |
| CT-S08 | Update | CT-S07 | P-C | L3 |
| CT-S09 | Scope | CT-I05, CT-S04 | F-C | L3 |
| CT-S10 | Lifetime | CT-S03, CT-M04 | F-C | L3 |
| CT-S11 | Invariant | CT-S01, CT-F05 | F-C | L2 |

## Control Flow

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-F01 | Sequence | CT-C09 | P-C | L3 |
| CT-F02 | Condition | CT-I07, CT-I09 | P-C | L3 |
| CT-F03 | Decision | CT-F02 | P-C | L3 |
| CT-F04 | Branch | CT-F03 | P-F | L2 |
| CT-F05 | Repetition | CT-F02, CT-S02 | P-C | L3 |
| CT-F06 | Iteration | CT-F05, CT-S08 | P-C | L3 |
| CT-F07 | Loop Condition | CT-F02, CT-F05 | P-C | L3 |
| CT-F08 | Boundary | CT-I08, CT-F02 | P-C | L3 |
| CT-F09 | Sentinel | CT-F02, CT-X01 | P-C | L3 |
| CT-F10 | Nested Control | CT-F03, CT-F05 | P-F | L2 |
| CT-F11 | Infinite Execution | CT-F05, CT-F07, CT-S08 | P-C | L3 |

## Abstraction

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-A01 | Decomposition | CT-C01, CT-C03 | P-C | L3 |
| CT-A02 | Responsibility | CT-A01 | P-C | L3 |
| CT-A03 | Function | CT-A01, CT-A02, CT-F01 | P-C | L3 |
| CT-A04 | Interface | CT-A02, CT-A03 | P-F | L2 |
| CT-A05 | Implementation | CT-A03, CT-A04 | P-F | L2 |
| CT-A06 | Parameter | CT-A03, CT-I04, CT-S04 | P-C | L3 |
| CT-A07 | Argument | CT-A03, CT-I07 | P-C | L3 |
| CT-A08 | Return Value | CT-A03, CT-I02 | P-C | L3 |
| CT-A09 | Call | CT-A03, CT-F01 | P-C | L3 |
| CT-A10 | Call Stack | CT-A09, CT-M11 | F-C | L2 |
| CT-A11 | Recursion | CT-A03, CT-A09, CT-F02 | F-A | L3 |
| CT-A12 | Module | CT-A04, CT-A05 | F-C | L3 |

## Memory

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-M01 | Bit | CT-I03 | F-C | L2 |
| CT-M02 | Byte | CT-M01 | F-C | L2 |
| CT-M03 | Address | CT-M02 | F-C | L3 |
| CT-M04 | Object | CT-I02, CT-I04, CT-M02 | P-F | L2 |
| CT-M05 | Layout | CT-M03, CT-M04 | F-C | L3 |
| CT-M06 | Pointer | CT-M03, CT-M04, CT-I04 | F-C | L3 |
| CT-M07 | Indirection | CT-M06 | F-C | L3 |
| CT-M08 | Aliasing | CT-M06, CT-M07 | F-C | L2 |
| CT-M09 | Null Reference | CT-M06 | F-C | L3 |
| CT-M10 | Storage Duration | CT-M04, CT-S10 | F-C | L3 |
| CT-M11 | Stack Storage | CT-M10, CT-A09 | F-C | L2 |
| CT-M12 | Static Storage | CT-M10 | F-C | L2 |
| CT-M13 | Dynamic Allocation | CT-M03, CT-M04, CT-M06 | F-C | L3 |
| CT-M14 | Ownership | CT-M13 | F-C | L3 |
| CT-M15 | Memory Safety | CT-M05, CT-M06, CT-M10, CT-M13 | F-C | L4 |

## Interaction

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-X01 | Input | CT-I01, CT-C09 | P-C | L3 |
| CT-X02 | Output | CT-I01, CT-C09 | P-C | L3 |
| CT-X03 | Stream | CT-X01, CT-X02 | P-F | L2 |
| CT-X04 | Format | CT-I03, CT-X01, CT-X02 | P-C | L3 |
| CT-X05 | Buffer | CT-M04, CT-X03 | F-C | L2 |
| CT-X06 | File | CT-X03 | F-C | L3 |
| CT-X07 | End of Input | CT-X01, CT-X03 | P-F | L2 |
| CT-X08 | Error Channel | CT-X02, CT-X03 | P-F | L1 |
| CT-X09 | Command Line | CT-C09, CT-X01 | F-C | L2 |
| CT-X10 | Protocol | CT-C02, CT-X01, CT-X02 | F-C | L2 |

## Engineering

| ID | Concept | Primary dependencies | Scope | Target maturity |
|---|---|---|---|---|
| CT-E01 | Expected Result | CT-C02, CT-I02 | P-C | L4 |
| CT-E02 | Test Case | CT-E01, CT-X01, CT-X02 | P-C | L4 |
| CT-E03 | Testing | CT-E02, CT-C09 | P-C | L4 |
| CT-E04 | Verification | CT-E01, CT-E03 | P-C | L4 |
| CT-E05 | Validation | CT-C01, CT-C02, CT-E04 | P-F | L2 |
| CT-E06 | Debugging | CT-E03, CT-E04 | P-C | L4 |
| CT-E07 | Symptom | CT-E06 | P-C | L3 |
| CT-E08 | Cause | CT-E06, CT-E07 | P-C | L3 |
| CT-E09 | Hypothesis | CT-E07, CT-E08 | P-C | L3 |
| CT-E10 | Regression Testing | CT-E03, CT-E06 | P-C | L3 |
| CT-E11 | Code Reading | CT-C05, CT-I07, CT-F01 | P-C | L3 |
| CT-E12 | Trace | CT-S01, CT-F01, CT-E11 | P-C | L4 |
| CT-E13 | Refactoring | CT-E03, CT-E04, CT-A01 | F-C | L3 |
| CT-E14 | Documentation | CT-C02, CT-A04 | P-F | L2 |
| CT-E15 | Version Control | CT-C05, CT-E14 | F-C | L2 |
| CT-E16 | AI-Assisted Programming | CT-E01, CT-E03, CT-E04, CT-E09 | P-C | L4 |
| CT-E17 | Evidence | CT-E01, CT-E04 | P-C | L4 |
| CT-E18 | Judgment | CT-E04, CT-E05, CT-E17 | P-C | L4 |

## Composite Concepts

| ID | Composite Concept | Component concepts | Scope | Description |
|---|---|---|---|---|
| CT-K01 | Array | CT-I11, CT-M04, CT-M05, CT-F08, CT-F06, CT-M15 | F-C | A fixed-size, same-type collection arranged contiguously. |
| CT-K02 | String | CT-I11, CT-I03, CT-K01, CT-F08, CT-X04 | F-C | A concept formed by character collections, termination rules, and text formatting. |
| CT-K03 | Structure | CT-I11, CT-I04, CT-M04, CT-M05 | F-C | A single data object composed of members of different types. |
| CT-K04 | File I/O | CT-X03, CT-X06, CT-X07, CT-X10, CT-E03 | F-C | Reading, writing, formatting, and error handling for persistent data. |
| CT-K05 | Modular Programming | CT-A01, CT-A02, CT-A04, CT-A05, CT-A12, CT-C06 | F-C | Organizing larger programs through interfaces, implementations, and separate compilation. |

## First Dependency Chains

### How a program begins to run

```text
CT-C01 Problem
→ CT-C02 Requirement
→ CT-C03 Algorithm
→ CT-C04 Program
→ CT-C05 Source Code
→ CT-C06 Translation
→ CT-C07 Compiler
→ CT-C08 Executable
→ CT-C09 Execution
→ CT-X02 Output
```

### Data and state

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-S03 Variable
→ CT-S06 Initialization
→ CT-S07 Assignment
→ CT-S02 State Change
→ CT-E12 Trace
```

### Decision and repetition

```text
CT-I07 Expression
→ CT-I08 Operator
→ CT-F02 Condition
→ CT-F03 Decision
→ CT-F05 Repetition
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Infinite Execution
```

### Functions and decomposition

```text
CT-C01 Problem
→ CT-A01 Decomposition
→ CT-A02 Responsibility
→ CT-A03 Function
→ CT-A06 Parameter
→ CT-A07 Argument
→ CT-A08 Return Value
→ CT-A09 Call
```

## Unit Composition Principles

A Unit should satisfy the following conditions:

1. It is driven by one understandable core question.
2. It contains one primary dependency chain rather than merely a syntax list.
3. The number of new concepts is controlled, and necessary prerequisites already exist or are explicitly supplied at the beginning.
4. It contains at least one Engineering concept such as prediction, tracing, testing, debugging, or verification.
5. C syntax serves as the concrete mapping of concepts and must not be the Unit’s only organizing principle.
6. A Unit may reuse learned concepts, but it must clearly identify what is newly introduced, deepened, and integrated.

## Questions to Confirm

- Should `Requirement` remain under Computation, or move to Engineering?
- Should `Variable` remain under State, using Information and Memory as dependencies?
- Do `Declaration` and `Definition` need to be taught separately in the preparatory course?
- How deeply should `Process`, `Error Channel`, and `Storage Duration` be treated in the preparatory course?
- Should `Ownership` remain as a cross-language concept even though C has no language-level ownership system?

## Navigation

- [Programming Concept Tree](14-programming-concept-tree.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](15-programming-concept-registry.zh-TW.md)
