# Course Risk Register

Version: 0.1.0  
Status: Architecture draft  
Corresponding Chinese version: [課程風險登錄表](09-risk-register.zh-TW.md)

## Document Purpose

This document identifies, evaluates, and manages major design and delivery risks for the 2026 summer preparatory course and the subsequent 16-week formal C programming course.

It answers:

1. Which factors may damage the course vision, competency development, or acceptance credibility?
2. When may a risk occur, and how can it be detected early?
3. Which preventive measures must be completed before delivery?
4. Which responses should be used after a risk is triggered?
5. Which residual risks must remain under observation even after mitigation?

This is not a generic administrative checklist. Every risk must be traceable to requirements, competencies, scope, acceptance, or delivery design and must have observable triggers and an accountable role.

## Constitutional Compliance

- Understanding, verification, and student responsibility take priority over superficial pacing and output quantity.
- The Chinese-taught and English-taught tracks must not diverge in core standards under delivery pressure.
- AI-related risk management prioritizes improved learning design rather than replacing governance with a total ban.
- Risks must not be treated by adding more content, lowering acceptance requirements, or introducing advanced data structures.
- Any major scope change must be reflected across the official design documents.

---

# 1. Risk Assessment Model

## 1.1 Probability

| Level | Definition |
|---|---|
| P1 Low | Unlikely under current conditions but still worth observing. |
| P2 Medium | Reasonably possible and requires prevention and monitoring. |
| P3 High | Likely and requires action before the course begins. |

## 1.2 Impact

| Level | Definition |
|---|---|
| I1 Low | Affects one activity or a small number of students and can be corrected within the planned pacing. |
| I2 Medium | Affects one delivery stage, track consistency, or several forms of evidence. |
| I3 High | Damages core competencies, acceptance credibility, course continuity, or constitutional principles. |

## 1.3 Priority

```text
Risk score = Probability × Impact
```

| Score | Priority | Required treatment |
|---:|---|---|
| 1–2 | Low | Record and review periodically. |
| 3–4 | Medium | Define prevention, triggers, and an accountable role. |
| 6–9 | High | Complete major mitigation before delivery and define a clear contingency plan. |

The score is used for ordering and does not replace professional judgment. Any risk involving student safety, fairness, or invalid core acceptance may be escalated to high priority regardless of its numeric score.

---

# 2. Risk Status and Accountability

| Status | Definition |
|---|---|
| Open | Identified but major mitigation is not yet complete. |
| Mitigating | Preventive or reducing measures are being implemented. |
| Watching | Major measures are in place and trigger indicators are monitored. |
| Triggered | The risk has occurred and the contingency response is active. |
| Closed | The risk has disappeared, been accepted, or been converted into another formal decision. |

Accountable roles:

- Course lead: final responsibility for scope, competencies, acceptance, and major adjustments.
- Instructor: classroom pacing, evidence collection, local adaptation, and risk reporting.
- Teaching assistant: observes learning gaps, supports acceptance, and records repeated problems or abnormal patterns.
- Document maintainer: bilingual consistency, navigation, versioning, and correction of material defects.
- Student: provides authentic evidence, discloses AI use, and participates in reassessment.

One person may hold several roles, but every risk must still have one primary accountable role.

---

# 3. High-Priority Risks

| ID | Risk | P | I | Score | Main triggers | Prevention and mitigation | Contingency response | Accountable role | Status |
|---|---|---:|---:|---:|---|---|---|---|---|
| R-01 | Students use AI to obtain complete answers and bypass understanding, tracing, and design | 3 | 3 | 9 | Sudden unexplained jump in code style or capability; inability to explain, modify, or trace submitted code; AI record contains only complete answers | Use staged hints, require pre-AI understanding and tests, requirement modification, micro-oral checks, and AI-review tasks; require at least two forms of evidence for core competencies | Reassess the missing competency through a new tracing, modification, or diagnosis task; lower the maturity judgment rather than replacing learning verification with punishment | Course lead, instructor | Mitigating |
| R-02 | The 10/12-hour preparatory course contains too much content, producing exposure without competency | 3 | 3 | 9 | Activities repeatedly compressed; tracing, testing, or oral checks cancelled; students can only imitate examples | Enforce `06-scope-boundary` and `08-delivery-map`; preserve minimum evidence and first reduce task count and context complexity | Stop adding content; convert extension content to demonstrations; focus on the minimum graduation evidence package and remediation | Course lead, instructor | Mitigating |
| R-03 | Chinese-taught and English-taught tracks develop different core standards because of time, language, or instructor differences | 2 | 3 | 6 | One track adds core topics; the same competency uses different passing standards; English language load is handled by lowering competency expectations | Share competency IDs, maturity levels, acceptance tasks, and minimum evidence; vary only pacing, scaffolding, and practice quantity | Recalibrate with common acceptance tasks; restore missing core evidence in the weaker track; remove unapproved extra core requirements | Course lead, document maintainer | Watching |
| R-04 | The formal course repeats preparatory activities at the same maturity instead of advancing capability | 2 | 3 | 6 | Weeks 1–3 still use the same examples and imitation tasks; new contexts, modifications, or diagnosis are absent | Begin the formal course with defects, requirement changes, comparison, and higher-maturity acceptance; use preparatory evidence as the baseline | Convert repetition into diagnosis or transfer tasks; adjust later weeks to restore higher-maturity activities | Course lead, instructor | Open |
| R-05 | Acceptance degrades into OJ results, output matching, or final-product review, invalidating competency judgments | 3 | 3 | 9 | Rubrics omit explanation, tracing, modification, or diagnosis; many correct programs are submitted by students who cannot explain them | Every SB-C competency requires both understanding-oriented and action-oriented evidence; use `AT-03`, `AT-06`, `AT-07`, and `AT-12` for sampling | Suspend high-maturity judgment; reassess the missing competency; correct rubrics and grading calculations | Course lead, instructor | Mitigating |
| R-06 | Memory and pointers are introduced as symbol manipulation, so students memorize `*`, `&`, allocation, and release steps | 3 | 3 | 9 | Students cannot draw values, locations, addresses, and aliases; they can apply syntax but cannot trace which location changes | Establish value, location, lifetime, call, and sequence models first; use frequent visual representation and tracing | Pause new pointer syntax; return to memory diagrams, alias tracing, and small modifications; reduce context complexity | Instructor | Open |
| R-07 | Advanced data structures are reintroduced as a way to integrate pointers or make the course feel complete | 2 | 3 | 6 | Weekly plans, assignments, or materials contain linked lists, trees, heaps, hashes, or graphs as core deliverables | Require every addition to pass the scope-change rules; keep data organization at sequences, records, indexing, and basic operations | Remove the topic or reduce it to a non-core demonstration; restore compressed testing, debugging, memory, and modification work | Course lead, document maintainer | Watching |
| R-08 | Beginner tool-environment differences consume excessive time and hide programming capability | 3 | 2 | 6 | Installation, encoding, path, terminal, or permission issues consume substantial class time; identical code behaves differently across environments | Provide a prevalidated environment, a minimum environment check, and a fallback path; distinguish tool failures from program failures | Switch to the fallback environment; provide a reproducible case; record environment incidents without treating tool fluency as competency | Instructor, teaching assistant | Open |
| R-09 | Prerequisite differences are too large: weaker students lose tracing ability while stronger students expand into unrelated advanced content | 3 | 2 | 6 | Large completion-time gaps; weaker students only copy; stronger students wait or add unplanned topics | Use a shared core with layered scaffolds; give stronger students harder modification, diagnosis, and transfer tasks rather than advanced topics | Start small-group remediation, extra oral checks, and alternate activities; rebalance practice difficulty while preserving common acceptance | Instructor, teaching assistant | Open |
| R-10 | Bilingual documents, competency IDs, weekly delivery, and acceptance rules become unsynchronized | 2 | 3 | 6 | Chinese and English files differ in content, numbering, links, or status; materials reference missing IDs | Submit official updates in bilingual pairs; update README navigation and cross-links together; run a consistency check before completion | Stop citing conflicting files; repair them using the Constitution and latest official baseline; record downstream effects | Document maintainer | Watching |

---

# 4. Medium-Priority Risks

| ID | Risk | P | I | Score | Trigger | Mitigation and response | Accountable role | Status |
|---|---|---:|---:|---:|---|---|---|---|
| R-11 | A three-hour session causes cognitive fatigue and lowers evidence quality near the end | 2 | 2 | 4 | Tracing and explanation errors rise late in class; activities collapse into instructor demonstrations | Change activity mode every 45–60 minutes, schedule short breaks, and avoid placing all important acceptance at the end | Instructor | Open |
| R-12 | English-medium delivery causes language load to be mistaken for programming weakness | 2 | 2 | 4 | Students can draw or implement but cannot answer quickly; technical terms are confused | Provide bilingual vocabulary, visual models, response frames, and shorter explanation tasks; assess core concepts rather than accent | Instructor, teaching assistant | Open |
| R-13 | Teaching assistants interpret maturity levels and AI boundaries differently, causing inconsistent acceptance | 2 | 2 | 4 | The same performance receives different judgments; AI rules are applied inconsistently | Calibrate with examples, shared rubrics, sample moderation, and an escalation path for disputes | Course lead, teaching assistant | Open |
| R-14 | Students fear admitting AI use, leading to inaccurate records and hidden use | 2 | 2 | 4 | AI-like output is evident but denied; records are empty or unnaturally identical | Explain that transparent use is acceptable and that the assessment focuses on understanding and verification rather than use itself | Instructor | Open |
| R-15 | Testing and debugging are postponed until late in the course and fail to become cross-cutting capabilities | 2 | 2 | 4 | Early assignments contain only sample output; students still cannot define expected results later | Preserve at least one test or defect activity in every unit and review each delivery stage | Instructor, document maintainer | Watching |
| R-16 | One large integrated project hides local competency gaps | 2 | 2 | 4 | Team members or AI complete most functionality; individual capability cannot be judged | Use distributed evidence, individual modification, oral checks, tracing, and diagnosis; treat the project as only one integration artifact | Instructor | Open |
| R-17 | Requirements, scope, or delivery change but materials and assessments do not update | 2 | 2 | 4 | Assignments still assess removed competencies; new competencies lack activities or evidence | Build a traceability matrix and identify affected files, materials, and assessments for every change | Course lead, document maintainer | Open |
| R-18 | Students can operate only one IDE and cannot distinguish tool, build, and program problems | 2 | 2 | 4 | A different environment prevents setup or diagnosis; every failure is described as “it does not run” | Include at least one visible build process and require classification of compile, link, and runtime problems | Instructor | Open |

---

# 5. Monitoring Indicators

At minimum, review these indicators after each delivery stage in every track:

| Indicator | Risks it may indicate |
|---|---|
| Proportion of students who pass code tests but cannot explain or trace | R-01, R-05, R-06 |
| Number of tracing, testing, or oral-check activities cancelled or shortened | R-02, R-05, R-15 |
| Differences in core tasks or passing rates between Chinese and English tracks | R-03, R-10, R-12 |
| Proportion of repeated activities between preparatory and formal courses | R-04 |
| Class time consumed by tool problems | R-08, R-18 |
| Competency IDs that dominate reassessment requests | R-02, R-06, R-09 |
| Proportion of AI suggestions adopted without verification | R-01, R-14 |
| Broken links, stale IDs, or bilingual inconsistencies in official files | R-10, R-17 |
| Number of topics added without scope review | R-07, R-17 |

Indicators are used to detect system problems and must not be used to publicly label or shame individual students.

---

# 6. Risk Treatment Strategies

| Strategy | Appropriate use |
|---|---|
| Avoid | Remove designs that directly violate scope or the Constitution, such as making advanced data structures core content. |
| Reduce | Lower probability or impact through scaffolding, practice, environment standardization, and complementary evidence. |
| Transfer | Move non-core technical support to teaching assistants, documentation, or fallback environments. |
| Accept | Accept low-cost risks that cannot be fully removed when monitoring and response are already defined. |

Unacceptable treatment strategies:

- Cancelling testing, tracing, debugging, or oral checks to preserve pacing.
- Replacing better evidence with more exercises.
- Replacing AI literacy and verification design with a total AI ban.
- Lowering English-track core standards to address language load.
- Adding advanced topics to occupy faster students.

---

# 7. Risk Review Cadence

## Before delivery

- Verify environment, materials, bilingual pairs, and navigation.
- Calibrate instructor and teaching-assistant maturity judgments with examples.
- Confirm that every core competency has complementary evidence.
- Check for unnecessary repetition between preparatory and formal courses.

## After every delivery stage

- Review triggers and monitoring indicators.
- Update risk status, measures, and residual risk.
- Adjust pacing and scaffolding only; do not expand scope without review.

## After the course

- Compare expected and actual risks.
- Record which measures worked and which created new problems.
- Feed major findings back into requirements, scope, acceptance, and delivery documents.

---

# 8. Completion Criteria

After this risk register is established, later design work must be able to:

- Link every major risk to requirements, competencies, scope, acceptance, or delivery decisions.
- Identify observable triggers rather than listing only abstract concerns.
- Assign preventive measures, contingency responses, and an accountable role.
- Address time, language, tool, and AI pressure without lowering core standards.
- Supply risk IDs to the next document, the [Traceability Matrix](10-traceability-matrix.en.md).

## Navigation

- [Previous: Course Delivery Map](08-delivery-map.en.md)
- [Back to Instructional Design Workspace](README.en.md)
- [繁體中文版](09-risk-register.zh-TW.md)
- [Next: Traceability Matrix](10-traceability-matrix.en.md)
