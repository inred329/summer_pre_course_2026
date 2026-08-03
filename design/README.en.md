# Instructional Design Workspace

Version: 0.7.0  
Status: In planning  
Corresponding Chinese version: [教學內容設計區](README.zh-TW.md)

## Document Purpose

This directory designs the 2026 Summer C Programming Preparatory Course and the connected 16-week formal course through a requirements-engineering and system-design approach.

The design sequence is:

1. Educational vision and problem.
2. Stakeholders and requirements.
3. Core concepts and relationships in the programming domain.
4. Knowledge dependencies needed to understand those concepts.
5. Student capabilities and maturity levels.
6. Scope boundaries between preparatory and formal courses.
7. Observable and assessable evidence.
8. Delivery pacing for both preparatory tracks and the formal course.
9. Risks, traceability, and later teaching-material design.

## Constitutional Compliance

Before drafting, revising, or translating any official document in this directory, review:

- [Course Constitution (Traditional Chinese)](../CONSTITUTION.zh-TW.md)
- [Course Constitution (English)](../CONSTITUTION.en.md)

Every document must at least:

- Promote genuine understanding rather than output completion.
- Be created as a synchronized, substantively equivalent bilingual pair.
- Give capabilities prerequisites and acceptance methods.
- Control cognitive load for beginners.
- Treat reading, modification, testing, debugging, explanation, and writing from scratch as equally important.
- Provide visuals for concepts and relationships that benefit from visualization.
- Use AI to support learning rather than replace core thinking.
- Make preparatory and formal courses a continuous capability progression.
- Be reachable from the root README through direct or indirect navigation.

## Official Design Documents

| Stage | Document | Purpose |
|---|---|---|
| 01 | [Course Product Vision](01-product-vision.en.md) | Defines the educational problem, product position, and success conditions. |
| 02 | [Instructional Requirements Map](02-requirements-map.en.md) | Defines educational, capability, and cross-cutting requirements. |
| 03 | [Programming Domain Model](03-programming-domain-model.en.md) | Defines the concepts that exist in the programming domain and their relationships. |
| 04 | [Programming Language Knowledge Dependency Graph](04-programming-language-knowledge-graph.en.md) | Defines major prerequisite knowledge and dependencies for understanding core concepts. |
| 05 | [Programming Competency Map](05-competency-map.en.md) | Converts concepts and dependencies into observable capabilities, maturity levels, and evidence. |
| 06 | [Course Scope Boundary](06-scope-boundary.en.md) | Defines core delivery, foundations, deferrals, and exclusions for preparatory and formal courses. |
| 07 | [Competency Acceptance Model](07-acceptance-model.en.md) | Defines minimum maturity evidence, standard acceptance tasks, AI boundaries, and passing criteria. |
| 08 | [Course Delivery Map](08-delivery-map.en.md) | Arranges shared capabilities, maturity targets, and evidence across both preparatory tracks and the 16-week formal course. |

Chinese navigation: [教學內容設計區](README.zh-TW.md)

## Design Document Structure

```text
design/
├── README.zh-TW.md
├── README.en.md
├── 01-product-vision.zh-TW.md
├── 01-product-vision.en.md
├── 02-requirements-map.zh-TW.md
├── 02-requirements-map.en.md
├── 03-programming-domain-model.zh-TW.md
├── 03-programming-domain-model.en.md
├── 04-programming-language-knowledge-graph.zh-TW.md
├── 04-programming-language-knowledge-graph.en.md
├── 05-competency-map.zh-TW.md
├── 05-competency-map.en.md
├── 06-scope-boundary.zh-TW.md
├── 06-scope-boundary.en.md
├── 07-acceptance-model.zh-TW.md
├── 07-acceptance-model.en.md
├── 08-delivery-map.zh-TW.md
└── 08-delivery-map.en.md
```

Planned additions:

```text
09-risk-register.*
10-traceability-matrix.*
```

## Division of the Three Core Models

| Document | Question answered |
|---|---|
| Domain model | What concepts exist in programming, and how are they related? |
| Knowledge dependency graph | What usually must be understood before another concept? |
| Competency map | What must students be able to do, and to what maturity? |

These must not be conflated: a domain relationship is not a learning sequence, a knowledge dependency is not a weekly schedule, and capability maturity is not the same as a topic having been introduced.

## Current Core Assumptions

- C is the instructional language, while programming capability and the logic of C are the core goals.
- Each concept develops through Need → Design Purpose → Language Logic → Syntax → Implementation → Verification.
- Data and state, flow and control, and functions and abstraction are foundational pillars.
- The toolchain, memory model, data organization, testing and debugging, and AI literacy are necessary dimensions.
- Data organization currently remains at the abstraction level of sequences, records, indexing, and operations; advanced data structures are not presumed to be course core content.
- Competency maturity is recognize, explain, trace, implement, diagnose, and transfer.
- Scope states are core delivery, foundation only, deepen later, implement later, and out of scope.
- Core capability acceptance requires at least one understanding-oriented and one action-oriented form of evidence.
- The English preparatory class totals 10 hours; the Chinese preparatory class totals 12 hours; the formal course totals 48 hours.
- Both preparatory tracks share the same core outcomes and acceptance standards.
- The Chinese-taught track's additional two hours support more tracing, remediation, diagnosis, and acceptance rather than a higher core standard.

## Next Step

Create `09-risk-register` to identify risks in pacing, cognitive load, bilingual equivalence, AI dependency, acceptance execution, and document maintenance.

## Navigation

- [Back to repository home](../README.md)
- [繁體中文版](README.zh-TW.md)
