# Course Risk Register

Version: 0.1.1  
Status: Revisable planning and traceability model  
Governance note: This register identifies risks and mitigations; it does not create grading, homework, attendance, or AI-use policy. The Constitution and official learning/assessment policy take precedence.  
Corresponding Chinese version: [課程風險登錄表](09-risk-register.zh-TW.md)

## Document Purpose

This document identifies, evaluates, and manages major design and delivery risks for the 2026 summer preparatory course and the connected formal C programming course.

Each risk should be traceable to requirements, competencies, scope, acceptance, delivery, materials, or technical verification and should have observable triggers, preventive measures, contingency actions, and an accountable role.

## Constitution 2.0 Alignment

- Student safety, dignity, fairness, understanding, and technical correctness take precedence over superficial pacing or output quantity.
- Chinese-taught and English-taught tracks must preserve substantively equivalent core standards.
- AI and other external tools are optional by default. Risk controls must not make optional AI use, AI logs, or non-use declarations universal requirements.
- Tool misuse is addressed through stronger evidence, verification, and assessment design rather than a blanket ban or mandatory surveillance.
- Scope pressure must not be resolved by removing essential testing/debugging practice or by adding unrelated advanced topics.
- A major change must be propagated to affected authoritative sources and dependent bilingual documents.

---

# 1. Risk Assessment Model

## 1.1 Probability

| Level | Definition |
|---|---|
| P1 Low | Unlikely under current conditions but worth observing. |
| P2 Medium | Reasonably possible and requires prevention and monitoring. |
| P3 High | Likely and requires action before or during delivery. |

## 1.2 Impact

| Level | Definition |
|---|---|
| I1 Low | Affects one activity or a small number of learners and can be corrected locally. |
| I2 Medium | Affects a delivery stage, track consistency, or multiple forms of evidence. |
| I3 High | Damages core capability, assessment credibility, course continuity, fairness, or constitutional principles. |

Risk score = Probability × Impact. Numeric score supports ordering but does not replace judgment; safety, fairness, or invalid-assessment risks may be escalated regardless of score.

---

# 2. Status and Accountable Roles

| Status | Meaning |
|---|---|
| Open | Identified; major mitigation is not complete. |
| Mitigating | Preventive or reducing measures are being implemented. |
| Watching | Major measures are in place and indicators are being observed. |
| Triggered | The event occurred and contingency actions are active. |
| Closed | The risk was removed, accepted, or converted into another documented decision. |

Typical accountable roles:

- Course lead: scope, competency standards, assessment-policy alignment, and major course changes.
- Instructor: pacing, learning evidence, classroom adaptation, and escalation.
- Teaching assistant: observes learning gaps and recurring technical/environment problems.
- Document maintainer: bilingual consistency, navigation, versioning, and correction of material defects.
- Student: provides authentic capability evidence and remains responsible for any result they adopt, including results from optional external assistance.

A learner is not universally required to disclose non-use or preserve AI logs. Any attribution or disclosure requirement must come from an applicable approved activity, academic-integrity rule, or assessment condition.

---

# 3. High-Priority Risks

| ID | Risk | P | I | Score | Main triggers | Prevention / mitigation | Contingency | Accountable role | Status |
|---|---|---:|---:|---:|---|---|---|---|---|
| R-01 | A learner presents work they cannot explain, modify, test, or diagnose because a person or tool supplied too much of the core reasoning or implementation | 3 | 3 | 9 | Large mismatch between artifact quality and live explanation; cannot trace or modify own work; tests are absent or unexplained | Use staged tasks, requirement changes, prediction/tracing, multiple evidence types, and live explanation consistent with policy; keep optional external assistance non-authoritative | Reassess the missing programming capability using a fresh tracing, modification, testing, or diagnosis task; judge capability evidence rather than tool use itself | Course lead, instructor | Mitigating |
| R-02 | Preparatory time is overloaded, causing exposure without durable capability | 3 | 3 | 9 | Activities are repeatedly compressed; testing, tracing, or discussion is cut; learners imitate without explanation | Enforce scope boundaries; reduce examples/context before reducing reasoning and verification | Stop adding content; move non-core topics to optional demonstration; protect minimum core evidence | Course lead, instructor | Mitigating |
| R-03 | Language tracks diverge in core capability or technical depth | 2 | 3 | 6 | One track adds/removes core topics; passing expectations differ; language load is handled by lowering technical standards | Share competency IDs, scope targets, technical contracts, and assessment criteria; vary pacing/scaffolds only | Recalibrate with common evidence and restore missing core learning opportunities | Course lead, document maintainer | Watching |
| R-04 | Formal-course work repeats preparatory activities at the same maturity | 2 | 3 | 6 | Same examples and imitation tasks recur without new modification, diagnosis, or transfer | Begin formal Units from preparatory evidence and increase maturity through new contexts, defects, and requirement changes | Convert repetition into diagnosis/transfer work and adjust later pacing | Course lead, instructor | Open |
| R-05 | Capability judgment collapses into OJ results, output matching, attendance, or final-product review | 3 | 3 | 9 | Rubrics omit explanation/tracing/testing; a single automated result dominates; presence is treated as capability | Follow official assessment policy; use diverse evidence and live reasoning where appropriate | Reassess missing evidence; correct implementation rubrics or task design | Course lead, instructor | Mitigating |
| R-06 | Pointers and memory are taught as symbols or one platform's diagrams rather than validity/lifetime reasoning | 3 | 3 | 9 | Learners memorize `*`, `&`, `malloc`, `free`; cannot explain object lifetime, bounds, aliasing, or invalid access | Establish object/value/address/lifetime models; mark stack/heap diagrams as implementation models; use boundary and failure cases | Pause new syntax and return to memory/lifetime traces and smaller defects | Instructor | Open |
| R-07 | Advanced data structures are added merely to integrate pointers or fill time | 2 | 3 | 6 | Linked lists, trees, heaps, hashes, or graphs appear as core without scope justification | Require scope-change review and prerequisite/evidence/time justification | Remove, defer, or reduce to optional demonstration; restore displaced core practice | Course lead, document maintainer | Watching |
| R-08 | Environment/tool differences consume learning time or are mistaken for programming capability | 3 | 2 | 6 | Installation, path, encoding, shell, permission, or compiler differences dominate class; identical source yields environment-specific behavior | Specify a validated target environment, fallback path, and environment check; distinguish tool failures from program failures | Use fallback environment or equivalent reasoning task and record environment incidents | Instructor, teaching assistant | Open |
| R-09 | Prerequisite differences become too large for one pacing path | 3 | 2 | 6 | Large completion-time gaps; weaker learners copy; stronger learners drift into unrelated advanced content | Shared core with layered scaffolds; harder modification/diagnosis/transfer for faster learners | Small-group remediation and alternate depth tasks without changing common core | Instructor, teaching assistant | Open |
| R-10 | Bilingual files, IDs, links, status, or policy references become unsynchronized | 2 | 3 | 6 | Versions, identifiers, requirements, code, links, or status differ across language pairs | Update bilingual pairs in the same unit of work; run consistency/link checks | Stop relying on conflicting copies; repair against higher-authority sources and record impact | Document maintainer | Watching |

---

# 4. Medium-Priority Risks

| ID | Risk | P | I | Score | Trigger | Mitigation / response | Accountable role | Status |
|---|---|---:|---:|---:|---|---|---|---|
| R-11 | Long sessions cause cognitive fatigue and lower evidence quality | 2 | 2 | 4 | Late-session explanation/tracing quality falls; instruction becomes lecture-only | Change activity mode, use breaks, and distribute demanding reasoning across the session | Instructor | Open |
| R-12 | English-medium language load is mistaken for programming weakness | 2 | 2 | 4 | Learner can reason with code/diagrams but cannot answer quickly in English | Use terminology support, diagrams, response scaffolds, and extra reading time while preserving technical standards | Instructor, teaching assistant | Open |
| R-13 | Instructors/TAs interpret maturity, evidence, or optional-tool boundaries inconsistently | 2 | 2 | 4 | Similar performance gets different judgments; one section treats optional tool use as mandatory | Calibrate with examples and authoritative policy; escalate unresolved interpretation differences | Course lead, teaching assistant | Open |
| R-14 | Learners hide external assistance because they believe tool use itself is punished | 2 | 2 | 4 | Students avoid discussing adopted suggestions or cannot identify what they actually understand | State clearly that optional use is not itself a capability deficit; focus on ownership, integrity rules, and verification of adopted results | Instructor | Open |
| R-15 | Testing/debugging is postponed until late rather than treated as cross-cutting | 2 | 2 | 4 | Early work only matches sample output; learners cannot define expectations or diagnose later | Include prediction/test/defect work across Units and review coverage | Instructor, document maintainer | Watching |
| R-16 | One integrated project hides individual capability gaps | 2 | 2 | 4 | Team members or tools complete most functionality; individual understanding is unclear | Use distributed evidence and individual modification/tracing/diagnosis; treat project as only one artifact | Instructor | Open |
| R-17 | Scope, policy, or delivery changes but dependent materials remain stale | 2 | 2 | 4 | Materials assess removed requirements or omit new boundaries | Use traceability matrix and affected-file review for every major change | Course lead, document maintainer | Open |
| R-18 | Learners can operate only one IDE and cannot separate source/build/runtime problems | 2 | 2 | 4 | Small environment change prevents diagnosis; all failures are called “it doesn't run” | Expose the target build process and use diagnostic classification without requiring mastery of multiple IDEs | Instructor | Open |
| R-19 | Conceptual diagrams are mistaken for C-standard guarantees or one implementation's physical behavior | 2 | 3 | 6 | Materials state that every implementation has the same compiler/assembler/linker stages, stack frames, or heap layout | Mark conceptual vs implementation-specific claims; verify concrete claims against target standard/toolchain/runtime | Course lead, document maintainer | Mitigating |

---

# 5. Monitoring Indicators

Review indicators at appropriate delivery checkpoints:

| Indicator | Risks it may indicate |
|---|---|
| Students pass code tests but cannot explain, trace, modify, or diagnose | R-01, R-05, R-06 |
| Reasoning/testing activities are repeatedly cut for pacing | R-02, R-05, R-15 |
| Core tasks or standards differ between language tracks | R-03, R-10, R-12 |
| Formal activities repeat preparatory maturity unchanged | R-04 |
| Class time lost to environment problems | R-08, R-18 |
| Repeated difficulty clusters around the same competency IDs | R-02, R-06, R-09 |
| Adopted external suggestions cannot be independently verified when relevant | R-01, R-14 |
| Broken links, stale IDs, old policy claims, or bilingual mismatches | R-10, R-17 |
| Topics added without scope review | R-07, R-17 |
| Implementation-specific diagrams are stated as universal language facts | R-19 |

Indicators diagnose system problems; they must not be used to publicly label or shame individual students.

---

# 6. Risk Treatment Strategies

| Strategy | Appropriate use |
|---|---|
| Avoid | Remove a design that directly violates the Constitution, policy, scope, safety, or fairness. |
| Reduce | Lower probability/impact through scaffolding, practice, environment standardization, verification, and complementary evidence. |
| Transfer | Move non-core support to documentation, TAs, or fallback environments without transferring the learner's core reasoning responsibility. |
| Accept | Accept low-cost residual risks when monitoring and response are adequate. |

Unacceptable treatments include lowering one language track's technical standard, cancelling essential reasoning/testing merely to preserve pacing, making optional AI use mandatory as an anti-cheating measure, substituting surveillance for capability evidence, or adding unrelated advanced topics for faster learners.

---

# 7. Review Cadence

## Before delivery

- Verify environment, materials, bilingual pairs, navigation, and authoritative-policy references.
- Calibrate competency/evidence judgments with examples.
- Confirm that core capability has suitable complementary evidence.
- Check for unnecessary repetition and implementation-specific claims.

## During / after delivery stages

- Review relevant triggers and indicators.
- Update risk status and residual risk.
- Adjust pacing/scaffolding without expanding scope silently.
- Record recurring student-readability or technical problems for material maintenance.

## After the course

- Compare expected and actual risks.
- Record which mitigations worked or caused side effects.
- Feed material findings back into requirements, scope, acceptance, delivery, and technical standards.

---

# 8. Maintenance and Completion Criteria

This register is maintained when:

- major risks are linked to concrete design or policy dependencies;
- triggers are observable rather than purely abstract;
- prevention, contingency, and an accountable role exist;
- tool/AI risks are handled without converting optional use into a universal requirement;
- bilingual versions remain equivalent;
- material changes propagate into the traceability matrix and active repository audit.

## Related Documents

- [Course Delivery Map](08-delivery-map.en.md)
- [Course Design Traceability Matrix](10-traceability-matrix.en.md)
- [Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](09-risk-register.zh-TW.md)
