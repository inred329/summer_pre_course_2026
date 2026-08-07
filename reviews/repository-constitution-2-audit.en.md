# Repository-Wide Constitution 2.0 Compliance Audit

Version: 1.8.0  
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
| `design/README.*` | Governance index / guide | All roles | C → A | P2 | Listed all design files as equally official, duplicated policy text, and contained obsolete next steps | Rewritten with authority order, governance roles, maintenance workflow, and current navigation | Complete |
| `design/01-product-vision.*` | Revisable planning model | Course designers and maintainers | C → A | P1 | Claimed governing authority and made AI use part of universal success evidence | Reclassified as planning context; external-assistance verification made conditional; AI non-use explicitly neutral | Complete |
| `design/02-requirements-map.*` | Revisable planning and traceability model | Course designers and maintainers | C → A | P1 | Presented later documents as controlled by this requirements baseline; defined AI literacy and AI records as universal requirements; retained stale sequential navigation | Reclassified as non-governing planning model; higher-authority precedence stated; external-assistance verification made conditional; mandatory AI records removed; maintenance navigation aligned | Complete |
| `design/03-programming-domain-model.*` | Revisable planning model | Course designers and maintainers | C → A | P1 | Embedded AI as a core programming domain, required transparent AI records, had bilingual metadata drift, and described a physical build pipeline too categorically | Reframed AI as optional external assistance; made disclosure contextual; synchronized version/status; added implementation-neutral toolchain caveats and corrected pointer/storage wording | Complete |
| `design/04-programming-language-knowledge-graph.*` | Revisable planning and traceability model | Course designers and maintainers | C → A | P1 | Treated AI judgment/verification as universal cross-cutting dependency, required an AI record path, used stale draft/stage navigation, and over-specified preprocessing/assembly/linking artifacts | Added conditional dependency type; made the external-assistance branch optional; removed universal record requirements; synchronized metadata; replaced stage navigation; clarified conceptual versus implementation-specific build stages and runtime models | Complete |

## 3. Governing Decisions

### 3.1 AI Must Not Become Implicitly Mandatory

AI may be offered as an extension, but it must not become mandatory through placement in a core sequence, completion checklist, fixed template, requirements baseline, domain model, dependency graph, competency field, or assessment field. AI non-use does not affect completion, participation, or assessment. Planning models may describe verification responsibilities only conditionally when optional external assistance is actually adopted.

### 3.2 Assessment Has One Authoritative Source

`design/13-learning-assessment-policy.*` is the sole authoritative assessment policy. READMEs, task packs, rubrics, templates, instructor guides, and planning models may provide navigation, traceability, or implementation guidance only.

### 3.3 Design Documents Do Not Share Equal Authority

The design workspace follows this authority order: Constitution, official policy, approved design standards, planning and traceability models, implementation guides and materials, then historical records. Lower-level files may not override higher-level sources.

### 3.4 Student Materials Must State Technical Contracts

Materials must state relevant value ranges, input states, termination conditions, lifetimes, dereference preconditions, allocation sizes, ownership, failure preservation, stream states, module dependencies, compile/link distinctions, and undefined behavior. Successful compilation or one correct output cannot replace those contracts.

### 3.5 Conceptual Models Must Not Be Mistaken for Implementation Guarantees

Design diagrams may simplify language-toolchain or runtime responsibilities, but they must mark implementation-dependent details. The C standard does not require a fixed physical pipeline of standalone preprocessor, compiler, assembler, and linker programs, nor one specific runtime representation such as a physical call stack. Concrete materials must identify and verify the target compiler and environment when those details matter.

### 3.6 Earlier Audits Are Historical

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

`design/01–04` now match this classification and the optional-AI policy. The next design-governance batch must continue with `design/05–11` and `design/14–17`, checking each bilingual pair for duplicated normative claims, stale metadata, stale next-step language, tool-specific assumptions, and substantive equivalence.

## 6. Next Audit Scope

### P2: Individual Design Documents

Review `design/05–11` and `design/14–17` individually for:

- conflicting authority claims or duplicated policy;
- mandatory AI/tool requirements that are not authorized by the official policy;
- stale draft/status or sequential “next stage” language;
- bilingual version/status/content mismatches;
- technical claims that confuse conceptual models with C-standard or implementation guarantees.

### P2: Automated Technical and Navigation Checks

- Bilingual pairing and substantive equivalence.
- Former-Constitution references.
- Broken links and orphan files.
- Compile manifests, GCC/Clang differences, and CI coverage.

## 7. Current Conclusion

All identified P0 issues have been corrected. Preparatory materials and formal Units F-U01 through F-U12 have completed bilingual review, and the paired P1 findings in `design/01–04` are now resolved and committed. The repository-wide audit is not complete: `design/05–11`, `design/14–17`, and automated navigation/technical validation remain, so PR #10 stays in draft.
