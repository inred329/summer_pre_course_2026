# Unit Material Template

Version: 0.1.0  
Status: Official template  
Last updated: 2026-08-03  
Major change summary: Established the shared structural baseline for all preparatory and formal-course unit materials.  
Corresponding Chinese version: [單元教材模板](TEMPLATE.zh-TW.md)

## Document Purpose

This template is used by instructors, teaching assistants, and material authors to create official unit materials. Every material must copy this structure, remove inapplicable prompt text, and retain all core fields.

## Basic Information

- Unit title:
- Applicable course: Chinese preparatory / English preparatory / formal course
- Session or week:
- Requirement IDs:
- Competency IDs:
- Target maturity:
- Scope state:
- Acceptance tasks:
- Risk IDs:
- Estimated time:

## 1. Learning Objectives

After completing this unit, students can:

1.
2.
3.

Objectives must be concrete, observable, and assessable. Avoid vague wording such as “become familiar with” or “understand a little.”

## 2. Prerequisites

Before starting, students should already be able to:

- 
- 

When prerequisite competency has not been established, provide a remediation entry instead of skipping it.

## 3. Required Tools and Environment

- Operating system or runtime environment:
- Compiler and version:
- Editor or IDE:
- Commands:
- Fallback environment:

## 4. Information Priority

### Must Understand

- 

### Must Complete

- 

### Recommended Practice

- 

### Extension Exploration

- 

### May Be Deferred

- 

## 5. Core Question

> What primary problem does this unit solve?

Explain the need and design purpose before presenting syntax.

## 6. Visual Model

Include a flowchart, state diagram, memory diagram, relationship diagram, or trace table that directly supports the unit objective.

For each visual, state:

- What students should observe
- What nodes and arrows mean
- How the visual corresponds to program behavior
- How students can verify that the visual is correct

## 7. Core Concepts and Language Logic

Explain in this order:

```text
Need
→ Design Purpose
→ Language Logic
→ Syntax
→ Implementation
→ Verification
```

Use the approved terminology in `design/11-terminology-glossary`.

## 8. Minimal Executable Example

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

### Execution Command

```bash

```

## 9. Execution Trace and Reasoning

Require prediction before execution.

| Step | Statement / Condition | Variable or State | Expected Result |
|---|---|---|---|
| 1 |  |  |  |

Explain key transitions, termination conditions, and the first likely point of failure.

## 10. Common Errors and Error Cases

Include at least:

- One reproducible error
- The error message or incorrect behavior
- An initial hypothesis
- A verification method
- The reason for the correction
- A regression test

Do not provide only the corrected answer.

## 11. Guided Practice

### Task

- What to do:
- Why it is being done:
- Permitted resources:
- Prohibited resources:
- What must be submitted or demonstrated:
- Completion criteria:

Begin with reading, prediction, completion, or modification before full implementation.

## 12. Independent Practice

### Task

- Requirement:
- Input:
- Output:
- Constraints:
- Permitted resources:
- AI rules:
- Required evidence:
- Completion criteria:

Permit alternative reasonable solutions that satisfy the specification, current scope, safety, and readability.

## 13. Testing and Verification

Students must establish expected results first.

| Type | Input | Expected Result | Actual Result | Judgment |
|---|---|---|---|---|
| Normal case |  |  |  |  |
| Boundary case |  |  |  |  |
| Necessary exceptional case |  |  |  |  |

## 14. Requirement Modification

Provide at least one small requirement change and require students to:

1. Identify affected parts.
2. Modify the program or model.
3. Update tests.
4. Run regression verification.
5. Explain the reason for the change.

## 15. AI Use Rules

### Permitted

- 

### Prohibited

- 

### Must Be Retained

- Understanding or initial approach before using AI
- A self-created expected result or test
- Summary of AI suggestions
- Verification method
- Reason for accepting, modifying, or rejecting the suggestion

“AI may be used appropriately” is not sufficient as the only rule.

## 16. Self-Check

Students should be able to answer:

- Can I explain the core concept in my own words?
- Can I predict the result before execution?
- Can I modify a requirement and update tests?
- Can I locate one error and explain why the correction works?
- Can I explain what AI contributed and how I verified it?

## 17. Acceptance and Remediation

- Target competency and maturity:
- Required understanding-oriented evidence:
- Required action-oriented evidence:
- Micro-oral questions:
- Passing criteria:
- Remediation method:

Correct output, successful compilation, or passing OJ must not be the sole evidence.

## 18. Unit Summary

Summarize in a few points:

- What problem the unit solved.
- Which new competencies students established.
- Where those competencies will be used next.
- Which content was intentionally deferred.

## 19. Instructor and Teaching-Assistant Notes

- Classroom observations:
- Common misconceptions:
- Remediation strategy:
- What must be preserved if time is short:
- Additional diagnosis or transfer activities if time permits:
- Out-of-scope content that must not be added:

## 20. Prepublication Check

- [ ] Chinese and English versions are substantively equivalent.
- [ ] Requirement, competency, maturity, scope, and acceptance IDs are correct.
- [ ] Code was compiled and executed in the specified environment.
- [ ] Input, output, and test data are consistent.
- [ ] Visual models match program behavior.
- [ ] Reading, tracing, modification, testing, or debugging activities are included.
- [ ] AI rules are specific.
- [ ] No unintroduced technique or advanced data structure was smuggled in.
- [ ] Navigation and traceability were updated.

## Navigation

- [Instructional Design Workspace](../design/README.en.md)
- [繁體中文版](TEMPLATE.zh-TW.md)
