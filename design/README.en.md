# Instructional Design Workspace

Version: 0.1.0  
Status: In planning  
Corresponding Chinese version: `README.zh-TW.md`

## Document Purpose

This directory is used to design the 2026 Summer C Programming Preparatory Course and the subsequent 16-week formal course using a requirements-engineering approach similar to software project design.

The course is not designed by starting with weekly schedules, slides, or textbook chapters. Instead, the design process defines the following in order:

1. The educational vision and problem to solve.
2. Stakeholders and their needs.
3. The capabilities students should possess at course completion.
4. Dependencies among those capabilities.
5. Observable and assessable evidence of learning.
6. Scope boundaries between the preparatory and formal courses.
7. Delivery pacing for the Chinese-taught and English-taught classes.
8. Materials, activities, assignments, and assessments.

## Constitutional Compliance

Before drafting, revising, or translating any official document in this directory, the following must be reviewed:

- `../CONSTITUTION.zh-TW.md`
- `../CONSTITUTION.en.md`

Every document must satisfy at least the following principles:

- Promote genuine student understanding rather than mere output completion.
- Create Chinese and English versions as synchronized, substantively equivalent pairs.
- Give every capability clear prerequisites and acceptance criteria.
- Control cognitive load for beginners.
- Treat reading, modification, testing, debugging, and explanation as equally important as writing from scratch.
- Use AI only to support learning, never to replace core responsibility for thinking.
- Ensure that the preparatory and formal courses form a continuous progression rather than duplicate each other.

## Design Document Structure

```text
design/
├── README.zh-TW.md
├── README.en.md
├── 01-product-vision.zh-TW.md
├── 01-product-vision.en.md
├── 02-requirements-map.zh-TW.md
└── 02-requirements-map.en.md
```

Planned additions:

```text
03-competency-map.*
04-scope-boundary.*
05-acceptance-model.*
06-delivery-map.*
07-risk-register.*
08-traceability-matrix.*
```

## Project Analogy

| Software Project | Course Design |
|---|---|
| Product vision | Educational vision |
| User needs | Student and instructor needs |
| Functional requirements | Learning outcomes and capability requirements |
| Non-functional requirements | Fairness, bilingual quality, maintainability, and cognitive load |
| Architecture and dependencies | Competency map and prerequisites |
| MVP | Minimum viable preparation provided by the preparatory course |
| Production release | The 16-week formal C programming course |
| Acceptance criteria | Observable evidence of learning |
| Test cases | Exercises, oral explanations, modification tasks, and assessments |
| Defects | Misconceptions and learning breakdowns |
| Traceability matrix | Alignment among goals, capabilities, materials, and assessments |

## Working Sequence

1. Establish the product vision and definition of success.
2. Build the requirements map.
3. Build the complete C programming competency map.
4. Define the final capabilities delivered by the formal course.
5. Work backward to identify the MVP scope of the preparatory course.
6. Assemble shared capabilities into different delivery schedules for the Chinese-taught and English-taught classes.
7. Create lesson plans and teaching materials only after the above steps are complete.

## Current Core Assumptions

- C is the instructional language, while programming capability is the core educational goal.
- Programming may initially be organized around three core pillars: data and variables, control flow, and functions and decomposition.
- The execution model, input/output, testing, debugging, and AI literacy are cross-cutting capabilities.
- The English preparatory class has five 2-hour sessions, totaling 10 hours.
- The Chinese preparatory class has four 3-hour sessions, totaling 12 hours.
- The formal course has 16 weeks of 3-hour sessions, totaling 48 hours.
- Both preparatory classes must share the same core learning outcomes; the additional two hours must not create a difference in core capability expectations.
