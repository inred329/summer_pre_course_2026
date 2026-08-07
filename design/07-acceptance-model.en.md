# Competency Acceptance Model

Version: 0.2.1  
Status: Revisable planning and traceability model  
Governance note: This document maps competencies to observable evidence patterns; it does not define grading, homework, attendance, AI, or final-exam policy. The [Learning and Assessment Policy](13-learning-assessment-policy.en.md) is authoritative for those rules.  
Corresponding Chinese version: [能力驗收模型](07-acceptance-model.zh-TW.md)

## Document Purpose

This document maps competency maturity to observable evidence patterns that may support learning activities, classroom observation, and final-assessment design.

It answers:

1. What kinds of evidence can distinguish recognition, explanation, tracing, implementation, diagnosis, and transfer?
2. What task forms can generate that evidence without reducing capability to one output or score?
3. How can competency IDs remain traceable into later delivery and assessment implementation?

This document does not create an assessment policy. Current rules for homework, participation, attendance, grade structure, the final one-to-one oral examination, and permitted AI/tool use come only from the official learning and assessment policy and any later approved bilingual exam procedure.

## 1. Acceptance Principles

- Correct output, successful translation/build, passing an OJ, a complete program, or tool approval alone cannot establish capability.
- Higher maturity should be supported by evidence that samples prerequisite understanding as well as action.
- Both language tracks use the same competency IDs, maturity meanings, and substantive acceptance expectations.
- Evidence tasks must remain within the approved scope boundary and established prerequisites.
- AI and other external tools are optional by default. No acceptance task may require AI use or a non-use declaration unless an explicitly approved activity makes external-tool judgment itself the learning objective.
- When a learner actually adopts external assistance, relevant acceptance evidence may examine whether the adopted result was understood, modified when needed, and technically verified.

## 2. Minimum Evidence Patterns by Maturity

| Level | Candidate task | Main evidence | Acceptance pattern |
|---|---|---|---|
| L1 Recognize | Identify a concept, state, boundary, or diagnostic category in code or a visual | EV-EX / EV-VI | Correctly identifies the item without confusing a nearby concept |
| L2 Explain | Explain purpose, reason, assumption, and limitation in the student's own words | EV-EX + EV-CO / EV-VI | Gives a causal explanation and handles a reasonable follow-up |
| L3 Trace | Predict relevant state and flow for a given case | EV-TR + EV-EX / EV-VI | Steps are consistent with the stated program and technical contract, including termination or lifetime transitions when relevant |
| L4 Implement | Complete or modify a small scoped program | EV-IM + EV-TE / EV-MO / EV-EX | Meets the requirement, handles stated boundaries, and explains design and testing |
| L5 Diagnose | Reproduce, narrow, hypothesize, correct, and regress | EV-DE + EV-TE + EV-EX | Uses evidence, identifies the cause, and verifies that the correction preserves required behavior |
| L6 Transfer | Apply the capability in a new context | EV-RE + EV-MO / EV-CO / EV-IM | Explains invariant principles, changed assumptions, and new risks |

These are evidence patterns rather than fixed scoring rubrics. A specific assessment may sample them differently as long as it remains consistent with the official policy and competency standard.

## 3. Candidate Task Forms

`AT-01` through `AT-12` are reusable task-form identifiers for materials, discussion, and assessment planning. They are not automatically required tasks, submission items, or grading components.

| Task ID | Task form | Main capability | Tool boundary |
|---|---|---|---|
| AT-01 | Concept recognition and classification | L1–L2 | The learner must still provide their own classification and explanation |
| AT-02 | Own explanation and follow-up | L2 | External references may support preparation but may not replace the learner's explanation |
| AT-03 | Paper/table/code tracing | L3 | The learner provides the trace; a tool-generated trace is not evidence of the learner's capability |
| AT-04 | Visual-model reconstruction | L2–L3 | The learner must be able to reconstruct and explain the model used as evidence |
| AT-05 | Minimal implementation | L4 | References may be used as permitted; the learner explains the implementation and tests |
| AT-06 | Requirement modification | L4–L6 | The learner performs and explains the relevant modification |
| AT-07 | Defect diagnosis | L3–L5 | External hypotheses may be considered when permitted, but the learner verifies the cause |
| AT-08 | Test design | L3–L5 | The learner must justify selected cases and expected results |
| AT-09 | Solution comparison and trade-off | L2–L6 | The learner performs the comparison and decision |
| AT-10 | Transfer to a new context | L6 | The learner must adapt reasoning rather than merely reproduce a complete prior answer |
| AT-11 | Conditional external-assistance review | PC-A, PC-V | Used only when external assistance was actually used or the activity explicitly targets tool judgment; adopted claims require reproducible verification |
| AT-12 | Final one-to-one oral-exam question form | Integrated sample | Any live-tool boundary is set by the approved exam procedure, not by this planning model |

## 4. Relationship to Homework and Classroom Participation

Homework, participation, attendance, and learning-record rules are defined by `design/13-learning-assessment-policy.*` and must not be duplicated here as independent requirements.

For traceability purposes, suitable evidence may arise from:

- a learner's own programs, tests, traces, errors, and revisions;
- classroom tracing, testing, debugging, comparison, or explanation;
- written, oral, code-based, diagram-based, anonymous, individual, or group participation modes permitted by policy;
- later modification or explanation of previously encountered work.

This model does not require students to submit homework, preserve AI logs, or produce a particular participation artifact.

## 5. Final One-to-One Oral Examination Traceability

The official policy establishes one final one-to-one oral examination as the summative capability assessment. This planning model does not set its duration, question count, resource rules, scoring percentages, or exact procedure.

A balanced oral-exam design should be able to sample core capability evidence such as:

1. Reading and explanation.
2. Execution/state tracing.
3. Requirement modification.
4. Test design and verification.
5. Defect diagnosis.
6. Function/responsibility decomposition or modular reasoning.

If the student actually used AI or another external assistant in work selected for discussion, the examiner may additionally ask the student to explain and verify the adopted result in accordance with the official policy. Students who did not use AI do not need an AI-specific question to prove programming capability.

## 6. Grade and Procedure Boundary

This document intentionally does not repeat grade percentages, attendance rules, homework rules, or final-exam resource boundaries.

Authoritative sources:

- Current learning and assessment policy: `design/13-learning-assessment-policy.en.md`.
- Any later approved bilingual final-oral-examination procedure, once created.

If this model and an authoritative policy differ, the authoritative policy prevails and this model must be updated.

## 7. Conditional External-Assistance Evidence

When AI or another external assistant was actually used and its use is relevant to an activity or assessment, evidence may examine whether the learner can:

- identify the adopted suggestion or affected part;
- explain assumptions and limitations;
- verify technical claims through programs, tests, compiler diagnostics, reliable references, tracing, or other reproducible evidence;
- modify the result when requirements change;
- explain why the suggestion was accepted, modified, or rejected.

This section does not require fixed prompts, complete conversation logs, before/after artifacts, standardized AI summaries, or non-use declarations. Records or attribution are required only when a specific approved activity, academic-integrity rule, or assessment condition calls for them.

## 8. Fairness and Evidence Accessibility

- Do not reject a reasonable solution merely because it differs from an example.
- Language fluency must not replace technical capability in judgment.
- Equivalent evidence modes should be available when a device, tool, or environment fails and the learning objective does not depend on that exact tool.
- Evidence design should support multiple communication modes rather than reward speaking speed or extroversion.
- Accommodations and exceptions must remain consistent with institutional requirements and the official assessment policy.

## 9. Maintenance Rules

When changing this model:

1. Keep both language versions substantively equivalent.
2. Preserve competency IDs or document deliberate migrations.
3. Check consistency with the competency map, scope boundary, official assessment policy, rubric/material implementations, and any approved oral-exam procedure.
4. Do not introduce new policy through an acceptance-task table.
5. Record material findings in the active repository audit.

## Related Documents

- [Programming Competency Map](05-competency-map.en.md)
- [Course Scope Boundary](06-scope-boundary.en.md)
- [Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Course Delivery Map](08-delivery-map.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](07-acceptance-model.zh-TW.md)
