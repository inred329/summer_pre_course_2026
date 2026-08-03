# Instructional Design Workspace

Version: 0.2.0  
Status: In planning  
Corresponding Chinese version: [教學內容設計區](README.zh-TW.md)

## Document Purpose

This directory is used to design the 2026 Summer C Programming Preparatory Course and the subsequent 16-week formal course using a requirements-engineering approach similar to software project design.

The course is not designed by starting with weekly schedules, slides, or textbook chapters. Instead, the design process defines the following in order:

1. The educational vision and problem to solve.
2. Stakeholders and their needs.
3. The complete programming-language knowledge space and concept dependencies.
4. The capabilities students should possess at course completion.
5. Observable and assessable evidence of learning.
6. Scope boundaries between the preparatory and formal courses.
7. Delivery pacing for the Chinese-taught and English-taught classes.
8. Materials, activities, assignments, and assessments.

## Constitutional Compliance

Before drafting, revising, or translating any official document in this directory, the following must be reviewed:

- [Course Constitution (Traditional Chinese)](../CONSTITUTION.zh-TW.md)
- [Course Constitution (English)](../CONSTITUTION.en.md)

Every document must satisfy at least the following principles:

- Promote genuine student understanding rather than mere output completion.
- Create Chinese and English versions as synchronized, substantively equivalent pairs.
- Give every capability clear prerequisites and acceptance criteria.
- Control cognitive load for beginners.
- Treat reading, modification, testing, debugging, and explanation as equally important as writing from scratch.
- Provide appropriate visuals for concepts and relationships that benefit from visualization.
- Use AI only to support learning, never to replace core responsibility for thinking.
- Ensure that the preparatory and formal courses form a continuous progression rather than duplicate each other.
- Make every official document reachable from the root README through a direct or indirect navigation path.

## Official Design Documents

| Stage | Document | Purpose |
|---|---|---|
| 01 | [Course Product Vision](01-product-vision.en.md) | Defines the educational problem, product positioning, success conditions, and relationship between the preparatory and formal courses. |
| 02 | [Instructional Requirements Map](02-requirements-map.en.md) | Defines educational, capability, cross-cutting, and acceptance-oriented requirements. |
| 03 | [Programming Language Knowledge Graph](03-programming-language-knowledge-graph.en.md) | Defines the relationships among translation and execution, data, control, functions, memory, data organization, verification, and AI. |

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
├── 03-programming-language-knowledge-graph.zh-TW.md
└── 03-programming-language-knowledge-graph.en.md
```

Planned additions:

```text
04-competency-map.*
05-scope-boundary.*
06-acceptance-model.*
07-delivery-map.*
08-risk-register.*
09-traceability-matrix.*
```

## Project Analogy

| Software Project | Course Design |
|---|---|
| Product vision | Educational vision |
| User needs | Student and instructor needs |
| Functional requirements | Learning outcomes and capability requirements |
| Non-functional requirements | Fairness, bilingual quality, maintainability, and cognitive load |
| Domain model | Programming-language knowledge graph and language logic |
| Architecture and dependencies | Competency map and prerequisites |
| MVP | Minimum viable preparation provided by the preparatory course |
| Production release | The 16-week formal C programming course |
| Acceptance criteria | Observable evidence of learning |
| Test cases | Exercises, oral explanations, modification tasks, and assessments |
| Defects | Misconceptions and learning breakdowns |
| Traceability matrix | Alignment among goals, knowledge, capabilities, materials, and assessments |

## Working Sequence

1. Establish the product vision and definition of success.
2. Build the requirements map.
3. Build the programming language knowledge graph.
4. Transform knowledge nodes into an observable and assessable competency map.
5. Define the final capabilities delivered by the formal course.
6. Work backward to identify the MVP scope of the preparatory course.
7. Assemble shared capabilities into different delivery schedules for the Chinese-taught and English-taught classes.
8. Create lesson plans and teaching materials only after the above steps are complete.

## Current Core Assumptions

- C is the instructional language, while programming capability and the logic of C are the core educational goals.
- Each concept should be developed through Need → Design Purpose → Language Logic → Syntax → Implementation → Verification.
- Programming is organized around data and state, flow and control, and functions and abstraction.
- Program translation and execution, the memory model, data organization, testing and debugging, and AI literacy are necessary knowledge dimensions.
- The English preparatory class has five 2-hour sessions, totaling 10 hours.
- The Chinese preparatory class has four 3-hour sessions, totaling 12 hours.
- The formal course has 16 weeks of 3-hour sessions, totaling 48 hours.
- Both preparatory classes must share the same core learning outcomes; the additional two hours must not create a difference in core capability expectations.

## Navigation

- [Back to repository home](../README.md)
- [繁體中文版](README.zh-TW.md)
