# Course Delivery Map

Version: 0.2.1  
Status: Revisable planning model  
Governance note: This document plans pacing and activity placement. The [Learning and Assessment Policy](13-learning-assessment-policy.en.md) is authoritative for homework, participation, attendance, grade structure, the final oral examination, and AI/tool rules.  
Corresponding Chinese version: [課程交付地圖](08-delivery-map.zh-TW.md)

## Document Purpose

This document plans three connected delivery paths: Chinese preparatory 4 × 3 hours, English preparatory 5 × 2 hours, and the connected formal C course.

A typical class cycle is:

```text
Discuss previous practice when applicable
→ Core question and mental model
→ Prediction or tracing
→ Minimal implementation / reasoning
→ Testing, debugging, and requirement modification
→ Independent follow-up practice
```

The official assessment policy determines whether practice is submitted or graded, how participation is observed, and how the final oral examination functions. This delivery map implements that policy; it does not redefine it.

## 1. Shared Delivery Principles

- Both preparatory language tracks deliver the same core capabilities and technical depth, while pacing and language support may differ.
- The Chinese track's additional time supports more tracing, discussion, remediation, and diagnosis rather than extra core requirements.
- Each class should provide multiple participation modes consistent with the official policy.
- Practice discussion should prioritize authentic errors, alternative solutions, boundary cases, and testing blind spots rather than replacing reasoning with one model answer.
- Every unit should include opportunities to predict, observe, diagnose, correct, modify, and verify.
- AI and other external tools are optional by default. Optional-tool activities must be directly skippable without reducing core completion or participation evidence.

## 2. Shared Preparatory Capability Baseline

By the end of either preparatory track, students should be able to:

- Explain, at an appropriate conceptual level, how C source text is translated/built and then executed in the specified environment.
- Trace basic data/state, conditions, and loop behavior.
- Complete and explain a small input–process–output program.
- Explain function responsibility and perform simple decomposition.
- Create expected results plus normal, boundary, and relevant invalid/failure cases.
- Reproduce, diagnose, correct, and retest at least one defect.
- Modify a small requirement and explain what changed.

If a student chooses to use AI or another external assistant, the student remains responsible for understanding and verifying any adopted result. Tool use itself is not part of this shared baseline.

## 3. Chinese Preparatory Track: Four Three-Hour Sessions

### Session 1: How a Program Begins to Run

- Entry: introduce course navigation, environment, and current learning/assessment policy.
- Core: conceptual translation/build responsibilities, the specified toolchain, minimal program, prediction, and basic diagnostic interpretation.
- Follow-up practice: From Source Code to Execution.

### Session 2: Data, Types, and Program State

- Discuss representative issues from previous practice when available.
- Core: values, objects/variables, types, expressions, input/output, state tracing, and input assumptions.
- Follow-up practice: Data and State Tracing.

### Session 3: Conditions, Loops, and Reliable Termination

- Discuss representative issues from previous practice.
- Core: conditions, loop state, termination, boundaries, off-by-one defects, and non-termination diagnosis.
- Follow-up practice: Conditions and Loops.

### Session 4: Functions and Integrated Verification

- Discuss representative issues from previous practice.
- Core: function responsibility, decomposition, requirement change, testing, debugging, and regression verification.
- Follow-up practice: Function/integration practice and a small integrated development cycle.
- Optional extension: review an AI or other external suggestion and verify any adopted claim with reproducible evidence. Students who skip this extension complete the same core session.

## 4. English Preparatory Track: Five Two-Hour Sessions

### Session 1: Execution and First Program

- Introduce course navigation, environment, and current learning/assessment policy.
- Core: conceptual translation/build responsibilities, the specified toolchain, minimal program, prediction, and basic diagnostics.
- Follow-up practice: Execution and first-program work.

### Session 2: Data, Types, and Program State

- Discuss representative issues from previous practice.
- Core: values, objects/variables, types, expressions, input/output, and state tracing.
- Follow-up practice: Data and state.

### Session 3: Conditions and Repetition

- Discuss representative issues from previous practice.
- Core: conditions, loop state, termination, boundaries, and defect diagnosis.
- Follow-up practice: Conditions and loops.

### Session 4: Functions and Decomposition

- Discuss representative issues from previous practice.
- Core: function responsibility, interfaces, calls, decomposition, and small caller-side tests.
- Follow-up practice: Functions and decomposition.

### Session 5: Integrated Development Cycle

- Discuss representative issues from previous practice.
- Core: requirement change, integrated reasoning, testing, debugging, regression verification, and reflection.
- Follow-up practice: integrated development-cycle work.
- Optional extension: review an AI or other external suggestion and verify any adopted claim. Skipping the extension does not affect core completion.

## 5. Practice-Discussion Flow

A useful implementation pattern is:

```text
Learners surface questions, defects, or anonymous blockers
→ Instructor selects representative cases
→ Class predicts or traces before correction
→ Compare tests, solutions, or diagnostics
→ Learners revise reasoning
→ Instructor connects the evidence to the new concept
```

The official policy currently recommends dedicated discussion time; the precise minutes belong to that policy and instructor implementation, not to the normative scope of this planning model.

## 6. Classroom Participation Delivery

Instructors or TAs may keep lightweight evidence notes compatible with the official policy, for example:

- raised a specific question or blocker;
- participated in tracing, testing, debugging, or comparison;
- shared an error, test, correction, or alternative solution;
- revised an earlier explanation;
- contributed through writing, diagrams, code operation, anonymous input, or group work.

This map does not convert attendance, speaking speed, or a particular artifact into a grading rule.

## 7. Connected Formal Course

The connected formal course may retain the same learning cycle while raising maturity toward implementation, diagnosis, transfer, modular reasoning, memory/lifetime responsibility, and stronger testing.

The formal-course delivery plan must remain consistent with the same official learning and assessment policy unless that authoritative policy is deliberately amended through the repository's governance process. This delivery map must not create a separate conflicting assessment regime.

## 8. Final-Oral-Examination Handoff

The official learning and assessment policy establishes the role of the final one-to-one oral examination. Delivery materials should prepare students to explain, trace, modify, test, diagnose, and justify their own work.

This planning model does not independently set the examination date, duration, question count, permitted resources, make-up procedure, or scoring method. Those details belong in an approved bilingual examination procedure when created.

## Maintenance Rules

When changing this delivery map:

1. Preserve substantive equivalence between language tracks and language versions.
2. Check the competency map and scope boundary before adding core content.
3. Check the official assessment policy before changing homework, participation, attendance, oral-exam, or tool-use statements.
4. Keep optional AI/tool activities explicitly conditional and directly skippable.
5. Verify concrete compiler/toolchain claims against the specified environment.
6. Record material governance findings in the active repository audit.

## Related Documents

- [Competency Acceptance Model](07-acceptance-model.en.md)
- [Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Course Scope Boundary](06-scope-boundary.en.md)
- [Materials Index](../materials/README.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](08-delivery-map.zh-TW.md)
