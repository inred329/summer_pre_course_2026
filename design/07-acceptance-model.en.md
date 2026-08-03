# Competency Acceptance Model

Version: 0.1.0  
Status: Architecture draft  
Corresponding Chinese version: [能力驗收模型](07-acceptance-model.zh-TW.md)

## Document Purpose

This document converts the [Programming Competency Map](05-competency-map.en.md) and [Course Scope Boundary](06-scope-boundary.en.md) into executable acceptance rules.

It answers:

1. What minimum evidence is required at each maturity level?
2. Which task forms are suitable for accepting understanding, tracing, implementation, diagnosis, and transfer?
3. How do we avoid treating correct output alone as proof of learning?
4. Where may AI participate, and which core evidence must be produced by the student?
5. How can the preparatory and formal courses use the same standards while targeting different maturity levels?

This document is not an item-level grading rubric and does not assign weeks. Later assignments, activities, examinations, and oral checks must derive concrete rubrics from this model.

## Constitutional Compliance

- Correct output is one form of evidence, not sufficient proof of capability.
- Every core capability requires at least two complementary forms of evidence.
- Acceptance tasks must be observable, repeatable, and explainable.
- Chinese-taught and English-taught classes use the same capability IDs, maturity levels, and passing standards.
- AI may not replace the student's initial understanding, key tracing, core judgment, or final explanation.
- Acceptance content may not exceed the scope boundary or introduce advanced data structures indirectly.

---

# 1. Acceptance Unit

Every assessable item consists of five elements:

```text
Capability ID + target maturity + task context + required evidence + passing criteria
```

Example:

```text
PC-C04 + L3 + trace one loop + EV-TR/EV-EX + fully explain initialization, condition, update, and termination
```

Acceptance criteria must not be written only as “can use loops” or “complete the program.”

---

# 2. Minimum Acceptance Rules by Maturity

| Level | Minimum task requirement | Minimum required evidence | Passing criteria | Insufficient performance |
|---|---|---|---|---|
| L1 Recognize | Identify the target concept in an example, error message, diagram, or program | EV-EX or EV-VI | Correctly identifies it without confusing nearby concepts | Guesses the name but cannot identify its location or role |
| L2 Explain | Explain the reason, role, and limitation of the concept in one's own words | EV-EX plus either EV-CO or EV-VI | Gives a causal explanation and answers at least one follow-up question | Recites a definition or copies AI or course text |
| L3 Trace | Predict state, control, function, or memory changes step by step for a given input | EV-TR plus either EV-EX or EV-VI | Every step matches execution and key transitions and termination are identified | Gives only final output or copies observed execution afterward |
| L4 Implement | Independently create or modify a program for a small requirement | EV-IM plus at least one of EV-TE, EV-EX, or EV-MO | Runs, satisfies the requirement, and the main design and tests can be explained | Passes only sample cases or cannot modify or explain the program |
| L5 Diagnose | Reproduce a defect, locate it, form a hypothesis, repair it, and perform regression checks | EV-DE, EV-TE, and EV-EX | Diagnosis is evidence-based, repair matches the cause, and existing behavior remains valid | Guess-and-edit behavior or simply accepts an AI repair |
| L6 Transfer | Apply the capability to an unseen requirement, representation, or language context | EV-RE plus at least one of EV-MO, EV-CO, or EV-IM | Identifies the invariant principle, required adaptation, and new risks | Reuses the original template with superficial changes |

## Cumulative Principle

Maturity levels are not six fully independent certificates. Higher-level acceptance must still sample necessary lower-level understanding:

- L4 must include explanation of core program behavior.
- L5 must include tracing of the key path that causes the defect.
- L6 must explain which principles remain unchanged and which implementation choices change.

---

# 3. Evidence Combination Rules

## 3.1 Minimum Combination for Core Capabilities

Every capability classified as `SB-C` requires at least:

1. One understanding-oriented artifact: `EV-EX`, `EV-VI`, `EV-TR`, or `EV-CO`.
2. One action-oriented artifact: `EV-IM`, `EV-MO`, `EV-TE`, or `EV-DE`.

Only targets at L1 or L2 may temporarily rely on understanding-oriented evidence alone.

## 3.2 Evidence That Cannot Stand Alone

The following cannot independently prove capability:

- All automated tests pass.
- The program compiles successfully.
- Complete source code is submitted.
- AI rates the answer positively.
- The student says, “I understand.”
- Output matches the sample.

## 3.3 Evidence Consistency

Conflicting evidence cannot be hidden by averaging scores.

For example, if the program is correct but the trace contradicts actual execution, understanding has not been established. The instructor should lower the maturity judgment or require supplemental acceptance.

---

# 4. Standard Acceptance Task Forms

| Task code | Task form | Main maturity accepted | AI boundary |
|---|---|---|---|
| AT-01 | Concept recognition and classification | L1–L2 | AI may be used for comparison after answering, not before classification |
| AT-02 | Independent explanation with follow-up | L2 | AI logs may be retained, but the student answers independently first |
| AT-03 | Paper or table-based tracing | L3 | AI may not perform the step-by-step trace during acceptance |
| AT-04 | Reconstruct a visual model | L2–L3 | AI may check the diagram but may not create the student's first version |
| AT-05 | Minimum implementation | L4 | Documentation may be consulted; AI rules depend on the activity, but every section must be explainable |
| AT-06 | Requirement modification | L4–L6 | AI may offer a risk list but may not deliver the finished modification |
| AT-07 | Defect diagnosis | L3–L5 | AI may propose candidate hypotheses; the student verifies and eliminates them |
| AT-08 | Test design | L3–L5 | AI may supplement missed cases only after the student submits an initial set |
| AT-09 | Compare solutions and trade-offs | L2–L6 | AI may generate candidates; the student performs comparison and decision-making |
| AT-10 | Transfer to a new context | L6 | References may be consulted, but the original complete solution may not simply be reused |
| AT-11 | Review an AI suggestion | PC-A and PC-V | The task requires verification of AI; accepting AI is not itself a passing condition |
| AT-12 | Micro oral check | Samples every level | AI may not provide live answers |

---

# 5. Preparatory-Course Acceptance Model

The preparatory course mainly accepts L2–L4, but not every capability must reach implementation.

## 5.1 Minimum Completion Evidence Package

Every student should complete at least:

1. One explanation of a small program's execution process: `PC-E`, `EV-EX + EV-VI`.
2. One condition or loop trace: `PC-C`, `EV-TR + EV-EX`.
3. One simple requirement modification: `PC-D/PC-C`, `EV-MO + EV-TE`.
4. One error classification and initial debugging task: `PC-E/PC-V`, `EV-DE + EV-EX`.
5. One AI-suggestion verification record: `PC-A`, `EV-AI + EV-TE`.

## 5.2 Passing Methods That Must Not Be Used

- One final project as the only evidence.
- Online-judge passing counts alone.
- Multiple-choice questions as the sole assessment of tracing.
- Attendance as a substitute for understanding evidence.
- Awarding L4 because AI generated a complete program.

---

# 6. Formal-Course Acceptance Model

The formal course should accumulate L4–L6 evidence progressively.

Each major competency group requires at least:

- One independent or resource-constrained implementation.
- One requirement modification.
- One testing or debugging task.
- One explanation, comparison, or oral sampling task.

Final acceptance of integrated capability `PC-I` should contain:

```text
Requirement understanding
→ data and control design
→ implementation
→ testing
→ defect repair
→ requirement change
→ regression verification
→ explanation and reflection
```

Even when the final product is functionally complete, inability to explain, modify, or diagnose it prevents an L5 or L6 judgment.

---

# 7. AI Acceptance Rules

## 7.1 Student Responsibilities That Must Be Preserved

The student must personally produce:

- A problem interpretation or initial approach before using AI.
- At least one independently created expected result or test.
- Technical verification of AI suggestions.
- Reasons for accepting, modifying, or rejecting suggestions.
- An explanation of the final program's core behavior.

## 7.2 Minimum AI-Use Record

| Field | Required content |
|---|---|
| Goal | What assistance was requested from AI |
| Current state | What was understood, attempted, and where the difficulty occurred |
| AI suggestion | A summary rather than a full transcript dump |
| Verification method | Documentation, compilation, execution, testing, or tracing |
| Decision | Accept, modify, or reject |
| Reason | Evidence-based justification |

A complete pasted conversation cannot replace this synthesis and judgment.

## 7.3 AI-Related Failure Conditions

- Cannot identify which parts came from AI.
- Cannot explain AI-generated core code.
- Claims correctness without independent testing.
- Uses “AI said so” as the only reason.
- Directly adopts a suggestion that conflicts with the course scope.

---

# 8. Pass, Conditional Pass, Supplemental Acceptance, and Fail

| Judgment | Condition |
|---|---|
| Pass | All required evidence reaches the target maturity and is mutually consistent |
| Conditional pass | Core behavior is established, but one minor evidence item can be supplemented |
| Supplemental acceptance | Evidence is insufficient, contradictory, or cannot be attributed to the student |
| Fail | Core capability is absent or completion depends on an external full answer |

Supplemental acceptance should target the missing capability rather than repeat all work. For example, when the program is correct but tracing is absent, the student may trace a new input live and answer follow-up questions.

---

# 9. Acceptance Design Checklist

Before publishing any formal activity or assessment, confirm:

1. Which capability IDs are referenced?
2. What is the target maturity?
3. Does it comply with `06-scope-boundary`?
4. Are there at least two complementary forms of evidence?
5. Can it distinguish understanding from accidental correctness?
6. Does it include normal, boundary, or failure cases?
7. Are AI-use rules explicit?
8. Can it be delivered with substantive equivalence in both language tracks?
9. Can instructors or teaching assistants make consistent judgments from the criteria?
10. Are the relevant rules reachable from the root README?

---

# 10. Completion Criteria and Next Document

After this document is established, later design work must be able to:

- Convert each capability into concrete activities and rubrics.
- Distinguish formative checks from summative acceptance.
- Build evidence accumulation for the preparatory and formal courses.
- Link requirements, domain concepts, knowledge dependencies, competencies, scope, acceptance, materials, and assessments in the traceability matrix.

The next document is `08-delivery-map.*`, which will arrange shared capabilities and acceptance evidence into different delivery pacing for the Chinese preparatory class, English preparatory class, and formal course.

## Navigation

- [Previous: Course Scope Boundary](06-scope-boundary.en.md)
- [Back to Instructional Design Workspace](README.en.md)
- [繁體中文版](07-acceptance-model.zh-TW.md)
