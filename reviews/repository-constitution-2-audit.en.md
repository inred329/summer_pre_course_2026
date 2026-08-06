# Repository-Wide Constitution 2.0 Compliance Audit

Version: 1.2.0  
Status: Active audit record  
Last updated: 2026-08-06  
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
| `materials/assignments/ai-use-log.*` | Optional Learning Resource | Students | A | P1 | Already optional, unsubmitted, and ungraded | Retained; indexes must not list it as required | Reviewed |
| `materials/assignments/preparatory-assignments.*` | Student Task Pack | Students, instructors | A | P1 | Homework is unsubmitted and ungraded; AI is outside core completion | Retained | Reviewed |
| `materials/assignments/rubric.*`, `grading-guide.*` | Assessment Standard / Instructor Guide | Instructors, TAs | A | P1 | AI is considered only when actually used | Retained | Reviewed |
| `materials/README.*` | Role-based materials index | Students, instructors, author-maintainers | C → A | P1 | Mixed audiences, copied policy, and premature completion claims | Rewritten as role-based entries linking the authoritative policy | Complete |
| `materials/TEMPLATE.*` | Authoring Standard / Guide | Authors and maintainers | C → A | P1 | Fixed AI chapter and mechanical structure | Replaced with purpose-driven guidance; AI only as optional extension | Complete |
| `materials/instructor/session-guides.*` | Instructor Guide | Instructors, TAs | A | P1 | Executable pacing, misconceptions, fallbacks, fairness supports, and concise records | Retained; `design/13` remains authoritative | Reviewed |
| `materials/formal/README.*` | Student-material index | Students | C → A | P1 | Claimed every Unit contained a fixed AI explanation | AI no longer affects completion, participation, or assessment | Complete |
| `materials/formal/unit-01*` through `unit-02*` | Student Material | Students | B → A | P1 | AI in the core path; completion standards did not exclude AI | Converted to optional extensions with non-AI completion standards | Complete |
| `materials/formal/unit-03-arrays.*` | Student Material | Students | B → A | P1 | Accumulation range, input validation, and empty-set contracts were weak | Added value-range and failure contracts; AI made optional | Complete |
| `materials/formal/unit-04-strings.*` | Student Material | Students | B → A | P1 | Truncation, residual input, and terminator risks were underexplained | Added line-truncation, buffer, and `\0` contracts | Complete |
| `materials/formal/unit-05-call-stack-recursion.*` | Student Material | Students | B → A | P1 | Recursion depth and representable-result limits were incomplete | Added base-case, depth, stack, and result-range limits | Complete |
| `materials/formal/unit-06-pointers.*` | Student Material | Students | B → A | P1 | Lifetime, nullability, one-past, and alias boundaries needed clarity | Added lifetime and dereference-range contracts | Complete |
| `materials/formal/unit-07-structures.*` | Student Material | Students | B → A | P1 | AI in core path; initialization and bounded-field contracts needed clarity | AI made optional and data contracts strengthened | Complete |
| `materials/formal/unit-08-dynamic-memory.*` | Student Material | Students | B → A | P1 | Allocation overflow, zero capacity, alias lifetime, and `realloc` contracts were incomplete | Added overflow, ownership, failure-preserving, and alias-invalidating contracts | Complete |
| `materials/formal/unit-09-files.*` | Student Material | Students | B → A | P1 | AI in core path; line truncation lacked a handling contract | Added complete I/O checks, EOF/error separation, and overlong-line handling | Complete |
| `materials/formal/unit-10-modular-programming.*` | Student Material | Students | B → A | P1 | AI in core path; `int` accumulation could overflow; `NULL` depended on an indirect include | AI made skippable; accumulation changed to `double`; `<stddef.h>` included directly; numeric-range contract added | Complete |

## 3. Governing Decisions

### 3.1 AI Must Not Become Implicitly Mandatory

AI may be offered as an extension, but it must not become mandatory through placement in the core sequence, completion checklist, fixed template, or assessment field. All reviewed preparatory Units, the formal-course index, and F-U01 through F-U10 now use directly skippable optional extensions.

### 3.2 Assessment Has One Authoritative Source

`design/13-learning-assessment-policy.*` is the sole authoritative assessment policy. READMEs, task packs, rubrics, templates, and instructor guides may provide navigation or implementation guidance only.

### 3.3 Student Materials Must State Technical Contracts

Materials must state value ranges, input states, termination conditions, lifetimes, dereference ranges, allocation sizes, ownership, failure preservation, stream states, module dependencies, compile/link stages, and undefined behavior where relevant. Successful compilation or one correct output cannot replace those contracts.

### 3.4 Earlier Audits Are Historical

Earlier reviews record decisions under a particular date and constitutional version. Current decisions follow Constitution 2.0 and this active audit.

## 4. Confirmed Student-Material Quality

Preparatory Units 1–4 and formal Units F-U01 through F-U10 now provide:

- concept-first entry through a problem context;
- prediction and state, flow, memory, stream, or module-dependency tracing;
- reproducible defects, diagnosis, and regression checks;
- requirement changes and normal, boundary, invalid, and failure cases;
- no substitution of compilation success, one output, or tool judgment for understanding;
- clear completion standards and bilingual correspondence;
- AI outside core completion;
- operable and verifiable technical boundaries and failure conditions.

No P0/P1 issue requiring the materials to be withdrawn was found in this batch. P3 wording and pacing refinements may follow classroom trials.

## 5. Next Audit Scope

### P1: Formal-Course Student Materials

- `materials/formal/unit-11*` and `unit-12*`
- AI positioning, readability, governance leakage, dependency order, defect diagnosis, and technical verifiability.

### P2: Design-Document Governance

Reclassify `design/01–11`, Concept Tree, Registry, Unit Map, Traceability, Acceptance, Risk, and Delivery so multiple files do not claim the same authoritative rule.

### P2: Automated Technical and Navigation Checks

- Bilingual pairing and substantive equivalence.
- Former-Constitution references.
- Broken links and orphan files.
- Compile manifests, GCC/Clang differences, and CI coverage.

## 6. Current Conclusion

All P0 issues identified so far have been corrected. The formal-course index and F-U01 through F-U10 are reviewed. F-U10 now moves AI outside the core path, removes signed-overflow risk from its average example, includes the direct header needed for `NULL`, and treats numeric range as part of the module interface contract. The repository-wide audit is not complete; F-U11, F-U12, design governance, and automated validation remain, so PR #10 stays in draft.
