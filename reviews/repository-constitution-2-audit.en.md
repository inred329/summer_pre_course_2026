# Repository-Wide Constitution 2.0 Compliance Audit

Version: 1.6.0  
Status: Active audit record  
Last updated: 2026-08-07  
Authoritative basis: `CONSTITUTION.en.md` 2.0.0  
Primary audience: Course designers, instructors, and maintainers  
Normative force: This document records findings and recommendations only; it does not create new rules

## 1. Purpose and Ratings

This audit examines governance level, primary audience, authoritative role, bilingual equivalence, student readability, technical verifiability, and consistency of AI and assessment rules under Constitution 2.0.

Ratings: A compliant, B minor correction, C structural correction, D noncompliant, H historicalized.  
Priorities: P0 immediate, P1 high, P2 medium, P3 general improvement.

## 2. Completed Audit Matrix

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | Students, instructors, maintainers | C → A | P0 | Duplicated assessment policy, progress reporting, and obsolete AI requirements | Rewritten as a three-role entry | Complete |
| `classes/zh/README.md`, `classes/en/README.md` | Material entry | Students | D → A | P0 | Early TBD drafts did not match current delivery | Rewritten for current 4×3-hour and 5×2-hour tracks | Complete |
| `design/13-learning-assessment-policy.*` | Official Policy | Students and instructors | D → A | P0 | Mandatory pre-AI artifacts, summaries, logs, and universal AI oral capability | AI made optional; non-use is not a deficit | Complete |
| `design/12-constitution-compliance-review.*` | Historical Record | Maintainers | D → H | P0 | Treated Constitution 1.2.0 as current | Historicalized with an obsolete warning | Complete |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | Maintainers | C → A | P0 | Claimed precedence and duplicated assessment policy | Removed normative force; retained only migration guidance | Complete |
| `materials/preparatory/unit-01*` through `unit-04*` | Student Material | Students | B → A | P1 | AI appeared in the core path and implied mandatory use | Converted to skippable optional extensions | Complete |
| `materials/assignments/*` | Student resources / assessment implementation | Students, instructors | B → A | P1 | Indexing and rubric wording could imply AI was required | Homework remains unsubmitted and ungraded; AI notes optional; rubrics consider AI only when actually used | Complete |
| `materials/README.*`, `materials/TEMPLATE.*` | Role-based index / authoring guide | Students, instructors, maintainers | C → A | P1 | Mixed audiences, copied policy, fixed AI chapter, and premature completion claims | Rewritten as role-based navigation and purpose-driven authoring guidance | Complete |
| `materials/instructor/session-guides.*` | Instructor Guide | Instructors, TAs | A | P1 | Executable pacing, misconceptions, fallbacks, fairness supports, and concise records | Retained; `design/13` remains authoritative | Reviewed |
| `materials/formal/README.*`, `materials/formal/unit-01*` through `unit-12*` | Student Material | Students | B → A | P1 | AI in core paths and multiple technical-contract gaps | AI made directly skippable; value, input, lifetime, allocation, stream, dependency, overflow, and failure contracts strengthened | Complete |
| `design/README.*` | Governance index / guide | All roles | C → A | P2 | Listed all design files as equally "official," duplicated policy text, and contained obsolete development next steps | Rewritten with authority order, governance roles, maintenance workflow, and current navigation | Complete |
| `design/01-product-vision.*` | Revisable planning model | Course designers and maintainers | C → A | P1 | Claimed governing authority and made AI use part of universal success evidence | Reclassified as planning context; external-assistance verification made conditional; AI non-use explicitly neutral | Complete |

## 3. Governing Decisions

### 3.1 AI Must Not Become Implicitly Mandatory

AI may be offered as an extension, but it must not become mandatory through placement in the core sequence, completion checklist, fixed template, or assessment field. All preparatory and formal Units now use directly skippable optional extensions. AI non-use does not affect completion, participation, or assessment.

### 3.2 Assessment Has One Authoritative Source

`design/13-learning-assessment-policy.*` is the sole authoritative assessment policy. READMEs, task packs, rubrics, templates, and instructor guides may provide navigation or implementation guidance only.

### 3.3 Design Documents Do Not Share Equal Authority

The design workspace now follows this authority order: Constitution, official policy, approved design standards, planning and traceability models, implementation guides and materials, then historical records. Lower-level files may not override higher-level sources.

### 3.4 Student Materials Must State Technical Contracts

Materials must state value ranges, input states, termination conditions, lifetimes, dereference ranges, allocation sizes, ownership, failure preservation, stream states, module dependencies, compile/link stages, and undefined behavior where relevant. Successful compilation or one correct output cannot replace those contracts.

### 3.5 Earlier Audits Are Historical

Earlier reviews record decisions under a particular date and constitutional version. Current decisions follow Constitution 2.0 and this active audit.

## 4. Confirmed Student-Material Quality

Preparatory Units 1–4 and formal Units F-U01 through F-U12 now provide:

- concept-first entry through a problem context;
- prediction and state, flow, memory, stream, or module-dependency tracing;
- reproducible defects, diagnosis, and regression checks;
- requirement changes and normal, boundary, invalid, and failure cases;
- no substitution of compilation success, one output, or tool judgment for understanding;
- clear completion standards and bilingual correspondence;
- AI outside core completion;
- operable and verifiable technical boundaries and failure conditions.

No P0/P1 issue requiring the materials to be withdrawn was found in this batch. P3 wording and pacing refinements may follow classroom trials.

## 5. Current Design-Governance Classification

- Constitution: `CONSTITUTION.*`.
- Official policy: `design/13-learning-assessment-policy.*`.
- Design standards: competency, scope, terminology, Concept Tree, Concept Registry, and Unit Map.
- Planning and traceability models: vision, requirements, domain model, knowledge graph, acceptance, delivery, risk, traceability, and student-material outlines.
- Historical record: `design/12-constitution-compliance-review.*`.
- Governance index: `design/README.*`.

`design/01-product-vision.*` now matches this classification. The next design-governance batch must apply the recorded corrections for `design/02–04` and continue inspecting the remaining individual files for duplicated normative claims, stale metadata, and bilingual equivalence.

## 6. Next Audit Scope

### P1: Recorded Design Corrections

Apply the existing paired findings for `design/02–04`, including authority conflicts, universal AI requirements, mandatory AI records, domain-model mixing, stale status text, and bilingual metadata differences.

### P2: Individual Design Documents

Review `design/05–11` and `14–17` for duplicated policy statements, conflicting authority claims, obsolete status text, stale next steps, and bilingual equivalence.

### P2: Automated Technical and Navigation Checks

- Bilingual pairing and substantive equivalence.
- Former-Constitution references.
- Broken links and orphan files.
- Compile manifests, GCC/Clang differences, and CI coverage.

## 7. Current Conclusion

All identified P0 issues have been corrected. Preparatory materials and formal Units F-U01 through F-U12 have completed bilingual review, and the paired `design/01` P1 findings are now resolved. Recorded P1 corrections remain in `design/02–04`, and the repository-wide audit is not complete. Individual design-document cleanup, audit-matrix expansion, and automated validation remain, so PR #10 stays in draft.
