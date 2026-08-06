# Instructional Design Workspace

Version: 2.0.0  
Status: Active design-governance index  
Last updated: 2026-08-07  
Major change summary: Reclassified the design workspace so documents no longer share an undifferentiated "official" status. Constitution, policy, standards, planning models, implementation guides, and historical records now have explicit roles.  
Corresponding Chinese version: [教學內容設計區](README.zh-TW.md)

## Document Purpose

This directory supports design and maintenance of the 2026 Summer C Programming Preparatory Course and its connected formal course. It is not a flat set of equally authoritative documents. Each file has a defined governance role and audience.

## Authority Order

When documents conflict, use this order:

1. `CONSTITUTION.en.md` — governing principles and amendment rules.
2. `design/13-learning-assessment-policy.en.md` — the sole authoritative learning and assessment policy.
3. Approved design standards — stable definitions used to maintain scope, competency, terminology, and material structure.
4. Planning and traceability models — operational design records that may be revised as the course evolves.
5. Guides and student materials — implementations of the higher-level rules.
6. Historical records — evidence of earlier decisions; they do not govern current work.

A lower-level document must not silently override a higher-level source. When a conflict is found, correct the lower-level document and record the decision in the active audit.

## Governance Classification

| Files | Governance role | Primary audience | What the files may decide |
|---|---|---|---|
| `../CONSTITUTION.en.md` | Constitution | All roles | Governing principles, non-negotiable constraints, amendment process |
| `13-learning-assessment-policy.en.md` | Official policy | Students, instructors, maintainers | Grading, participation, homework, oral examination, and AI-use policy |
| `05-competency-map.en.md`, `06-scope-boundary.en.md`, `11-terminology-glossary.en.md`, `14-programming-concept-tree.en.md`, `15-programming-concept-registry.en.md`, `16-unit-map.en.md` | Design standards | Designers and maintainers | Stable competency, scope, terminology, concept, and Unit definitions within constitutional and policy limits |
| `01-product-vision.en.md`, `02-requirements-map.en.md`, `03-programming-domain-model.en.md`, `04-programming-language-knowledge-graph.en.md`, `07-acceptance-model.en.md`, `08-delivery-map.en.md`, `09-risk-register.en.md`, `10-traceability-matrix.en.md`, `17-student-material-outlines.en.md` | Planning and traceability models | Designers, instructors, maintainers | Rationale, dependencies, delivery planning, risks, mappings, and draft material structures; they do not create assessment policy |
| `12-constitution-compliance-review.en.md` | Historical record | Maintainers | Earlier review evidence only; Constitution 1.2.0 findings are not current requirements |
| `README.en.md` | Governance index / guide | All roles | Navigation and classification only; no independent policy |

## Document Responsibilities

### Constitution and official policy

- The Constitution defines governing principles.
- `13-learning-assessment-policy.en.md` is the only file that may define official grading, participation, homework, oral-examination, and AI-use rules.
- Other documents may summarize or implement the policy but should link to it rather than duplicate it.

### Design standards

Standards provide stable maintenance definitions. They must remain consistent with the Constitution and official policy and should change only through an explicit design decision with bilingual updates.

### Planning and traceability models

Planning models explain why and how the course is organized. They are important design evidence, but they are revisable and must not be treated as independent policy sources.

### Historical records

Historical records preserve earlier reasoning and migration context. They must be clearly labeled and must not be cited as current requirements.

## Current Design Principles

- C is the instructional language; transferable programming competency is the core goal.
- Concepts are the knowledge source; Units compose concept-dependency chains; Lessons are delivery slices of Units.
- Materials use problem context, prediction, visual or execution models, implementation, defect diagnosis, verification, and modification.
- Reading, prediction, modification, testing, debugging, and explanation are all valid evidence of learning.
- AI use is optional. It is never a prerequisite for Unit completion, participation, or assessment.
- Every Unit should provide reproducible errors, technical contracts, boundary cases, and regression checks.
- The Chinese-taught and English-taught tracks may differ in pacing and language scaffolding but must preserve equivalent core capability and assessment expectations.

## Maintenance Workflow

1. Identify the highest-authority source that governs the proposed change.
2. Update the bilingual pair together.
3. Update dependent standards, planning models, guides, and materials without copying policy text unnecessarily.
4. Verify links, bilingual pairing, terminology, and executable technical examples.
5. Record material governance changes in `reviews/repository-constitution-2-audit.*`.
6. Keep historical records intact but clearly non-normative.

## Navigation

- [Course Constitution](../CONSTITUTION.en.md)
- [Official Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Materials and Activity Resources](../materials/README.en.md)
- [Active Constitution 2.0 Audit](../reviews/repository-constitution-2-audit.en.md)
- [Back to repository home](../README.md)
- [繁體中文版](README.zh-TW.md)
