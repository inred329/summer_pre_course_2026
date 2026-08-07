# Programming Concept Registry

Version: 0.1.1  
Status: Active design standard  
Governance note: This standard assigns stable Concept IDs and dependency/scope metadata. Competency maturity is defined by `05-competency-map.*` and `06-scope-boundary.*`; this registry does not redefine L1–L6 or create assessment/tool policy.  
Corresponding Chinese version: [程式設計 Concept Registry](15-programming-concept-registry.zh-TW.md)

## Document Purpose

The Concept Tree answers “Which concepts exist?” This Registry gives those concepts stable identifiers, major prerequisite relationships, and a coarse course-placement marker so Units and materials can refer to them consistently.

Concept IDs should be preserved across ordinary wording refinements. If a concept is intentionally renamed or split, dependent Units/materials and the active traceability/audit records must be updated in the same change set.

## ID Prefixes

| Domain | Prefix |
|---|---|
| Computation | `CT-C` |
| Information | `CT-I` |
| State | `CT-S` |
| Control Flow | `CT-F` |
| Abstraction | `CT-A` |
| Memory and Lifetime | `CT-M` |
| Interaction | `CT-X` |
| Engineering and Verification | `CT-E` |
| Composite Concept | `CT-K` |

## Course-Placement Markers

These are registry routing markers, not maturity definitions:

- `P-C`: preparatory core concept.
- `P-F`: preparatory foundation; may be deepened/implemented later.
- `F-C`: formal-course core concept.
- `F-A`: formal-course advanced/deferred concept; inclusion still requires scope justification.
- `X`: conditional/optional concept; applies only when the corresponding optional activity/tool is actually used.

For actual maturity meanings use the standard `L0–L6` model in `05-competency-map.*` / `11-terminology-glossary.*`. For core/optional decisions use `06-scope-boundary.*`.

---

## Computation

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-C01 | Problem | — | P-C |
| CT-C02 | Requirement | CT-C01 | P-C |
| CT-C03 | Algorithm / Design Procedure | CT-C01, CT-C02 | P-C |
| CT-C04 | Program | CT-C03 | P-C |
| CT-C05 | Source Code | CT-C04 | P-C |
| CT-C06 | C Translation | CT-C05 | P-C |
| CT-C07 | C Implementation / Compiler Tool | CT-C06 | P-C |
| CT-C08 | Executable / Loadable Program Representation | CT-C06, CT-C07 | P-C |
| CT-C09 | Execution | CT-C08 | P-C |
| CT-C10 | Process / Runtime Instance | CT-C09 | P-F |
| CT-C11 | Termination | CT-C09 | P-C |
| CT-C12 | Diagnostic | CT-C06 | P-C |

`CT-C06–C08` describe conceptual responsibilities. A standalone preprocessor, assembler, linker, object file, or OS executable format is not implied unless the target toolchain actually exposes it.

---

## Information

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-I01 | Data | CT-C04 | P-C |
| CT-I02 | Value | CT-I01 | P-C |
| CT-I03 | Representation | CT-I01, CT-I02 | P-F |
| CT-I04 | Type | CT-I02, CT-I03 | P-C |
| CT-I05 | Identifier | CT-C05 | P-C |
| CT-I06 | Literal / Constant Form | CT-I02, CT-I04 | P-C |
| CT-I07 | Expression | CT-I02, CT-I04, CT-I05 | P-C |
| CT-I08 | Operator | CT-I07 | P-C |
| CT-I09 | Evaluation | CT-I07, CT-I08 | P-C |
| CT-I10 | Conversion | CT-I03, CT-I04, CT-I09 | P-F |
| CT-I11 | Collection | CT-I01, CT-I04 | F-C |

---

## State

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-S01 | State | CT-C09, CT-I02 | P-C |
| CT-S02 | State Change | CT-S01, CT-I09 | P-C |
| CT-S03 | Variable / Named Object | CT-I04, CT-I05, CT-S01 | P-C |
| CT-S04 | Declaration | CT-I04, CT-I05 | P-C |
| CT-S05 | Definition | CT-S04 | P-F |
| CT-S06 | Initialization | CT-S03, CT-S04 | P-C |
| CT-S07 | Assignment | CT-S02, CT-S03, CT-I07 | P-C |
| CT-S08 | Update | CT-S07 | P-C |
| CT-S09 | Scope | CT-I05, CT-S04 | F-C |
| CT-S10 | Lifetime | CT-S03, CT-M04 | F-C |
| CT-S11 | Invariant | CT-S01, CT-F05 | F-C |

---

## Control Flow

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-F01 | Sequence | CT-C09 | P-C |
| CT-F02 | Condition | CT-I07, CT-I09 | P-C |
| CT-F03 | Selection / Decision | CT-F02 | P-C |
| CT-F04 | Branch / Transfer | CT-F03 | P-F |
| CT-F05 | Repetition | CT-F02, CT-S02 | P-C |
| CT-F06 | Iteration | CT-F05, CT-S08 | P-C |
| CT-F07 | Loop Condition | CT-F02, CT-F05 | P-C |
| CT-F08 | Boundary | CT-I08, CT-F02 | P-C |
| CT-F09 | Sentinel / End Condition | CT-F02, CT-X01 | P-C |
| CT-F10 | Nested Control | CT-F03, CT-F05 | P-F |
| CT-F11 | Nontermination | CT-F05, CT-F07, CT-S08 | P-C |

---

## Abstraction

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-A01 | Decomposition | CT-C01, CT-C03 | P-C |
| CT-A02 | Responsibility | CT-A01 | P-C |
| CT-A03 | Function | CT-A01, CT-A02, CT-F01 | P-C |
| CT-A04 | Interface | CT-A02, CT-A03 | P-F |
| CT-A05 | Implementation | CT-A03, CT-A04 | P-F |
| CT-A06 | Parameter | CT-A03, CT-I04, CT-S04 | P-C |
| CT-A07 | Argument | CT-A03, CT-I07 | P-C |
| CT-A08 | Return Value | CT-A03, CT-I02 | P-C |
| CT-A09 | Call | CT-A03, CT-F01 | P-C |
| CT-A10 | Activation Model | CT-A09, CT-M04, CT-S10 | F-C |
| CT-A11 | Recursion | CT-A03, CT-A09, CT-F02, CT-C11 | F-A |
| CT-A12 | Module | CT-A04, CT-A05 | F-C |

`CT-A10` may be visualized with a call stack for a target implementation, but the physical stack representation is not a C-language guarantee.

---

## Memory and Lifetime

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-M01 | Bit | CT-I03 | F-C |
| CT-M02 | Byte | CT-M01 | F-C |
| CT-M03 | Address | CT-M02, CT-M04 | F-C |
| CT-M04 | Object / Storage | CT-I02, CT-I04 | P-F |
| CT-M05 | Layout | CT-M03, CT-M04 | F-C |
| CT-M06 | Pointer | CT-M03, CT-I04 | F-C |
| CT-M07 | Indirection / Dereference | CT-M06 | F-C |
| CT-M08 | Aliasing | CT-M06, CT-M07 | F-C |
| CT-M09 | Null Pointer | CT-M06 | F-C |
| CT-M10 | Storage Duration | CT-M04 | F-C |
| CT-M11 | Automatic Storage / Call-Lifetime Model | CT-M10, CT-A09 | F-C |
| CT-M12 | Static Storage | CT-M10 | F-C |
| CT-M13 | Allocated Storage / Dynamic Allocation | CT-M03, CT-M04, CT-M06 | F-C |
| CT-M14 | Ownership / Release Responsibility | CT-M13, CT-S10 | F-C |
| CT-M15 | Memory Safety | CT-M05, CT-M06, CT-M10, CT-M13 | F-C |

“Heap” and physical “stack” are implementation/teaching terms, not required C abstract-machine regions. Materials should use `allocated storage` and `automatic storage duration` when language-level precision matters.

---

## Interaction

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-X01 | Input | CT-I01, CT-C09 | P-C |
| CT-X02 | Output | CT-I01, CT-C09 | P-C |
| CT-X03 | Stream | CT-X01, CT-X02 | P-F |
| CT-X04 | Format | CT-I03, CT-X01, CT-X02 | P-C |
| CT-X05 | Buffer | CT-M04, CT-X03 | F-C |
| CT-X06 | File | CT-X03 | F-C |
| CT-X07 | End of Input | CT-X01, CT-X03 | P-F |
| CT-X08 | Error Channel / Error State | CT-X02, CT-X03 | P-F |
| CT-X09 | Command-Line Input | CT-C09, CT-X01 | F-C |
| CT-X10 | Protocol | CT-C02, CT-X01, CT-X02 | F-C |

---

## Engineering and Verification

| ID | Concept | Primary dependencies | Placement |
|---|---|---|---|
| CT-E01 | Expected Result / Property | CT-C02, CT-I02 | P-C |
| CT-E02 | Test Case | CT-E01, CT-X01, CT-X02 | P-C |
| CT-E03 | Testing | CT-E02, CT-C09 | P-C |
| CT-E04 | Verification | CT-E01, CT-E03 | P-C |
| CT-E05 | Validation | CT-C01, CT-C02, CT-E04 | P-F |
| CT-E06 | Debugging | CT-E03, CT-E04 | P-C |
| CT-E07 | Symptom | CT-E06 | P-C |
| CT-E08 | Cause | CT-E06, CT-E07 | P-C |
| CT-E09 | Hypothesis | CT-E07, CT-E08 | P-C |
| CT-E10 | Regression Verification | CT-E03, CT-E06 | P-C |
| CT-E11 | Code Reading | CT-C05, CT-I07, CT-F01 | P-C |
| CT-E12 | Trace | CT-S01, CT-F01, CT-E11 | P-C |
| CT-E13 | Refactoring | CT-E03, CT-E04, CT-A01 | F-C |
| CT-E14 | Documentation | CT-C02, CT-A04 | P-F |
| CT-E15 | Version Control | CT-C05, CT-E14 | F-C |
| CT-E16 | External Assistance | CT-E01, CT-E04, CT-E09 | X |
| CT-E17 | Evidence | CT-E01, CT-E04 | P-C |
| CT-E18 | Judgment | CT-E04, CT-E05, CT-E17 | P-C |
| CT-E19 | Human Review of External Suggestions | CT-E16, CT-E18 | X |
| CT-E20 | Contextual Disclosure | CT-E16, CT-E17 | X |

`CT-E16`, `CT-E19`, and `CT-E20` are conditional. They do not imply AI use, fixed prompts, logs, before/after artifacts, or non-use declarations. When optional assistance is actually adopted, core verification/evidence concepts remain applicable.

---

## Composite Concepts

| ID | Composite Concept | Component concepts | Placement | Description |
|---|---|---|---|---|
| CT-K01 | Array | CT-I11, CT-M04, CT-M05, CT-F08, CT-F06, CT-M15 | F-C | Same-element-type array with explicit index/bounds/lifetime reasoning. |
| CT-K02 | String | CT-I11, CT-I03, CT-K01, CT-F08, CT-X04, CT-X05 | F-C | Null-terminated character-sequence concept plus capacity/format boundaries. |
| CT-K03 | Structure / Record | CT-I11, CT-I04, CT-M04, CT-M05 | F-C | Related fields grouped in one structure object/type. |
| CT-K04 | File I/O | CT-X03, CT-X06, CT-X07, CT-X10, CT-E03 | F-C | Persistent/external data interaction with stream state, format, errors, and resource lifetime. |
| CT-K05 | Modular Programming | CT-A01, CT-A02, CT-A04, CT-A05, CT-A12, CT-C06 | F-C | Interface/implementation organization across translation/build boundaries. |

---

## Representative Dependency Chains

### Program to observable evidence

```text
CT-C01 Problem
→ CT-C02 Requirement
→ CT-C03 Algorithm / Design
→ CT-C04 Program
→ CT-C05 Source Code
→ CT-C06 C Translation
→ CT-C08 Executable / Loadable Representation
→ CT-C09 Execution
→ CT-E01 Expected Result / Property
→ CT-E04 Verification
```

### Data and state

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-S03 Variable / Named Object
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
→ CT-F03 Selection
→ CT-F05 Repetition
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Nontermination
```

### Functions and decomposition

```text
CT-C01 Problem
→ CT-A01 Decomposition
→ CT-A02 Responsibility
→ CT-A03 Function
→ CT-A04 Interface
→ CT-A06 Parameter
→ CT-A07 Argument
→ CT-A08 Return Value
→ CT-A09 Call
```

### Conditional external assistance

```text
Relevant Core Understanding
→ CT-E16 External Assistance (optional)
→ CT-E19 Human Review
→ CT-E04 Verification
→ CT-E18 Judgment
→ CT-E20 Contextual Disclosure only when specifically required
```

The conditional chain is never a prerequisite for students who do not use external assistance.

---

## Unit Composition Rules

A Unit should:

1. Be driven by a student-understandable core question.
2. Use one coherent primary dependency chain rather than a syntax list.
3. Control the number of newly introduced concepts and provide prerequisites where needed.
4. Include at least one Engineering concept such as expected-result reasoning, tracing, testing, debugging, or verification.
5. Treat C syntax as a concrete mapping rather than the only organizing principle.
6. Identify what is introduced, deepened, and reused.
7. Keep `X` concepts optional/conditional and outside the core completion chain unless an approved activity explicitly targets them.

## Maintenance Rules

- Preserve stable IDs unless a documented migration is necessary.
- Keep both language versions substantively equivalent.
- Do not redefine maturity levels locally.
- Check `05`, `06`, `11`, `14`, `16`, and dependent materials when an ID meaning changes.
- Record material changes in the active repository audit.

## Related Documents

- [Programming Concept Tree](14-programming-concept-tree.en.md)
- [Programming Competency Map](05-competency-map.en.md)
- [Course Scope Boundary](06-scope-boundary.en.md)
- [Terminology Glossary](11-terminology-glossary.en.md)
- [Concept-Driven Unit Map](16-unit-map.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](15-programming-concept-registry.zh-TW.md)
