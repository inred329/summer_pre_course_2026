# Course Design Constitution Compliance Review

Version: 0.1.0  
Status: Official design review record  
Last updated: 2026-08-03  
Major change summary: Completed the constitutional consistency review of design documents `01–11`, documenting corrected gaps and controls required for the material-development stage.  
Corresponding Chinese version: [課程設計憲法遵循審查](12-constitution-compliance-review.zh-TW.md)

## Document Purpose

This document records the review of official design documents `design/01–11` against the Course Constitution so that instructors, teaching assistants, material authors, and maintainers can determine whether the current design baseline may proceed to materials and activity development.

This document does not replace or summarize away the Constitution. If it conflicts with the Course Constitution, the Constitution prevails.

## Review Scope

- Chinese and English Course Constitution, version 1.2.0.
- `design/01-product-vision.*` through `design/11-terminology-glossary.*`.
- Root `README.md` and both design indexes.

## Conclusion

No major constitutional conflict requiring a halt to subsequent work was found in the current design baseline.

Two governance gaps were identified and corrected within the same work stage:

1. The Chinese–English terminology glossary required by Article 13 was missing.
2. Important documents did not consistently record the last updated date and major change summary required by Article 20.

The first gap has been corrected through `11-terminology-glossary.*`. The second requirement is formally applied beginning with document `11`; existing documents `01–10` should receive dates and summaries the next time they undergo substantive revision rather than through a large batch of low-value formatting-only commits.

## Article-by-Article Review Result

| Constitutional Requirement | Design Implementation | Judgment | Continuing Control |
|---|---|---|---|
| Genuine understanding must not be replaced by correct output | `05` Competency Map and `07` Acceptance Model require complementary evidence | Compliant | Materials and assessments must not rely only on OJ or output |
| Bilingual completion and synchronization | Documents `01–12` exist in pairs and READMEs support language switching | Compliant | Every modification must update both versions in the same work unit |
| Single Source of Truth | Shared IDs, paired filenames, and traceability matrix | Substantially compliant | Code and test data should be maintained as shared files |
| Clear document purpose | Each document states its purpose and boundaries | Compliant | Materials must additionally state audience, tools, and completion criteria |
| Independent readability | Design documents provide background, dependencies, navigation, and completion conditions | Compliant | Student-facing documents must include complete operating information |
| Navigation integrity | Root README → design index → official documents | Compliant | Navigation must be updated whenever files change |
| Concrete, executable instructions | `07` defines acceptance tasks and evidence | Compliant | Actual activities must state submissions, resources, and completion standards |
| Terminology consistency | `11-terminology-glossary.*` | Corrected | New terms must enter the glossary before materials |
| Consistent document structure | Design documents share metadata, purpose, compliance, and navigation | Substantially compliant | A formal teaching-material template is still required |
| Code and prose correspondence | Large-scale official teaching code has not yet been produced | To be verified during material development | Every program must be compiled and tested |
| Appropriate visualization | Documents `03–10` use Mermaid for concepts and processes | Compliant | Material visuals must be verified against code, tracing, and tests |
| Cognitive-load control | `06`, `08`, and `09` define limits and risks | Compliant | Units must limit new concepts and use minimal examples |
| Information priority levels | `06` uses SB states and `08` separates core and extension | Compliant | Student materials must mark must-understand, must-do, extension, and defer |
| Technical accuracy and source responsibility | `09` treats error and unverified AI output as risks | Substantially compliant | Tool versions, changing rules, and external facts need source/version labels |
| Version and change traceability | Documents have versions and Git preserves history | Partially compliant | Add date and major-change summary when revising `01–10` |
| Progressive learning | `04` dependencies, `05` maturity, and `08` delivery path | Compliant | Materials should begin with prediction and modification before full independent construction |
| Reading, modification, and debugging as equal skills | `05`, `07`, and `08` include them as formal evidence | Compliant | Every major stage must include each at least once |
| Errors as official teaching material | `07` AT-07, `08` diagnosis tasks, and `09` controls | Compliant | Build a reproducible error-case library |
| Testing and verification as core skills | `05` PC-V, `07` EV-TE, and `08` cross-cutting delivery | Compliant | Every programming activity begins with expected results |
| Multiple reasonable solutions permitted | Acceptance focuses on behavior and evidence, not one structure | Compliant | Rubrics must not penalize a different reasonable solution merely for differing from the model |
| Preparatory and formal course continuity | `06` scope and `08` maturity progression | Compliant | Formal course must not repeat the same maturity activities |
| AI must not replace core thinking | `05` PC-A, `07` AI rules, and `09` R-01 | Compliant | Every activity must state permitted, prohibited, and retained records |
| AI content requires human verification | `07` AT-11, `09` technical risks, and `10` traceability | Compliant | Materials require human compilation, testing, and review before publication |
| Instructional fairness | `08` uses same standards with different pacing; `09` R-03 | Compliant | Compare core evidence and remediation outcomes across tracks |
| Maintainability and handoff | IDs, versions, indexes, risks, and traceability exist | Compliant | Build teaching-material templates and maintenance checklists |

## Why No Major Conflict Was Found

### 1. Learning Purpose and Acceptance Align

The design does not treat successful execution, passing OJ, project completion, or positive AI feedback as sufficient. Competency maturity requires explanation, tracing, modification, testing, diagnosis, and transfer.

### 2. AI Positioning Aligns

AI is defined as a collaborator for explanation, hints, testing, and debugging. Students retain responsibility for initial understanding, the core approach, expected results, technical verification, and final explanation.

### 3. Bilingual Fairness Aligns

The Chinese-taught and English-taught preparatory tracks use the same competencies, maturity targets, and minimum evidence. The extra two Chinese-track hours support practice, remediation, and acceptance rather than a higher graduation standard.

### 4. Course Scope Is Controlled

The formal core currently focuses on C programming, the memory model, sequences, strings, records, and basic operations. Linked lists, trees, heaps, hash tables, and graphs are not presumed core deliverables.

### 5. Document Governance Forms a Closed Loop

Requirements, concepts, knowledge, competencies, scope, acceptance, delivery, risk, and traceability all have explicit documents and identifiers and are reachable from the root README.

## Mandatory Conditions Before Entering Material Development

Every new teaching material, activity, assignment, rubric, or instructor document must:

1. Be created in Chinese and English together.
2. Cite at least one requirement ID and competency ID.
3. State target maturity and scope state.
4. State prerequisites, tools, resources, AI boundaries, and completion criteria.
5. Include an appropriate visual model, minimal example, trace, test, or operation.
6. Not use program completion or correct output as sole evidence.
7. Have code and test data verified in the specified environment.
8. Use approved terminology from `11-terminology-glossary`.
9. Update navigation and traceability.
10. Complete scope and risk review before adding core content.

## Recommended Next Work Unit

Create a bilingual teaching-material template as the single structural baseline for all unit materials. The template should operationalize Articles 10, 12, 14, 15, 16, 17, 18, 36, and 37 of the Constitution.

## Navigation

- [Previous stage: Chinese–English Terminology Glossary](11-terminology-glossary.en.md)
- [Back to Instructional Design Workspace](README.en.md)
- [繁體中文版](12-constitution-compliance-review.zh-TW.md)
