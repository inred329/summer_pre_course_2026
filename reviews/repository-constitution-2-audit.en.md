# Repository-Wide Constitution 2.0 Compliance Audit

Version: 0.9.0  
Status: Active audit record  
Last updated: 2026-08-06  
Authoritative basis: `CONSTITUTION.en.md` 2.0.0  
Primary audience: Course designers, instructors, and maintainers  
Normative force: This document records findings and recommendations only; it does not create new rules

## 1. Purpose and Ratings

This audit examines governance level, primary audience, authoritative role, bilingual equivalence, student readability, technical verifiability, and consistency of AI and assessment rules under Constitution 2.0.

Ratings: A compliant, B minor revision, C structural revision, D non-compliant, H historicized.  
Priorities: P0 immediate correction, P1 high priority, P2 medium priority, P3 general improvement.

## 2. Completed Audit Matrix

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | Students, instructors, designers-maintainers | C → A | P0 | Duplicated policy, progress reporting, and obsolete AI requirements | Rewritten as a three-role routing entry | Completed |
| `classes/zh/README.md` | Material entry | Chinese-track students | D → A | P0 | Early TBD draft contradicted the current course | Rewritten as the current 4×3-hour entry | Completed |
| `classes/en/README.md` | Material entry | English-track students | D → A | P0 | Early TBD draft contradicted the current course | Rewritten as the current 5×2-hour entry | Completed |
| `design/13-learning-assessment-policy.*` | Official Policy | Students and instructors | D → A | P0 | Required pre-AI artifacts, summaries, records, and universal AI oral capability | Made AI optional; non-use is not a deficit | Completed |
| `design/12-constitution-compliance-review.*` | Historical Record | Designers and maintainers | D → H | P0 | Treated Constitution 1.2.0 as current | Historicized with obsolete-policy warnings | Completed |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | Maintainers | C → A | P0 | Claimed precedence and duplicated assessment policy | Removed normative force; retained migration guidance only | Completed |
| `materials/preparatory/unit-01*` through `unit-04*` | Student Material | Students | B → A | P1 | AI activities sat in the core path and implied required work | Recast as skippable optional extensions; completion does not depend on AI | Completed |
| `materials/assignments/ai-use-log.*` | Optional Learning Resource | Students | A | P1 | Optional, unsubmitted, ungraded, and requires no non-use declaration | Retain; indexes must not present it as required | Reviewed |
| `materials/assignments/preparatory-assignments.*` | Student Task Pack | Students and instructors | A | P1 | Homework is unsubmitted and ungraded; AI is outside core completion | Retain | Reviewed |
| `materials/assignments/rubric.*` | Assessment Standard | Instructors and assistants | A | P1 | AI is considered only when actually used | Retain | Reviewed |
| `materials/assignments/grading-guide.*` | Instructor Guide | Instructors and assistants | A | P1 | Supports multiple evidence modes and does not make AI routine | Retain | Reviewed |
| `materials/README.*` | Role-based materials index | Students, instructors, authors-maintainers | C → A | P1 | Mixed audiences, copied policy, claimed audit completion, and made AI a shared Unit standard | Rewritten as role-based entries that link the authoritative policy | Completed |
| `materials/TEMPLATE.*` | Authoring Standard / Guide | Material authors and maintainers | C → A | P1 | Required a fixed AI section and mechanical uniformity | Rewritten as a purpose-driven suggested template; AI may appear only as an optional extension | Completed |
| `materials/instructor/session-guides.*` | Instructor Guide | Instructors and assistants | A | P1 | Pacing, misconceptions, fallback, fairness support, and post-class records are executable | Retain; `design/13` remains authoritative | Reviewed |
| `materials/formal/README.*` | Student-material index | Students | C → A | P1 | Claimed every Unit contained a fixed AI explanation | Rewrote the path; AI does not affect completion, participation, or assessment | Completed |
| `materials/formal/unit-01-representation-types.*` | Student Material | Students | B → A | P1 | AI was in the core path; completion did not exclude AI | Recast AI as skippable and added a non-AI completion standard | Completed |
| `materials/formal/unit-02-complex-control-flow.*` | Student Material | Students | B → A | P1 | AI was in the core path; no no-record/no-declaration rule | Recast as optional and added a non-AI completion standard | Completed |
| `materials/formal/unit-03-arrays.*` | Student Material | Students | B → A | P1 | AI in core path; insufficient accumulation range and input contracts | Added representable-range, validation, and empty-collection contracts | Completed |
| `materials/formal/unit-04-strings.*` | Student Material | Students | B → A | P1 | AI in core path; fixed-size input did not fully explain truncation, residual input, and terminator risks | Made AI optional; added truncation detection, buffer, and `\0` contracts | Completed |
| `materials/formal/unit-05-call-stack-recursion.*` | Student Material | Students | B → A | P1 | AI in core path; recursion depth and representable result range lacked a complete contract | Made AI optional; added base-case, depth, stack, and result-range limits | Completed |
| `materials/formal/unit-06-pointers.*` | Student Material | Students | B → A | P1 | AI in core path; lifetime, nullability, one-past, and aliasing boundaries needed clarification | Made AI optional; added lifetime, dereference-range, and aliasing contracts | Completed |
| `materials/formal/unit-07-structures.*` | Student Material | Students | B → A | P1 | AI remained in the core path; non-use was not explicitly excluded from completion | Recast AI as directly skippable and added a non-AI completion standard with no record or declaration requirement | Completed |

## 3. Major Decisions

### 3.1 AI activities must not become implicitly required

AI may be offered as an extension, but placement in a core chapter, completion list, fixed template, or assessment field must not turn it into required work. All reviewed preparatory Units, the formal-course index, and F-U01 through F-U07 now make AI directly skippable.

### 3.2 Assessment has one authoritative source

`design/13-learning-assessment-policy.*` is the sole authoritative source for formal assessment. READMEs, task packs, rubrics, templates, and instructor guides may provide navigation or implementation guidance only.

### 3.3 Student materials must expose technical contracts

Materials involving arrays, strings, recursion, pointers, and structures must state value ranges, input state, termination conditions, lifetime, dereference boundaries, string capacity, field validation, and undefined-behavior risks. Compilation success or one correct output cannot replace these contracts.

### 3.4 Prior reviews have historical force only

Prior reviews record judgments under a specific date and constitutional baseline. Current decisions follow Constitution 2.0 and this active audit.

## 4. Confirmed Student-Material Quality

Preparatory Units 1–4 and formal-course F-U01 through F-U07 now provide:

- Problem context before syntax.
- Prediction and state, flow, or memory tracing.
- Reproducible defects, diagnosis, and regression verification.
- Requirement modification and multiple test categories.
- No reliance on compilation success, one output, or tool judgment as proof of understanding.
- Clear prerequisites, completion standards, and paired bilingual versions.
- No dependency on AI for core completion.
- Operationally verifiable technical boundaries and failure conditions.

These files may still receive P3 prose and pacing refinements after classroom trials, but no P0/P1 issue requiring their use to stop remains.

## 5. Next Audit Scope

### P1: Formal-course student materials

- `materials/formal/unit-08*` through `unit-12*`
- Whether AI remains in a core completion path.
- Whether internal governance, instructor prompts, or grading administration pollute student reading.
- Concept-first sequencing, dependency order, defect diagnosis, and technical verifiability.

### P2: Governance levels of design documents

Reclassify `design/01–11`, the Concept Tree, Registry, Unit Map, Traceability, Acceptance, Risk, and Delivery documents so multiple files do not claim authority over the same rule.

### P2: Automated technical and navigation checks

- Chinese–English pairing and substantive equivalence.
- Former-Constitution references.
- Broken links and orphaned files.
- Compile manifests, GCC/Clang differences, and CI coverage.

## 6. Current Conclusion

All P0 issues identified so far have been corrected. The formal-course index and F-U01 through F-U07 have been reviewed. F-U07 now places AI outside the core completion path while retaining explicit contracts for full initialization, valid pointers, bounded strings, structure assignment, and field validation. The repository-wide audit is not complete; the next batch continues with F-U08 through F-U12, design governance, and automated validation, so the pull request remains a draft.
