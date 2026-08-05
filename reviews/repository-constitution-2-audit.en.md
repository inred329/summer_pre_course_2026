# Repository-Wide Constitution 2.0 Compliance Audit

Version: 0.2.0  
Status: Active audit record  
Authoritative basis: `CONSTITUTION.en.md` 2.0.0  
Primary audience: Course designers, instructors, and maintainers  
Normative force: This document records findings and recommendations only; it does not create new rules

## 1. Purpose

This audit re-examines repository documents under Constitution 2.0 through a traceable, prioritized, batch-oriented correction process.

The audit determines:

1. The document's governance level.
2. Its primary audience.
3. Whether it has a clear and unique authoritative role.
4. Whether its Traditional Chinese and English versions are complete and substantively equivalent.
5. Whether student-facing documents satisfy the right to readable materials and the teaching principles.
6. Whether technical content is verifiable.
7. Whether AI, assessment, and language-track rules comply with Constitution 2.0.
8. Whether the document should be retained, rewritten, moved, merged, historicized, or deleted.

## 2. Classification and Ratings

| Level | Purpose |
|---|---|
| Constitution | Non-negotiable and long-term stable principles |
| Standards | Consistency requirements, templates, formats, and quality baselines |
| Guides and Policies | Adaptable procedures, execution methods, and current-term rules |
| Materials | Actual teaching and learning content |
| Historical Record | Evidence of decisions and evolution only |

Compliance ratings: A compliant, B minor revision, C structural revision, D non-compliant, H historicized.

Priorities: P0 immediate correction, P1 high priority, P2 medium priority, P3 general improvement.

## 3. First-Batch Audit Results

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | Students, instructors, designers-maintainers | C → A | P0 | Duplicated assessment policy, design philosophy, progress reporting, and obsolete AI requirements, creating unclear authority boundaries | Rewritten as a role-based routing entry with concise orientation and authoritative links only | Completed |
| `classes/zh/README.md` | Material entry | Chinese-track students | D → A | P0 | Early TBD draft contradicted the current four 3-hour sessions and completed materials | Rewritten as the current student entry and policy route | Completed |
| `classes/en/README.md` | Material entry | English-track students | D → A | P0 | Early TBD draft omitted the current five 2-hour sessions and student route | Rewritten as the current student entry and policy route | Completed |
| `design/13-learning-assessment-policy.*` | Official Policy | Students and instructors | D → A | P0 | Required pre-AI artifacts, AI summaries, and adoption reasons, and treated AI judgment as a fixed oral-exam capability for every student | Updated to 0.2.0; AI is optional by default, non-use is not a deficit, and students remain responsible only for results they adopt | Completed |
| `design/12-constitution-compliance-review.*` | Historical Record | Designers and maintainers | D → H | P0 | Based on Constitution 1.2.0 and still declared fixed metadata, IDs, and AI records to be mandatory material-development conditions | Reclassified as historical, with an obsolete-policy warning and current-audit links | Completed |

## 4. First-Batch Decisions

### 4.1 Root README role

The root README is a routing entry, not a duplicate assessment policy, progress report, or complete design explanation. Official rules belong to Constitution 2.0 and the corresponding authoritative policy files.

### 4.2 Track-entry role

Track READMEs serve students by providing current course positioning, material entry points, and policy links. They must not retain internal TODOs, owner fields, or obsolete module plans.

### 4.3 AI in assessment

AI is optional by default. A student who uses AI must still explain, modify, and verify the adopted result. A student who does not use AI needs no declaration and lacks no capability evidence.

### 4.4 Former constitutional reviews

Reviews performed under Constitution 1.2.0 retain historical value only. They may not define current material gates or require obsolete AI, metadata, ID, or template rules.

## 5. Next Scan Scope

### P0: Obsolete AI and assessment rules

Search and review:

- `AI 使用紀錄` and `AI-use log`.
- `保留 AI 使用前` and `before AI use`.
- `未使用 AI 聲明` and `non-use declaration`.
- Whether `AI judgment` is treated as a fixed capability for every student.
- Whether `ASSESSMENT-NOTE` duplicates or overrides the official assessment policy.

### P1: Student-material readability

Review Units in batches for:

- Concept IDs, capability IDs, maintenance status, or instructor prompts in the student reading flow.
- Excessive fields, lists, or specification tables replacing explanation and reasoning.
- Natural movement from problem context to concept, syntax, observation, and verification.
- Required prerequisites that have not been established.

### P2: Governance levels of design documents

Reclassify `design/01–11`, the Concept Tree, Registry, Unit Map, Traceability Matrix, Acceptance, Risk, and Delivery documents as Standards, Policies, Design Sources, or Historical Records so that not every file claims baseline authority.

### P2: Automated technical and navigation checks

Strengthen:

- Chinese–English pairing checks.
- Former-Constitution reference scans.
- Broken-link and orphan-file scans.
- Compile manifests and technical-validation scope.

## 6. Execution Model

Further corrections will be processed in reviewable batches:

1. Obsolete AI and assessment-rule cleanup.
2. Student-material readability by Unit group.
3. Instructor-document boundaries and executability.
4. Governance levels and authoritative sources for design documents.
5. CI, bilingual pairing, links, and technical validation.

Every batch must update Traditional Chinese and English together and write official rules back into the true authoritative source.

## 7. Current Conclusion

The first P0 batch is complete: the root README now serves as a routing entry, both track entries reflect the current course, the assessment policy no longer imposes obsolete AI requirements, and the former constitutional review has been historicized.

The next priority is a repository-wide scan for obsolete AI and assessment language so that student materials, instructor documents, or supplemental policies cannot reintroduce requirements that conflict with Constitution 2.0.
