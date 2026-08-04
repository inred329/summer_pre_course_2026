# P-U01 Student Material Constitution Review

Version: 1.0.0  
Status: Official review record  
Last updated: 2026-08-04  
Reviewed files: `materials/preparatory/unit-01-execution.en.md` and its Chinese counterpart  
Corresponding Chinese version: [P-U01 學生教材憲法遵循審查](pu01-constitution-review.zh-TW.md)

## Document Purpose

This document records the constitution-compliance review of the full P-U01 student-material trial, the gaps corrected during review, and the writing rules that should carry forward to the remaining 15 Units.

This is a maintenance and review record. It is not student teaching material and adds no assessment requirement.

## Review Conclusion

After the corrections described below, no constitution-level blocker was found in the bilingual P-U01 student materials. The chapter may continue to serve as the trial baseline for expanding later Units.

Overall decision: **Compliant, with two completed corrections.**

## 1. Compliant Areas

### 1.1 Bilingual Completion and Substantive Equivalence

- Chinese and English were updated in the same work unit.
- Chapter sequence, objectives, code, commands, output, error cases, test table, practice, and AI activity are equivalent.
- Both versions link to one another.

Related constitution articles: 5, 6, 7, and 8.

### 1.2 Independent Readability

The material provides:

- beginner prerequisites
- GCC/Clang and Windows/Unix-like commands
- a complete minimal program
- expected output
- compilation and execution steps
- common errors and correction procedures
- guided and independent practice
- self-check and chapter summary

The chapter does not rely on oral background known only to the instructor.

Related constitution articles: 9, 10, 12, and 14.

### 1.3 Problem and Concept Before Syntax

The chapter begins with the question of how program text becomes an execution result and first establishes this model:

```text
Source code
→ Compilation
→ Executable
→ Start
→ Execution
→ Output
```

Only then does it explain the roles of `#include`, `main`, `printf`, and `return 0`. Syntax is presented as part of solving the problem, not as a list to memorize first.

Related constitution articles: 15 and 21.

### 1.4 Prediction, Observation, and Verification

Before revealing results, the chapter asks students to predict:

- whether saving produces output
- whether compilation equals execution
- whether `main` begins when compilation fails
- which version runs after editing without recompiling
- which stage contains a missing-semicolon problem

Students then verify those predictions through compilation, execution, error reproduction, correction, and regression checking.

Related constitution articles: 15, 20, and 23.

### 1.5 Correct Case, Typical Errors, and Reproducible Diagnosis

The chapter includes:

- a correct minimal program
- a missing-semicolon compile error
- an old-executable case after source editing
- a compilable program that does not satisfy the requirement
- correction followed by recompilation and regression checking

Errors are not merely identified. Students classify the stage, read diagnostic evidence, compare versions, correct the defect, and verify again.

Related constitution articles: 15, 16, and 20.

### 1.6 Visual Model Aligned with Text and Code

The Mermaid toolchain diagram matches the prose sequence, compile command, execution command, and error cases. The figure supports the mental model rather than serving as decoration.

Related constitution article: 17.

### 1.7 Controlled Cognitive Load

- One minimal program is reused throughout the chapter.
- Functions, variables, input, conditions, and loops are not introduced prematurely.
- Unfamiliar syntax is explained only to the level currently needed.
- Examples progress from normal execution to compile error, stale executable, and requirement modification.

Related constitution articles: 18, 19, and 22.

### 1.8 Assessment Administration Does Not Dominate the Student Chapter

The revision removed:

- instructor pacing
- competency and risk ID lists
- micro-oral language
- per-task passing and remediation language
- detailed AI-use logging requirements

Only the student-relevant statement remains: activities are not submitted, and students may keep their own records for review or discussion.

This is consistent with the current policy of unsubmitted homework, no per-assignment grading, and one final one-on-one oral examination.

## 2. Findings Corrected During This Review

### Correction 1: Add Explicit Purpose and Completion Standard

The first trial opened directly with the core question. Readers could infer its use, but it did not explicitly state:

- who the readers are
- what kind of document it is
- what completion means
- whether activities require submission

Both language versions now include a “Document Purpose and Completion Standard” section. It states that the file is an independently readable student chapter rather than an instructor schedule or assessment guide, and that completion means being able to explain, predict, operate, and revise understanding from evidence rather than merely producing output.

Related constitution articles: 9, 10, and 12.

### Correction 2: Clarify That AI Responses Still Require Judgment

The trial already reduced AI to one brief post-Unit concept-explanation activity, but it did not explicitly say that AI responses may be wrong.

Both language versions now state that when an AI response conflicts with the chapter diagram, compiler behavior, or reproducible execution results, students should judge it using observable evidence rather than accept it as an answer.

Related constitution basis: the preamble, Article 15 item 6, and the principle that AI is a learning tool rather than a substitute for thinking.

## 3. Non-Blocking Items to Watch

### 3.1 Information Levels May Need More Explicit Labels Later

P-U01 uses phrases such as “you do not need to memorize this yet” and “for now, recognize the role,” so the current importance levels are understandable. It does not yet use fixed labels for:

- must understand
- recommended practice
- extension
- may skip for now

This is not currently a violation. Longer later Units may benefit from a consistent labeling system.

### 3.2 Mermaid Rendering Must Be Checked in the Publishing Environment

The diagram meaning and bilingual structure are aligned. Before formal publication, the actual student reading environment should be checked for Mermaid support. If it cannot render Mermaid, an equivalent text or static-image fallback will be required.

### 3.3 Compiler Error Text Should Not Be Hard-Coded

Exact diagnostics vary across GCC and Clang versions and platforms. The chapter correctly asks students to read the “first useful message” without prescribing one exact message. Later Units should preserve this approach.

## 4. Baseline for the Remaining 15 Units

Later student chapters should retain at least:

1. An explicit document purpose and completion standard.
2. One student-understandable core question.
3. Prediction before answers or execution results are revealed.
4. A visual model, or an explicit reason why one is not appropriate.
5. Concept formation before syntax.
6. At least one minimal correct case.
7. At least one reproducible, diagnosable, and correctable typical error.
8. Execution tracing or explicit reasoning.
9. Guided practice, independent practice, and requirement modification.
10. Testing or another observable form of verification.
11. One brief, low-weight AI concept-explanation activity.
12. A reminder that AI responses still require evidence-based judgment.
13. A self-check, summary, and connection to the next Unit.
14. Chinese and English maintenance in the same work unit.
15. No instructor pacing, grading operations, or administrative detail in the main student chapter.

## 5. Final Decision

After the corrections in this review, the bilingual P-U01 student materials comply with the course constitution’s core requirements for student-facing teaching material and can serve as the structural and writing reference for expanding later Units.

This decision does not make the chapter permanently final. After classroom trial reading, the material should continue to evolve based on student prediction errors, reading difficulty, operational failures, and concept confusion.

## Navigation

- [Course Constitution](../../CONSTITUTION.en.md)
- [P-U01 English Student Material](../preparatory/unit-01-execution.en.md)
- [Materials Index](../README.en.md)
- [繁體中文版](pu01-constitution-review.zh-TW.md)
