# Instructional Requirements Map

Version: 0.1.1  
Status: Revisable planning and traceability model  
Corresponding Chinese version: `02-requirements-map.zh-TW.md`

## Document Purpose

This document uses a requirements-engineering approach to decompose the course vision into educational requirements, stakeholder needs, core capability requirements, quality requirements, and assessable acceptance conditions.

It is not a lesson schedule, a table of C-language chapters, or a governing policy source. Later competency maps, scope boundaries, delivery plans, materials, and assessments may trace to and refine requirements in this document, but the Constitution and official assessment policy take precedence whenever a conflict exists.

## 1. Requirements Levels

```text
Educational vision
└── Stakeholder needs
    ├── Core capability requirements
    ├── Cross-cutting learning capability requirements
    ├── Instructional delivery requirements
    └── Quality and governance requirements
        └── Observable acceptance evidence
```

## 2. Stakeholders

| ID | Stakeholder | Primary Need |
|---|---|---|
| ST-01 | Beginning student | Begin learning programming with a manageable cognitive load |
| ST-02 | Student in the Chinese-taught class | Receive complete and equivalent core learning content in Chinese |
| ST-03 | Student in the English-taught class | Receive complete and equivalent core learning content in English |
| ST-04 | Instructor | See capability dependencies, learning evidence, and acceptable adaptation space |
| ST-05 | Teaching assistant | Support practice, diagnosis, and feedback from official documentation |
| ST-06 | Material maintainer | Trace relationships among language versions, requirements, materials, and assessments |
| ST-07 | Instructor of a later course | Reasonably rely on clearly defined and assessed foundational capabilities |

## 3. Highest-Level Educational Requirements

### EDU-01 — Build a Transferable Mental Model of Programming

Students should understand that a program is not a collection of isolated syntax. It is an executable model that expresses a solution through data, control flow, and functions.

Acceptance direction: Students can use their own words and a simple diagram to explain how data enters a program, how it is processed, how it affects control flow, and how output is produced.

### EDU-02 — Build Genuine Problem-Solving Capability

Students should identify inputs, outputs, rules, and constraints in a problem statement and decompose the problem into implementable and verifiable steps.

Acceptance direction: Students can express a solution first in natural language, a table, a flowchart, or pseudocode before converting it into a program.

### EDU-03 — Build a Complete Development Cycle

Students should treat reading, predicting, implementing, testing, debugging, modifying, and explaining as one learning cycle rather than focusing only on successful execution.

Acceptance direction: Students can state expected results, design tests, compare actual results, locate problems, and explain why a correction works.

### EDU-04 — Retain Responsibility When Using External Assistance

AI and other external assistance are optional learning tools rather than required course capabilities. When a student chooses to adopt an external explanation, hint, test suggestion, debugging suggestion, or generated fragment, the student remains responsible for understanding the problem, making the core design decision, and verifying the adopted result.

Acceptance direction when external assistance is actually adopted: Students can explain what they used, why they accepted or modified it, and what evidence they used to verify it. Choosing not to use AI or other optional assistance does not reduce completion, participation, assessment, or success.

## 4. Core Capability Requirements

### Data and Variables

#### CAP-D01 — Understand Values, Variables, and State

Students can distinguish a value, a variable name, and the current state, and can trace changes caused by assignment operations.

Dependency: Basic model of sequential program execution.

Acceptance evidence: Variable-trace tables, output prediction, error correction, and oral explanation.

#### CAP-D02 — Use Basic Data Types

Students can select and use basic data types according to problem needs and understand how types affect representation range, operations, and input/output.

Dependency: CAP-D01.

Acceptance evidence: Type-selection tasks, input/output implementation, diagnosis of type errors, and case comparison.

#### CAP-D03 — Construct and Understand Expressions

Students can translate calculation rules into expressions, understand evaluation order, and manually verify simple results.

Dependencies: CAP-D01 and CAP-D02.

Acceptance evidence: Expression translation, result prediction, parenthesis modification, and test cases.

#### CAP-D04 — Handle Input and Output

Students can obtain data from standard input, present results through standard output, and understand that formats and data types must match.

Dependencies: Execution model and CAP-D02.

Acceptance evidence: Minimal input/output programs, format correction, input-case testing, and output explanation.

### Control Flow

#### CAP-C01 — Understand Sequential Execution

Students can trace the effect of each statement on program state and output in execution order.

Dependencies: Basic execution model and CAP-D01.

Acceptance evidence: Line-by-line tracing, reordering code fragments, output prediction, and identifying the first point of inconsistency.

#### CAP-C02 — Use Conditional Selection

Students can build Boolean conditions from problem rules and use appropriate selection structures to express one-way, two-way, or multi-way decisions.

Dependencies: CAP-D02, CAP-D03, and CAP-C01.

Acceptance evidence: Path prediction, boundary testing of conditions, requirement modification, and explanation of branch choice.

#### CAP-C03 — Use Repetition Structures

Students can recognize repeated work, define loop state and stopping conditions, and use an appropriate loop to express repetition.

Dependencies: CAP-D01, CAP-D03, CAP-C01, and CAP-C02.

Acceptance evidence: Iteration tables, explanation of stopping conditions, correction of infinite loops, and counting or accumulation tasks.

#### CAP-C04 — Combine Control Structures

Students can combine sequence, selection, and repetition within a reasonable cognitive load to solve basic multi-step problems.

Dependencies: CAP-C01 through CAP-C03.

Acceptance evidence: Flowchart-to-code mapping, modification of existing control flow, and testing of normal and boundary cases.

### Functions and Problem Decomposition

#### CAP-F01 — Understand the Responsibility of a Function

Students can treat a function as a callable unit with a name, a clear responsibility, inputs, and outputs rather than merely as a syntax pattern.

Dependencies: CAP-D01 and CAP-C01.

Acceptance evidence: Identifying function responsibilities, describing a function in one sentence, matching inputs and outputs, and predicting call results.

#### CAP-F02 — Define and Call Basic Functions

Students can write and call basic functions with parameters and return values and trace the data flow before and after a call.

Dependencies: CAP-D02, CAP-D03, and CAP-F01.

Acceptance evidence: Completing functions, tracing calls, modifying parameters, testing return values, and correcting errors.

#### CAP-F03 — Decompose Problems with Functions

Students can divide a larger problem by responsibility, avoid assigning too much work to one function, and explain the reason for the decomposition.

Dependencies: CAP-C04 and CAP-F02.

Acceptance evidence: Requirement decomposition, function-interface design, refactoring an existing program, and comparing alternative decompositions.

#### CAP-F04 — Understand Scope and Data Transfer

Students can understand basic local scope and the roles of parameters and return values and avoid relying on unclear sources of data.

Dependency: CAP-F02.

Acceptance evidence: Scope tracing, name-conflict analysis, modification of data transfer, and behavior prediction.

## 5. Cross-Cutting Capability Requirements

### X-01 — Program Execution Model

Students can distinguish source code, compilation, execution, input, output, and errors and know that a C program begins at `main` and proceeds through statements.

### X-02 — Program Reading and Explanation

Students can identify data, control flow, and function responsibilities in an existing program and describe its behavior.

### X-03 — Testing and Verification

Students can create normal, boundary, and necessary exceptional cases and compare expected and actual results.

### X-04 — Debugging and Modification

Students can read error messages or observe incorrect behavior, narrow the problem scope, form a hypothesis, and verify a correction.

### X-05 — Communication and Reflection

Students can explain their solution, limitations, basis for testing, and remaining uncertainties.

### X-06 — Verification of Adopted External Assistance

When students choose to adopt AI-generated or other external suggestions, they can explain the adopted contribution and verify it using appropriate technical evidence. This requirement is conditional on actual use; students are not required to interact with AI, retain AI records, or make a non-use declaration.

## 6. Instructional Delivery Requirements

### DEL-01 — Shared Core Capabilities

The Chinese-taught and English-taught preparatory classes must deliver the same core capability requirements and acceptance standards and must follow the same official assessment and optional-AI policy.

### DEL-02 — Different Pacing, One Requirements Baseline

The 10-hour English-taught class and 12-hour Chinese-taught class must use the same competency map. Differences may appear only in:

- How activities are grouped into sessions.
- The ratio of explanation to practice.
- Time for reinforcement and formative diagnosis.
- Non-core extension activities.

### DEL-03 — Continuity Between Preparatory and Formal Courses

The preparatory course should deliver the minimum prerequisite capabilities needed by the formal course, but should not aim to finish formal-course content early.

The formal course should rapidly reactivate preparatory capabilities and then increase depth, independence, and integration.

### DEL-04 — Capabilities Before Weeks

The course schedule must be generated from capability dependencies and acceptance needs. It must not begin by fixing chapter weeks and then forcing capabilities into them.

### DEL-05 — Formative Evidence First

The preparatory course primarily identifies risks, establishes foundations, and provides feedback. Unless otherwise decided in the official assessment policy, high-stakes summative assessment should not be its primary delivery method.

## 7. Quality and Non-Functional Requirements

### NFR-01 — Substantive Bilingual Equivalence

All official requirements, capabilities, course, and assessment documents must be available in both Traditional Chinese and English and support item-by-item comparison.

### NFR-02 — Traceability

Every teaching material and assessment must ultimately trace to at least one requirement, and every core requirement must have corresponding instruction and acceptance evidence.

### NFR-03 — Cognitive Load Control

Each learning unit should limit the number of newly introduced concepts and use minimal examples, manually verifiable data, and staged integration.

### NFR-04 — Fairness

Neither class may face an unreasonable disadvantage in shared core capabilities because of instructional language, number of sessions, student background, or equipment differences.

### NFR-05 — Maintainability

Documents must use consistent identifiers, versions, paired language filenames, and explicit dependencies so that another instructor can take over.

### NFR-06 — Technical Accuracy

Code examples, tool procedures, test data, and terminology must be technically verified before publication. AI-generated or other externally generated content must not be published merely because a tool produced it.

### NFR-07 — Adaptability

Instructors may adjust examples, practice volume, and pacing according to student response, but may not arbitrarily lower core requirements or acceptance standards.

## 8. Requirement Priority

The following priorities are used:

- P0: Indispensable; without it, the course violates the Constitution or cannot achieve its main purpose.
- P1: Core to the formal course; the preparatory course may target a lower maturity level.
- P2: Important extension; scheduled according to available time and student readiness.
- P3: Deferred to a future version or another course.
- Conditional: Applies only when the corresponding optional tool or activity is actually adopted.

Current classification:

| Requirement | Preparatory Course | Formal Course |
|---|---|---|
| X-01 Execution model | P0 | P0 |
| CAP-D01–D04 | P0/P1 | P0 |
| CAP-C01–C03 | P0/P1 | P0 |
| CAP-C04 | P2 | P0 |
| CAP-F01 | P0 | P0 |
| CAP-F02 | P1 | P0 |
| CAP-F03–F04 | P2 | P0/P1 |
| X-02–X-05 | P0 | P0 |
| X-06 adopted external assistance verification | Conditional | Conditional |
| DEL-01–DEL-05 | P0 | P0 |
| NFR-01–NFR-07 | P0 | P0 |

This table is a planning baseline and does not independently override the Constitution, official assessment policy, scope standard, or approved competency standard.

## 9. Definition of Done for a Requirement

A requirement is considered designed only when all of the following are true:

1. It has a unique identifier and clear statement.
2. Its educational rationale is stated.
3. Prerequisite capabilities are identified.
4. Observable student behavior is defined.
5. At least one type of acceptance evidence is specified.
6. Corresponding Chinese and English versions exist.
7. It can be traced to teaching material, an activity, or an assessment.
8. It does not conflict with the Constitution or official assessment policy.

## 10. Maintenance and Navigation

This requirements map is maintained alongside the related domain model, knowledge dependency graph, competency standard, scope boundary, delivery models, materials, and assessments. Changes should be made by dependency impact rather than by an assumed sequential document stage.

- [Instructional Design Workspace](README.en.md)
- [Programming Domain Model](03-programming-domain-model.en.md)
- [Programming Language Knowledge Dependency Graph](04-programming-language-knowledge-graph.en.md)
- [Programming Competency Map](05-competency-map.en.md)
- [繁體中文版](02-requirements-map.zh-TW.md)
