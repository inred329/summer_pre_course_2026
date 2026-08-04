# Student Material Outlines for 16 Units

Version: 0.1.0  
Status: Student-material outline draft  
Last updated: 2026-08-04  
Corresponding Chinese version: [16 個 Unit 的學生教材大綱](17-student-material-outlines.zh-TW.md)

## Document Purpose

This document converts the Concept-Driven Unit Map into student-material outlines that can be written, reviewed, and expanded one Unit at a time.

Each Unit is intended to support independent student reading and should ordinarily follow:

> Core Question → Prediction → Visual Model → Concept → C-Language Mapping → Execution Trace → Error Diagnosis → Practice → Post-Unit Concept Explanation → Summary

AI appears only as a brief post-Unit conversational audience. It is not the subject of the material and does not replace the student’s own prediction, implementation, testing, or debugging.

---

# Preparatory Course

## P-U01 — How Does Program Text Become an Execution Result?

### Core Question

How does human-readable program text become behavior that a computer actually executes?

### Learning Objectives

After completing this Unit, students should be able to:

- Distinguish a problem, requirement, algorithm, source code, executable, and running program.
- Explain that compilation and execution are different stages.
- Predict the output of a minimal C program.
- Read basic compiler diagnostics.
- Explain why source-code changes require recompilation.

### Suggested Material Sequence

1. Why can a computer not directly understand arbitrary human-readable text?
2. Problem, requirement, and algorithm.
3. What source code is.
4. What a compiler does.
5. Executable and running process.
6. `main`, `printf`, and `return 0`.
7. Predicting output before execution.
8. Editing source code without recompiling.
9. Missing semicolon and other minimal compile errors.
10. Turning an error message into a testable hypothesis.

### Visual Models

- Problem → Requirement → Algorithm → Source Code → Compiler → Executable → Execution → Output.
- Separation of source file, executable file, and running process.

### Minimal Examples

- First `Hello, world!` program.
- Changing output text and recompiling.
- Comparing an old executable with newly edited source code.

### Error Cases

- Missing semicolon.
- Missing closing quotation mark.
- Running an old executable after editing source code.
- Mistaking a compile error for a runtime error.

### Practice Directions

- Predict the output of three tiny programs.
- Put compilation and execution steps in order.
- Use a diagnostic message to identify and verify a possible cause.
- Change an output requirement and rebuild the program.

### Post-Unit Concept Explanation

Explain to AI the relationship among source code, compiler, executable, and execution.

### Unit Summary

A program is not one file. It is a transformation process from a requirement to observable execution behavior.

---

## P-U02 — How Does a Program Remember Data and Change State?

### Core Question

How does a program preserve current data and produce a new state after each execution step?

### Learning Objectives

- Distinguish data, value, type, and variable.
- Explain initialization, assignment, and update.
- Trace a program line by line using a state table.
- Predict simple expression results.
- Identify basic uninitialized-value, type, and format errors.

### Suggested Material Sequence

1. Why a program needs to remember data.
2. Values and types.
3. A variable as the relationship among a name, an object, and its current value.
4. Declaration and initialization.
5. Assignment is not mathematical equality.
6. How an old state becomes a new state.
7. Expressions and evaluation.
8. `int`, `double`, and `char`.
9. How input changes state and output reveals state.
10. Integer division and introductory type conversion.

### Visual Models

- Variable-state table.
- Old value → evaluation → new value for `x = x + 1`.
- Type as a rule for interpreting a value.

### Minimal Examples

- Declaring, initializing, and printing an integer.
- Reading two numbers and computing a result.
- Comparing one operation under integer and floating-point types.

### Error Cases

- Using an uninitialized variable.
- Treating `=` as mathematical equality.
- Mismatched `scanf` or `printf` formats.
- Expecting a fractional result from integer division.

### Practice Directions

- Complete variable-state tables.
- Predict values after consecutive assignments.
- Compare operations across types.
- Correct input/output format mistakes.

### Post-Unit Concept Explanation

Explain to AI the relationship among value, type, variable, and program state.

### Unit Summary

Program execution is a process in which state is repeatedly read, computed, and updated.

---

## P-U03 — How Does a Program Select and Repeat?

### Core Question

When different situations require different actions, or one action must repeat, how does a program decide what happens next?

### Learning Objectives

- Explain sequence, condition, decision, and repetition.
- Predict branch paths and loop iteration counts.
- Trace counters, accumulators, and loop conditions.
- Identify off-by-one errors and infinite loops.
- Reverify control flow after a requirement change.

### Suggested Material Sequence

1. Default sequential execution.
2. How a condition produces true or false.
3. Decision with `if` and `else`.
4. Multiple conditions and logical operators.
5. Why repetition is needed.
6. The condition-driven model of `while`.
7. The counting model of `for`.
8. State change during each iteration.
9. Boundaries, `<`, and `<=`.
10. Infinite loops and termination conditions.

### Visual Models

- Branch flowchart.
- Loop-state table.
- Start value, continuation condition, update, and exit cycle.

### Minimal Examples

- Testing whether a number is positive or negative.
- Summing values from 1 through n.
- Sentinel-controlled input loop.

### Error Cases

- Reversed condition.
- Missing update to the loop variable.
- One extra or one missing iteration.
- Incorrect compound condition.

### Practice Directions

- Predict branch paths.
- Record loop state iteration by iteration.
- Correct an off-by-one error.
- Convert a fixed-count loop into a sentinel loop.

### Post-Unit Concept Explanation

Explain to AI the relationship among condition, decision, repetition, and boundary.

### Unit Summary

Control flow determines which part executes next and when execution stops.

---

## P-U04 — How Can a Large Problem Be Divided into Understandable Work?

### Core Question

When a program becomes longer, how can responsibilities be separated so each part can be understood, tested, and modified?

### Learning Objectives

- Explain the relationship among decomposition, responsibility, and function.
- Distinguish parameters, arguments, and return values.
- Read a function interface and predict call results.
- Design basic function tests.
- Extract repeated or complex logic into functions.

### Suggested Material Sequence

1. Why long programs are difficult to understand.
2. Problem decomposition and single responsibility.
3. Function as a callable unit of computation.
4. Interface and implementation.
5. Parameters and arguments.
6. Return values.
7. Local variables.
8. Function declaration, definition, and call.
9. Tracing data before and after a call.
10. Normal, boundary, and regression tests for functions.

### Visual Models

- Responsibility diagram that divides a large problem into smaller problems.
- Caller → Argument → Parameter → Function → Return Value.

### Minimal Examples

- `max` function.
- Temperature-conversion function.
- Extracting repeated computation into a function.

### Error Cases

- Unclear function responsibility.
- Wrong parameter order.
- Missing return value.
- Mismatch between caller and function prototype.

### Practice Directions

- Write a one-sentence responsibility for a function.
- Identify code fragments that should become functions.
- Predict parameter and return values.
- Add boundary tests to a function.

### Post-Unit Concept Explanation

Explain to AI the relationship among function, parameter, argument, return value, and responsibility.

### Unit Summary

Functions let a large problem be divided into parts with clear responsibilities that can be tested and reused.

---

# Formal Course

## F-U01 — Why Do Representation, Type, and Operations Affect Results?

### Core Question

Why can the same value or operation produce different results because of representation and type?

### Learning Objectives

- Explain the difference among value, representation, and type.
- Understand bit, byte, MSB, and LSB.
- Observe integer ranges, character encoding, and floating-point error.
- Predict implicit and explicit conversion results.
- Choose correct input/output formats.

### Suggested Material Sequence

1. The same information can have different representations.
2. Bit, byte, and bit position.
3. MSB and LSB.
4. Unsigned and signed integer ranges.
5. Characters and encoding.
6. Floating-point values are approximations.
7. Operator type rules.
8. Integer promotion and conversion.
9. Formatted input and output.
10. Using tests to observe representation limits.

### Visual Models

- MSB and LSB in a bit sequence.
- The same bits interpreted under different types.
- Discrete floating-point values compared with the real-number line.

### Error Cases

- Treating overflowed results as mathematical integers.
- Mixing signed and unsigned values carelessly.
- Direct floating-point equality comparison.
- Incorrect format specifier.

### Practice Directions

- Identify MSB and LSB.
- Manually calculate small binary values.
- Predict conversion results.
- Design a program that reveals floating-point error.

### Post-Unit Concept Explanation

Explain to AI the difference between MSB and LSB and their positions in a bit representation.

### Unit Summary

A type determines how bits are interpreted, and a representation limits the results a program can produce.

---

## F-U02 — How Can Reliable Multi-Branch and Repetitive Flows Be Built?

### Core Question

When conditions, boundaries, and repetition rules become complex, how can we still explain why the flow is correct?

### Learning Objectives

- Organize multiple branches and nested control.
- Use sentinels and invariants to describe loops.
- Design tests that cover normal and boundary situations.
- Compare alternative control-flow structures.
- Correct logic errors in complex flows.

### Suggested Material Sequence

1. Classifying multi-branch problems.
2. `else if` and `switch`.
3. Nested decisions.
4. Nested loops.
5. Sentinel and end of data.
6. Invariant: what remains true before and after each iteration.
7. Consistency among state, condition, and update.
8. Control-flow test table.
9. Refactoring complex conditions.
10. Regression verification after requirement changes.

### Error Cases

- Overlapping or missing branches.
- Unintended `switch` fall-through.
- Treating a sentinel as ordinary data.
- Incorrect nested-loop update.

### Practice Directions

- Complete branch-classification tables.
- Build a sentinel-loop state trace.
- Locate where an invariant is broken.
- Compare two equivalent flows.

### Post-Unit Concept Explanation

Explain to AI the differences among sentinel, loop condition, boundary, and invariant.

### Unit Summary

Reliable control flow requires complete classification, clear boundaries, and state conditions that can be continuously checked.

---

## F-U03 — How Does Data Form an Ordered Collection?

### Core Question

When multiple values of the same type must be stored and processed together, how are they organized, located, and traversed?

### Learning Objectives

- Explain collection, array, index, length, and boundary.
- Understand the memory layout of array elements.
- Traverse a one-dimensional array safely.
- Pass an array to a function.
- Identify out-of-bounds access and lost-length problems.

### Suggested Material Sequence

1. Problems with many separate variables of the same type.
2. Collection and array.
3. Meaning of zero-based indexing.
4. Length and valid range.
5. Contiguous memory layout.
6. Traversal, search, and accumulation.
7. Array as a function parameter.
8. Length must be passed separately.
9. Introductory model of multidimensional arrays.
10. Out-of-bounds access and memory safety.

### Error Cases

- Using `index == length`.
- Failing to initialize all elements.
- Assuming a function can recover array length automatically.
- Traversal condition inconsistent with actual length.

### Practice Directions

- Label indexes and values manually.
- Implement search, maximum, and average.
- Correct an out-of-bounds program.
- Extract repeated array processing into functions.

### Post-Unit Concept Explanation

Explain to AI the relationship among array, index, length, and boundary.

### Unit Summary

An array places same-type data in order, but safe use always requires knowing the valid index range.

---

## F-U04 — How Is Text Represented and Processed as Data?

### Core Question

How does a computer store text as data, and how does it know where the text ends?

### Learning Objectives

- Explain character, encoding, character array, and string.
- Understand the role of the null terminator.
- Read and process text safely.
- Distinguish capacity, content length, and input limit.
- Identify buffer overflow and missing termination.

### Suggested Material Sequence

1. How a character becomes a numeric value.
2. Character array and string.
3. Null terminator.
4. String literals.
5. Capacity and string length.
6. `fgets` and input newline.
7. Basic string functions.
8. Traversing a string manually.
9. Buffer and safe boundary.
10. Conceptual limits of encoding and UTF-8.

### Error Cases

- Forgetting space for the null terminator.
- Treating an unterminated character array as a string.
- Input exceeding the buffer.
- Treating byte count as character count.

### Practice Directions

- Label every position in a string.
- Compute string length.
- Remove the newline left by `fgets`.
- Correct unsafe text-input programs.

### Post-Unit Concept Explanation

Explain to AI the relationship among character array, string, buffer, and null terminator.

### Unit Summary

A C string is a character array whose end is marked by a special terminator; safe processing requires both capacity and boundary awareness.

---

## F-U05 — How Does a Function Call Create a New Execution Environment?

### Core Question

During a function call, how are parameters, local state, and unfinished work preserved?

### Learning Objectives

- Explain call stack and stack frame.
- Connect scope, lifetime, and automatic storage.
- Trace nested function calls.
- Understand recursive base and recursive cases.
- Identify infinite recursion and stack overflow.

### Suggested Material Sequence

1. Why the caller can continue after a called function returns.
2. Contents of a stack frame.
3. Lifetime of parameters and local variables.
4. Scope and lifetime are different.
5. Nested-call tracing.
6. Recursion as a function calling itself.
7. Base case.
8. Recursive case and problem reduction.
9. Expansion and return phases.
10. Stack overflow.

### Error Cases

- Missing base case.
- Recursive problem does not get smaller.
- Returning data whose local lifetime has ended.
- Confusing scope with lifetime.

### Practice Directions

- Draw a multi-level call stack.
- Trace recursive parameters.
- Compare iterative and recursive solutions.
- Correct nonterminating recursion.

### Post-Unit Concept Explanation

Explain to AI the relationship among call stack, stack frame, scope, and lifetime.

### Unit Summary

Each function call creates a temporary execution environment; recursion allows several environments of the same function to coexist.

---

## F-U06 — How Can Data Be Manipulated Indirectly Through Addresses?

### Core Question

How can one value refer to another object and use its address to access or modify it?

### Learning Objectives

- Distinguish object, address, pointer, and pointee.
- Use `&` and `*`.
- Explain indirection and aliasing.
- Use pointer parameters to modify caller data.
- Identify null, dangling, and out-of-range pointers.

### Suggested Material Sequence

1. An object occupies a location in memory.
2. An address is a value that can be stored.
3. Pointer type and target.
4. Address-of and dereference.
5. Pointer-and-pointee state diagram.
6. Aliasing.
7. Pointer parameter.
8. Null pointer.
9. Pointer arithmetic and arrays.
10. Lifetime and memory safety.

### Error Cases

- Dereferencing an uninitialized pointer.
- Dereferencing a null pointer.
- Pointer to an object whose lifetime has ended.
- Pointer arithmetic outside an array.

### Practice Directions

- Draw pointer-to-object relationships.
- Predict modification through aliases.
- Swap two values using pointer parameters.
- Correct invalid-pointer cases.

### Post-Unit Concept Explanation

Explain to AI the relationship among address, pointer, dereference, and pointee.

### Unit Summary

A pointer stores an address, and dereference allows indirect access to another object through that address.

---

## F-U07 — How Can One Data Object Contain Different Fields?

### Core Question

When one entity contains several kinds of data, how can those fields be combined into one meaningful object?

### Learning Objectives

- Explain structure type, object, and member.
- Create and initialize structure objects.
- Access and update members.
- Pass a structure or structure pointer.
- Understand nested structures and layout.

### Suggested Material Sequence

1. One entity needs fields of different types.
2. `struct` defines a new type.
3. Structure object.
4. Member access.
5. Initialization and assignment.
6. Structure as function parameter and return value.
7. Structure pointer and `->`.
8. Nested structure.
9. Array of structures.
10. `typedef` and interface readability.

### Error Cases

- Confusing type definition with object creation.
- Incorrect use of `.` and `->`.
- Uninitialized members.
- Invalid lifetime of a structure pointer.

### Practice Directions

- Create student, coordinate, or date structures.
- Update or compare structures through functions.
- Traverse an array of structures.
- Trace member paths through nested structures.

### Post-Unit Concept Explanation

Explain to AI the relationship among structure type, structure object, member, and member access.

### Unit Summary

A structure lets fields of different types jointly describe one meaningful entity.

---

## F-U08 — How Does a Program Obtain and Release Space During Execution?

### Core Question

When data size or lifetime cannot be fixed in advance, how does a program manage storage?

### Learning Objectives

- Explain why dynamic allocation is needed.
- Use `malloc`, `calloc`, `realloc`, and `free`.
- Understand ownership and lifetime.
- Identify leaks, dangling pointers, and double free.
- Build a complete allocate-use-resize-release process.

### Suggested Material Sequence

1. Limits of fixed-size data.
2. Dynamically allocated storage and pointer.
3. `malloc` and allocation failure.
4. `calloc`.
5. Handling `realloc` success and failure.
6. `free`.
7. Ownership: who is responsible for release.
8. Memory leak.
9. Dangling pointer and double free.
10. Observing memory problems through tools or tests.

### Error Cases

- Not checking allocation result.
- Overwriting the only pointer and causing a leak.
- Using memory after release.
- Releasing memory twice.
- Losing the original pointer after failed `realloc`.

### Practice Directions

- Dynamically create an integer array.
- Expand data capacity.
- Mark ownership responsibility.
- Diagnose allocation and release errors.

### Post-Unit Concept Explanation

Explain to AI the relationship among dynamic allocation, ownership, lifetime, and `free`.

### Unit Summary

Dynamic memory provides flexibility, but the program must explicitly manage ownership and release responsibility.

---

## F-U09 — How Does a Program Interact with Files and Persistent Data?

### Core Question

When data must remain after a program ends, how does the program read, write, and detect errors?

### Learning Objectives

- Explain stream, file, position, and EOF.
- Open, read, write, and close files.
- Check file-operation results.
- Distinguish file format from internal representation.
- Design reproducible file-error handling.

### Suggested Material Sequence

1. Temporary input/output and persistent data.
2. Stream model.
3. `FILE *`.
4. `fopen` modes.
5. Text output.
6. Text input.
7. EOF and function return values.
8. Format and protocol.
9. Closing files and resource responsibility.
10. Error channel and diagnostics.

### Error Cases

- Using a stream after file-open failure.
- Incorrect `feof` pattern.
- Forgetting to close a file.
- Write format inconsistent with read format.

### Practice Directions

- Write records and read them back.
- Design a simple text-file format.
- Handle missing or malformed files.
- Compare normal end-of-input with read errors.

### Post-Unit Concept Explanation

Explain to AI the relationship among stream, file, EOF, format, and protocol.

### Unit Summary

File interaction is stateful data-flow processing that must handle format, termination, and errors.

---

## F-U10 — How Can a Program Be Divided into Independently Maintainable Modules?

### Core Question

How can interface and implementation be separated so different program parts can be understood, compiled, and replaced independently?

### Learning Objectives

- Explain module, interface, and implementation.
- Distinguish header file and source file.
- Understand separate compilation and linking.
- Use include guards.
- Design clear module responsibilities.

### Suggested Material Sequence

1. Limits of one source file.
2. Module and responsibility.
3. What an interface should reveal.
4. What an implementation should hide.
5. Header file.
6. Source file.
7. `#include` and include guard.
8. Separate compilation.
9. Linking and unresolved symbols.
10. Changing implementation without changing interface.

### Error Cases

- Inappropriate definitions in a header.
- Missing include guard.
- Declaration-definition mismatch.
- Forgetting to link one source file.

### Practice Directions

- Divide a one-file program into modules.
- Design function interfaces.
- Correct a linking error.
- Replace a module implementation and rerun regression tests.

### Post-Unit Concept Explanation

Explain to AI the relationship among module, interface, implementation, separate compilation, and linking.

### Unit Summary

Modularity keeps interfaces stable while implementations can be understood, tested, and replaced independently.

---

## F-U11 — How Can Programs Be Proven, Diagnosed, and Improved Systematically?

### Core Question

What evidence beyond correct output is needed before a program can be trusted?

### Learning Objectives

- Distinguish testing, verification, and validation.
- Reproduce and narrow an error systematically.
- Design normal, boundary, error, and regression tests.
- Read and review existing programs.
- Refactor while preserving behavior.

### Suggested Material Sequence

1. Why one correct output is insufficient.
2. Expected result and test case.
3. Normal, boundary, and error cases.
4. Verification and validation.
5. Reproduce, isolate, hypothesize, test.
6. Error diagnosis.
7. Regression testing.
8. Code reading.
9. Code review.
10. Refactoring and behavior preservation.

### Error Cases

- Testing only one case.
- Fixing a symptom without finding the cause.
- Failing to rerun tests after modification.
- Changing behavior during refactoring.

### Practice Directions

- Add tests to an existing program.
- Narrow an error from its symptom.
- Compare behavior before and after correction.
- Review another program that runs but is unreliable.

### Post-Unit Concept Explanation

Explain to AI the differences among testing, verification, validation, debugging, and regression.

### Unit Summary

A trustworthy program requires reproducible tests, a diagnostic process, and evidence after correction—not one apparently correct output.

---

## F-U12 — How Can a Program Integrate Concepts Across the Course?

### Core Question

How can requirements, data, control, functions, memory, interaction, and engineering be integrated into one maintainable program?

### Learning Objectives

- Build data and function models from requirements.
- Divide a program into modules and responsibilities.
- Choose suitable data representation and storage.
- Establish testing, error handling, and regression processes.
- Explain design decisions and limitations.

### Suggested Material Sequence

1. Read and clarify requirements.
2. Define input, output, and constraints.
3. Build a data model.
4. Define function and module responsibilities.
5. Plan control flow.
6. Decide memory and resource responsibility.
7. Design interfaces and file formats.
8. Build the smallest executable version.
9. Test, debug, modify, and regress.
10. Explain and reflect on design choices.

### Suggested Integration Projects

- Small student or membership record system.
- Text-file data-analysis tool.
- Simple inventory or grade-management system.
- Small program with querying, modification, persistence, and error handling.

### Error Cases

- Starting implementation before clarifying requirements.
- Concentrating all responsibilities in `main`.
- Inconsistent file format and module interface.
- Missing tests and error handling.
- Breaking existing behavior after feature changes.

### Practice Directions

- Convert requirements into a Concept and responsibility list.
- Create module and data-flow diagrams.
- Implement and test in stages.
- Run regression verification after requirement changes.
- Explain the overall design orally.

### Post-Unit Concept Explanation

Explain to AI how your integrated program connects data, control, functions, memory, interaction, and testing.

### Unit Summary

An integrated program does not merely combine syntax. It coordinates multiple Concepts through clear responsibilities to solve a requirement.

---

## Material Development Order After These Outlines

1. Complete the full Chinese and English student materials for P-U01.
2. Revise the shared chapter template using lessons learned from writing P-U01.
3. Complete P-U02, P-U03, and P-U04 in order.
4. Trial the preparatory Units and record student reading and comprehension problems.
5. Expand F-U01 through F-U12 in formal-course order.
6. Every completed Unit must be checked against the Concept Registry, Unit Map, and Constitution 1.3.0.

## Navigation

- [Programming Concept Tree](14-programming-concept-tree.en.md)
- [Programming Concept Registry](15-programming-concept-registry.en.md)
- [Concept-Driven Unit Map](16-unit-map.en.md)
- [Instructional Design Workspace](README.en.md)
- [繁體中文版](17-student-material-outlines.zh-TW.md)
