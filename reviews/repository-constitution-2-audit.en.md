# Repository-Wide Constitution 2.0 Compliance Audit

Version: 0.1.0  
Status: Audit baseline draft  
Authoritative basis: `CONSTITUTION.en.md` 2.0.0  
Primary audience: Course designers, instructors, and maintainers  
Normative force: This document records findings and recommendations only; it does not create new rules

## 1. Purpose

This audit re-examines every official repository document under Constitution 2.0. Its purpose is not to rewrite everything at once, but to establish a traceable, prioritized, and batch-oriented correction process.

The audit must determine:

1. The document's governance level.
2. Its primary audience.
3. Whether it has a clear and unique authoritative role.
4. Whether its Traditional Chinese and English versions are complete and substantively equivalent.
5. Whether student-facing documents satisfy the right to readable materials and the teaching principles.
6. Whether technical content is verifiable.
7. Whether AI, assessment, and language-track rules comply with Constitution 2.0.
8. Whether the document should be retained, rewritten, moved, merged, historicized, or deleted.

## 2. Audit Principles

### 2.1 The Constitution is not a checklist substitute

Constitution 2.0 provides highest-level principles only. Formats, templates, and workflows belong in Standards, Guides, or Policies. The audit must not smuggle new operational detail into constitutional interpretation.

### 2.2 Student documents take priority

Problems in student materials take priority over internal governance neatness. Anything that obstructs continuous reading, concept formation, or verification is high priority.

### 2.3 Presence does not equal validity

A file's presence in version control does not mean it is current, publishable, or authoritative. Obsolete reviews, duplicated policies, and undiscoverable documents must have their roles reassessed.

### 2.4 Review documents do not create rules

Corrections must be written back into the actual authoritative source. Audit reports record evidence, judgments, and recommendations only.

## 3. Document Classification Model

Each file shall first be classified into one of these levels:

| Level | Purpose | Typical content |
|---|---|---|
| Constitution | Non-negotiable and long-term stable principles | Highest purpose, adjudication principles, governance boundaries |
| Standards | Consistency requirements and quality baselines | Document types, writing standards, templates, metadata, navigation standards |
| Guides and Policies | Adaptable procedures and current-term rules | Assessment policy, delivery workflow, publication process, technical validation method |
| Materials | Actual teaching and learning content | Student materials, instructor guides, activities, code examples |
| Historical Record | Evidence of decisions and evolution only | Completed reviews, migration reports, historical decision records |

Every official document must have one primary audience: student, instructor, designer or maintainer, or reviewer.

## 4. Compliance Ratings

### A — Compliant

The role is clear, the document serves its primary audience, and no major bilingual or technical issue exists.

### B — Minor revision

The core can remain, but navigation, wording, boundaries, metadata, or local synchronization needs improvement.

### C — Structural revision

The document still has value, but mixes audiences, lacks an authoritative role, weakens student readability, or duplicates rules defined elsewhere.

### D — Non-compliant

The document conflicts with Constitution 2.0, is obsolete, cites the former Constitution as current, is technically unverifiable, or creates a serious barrier to student understanding.

### H — Historicize

The document no longer governs current work but is worth retaining as evidence of evolution or decision-making. It must be clearly marked historical and must not appear in current navigation as an active policy.

## 5. Risk Priority

### P0 — Immediate correction

- Incorrect or obsolete highest-level rules, policies, or assessment requirements.
- Technical errors or major misdirection in student-visible content.
- Substantive conflict between language versions.
- Conflicting authoritative sources.

### P1 — High priority

- Student materials that do not support continuous reading.
- Instructor and student content mixed together.
- AI rules that still require use, logs, or declarations by default.
- Incorrect knowledge-dependency order.
- Important code or explanation that cannot be verified.

### P2 — Medium priority

- READMEs or indexes that do not let the primary audience reasonably reach a document.
- Unclear document type or primary audience.
- Duplicate rules, duplicate definitions, or excessive metadata.
- Review documents that have not been historicized.

### P3 — General improvement

- Layout, terminology, formatting, or minor bilingual differences that do not affect understanding or decisions.

## 6. Initial Repository-Wide Audit Sequence

### Batch 1: Authoritative sources and navigation

- Root `README.md`
- `CONSTITUTION.zh-TW.md`
- `CONSTITUTION.en.md`
- `classes/zh/README.md`
- `classes/en/README.md`
- `design/13-learning-assessment-policy.*`
- Every file that still references Constitution 1.3.0 or obsolete AI rules

Purpose: establish Constitution 2.0 as the sole highest baseline, remove duplicated or obsolete rules, and create clear entry points for students, instructors, and maintainers.

### Batch 2: Student learning materials

- All student-facing Unit materials
- Student navigation, homework, and assessment explanations
- Student-visible code examples and setup documents

Purpose: review prose flow, paragraph transitions, concept-first sequencing, prerequisites, errors and verification, internal-governance pollution, and technical correctness.

### Batch 3: Instructor documents

- Unit instructor guides
- Classroom execution flows
- Observation, prompting, misconception, and fallback materials

Purpose: ensure instructor documents are executable without rewriting student materials or prematurely exposing instructor prompts.

### Batch 4: Design and governance documents

- `design/01` onward
- Concept Tree, Registry, Unit Map, and Traceability Matrix
- Terminology, Scope, Acceptance, Risk, and Delivery files

Purpose: identify authoritative roles, dependencies, duplicated definitions, and whether each file belongs in Standards, Policies, or Historical Record.

### Batch 5: Review and historical documents

- `design/12-constitution-compliance-review.*`
- `reviews/constitution-maturity-review.*`
- Other completed audit, review, and validation documents

Purpose: record audit baselines and dates, historicize reviews based on former constitutions, and prevent them from being mistaken for current policy.

### Batch 6: Technical validation and automation

- `.github/workflows/technical-validation.yml`
- All code examples and compile manifests
- Link, bilingual-pairing, and navigation-integrity checks

Purpose: assign automatically verifiable work to CI without delegating readability or pedagogy judgments to automation.

## 7. Required Audit Fields

| Field | Meaning |
|---|---|
| Path | Document path |
| Language Pair | Corresponding language version |
| Governance Level | Constitution / Standards / Guides and Policies / Materials / Historical Record |
| Primary Audience | Student / Instructor / Designer-Maintainer / Reviewer |
| Authoritative Role | Whether the file is the unique source for a rule |
| Constitution Articles | Relevant articles |
| Rating | A / B / C / D / H |
| Priority | P0 / P1 / P2 / P3 |
| Findings | Concrete issues and evidence |
| Action | Retain / Rewrite / Move / Merge / Historicize / Delete |
| Validation | Bilingual, technical, navigation, and human-review method |

## 8. Known Initial Risks

1. `design/12-constitution-compliance-review.*` was produced under the former Constitution and may no longer be suitable as a current compliance conclusion. It should be historicized or rewritten first.
2. The root README may still act as a complete legacy index rather than role-based navigation.
3. The design directory contains many files that may simultaneously act as Standards, Policies, Reviews, and Historical Records; their authoritative boundaries need separation.
4. Student materials have passed technical validation, but Article 6 still requires human readability review. CI success does not prove fluent prose.
5. Assessment policy and Unit-level AI, homework, submission, and assessment language may redefine the same rules in multiple places and must return to a single authoritative source.

## 9. Execution Model

Repository correction shall be split into focused PRs rather than one repository-wide rewrite:

1. PR A: Navigation, document classification, and authoritative sources.
2. PR B: Assessment and AI policy consistency.
3. PR C: Student-material readability, processed in Unit batches.
4. PR D: Instructor-document boundaries and executability.
5. PR E: Governance levels and historicization of design documents.
6. PR F: CI, bilingual pairing, links, and technical validation improvements.

Every PR must update Traditional Chinese and English versions together and identify the Constitution 2.0 articles it implements.

## 10. Current Conclusion

Constitution 2.0 is now the sole official baseline. The next step is not an indiscriminate rewrite of every file. The repository must first establish authoritative sources and document roles, then correct files in P0-to-P3 order.

This file is the operational baseline for the audit. It is not a new Constitution or policy source.
