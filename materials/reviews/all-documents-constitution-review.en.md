# Repository-Wide Constitution Compliance Review

Version: 1.0.0  
Status: Official review record  
Last updated: 2026-08-05  
Corresponding Chinese version: [全文件憲法遵循重審](all-documents-constitution-review.zh-TW.md)

## Document Purpose

This document re-examines the repository's current official documents against `CONSTITUTION.en.md`, including:

- the root README and primary navigation
- design documents `design/01–17`
- Preparatory student materials P-U01 through P-U04
- Formal student materials F-U01 through F-U12
- material indexes, templates, assessment, homework, and instructor resources
- AI-related documents and wording

The review does not merely confirm that files exist. It checks bilingual completion, discoverability, independent readability, Concepts before syntax, prediction and verification, error-based teaching, cognitive-load control, competency orientation, and AI as an aid rather than a substitute for thinking.

## Overall Decision

The repository now establishes a complete design chain:

```text
Course Constitution
→ Vision and Requirements
→ Concept Tree / Registry
→ Unit Map
→ 16 Unit Outlines
→ 16 Bilingual Student Units
→ Homework, Assessment, and Instructor Resources
```

The overall direction aligns with the Constitution, but three explicit problems were found and corrected before PR #8 can be merged:

1. The Chinese formal-course index contained three broken links.
2. The general materials index still described an old stage in which only the preparatory materials were complete, leaving the 12 formal Units unreachable from the main materials index.
3. The materials index still described AI-use records and verification as routine requirements for every Unit, conflicting with the current low-weight concept-conversation role.

These problems have been corrected in both languages on `agent/complete-remaining-15-units`.

## 1. Bilingual Completion

### Confirmed

- The Course Constitution has Traditional Chinese and English versions.
- Design documents `01–17` have bilingual counterparts.
- P-U01 through P-U04 have Chinese and English student materials.
- F-U01 through F-U12 have Chinese and English student materials.
- The formal-course and general materials indexes are bilingual.
- The 30 Unit files in PR #8 are fully paired; no Unit exists in only one language.

### Remaining Concern

Bilingual file pairing is complete, but terminology, code, test data, error cases, and exercise constraints still require Unit-by-Unit substantive-equivalence review. F-U05 through F-U12 deserve particular attention because their Concepts are more complex.

## 2. Document Purpose and Independent Readability

### Confirmed

- P-U01 clearly separates student material, instructor guidance, and assessment policy.
- P-U02 through P-U04 and F-U01 through F-U12 include purpose, core question, completion standard, practice, and summary.
- Materials no longer depend on instructor-only oral context for the main learning path.
- Scheduling, participation observation, and grading administration primarily remain in instructor and assessment documents.

### Remaining Concern

The more complex formal Units have complete structures but use a compact treatment. Independent comprehension must still be tested for:

- F-U05: call frames, scope, lifetime, and recursion
- F-U06: address, pointer, indirection, and aliasing
- F-U08: allocation, ownership, lifetime, and release
- F-U10: interface, implementation, translation, and linking

## 3. Pedagogical Sequence

### Confirmed

Most Units follow:

```text
Core question
→ prediction or observable problem
→ visual model
→ Concept
→ minimal program
→ trace
→ error case
→ practice and requirement modification
→ self-check and summary
```

The materials generally establish Concepts before C syntax and include at least one reproducible error case with a correction process.

### Remaining Concern

A shared template must not force every Unit into the same depth. Each Concept requires appropriate treatment:

- representation and types require bit and conversion diagrams
- pointers and dynamic memory require memory and lifetime diagrams
- modular programming requires file, compilation, and linking relationships
- testing and debugging require an evidence chain, not only code examples

## 4. Prediction, Errors, and Verification

### Confirmed

- P-U01 through P-U04 contain prediction, tracing, diagnosis, and requirement modification.
- Formal Units generally include normal cases, error cases, tests, or regression work.
- Documents state that successful compilation, completed execution, passing an OJ, or positive AI feedback cannot independently establish capability.

### Still Required

The repository does not yet contain actual compile verification for every Unit example. All complete programs should be compiled as C17 and checked for:

- GCC and Clang warnings
- Linux/macOS and Windows command differences
- expected input and output
- undefined and implementation-defined behavior
- array and string bounds
- dynamic-memory defects
- file-open and EOF handling
- multi-file linking

PR #8 should remain Draft until this technical verification is complete.

## 5. Cognitive Load and Information Priority

### Confirmed

- Materials use short sections, small programs, tables, and diagrams.
- New Concepts generally follow the Unit Map dependency order.
- Preparatory Units do not require full understanding of pointers, dynamic allocation, or advanced data structures too early.

### Needs Strengthening

The Constitution requires explicit distinctions among:

- must understand
- must complete
- recommended practice
- extension exploration
- may be deferred

P-U01 and the formal Units mostly express priority through prose rather than consistent labels. This is not an immediate blocker, but longer Units should add explicit information levels so all content does not appear equally important.

## 6. AI Role

### Current Official Role

AI is not a standalone Unit and is not a major learning activity in each chapter. Each Unit ends with one brief activity:

> The student explains the core Concept to AI in their own words.

No fixed prompt or conversation submission is required, and AI is not authoritative. When an AI response conflicts with code, tests, compiler behavior, or reproducible results, the student must judge using evidence.

### Corrected Problem

The general materials index previously required explicit permitted/prohibited AI rules and retained evidence as a routine part of every Unit. That wording overemphasized AI and conflicted with the current design decision. It now states:

- AI is a low-weight concept-conversation tool.
- The AI-use log is an optional extension resource.
- AI use is not a Unit completion requirement.

## 7. Navigation and Discoverability

### Confirmed Navigation Chain

```text
README.md
→ materials/README.zh-TW.md or materials/README.en.md
→ preparatory/ or formal/ index
→ each Unit
→ corresponding language and adjacent Units
```

### Corrected Problem

The Chinese formal-course index previously linked to three nonexistent paths:

- F-U02: `unit-02-advanced-control.zh-TW.md`
- F-U10: `unit-10-modules.zh-TW.md`
- F-U12: `unit-12-integration.zh-TW.md`

The correct files are:

- `unit-02-complex-control-flow.zh-TW.md`
- `unit-10-modular-programming.zh-TW.md`
- `unit-12-integrated-application.zh-TW.md`

The general materials index now includes the formal-course entry, so the 12 formal Units are no longer orphaned.

## 8. Assessment and Homework Policy

### Confirmed

- Homework is not submitted, graded, or individually marked.
- The next class reserves time for homework discussion.
- Roll call and attendance percentage are not graded.
- Participation may be shown through multiple forms.
- Official grades consist only of classroom participation and one final one-on-one oral examination.

### Remaining Concern

The root README, materials indexes, instructor guides, homework pack, and rubric must continue using the same wording. Any older file that still requires per-assignment passing, remediation, micro-orals, or mandatory homework submission must be corrected according to `design/13` and the assessment override.

## 9. Single Source of Truth and Maintainability

The Concept Tree, Registry, Unit Map, outlines, and student materials now have a traceable relationship. However, Chinese and English Markdown files remain separate files and therefore remain vulnerable to long-term drift.

Recommended automated checks:

- every `.zh-TW.md` has a corresponding `.en.md`
- Unit title, version, status, and updated date match
- code blocks and test data match
- cross-links resolve
- indexed files exist
- every Unit contains required sections

## 10. Conditions Before Merge

PR #8 should remain Draft until:

1. The 15 newly added Units receive technical and substantive bilingual review.
2. Every complete C program example is actually compiled.
3. All adjacent-Unit and language-switch links are checked.
4. Technical and pedagogical defects found in review are corrected.
5. The material template is aligned with the current structure, or its update is explicitly recorded as the next PR.

## Review Conclusion

The repository's course-design direction, 16-Unit structure, bilingual strategy, student-material format, assessment policy, and AI role are broadly aligned with the Constitution.

This review corrected explicit navigation and AI-position inconsistencies. However, PR #8 has not yet completed actual C17 compilation and Unit-by-Unit technical-equivalence verification. The current decision is therefore:

> **The document architecture and instructional design are conditionally compliant; PR #8 should not be merged until technical verification is complete.**

## Navigation

- [Course Constitution](../../CONSTITUTION.en.md)
- [Materials and Activity Resources](../README.en.md)
- [P-U01 Constitution Compliance Review](pu01-constitution-review.en.md)
- [繁體中文版](all-documents-constitution-review.zh-TW.md)
