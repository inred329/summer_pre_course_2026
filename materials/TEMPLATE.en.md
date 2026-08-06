# Unit Material Template

Version: 1.1.0  
Status: Suggested template for material authors  
Last updated: 2026-08-06  
Major change summary: Removed the fixed AI section and mechanical chapter requirements. The template now centers teaching purpose, primary audience, and core capability; AI may appear only as a skippable optional extension.  
Corresponding Chinese version: [單元教材模板](TEMPLATE.zh-TW.md)

## Document Purpose

This template helps authors create Unit materials that students can read independently, practice with, review, and consult later. It provides a suggested structure and prepublication checks; it is not a fixed outline that every Unit must copy section by section.

Instructor scheduling, classroom observation, grading administration, answer-revealing prompts, and final-oral procedures belong in instructor or assessment documents rather than student chapters.

Official assessment rules are defined only by `design/13-learning-assessment-policy.*`. This template must not create submission, grading, attendance, AI-record, or oral-examination rules.

## Completion Standard

Completing a Unit means more than producing output. According to the Unit's teaching purpose, students should demonstrate an appropriate combination of capabilities such as:

- explaining the central Concept or mental model
- predicting or tracing program behavior
- reading, modifying, or completing a minimal implementation
- diagnosing a representative error
- building tests and responding to a small requirement change
- validating a judgment with code, tests, compiler behavior, or other reproducible evidence

Every Unit does not need every activity. Selection should serve the core question and control cognitive load.

AI is optional by default. Not using AI does not affect Unit completion, participation, or assessment. When an AI activity is included, it must be marked as a directly skippable optional extension. Core completion standards and self-checks must not depend on AI.

## Basic Information

- Unit title:
- Primary audience: students
- Core question:
- Prerequisite Concepts:
- Concepts introduced or deepened:
- Intentionally deferred content:
- Related later Units:
- Tools and language standard:

## Suggested Structure

Use, merge, omit, or reorder the following sections according to teaching need.

### 1. Before Starting

- What question does the Unit answer?
- What should students already be able to do?
- Which observable behaviors demonstrate completion?
- What may be skipped for now?

Objectives should be concrete and observable. Avoid vague wording such as “become familiar with” or “understand.”

### 2. Problem, Need, or Observable Phenomenon

Establish a problem, requirement, contradiction, error symptom, or prediction task before introducing syntax.

Students may first predict:

- output
- state
- control path
- call order
- memory relationship
- error category

### 3. Mental Model and Visual Representation

Use a flowchart, state diagram, memory diagram, relationship diagram, sequence diagram, or trace table when it supports the learning goal.

For each visual, explain:

- what students should observe
- what nodes, arrows, locations, or states mean
- how the visual corresponds to program behavior
- how it can be verified through tracing, execution, or testing

Decorative visuals without instructional value are unnecessary.

### 4. Core Concepts and Language Logic

A useful sequence is:

```text
Problem or need
→ Mental model
→ Core Concept
→ C syntax and tools
→ Program behavior
→ Verification method
```

Use consistent terminology, but do not place requirement IDs, competency IDs, traceability matrices, or maintenance metadata into the student reading flow merely for internal governance.

### 5. Minimal Example

Clearly identify whether content is a:

- complete program
- program fragment
- pseudocode example
- deliberately defective example

```c
/* code */
```

Provide as needed:

- expected input
- expected output
- compile command
- execution method
- verified tool and version

Introduce only currently necessary concepts. Do not overload one example with techniques that have not been established.

### 6. Tracing, Diagnosis, and Verification

Choose activities that serve the learning objective:

| Step | Statement / Condition | Current State | Expected or Observed Result |
|---|---|---|---|
| 1 |  |  |  |

A representative error case should include:

- a reproducible symptom
- possible cause
- diagnostic steps
- reason for the correction
- test after correction
- necessary regression confirmation

Do not provide only the corrected answer, and do not treat accidental output as technical evidence.

### 7. Practice and Requirement Modification

According to the Unit, use reading, prediction, completion, tracing, modification, testing, or independent implementation.

A task should state at least:

- what to do
- why it is being done
- permitted resources
- constraints or safety conditions
- completion standard

Permit alternative reasonable solutions that satisfy the specification, current scope, safety, and readability.

A test table may be used when useful:

| Type | Input or Action | Expected Result | Actual Result | Judgment |
|---|---|---|---|---|
| Normal |  |  |  |  |
| Boundary |  |  |  |  |
| Necessary exceptional |  |  |  |  |
| Regression |  |  |  |  |

A requirement change may ask students to:

1. Identify affected parts.
2. Update expected results and tests.
3. Modify the program or model.
4. Run regression verification.
5. Explain the reason for the change.

### 8. Optional Extensions

Extensions must be clearly separated from core work and directly skippable.

An AI extension may use wording such as:

> Optional: Give AI an explanation you have already written, note whether it raises a new question, and judge its claims using code, compiler behavior, tests, or reproducible results.

Do not require:

- a fixed prompt
- a particular AI tool
- saving or submitting a full conversation
- a declaration of non-use
- treating an AI response as an authoritative answer or core capability evidence

### 9. Self-Check and Summary

Self-checks should contain only core capabilities, for example:

- I can explain the central Concept in my own words.
- I can make a reasonable prediction before execution.
- I can trace the key state or flow.
- I can reproduce and diagnose a representative error.
- I can build tests and respond to a requirement change.

The summary should state:

- what problem the Unit solved
- which capabilities were established
- which content was intentionally deferred
- how a later Unit uses these Concepts

## Prepublication Check

- [ ] Primary audience, core question, and completion standard are clear.
- [ ] Chinese and English versions are substantively equivalent and naturally readable in each language.
- [ ] Prerequisite, new, and deferred Concepts are explicit.
- [ ] A problem, need, or mental model appears before syntax.
- [ ] The number of activities and new concepts respects cognitive load.
- [ ] Complete programs were compiled and executed in the specified environment.
- [ ] Code, input, output, and test data are consistent.
- [ ] Intentional defect cases are clearly labeled and safely reproducible.
- [ ] Correct output, successful compilation, OJ results, or tool approval are not sole capability evidence.
- [ ] Any AI activity is marked as a skippable optional extension.
- [ ] Core completion standards and self-checks do not depend on AI.
- [ ] Instructor scheduling, grading administration, answer prompts, and internal-governance content do not pollute the student flow.
- [ ] Navigation and language-switch links are complete.

## Navigation

- [Materials and Activity Resources](README.en.md)
- [Learning and Assessment Policy](../design/13-learning-assessment-policy.en.md)
- [Course Constitution 2.0](../CONSTITUTION.en.md)
- [繁體中文版](TEMPLATE.zh-TW.md)
