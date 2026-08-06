# Repository-Wide Constitution 2.0 Compliance Audit

Version: 0.4.0  
Status: Active audit record  
Last updated: 2026-08-06  
Authoritative basis: `CONSTITUTION.en.md` 2.0.0  
Primary audience: Course designers, instructors, and maintainers  
Normative force: This document records findings and recommendations only; it does not create new rules

## 1. Purpose

This audit re-examines all official repository documents under Constitution 2.0. It records governance level, primary audience, authoritative role, bilingual equivalence, student readability, technical verifiability, and consistency of AI and assessment rules.

Compliance ratings: A compliant, B minor revision, C structural revision, D non-compliant, H historicized.  
Priorities: P0 immediate correction, P1 high priority, P2 medium priority, P3 general improvement.

## 2. Completed Audit Matrix

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | Students, instructors, designers-maintainers | C → A | P0 | Duplicated assessment policy, design philosophy, progress reporting, and obsolete AI requirements | Rewritten as a three-role routing entry | Completed |
| `classes/zh/README.md` | Material entry | Chinese-track students | D → A | P0 | Early TBD draft contradicted the current course | Rewritten as the current 4×3-hour entry | Completed |
| `classes/en/README.md` | Material entry | English-track students | D → A | P0 | Early TBD draft contradicted the current course | Rewritten as the current 5×2-hour entry | Completed |
| `design/13-learning-assessment-policy.*` | Official Policy | Students and instructors | D → A | P0 | Required pre-AI artifacts, summaries, records, and universal AI oral capability | Made AI optional; non-use is not a deficit | Completed |
| `design/12-constitution-compliance-review.*` | Historical Record | Designers and maintainers | D → H | P0 | Treated Constitution 1.2.0 as the current baseline | Historicized with obsolete-policy warnings | Completed |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | Maintainers | C → A | P0 | Claimed official precedence and duplicated assessment policy | Removed normative force; retained only legacy-wording migration guidance | Completed |
| `materials/preparatory/unit-01-execution.*` | Student Material | Students | B → A | P1 | AI activity sat in the core numbered flow and implied required work | Marked as skippable optional extension; completion does not depend on AI | Completed |
| `materials/preparatory/unit-02-data-state.*` | Student Material | Students | B → A | P1 | AI activity sat in the core numbered flow and implied required work | Marked as skippable optional extension; completion does not depend on AI | Completed |
| `materials/preparatory/unit-03-control-flow.*` | Student Material | Students | B → A | P1 | AI activity sat in the core numbered flow and implied required work | Marked as skippable optional extension; completion does not depend on AI | Completed |
| `materials/preparatory/unit-04-functions-integration.*` | Student Material | Students | B → A | P1 | AI activity sat in the core numbered flow and implied required work | Marked as skippable optional extension; completion does not depend on AI | Completed |
| `materials/assignments/ai-use-log.*` | Optional Learning Resource | Students | A | P1 | Clearly optional, unsubmitted, ungraded, and requires no non-use declaration | Retain; indexes must not present it as required | Reviewed |
| `materials/assignments/preparatory-assignments.*` | Student Task Pack | Students and instructors | A | P1 | Homework is unsubmitted and ungraded; AI remains optional and outside core completion | Retain | Reviewed |
| `materials/assignments/rubric.*` | Assessment Standard | Instructors and assistants | A | P1 | AI explanation and verification are considered only when AI was actually used; non-use does not affect grading | Retain | Reviewed |
| `materials/assignments/grading-guide.*` | Instructor Guide | Instructors and assistants | A | P1 | AI and external suggestions are not fixed activities; participation and assessment support multiple evidence modes | Retain | Reviewed |
| `materials/README.*` | Role-based materials index | Students, instructors, authors-maintainers | C → A | P1 | Mixed three audiences, duplicated official policy, claimed review completion, made AI conversation a shared Unit standard, and retained obsolete Override naming | Rewritten as role-based entry points; policy linked rather than copied; AI made optional; prior reviews identified as time-bound records | Completed |
| `materials/TEMPLATE.*` | Authoring Standard / Guide | Material authors and maintainers | C → A | P1 | Required a fixed AI section and AI self-check and mechanically prescribed the same structure for every Unit | Rewritten as a purpose-driven suggested template; fixed AI section removed; core completion does not depend on AI | Completed |

## 3. Major Decisions

### 3.1 Position of AI activities in student materials

AI may be offered as an extension tool, but it must not become implicitly required through placement in the core reading path, completion checklist, fixed template field, or assessment criteria. All reviewed preparatory Units and the material template now present AI only as a clearly labeled, directly skippable optional extension.

### 3.2 Role of the AI verification-note template

`ai-use-log.*` is an optional personal review template. It must not become an assignment attachment, required oral-exam evidence, non-use declaration, or routine instructor checklist.

### 3.3 Single authoritative source for assessment rules

`design/13-learning-assessment-policy.*` is the sole authoritative source for the official assessment system. READMEs, task packs, rubrics, templates, and instructor guides may provide navigation or operational guidance but may not duplicate the full policy or create conflicting rules.

### 3.4 A template is not a fixed chapter contract

A material template should provide design support rather than require every Unit to reproduce the same mechanical outline. Activities, visuals, defect cases, and requirement modifications should be selected according to the core question, prerequisites, and cognitive load. Essential quality is controlled through the prepublication check.

### 3.5 Force of prior review records

Prior reviews record judgments made at a particular date under a particular constitutional baseline. A filename containing “official,” “complete,” or “compliant” does not make that review a current guarantee. Current decisions follow Constitution 2.0 and this active repository-wide audit.

## 4. Confirmed Student-Material Quality

Preparatory Units 1–4 currently provide:

- Problem context before syntax.
- Prediction before execution and state or flow tracing.
- Reproducible defects, diagnosis, and regression verification.
- Requirement modification and multiple test categories.
- No reliance on compilation success, one output, or tool judgment as proof of understanding.
- Clear prerequisites, completion standards, and paired bilingual versions.
- No dependency on AI for core completion.

The Units may still receive P3 prose and pacing refinements after classroom trials, but this review found no P0/P1 technical or instructional defect requiring their use to stop.

## 5. Next Audit Scope

### P1: Instructor-document boundaries

- `materials/instructor/*`
- Whether guides are directly executable without rewriting student chapters.
- Whether they include instructor prompts, misconceptions, fallback activities, and fairness support.
- Whether they still duplicate assessment policy or imply routine AI use.

### P1: Formal-course student materials

- `materials/formal/*`
- Whether AI activities remain in core completion paths.
- Whether internal governance fields, instructor prompts, or grading administration pollute student reading.
- Whether Concept-first sequencing, dependency order, defect diagnosis, and technical verifiability are adequate.

### P2: Governance levels of design documents

Reclassify `design/01–11`, the Concept Tree, Registry, Unit Map, Traceability, Acceptance, Risk, and Delivery documents so multiple files do not claim authority over the same rule.

### P2: Automated technical and navigation checks

- Chinese–English pairing and substantive equivalence.
- Former-Constitution references.
- Broken links and orphaned files.
- Compile manifests, GCC/Clang differences, and CI coverage.

## 6. Current Conclusion

All P0 issues identified so far have been corrected. AI positioning and authoritative-source defects in preparatory Units, assignment and assessment files, materials indexes, and templates have been corrected. The repository-wide audit is not complete; the next batch covers instructor documents, formal-course student materials, design governance, and automated validation, so the pull request remains a draft.
