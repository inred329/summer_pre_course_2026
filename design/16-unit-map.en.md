# Concept-Driven Unit Map

Version: 0.1.0  
Status: Unit composition draft  
Last updated: 2026-08-04  
Corresponding Chinese version: [Concept 驅動的 Unit Map](16-unit-map.zh-TW.md)

## Document Purpose

This document composes cross-language programming Concepts from the Concept Tree and Concept Registry into teachable, readable, and traceable Units.

A Unit is not a chapter label or syntax list. It consists of:

1. One student-understandable core question.
2. One primary Concept dependency chain.
3. A limited number of newly introduced Concepts.
4. Existing Concepts that are deepened or reused.
5. At least one prediction, tracing, testing, debugging, or verification activity.
6. Corresponding C-language tools and syntax.

This document defines the Unit skeleton only. It does not determine weekly pacing or replace the final student-facing materials.

## Unit Composition Markers

- `N`: Concept introduced for the first time in this Unit.
- `D`: Concept deepened in this Unit.
- `R`: Concept reused in this Unit.
- `P`: Preparatory-course scope.
- `F`: Formal-course scope.

---

# Preparatory-Course Units

## P-U01 — How Does Program Text Become an Execution Result?

Core question: **How does human-readable program text become behavior that a computer actually executes?**

Primary Concept chain:

```text
CT-C01 Problem
→ CT-C02 Requirement
→ CT-C03 Algorithm
→ CT-C04 Program
→ CT-C05 Source Code
→ CT-C06 Translation
→ CT-C07 Compiler
→ CT-C08 Executable
→ CT-C09 Execution
→ CT-X02 Output
→ CT-E01 Expected Result
```

Concept use:

- `N`: Problem, Requirement, Program, Source Code, Translation, Compiler, Executable, Execution, Output, Expected Result
- `D`: Algorithm
- `R`: None

C-language mapping:

- Minimal `main` program
- `#include <stdio.h>`
- `printf`
- GCC/Clang compilation command
- Executable and terminal execution
- `return 0`

Students must experience:

- Predicting output before execution
- Distinguishing compilation from execution
- Producing and diagnosing one compile error
- Comparing edited source run without recompilation against the recompiled version

---

## P-U02 — How Does a Program Remember Data and Change State?

Core question: **How does a program preserve current data and produce a new state after each execution step?**

Primary Concept chain:

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-S01 State
→ CT-S03 Variable
→ CT-S06 Initialization
→ CT-S07 Assignment
→ CT-S08 Update
→ CT-I07 Expression
→ CT-I09 Evaluation
```

Concept use:

- `N`: Data, Value, Type, State, Variable, Initialization, Assignment, Update, Expression, Evaluation
- `D`: Expected Result, Output
- `R`: Program, Execution

C-language mapping:

- `int`, `double`, and `char`
- Variable declaration and initialization
- Assignment operator
- Arithmetic operators
- `scanf` and `printf`
- Initial observation of integer division and type conversion

Students must experience:

- Building variable-state tables
- Tracing old and new values line by line
- Predicting expression results
- Comparing integer and floating-point representation
- Diagnosing uninitialized, type-mismatch, or incorrect-format cases

---

## P-U03 — How Does a Program Select and Repeat?

Core question: **When different situations require different actions, or one action must repeat, how does a program determine the next step?**

Primary Concept chain:

```text
CT-F01 Sequence
→ CT-F02 Condition
→ CT-F03 Decision
→ CT-F05 Repetition
→ CT-F06 Iteration
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Infinite Execution
```

Concept use:

- `N`: Sequence, Condition, Decision, Repetition, Iteration, Loop Condition, Boundary, Infinite Execution
- `D`: Expression, Evaluation, State Change, Update
- `R`: Input, Output, Expected Result

C-language mapping:

- Relational and logical operators
- `if` and `else`
- `while` and `for`
- `break` and `continue` as extension mappings
- Counters, accumulators, and sentinels

Students must experience:

- Predicting branch paths
- Tracing loop state iteration by iteration
- Comparing `<` and `<=` boundary behavior
- Diagnosing infinite loops and off-by-one errors
- Running regression checks after a requirement change

---

## P-U04 — How Can a Large Problem Be Divided into Understandable Work?

Core question: **When a program grows longer, how can responsibilities be separated so each part can be understood, tested, and modified?**

Primary Concept chain:

```text
CT-A01 Decomposition
→ CT-A02 Responsibility
→ CT-A03 Function
→ CT-A04 Interface
→ CT-A06 Parameter
→ CT-A07 Argument
→ CT-A08 Return Value
→ CT-A09 Call
→ CT-E02 Test Case
→ CT-E03 Testing
→ CT-E04 Verification
```

Concept use:

- `N`: Decomposition, Responsibility, Function, Interface, Parameter, Argument, Return Value, Call
- `D`: Test Case, Testing, Verification, Requirement
- `R`: State, Decision, Repetition, Expected Result

C-language mapping:

- Function declaration, definition, and call
- Parameters and return values
- Local variables
- Function prototypes
- Small integrated program

Students must experience:

- Writing a one-sentence function responsibility
- Predicting parameters and return values
- Tracing state before and after a call
- Designing normal, boundary, and regression cases for a function
- Verifying a plausible but incorrect AI function suggestion

---

# Formal-Course Units

The formal course does not reset the preparatory course. Preparatory Concepts continue to deepen and combine with new Concepts.

## F-U01 — Why Do Representation, Type, and Operations Affect Results?

Core question: **Why can the same value or operation produce different outcomes because of representation and type?**

Primary Concepts: Representation, Type, Operator, Evaluation, Conversion, and Format.

Deepened: Value, Expression, Expected Result, and Testing.

C mapping: integer ranges, floating-point error, character encoding, implicit and explicit conversion, and formatted output.

---

## F-U02 — How Can Reliable Multi-Branch and Repetitive Flows Be Built?

Core question: **When conditions, boundaries, and repetition rules become complex, how can correctness still be demonstrated?**

Primary Concepts: Branch, Nested Control, Sentinel, and Invariant.

Deepened: Decision, Repetition, Boundary, State Change, and Verification.

C mapping: `switch`, nested control, compound conditions, sentinel loops, and loop invariants.

---

## F-U03 — How Does Data Form an Ordered Collection?

Core question: **When multiple related values must be stored and processed together, how are they organized, located, and traversed?**

Primary Concepts: Collection, Object, Layout, Boundary, Iteration, and Memory Safety.

Composite Concept: `CT-K01 Array`.

C mapping: one-dimensional arrays, indexes, length, traversal, out-of-bounds access, and arrays as function parameters.

---

## F-U04 — How Is Text Represented and Processed as Data?

Core question: **How does a computer store text as data, and how does it know where the text ends?**

Primary Concepts: Representation, Collection, Layout, Sentinel, Buffer, and Format.

Composite Concept: `CT-K02 String`.

C mapping: `char` arrays, null terminator, string literals, `fgets`, string functions, and buffer safety.

---

## F-U05 — How Does a Function Call Create a New Execution Environment?

Core question: **During a function call, how are parameters, local state, and unfinished work preserved?**

Primary Concepts: Call Stack, Scope, Lifetime, Stack Storage, and Recursion.

Deepened: Function, Call, Parameter, Return Value, and Invariant.

C mapping: automatic local variables, call frames, recursion, base cases, and the concept of stack overflow.

---

## F-U06 — How Can Data Be Manipulated Indirectly Through Addresses?

Core question: **How can one value refer to another object and use its address to access or modify it?**

Primary Concepts: Address, Pointer, Indirection, Aliasing, Null Reference, Lifetime, and Memory Safety.

C mapping: `&`, `*`, pointer parameters, null pointers, and limited pointer arithmetic.

---

## F-U07 — How Can One Data Object Contain Different Fields?

Core question: **When one entity contains several different kinds of data, how can they be combined into one meaningful object?**

Primary Concepts: Collection, Object, Layout, Type, and Interface.

Composite Concept: `CT-K03 Structure`.

C mapping: `struct`, member access, nested structures, structure assignment, and `typedef`.

---

## F-U08 — How Does a Program Obtain and Release Space During Execution?

Core question: **When data size or lifetime cannot be fixed in advance, how does a program manage storage?**

Primary Concepts: Dynamic Allocation, Ownership, Lifetime, Pointer, and Memory Safety.

C mapping: `malloc`, `calloc`, `realloc`, `free`, memory leaks, dangling pointers, and double free.

---

## F-U09 — How Does a Program Interact with Files and Persistent Data?

Core question: **When data must remain after a program ends, how does the program read, write, and detect errors?**

Primary Concepts: Stream, File, End of Input, Format, Buffer, Protocol, and Error Channel.

Composite Concept: `CT-K04 File I/O`.

C mapping: `FILE *`, `fopen`, `fclose`, text-file I/O, EOF, and checking function return values.

---

## F-U10 — How Can a Program Be Divided into Independently Maintainable Modules?

Core question: **How can interface and implementation be separated so different program parts can be understood, compiled, and replaced independently?**

Primary Concepts: Module, Interface, Implementation, Translation, Compiler, and Responsibility.

Composite Concept: `CT-K05 Modular Programming`.

C mapping: `.h`, `.c`, include guards, separate compilation, and linking.

---

## F-U11 — How Can Programs Be Proven, Diagnosed, and Improved Systematically?

Core question: **What evidence beyond correct output is needed before a program can be trusted?**

Primary Concepts: Testing, Verification, Validation, Debugging, Error Diagnosis, Regression, Refactoring, Code Reading, and Code Review.

C mapping: test tables, reproducing errors, narrowing scope, regression after correction, comparing programs, and refactoring.

---

## F-U12 — How Can Students Collaborate Responsibly with AI?

Core question: **When AI can quickly produce programs and explanations, how do students preserve judgment and build trustworthy evidence?**

Primary Concepts: AI Collaboration, Expected Result, Testing, Verification, Error Diagnosis, and Documentation.

C mapping: reviewing AI-generated C programs, verifying incorrect suggestions, strengthening tests, comparing solutions, and recording decisions.

---

## F-U13 — How Can a Program Integrate Concepts Across the Course?

Core question: **How can requirements, data, control, functions, memory, interaction, and engineering be integrated into one program?**

Primary Concepts: Requirement, Algorithm, Decomposition, Module, Protocol, Testing, Validation, and Maintenance.

This Unit does not introduce a large amount of new syntax. It requires students to integrate, modify, diagnose, verify, and explain.

---

## Relationship Between Units and Lessons

A Unit is not equal to one class meeting. A Lesson is a delivery slice of a Unit.

The same Unit may:

- Be taught in a longer integrated block in the Chinese-taught class.
- Be split into more Lessons in the English-taught class with terminology, reading, and communication scaffolds.
- Be deepened across several weeks in the formal course.

A Lesson must not change the Unit's core question, Concept chain, or capability standards.

## First-Version Quantity Conclusion

Current recommendation:

- Preparatory course: 4 Units.
- Formal course: 13 Units.
- Total: 17 Unit skeletons.

This number is not constitutionally fixed. Units may later be merged or split according to Concept boundaries, classroom trials, and available hours, but week count must not replace Concept-based derivation.

## Next Steps

1. Check whether each Unit has a complete Concept dependency chain.
2. Confirm that the number of new Concepts in each Unit is suitable for beginners.
3. Compare the map with current Preparatory Units 1–4 and decide what to retain, split, or rewrite.
4. Create a student-material outline for each Unit.
5. Only then schedule Lessons for the Chinese-taught, English-taught, and formal courses.

## Navigation

- [Programming Concept Tree](14-programming-concept-tree.en.md)
- [Programming Concept Registry](15-programming-concept-registry.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](16-unit-map.zh-TW.md)
