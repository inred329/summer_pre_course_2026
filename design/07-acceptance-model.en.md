# Competency Acceptance Model

Version: 0.2.0  
Status: Official assessment baseline  
Last updated: 2026-08-03  
Major change summary: Changed to unsubmitted, ungraded homework; formative classroom participation; and one final one-on-one oral examination as the only summative assessment.  
Corresponding Chinese version: [能力驗收模型](07-acceptance-model.zh-TW.md)

## Document Purpose

This document converts competency maturity into observable acceptance rules and aligns with the [Learning and Assessment Policy](13-learning-assessment-policy.en.md).

The official course grade has only two components:

1. Classroom participation: continuous formative observation.
2. One final one-on-one oral examination: the only summative capability verification.

Homework is required practice, but it is not submitted or graded individually. Students keep their own programs, tests, traces, error records, and AI-use notes for classroom discussion and final oral-exam preparation.

## 1. Acceptance Principles

- Correct output, successful compilation, passing OJ, or complete source code alone cannot establish capability.
- Core capability requires both understanding-oriented and action-oriented evidence.
- Attendance, roll call, or speaking frequency alone cannot represent participation.
- Both language tracks use the same competency IDs, maturity targets, and grading standards.
- AI may not replace initial understanding, key tracing, core judgment, or final explanation.
- Acceptance may not exceed the scope boundary or introduce untaught advanced data structures.

## 2. Minimum Maturity Rules

| Level | Minimum task | Main evidence | Passing criterion |
|---|---|---|---|
| L1 Recognize | Identify a concept in code, an error, or a visual | EV-EX / EV-VI | Correctly identifies it without confusing nearby concepts |
| L2 Explain | Explain purpose, reason, and limitation in the student's own words | EV-EX + EV-CO / EV-VI | Gives a causal explanation and answers a follow-up |
| L3 Trace | Predict state and flow step by step for a given input | EV-TR + EV-EX / EV-VI | Every step matches program behavior and identifies transitions and termination |
| L4 Implement | Complete or modify a small program | EV-IM + EV-TE / EV-MO / EV-EX | Meets the requirement and explains design and testing |
| L5 Diagnose | Reproduce, locate, hypothesize, correct, and regress | EV-DE + EV-TE + EV-EX | Uses evidence and preserves prior behavior |
| L6 Transfer | Apply capability in a new context | EV-RE + EV-MO / EV-CO / EV-IM | Explains invariant principles, changed parts, and new risks |

Higher-level acceptance still samples prerequisite understanding: L4 must explain, L5 must trace the defect path, and L6 must explain the transfer principle.

## 3. Standard Task Forms

`AT-01` through `AT-11` may support practice, classroom discussion, and final-exam question generation. `AT-12` is redefined as the final one-on-one oral examination and no longer means a micro-oral check after each assignment.

| Task ID | Task form | Main capability | AI boundary |
|---|---|---|---|
| AT-01 | Concept recognition and classification | L1–L2 | Compare after answering; do not obtain the answer first |
| AT-02 | Own explanation and follow-up | L2 | Student answers independently first |
| AT-03 | Paper or table tracing | L3 | AI may not calculate the trace step by step |
| AT-04 | Visual-model reconstruction | L2–L3 | AI may review, not create the first version |
| AT-05 | Minimal implementation | L4 | Documentation is allowed; student explains each section |
| AT-06 | Requirement modification | L4–L6 | Student performs the core modification |
| AT-07 | Defect diagnosis | L3–L5 | AI may suggest hypotheses; student verifies them |
| AT-08 | Test design | L3–L5 | AI may add cases only after the student's first set |
| AT-09 | Solution comparison and trade-off | L2–L6 | Student compares and decides |
| AT-10 | Transfer to a new context | L6 | Do not reuse a complete prior answer |
| AT-11 | AI suggestion review | PC-A, PC-V | Verify with tests or tracing |
| AT-12 | Final one-on-one oral examination | Integrated sample | AI may not answer live |

## 4. Homework and Classroom Participation

### 4.1 Homework

- Homework is assigned after each class.
- It is not submitted, graded, or individually marked.
- Students keep their own programs, tests, traces, error notes, and AI-use records.
- The next class reserves 15–25 minutes to discuss the previous homework.
- Homework may become the context or modification material for the final oral examination.

### 4.2 Classroom Participation

Participation is not attendance or speaking frequency. Valid evidence includes:

- Asking a specific question or describing a blocker.
- Answering, extending, or correcting a technical explanation.
- Joining peer tracing, testing, debugging, or comparison.
- Sharing an error, a test case, or an alternative solution.
- Participating through writing, anonymous questions, diagrams, program operation, or group records.

Instructors should judge sustained, meaningful engagement rather than reward fast speaking or penalize introverted communication.

## 5. Final One-on-One Oral Examination

The final oral examination is the only summative assessment. Its detailed content and procedure will be designed later, but it must collectively verify:

1. Reading and explanation.
2. Execution tracing.
3. Requirement modification.
4. Test design and verification.
5. Defect diagnosis.
6. Function or responsibility decomposition.
7. AI suggestion judgment and verification.

Students may bring their saved homework and learning records as references, but references or AI may not replace live reasoning and explanation.

## 6. Grade Structure

The official course announcement may choose within these ranges:

- Classroom participation: 20–30%.
- Final one-on-one oral examination: 70–80%.

Roll call, number of submitted assignments, OJ count, or screenshots of completion may not become a third major grade source.

## 7. AI Acceptance

Students should retain their pre-AI understanding, self-created expected results or tests, a summary of the AI suggestion, the verification method, and the reason for accepting, modifying, or rejecting it.

The following do not establish AI literacy:

- Saying only that AI approved the answer.
- Being unable to identify AI-influenced parts.
- Being unable to explain or modify AI-generated core code.
- Claiming correctness without independent testing.

## 8. Fairness and Exceptions

- Do not deduct marks solely because a reasonable solution differs from the example.
- The English track may use terminology cards, sentence scaffolds, and extra reading time.
- Language fluency affects judgment only when it prevents technical understanding.
- Tool or device failure uses a fallback environment or equivalent tracing, testing, and explanation task.
- Reasonable absence does not directly lose roll-call points; students still demonstrate capability through later participation and the final oral examination.

## 9. Next Work

Question types, duration, selection method, resource boundaries, make-up arrangements, and inter-rater consistency for the final oral examination will be defined in a separate bilingual official document.

## Navigation

- [Learning and Assessment Policy](13-learning-assessment-policy.en.md)
- [Course Delivery Map](08-delivery-map.en.md)
- [繁體中文版](07-acceptance-model.zh-TW.md)
