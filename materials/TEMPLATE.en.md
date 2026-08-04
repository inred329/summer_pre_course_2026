# Unit Material Template

Version: 1.0.0  
Status: Official template  
Last updated: 2026-08-05  
Major change summary: Rewritten to match the current 16-Unit student-material baseline and remove per-Unit acceptance, remediation, micro-orals, and mandatory AI records.  
Corresponding Chinese version: [單元教材模板](TEMPLATE.zh-TW.md)

## Document Purpose and Completion Standard

This template is for authors creating official Units that students can read independently, practice with, review, and consult later. Instructor scheduling, classroom observation, grading administration, and final-oral procedures belong in instructor or assessment documents rather than student chapters.

Completing a Unit means more than producing output. Students should be able to explain the central Concept, predict or trace behavior, implement a minimal case, diagnose a representative error, test results, and handle a small requirement change.

Activities are normally unsubmitted, ungraded, and not individually marked. Students may keep predictions, programs, errors, and corrections for classroom discussion and review.

## Basic Information

- Unit title:
- Core question:
- Prerequisite Concepts:
- Concepts introduced or deepened:
- Related later Units:
- Tools and C standard: C17

## 1. Learning Objectives

After completing the Unit, students should be able to:

1. Explain the central Concept.
2. Predict or trace program behavior.
3. Complete a minimal implementation.
4. Diagnose and correct one representative error.
5. Build tests and respond to a small requirement change.

Objectives must be concrete and observable. Avoid vague wording such as “become familiar with” or “understand.”

## 2. Prerequisites and Content That May Be Deferred

### Students Should Already Be Able To

- 

### Must Understand in This Unit

- 

### Must Be Able To Do

- 

### Recommended Practice

- 

### Extension Exploration

- 

### May Be Deferred

- 

## 3. Required Tools and Environment

- Compiler and version:
- Compile command:
- Execution method:
- Fallback environment:

When tools fail, paper tracing, instructor equipment, or an equivalent environment may be used for the core activity. Tool problems must not replace understanding and verification.

## 4. Core Question and Prediction First

Begin with a problem, requirement, or observable phenomenon.

> What question does this Unit answer?

Before revealing the result, ask students to predict at least one of the following:

- output
- state
- control path
- call order
- memory relationship
- error category

## 5. Visual Model

Include a flowchart, state diagram, memory diagram, relationship diagram, sequence diagram, or trace table that directly supports the learning objective.

For each visual, explain:

- what students should observe
- what nodes, arrows, locations, or states mean
- how the visual corresponds to program behavior
- how students can verify it through tracing, execution, or testing

## 6. Core Concepts and Language Logic

Use an order appropriate to the Unit:

```text
Problem or need
→ Mental model
→ Core Concept
→ C syntax and tools
→ Program behavior
→ Verification method
```

Use the approved terminology in `design/11-terminology-glossary`. Provide both language forms for important terms on first use when appropriate.

## 7. Minimal Example

Clearly label whether the content is a complete program, fragment, pseudocode, or intentionally incorrect example.

```c
/* code */
```

### Expected Input

```text

```

### Expected Output

```text

```

### Compile and Run

```bash

```

Introduce only the new concepts currently needed. Do not overload one example with unestablished techniques.

## 8. Execution, State, or Memory Trace

Require prediction before tracing key states.

| Step | Statement / Condition | Current State | Expected or Observed Result |
|---|---|---|---|
| 1 |  |  |  |

Explain key transitions, termination, lifetime, or the first likely point of failure.

## 9. Representative Error and Diagnosis

Include at least one reproducible, diagnosable, and correctable error case:

- observed symptom
- possible cause
- diagnostic steps
- reason for the correction
- test after correction
- regression check

Do not provide only the corrected answer.

## 10. Guided Practice

### Task

- What to do:
- Why it is being done:
- Permitted resources:
- Completion standard:

Begin with reading, prediction, completion, tracing, or modification before a larger implementation.

## 11. Independent Practice

### Task

- Requirement:
- Input:
- Output:
- Constraints:
- Normal case:
- Boundary case:
- Necessary exceptional case:
- Completion standard:

Permit alternative reasonable solutions that satisfy the specification, current scope, safety, and readability.

## 12. Testing and Requirement Modification

Students establish expected results before execution.

| Type | Input or Action | Expected Result | Actual Result | Judgment |
|---|---|---|---|---|
| Normal |  |  |  |  |
| Boundary |  |  |  |  |
| Necessary exceptional |  |  |  |  |
| Regression |  |  |  |  |

Provide at least one small requirement change and ask students to:

1. Identify affected parts.
2. Update expectations and tests.
3. Modify the program or model.
4. Run regression verification.
5. Explain the reason for the change.

## 13. Explain the Concept to AI

Use one brief activity, for example:

> Explain the Unit's central Concept to AI in your own words.

No fixed prompt, specific tool, saved conversation, or submission is required. AI responses may be incomplete or incorrect. When they conflict with code, compiler behavior, tests, or reproducible results, students should judge again using evidence.

## 14. Self-Check

Students should confirm that:

- I can explain the central Concept in my own words.
- I can make a reasonable prediction before execution.
- I can trace the key state or flow.
- I can reproduce and diagnose one representative error.
- I can build tests and complete one requirement change.
- When I use AI, I can judge whether its response matches reproducible evidence.

## 15. Unit Summary and Next Step

Summarize briefly:

- What problem the Unit solved.
- Which new capabilities were established.
- Which content was intentionally deferred.
- How the next Unit uses these Concepts.

## 16. Prepublication Check

- [ ] Chinese and English versions are substantively equivalent.
- [ ] The purpose, reader, and completion standard are clear.
- [ ] Prerequisite Concepts, new Concepts, and deferred content are explicit.
- [ ] Problem and Concept appear before syntax.
- [ ] Appropriate prediction and visual representation are included.
- [ ] Complete programs were compiled and executed in the specified environment.
- [ ] Code, input, output, and test data are consistent.
- [ ] Correct cases and reproducible error-diagnosis cases are included.
- [ ] Guided practice, independent practice, testing, and requirement modification are included.
- [ ] AI remains a low-weight concept conversation, not a completion requirement or authoritative evidence.
- [ ] Instructor scheduling, per-Unit grading, micro-orals, and remediation administration are absent.
- [ ] Navigation and language-switch links are complete.

## Navigation

- [Materials and Activity Resources](README.en.md)
- [Instructional Design Workspace](../design/README.en.md)
- [繁體中文版](TEMPLATE.zh-TW.md)
