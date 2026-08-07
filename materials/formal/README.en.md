# Formal Course Student Materials

Version: 1.0.2  
Status: Complete bilingual student-material set  
Last updated: 2026-08-06  
Corresponding Chinese version: [正式課程學生教材](README.zh-TW.md)

## Purpose

This directory contains the 12 formal-course student Units that follow the four preparatory Units. Each Unit is designed for independent reading, review, experimentation, diagnosis, and explanation.

The materials use C as the instructional language while emphasizing transferable programming Concepts. Each Unit builds its main learning path from a core question, mental model, minimal examples, prediction or tracing, reproducible errors, practice, requirement modification, self-check, and summary.

Some Units also provide clearly marked optional AI extensions. These activities may be skipped. Not using AI does not affect Unit completion, classroom participation, or assessment. When a student chooses to use AI, its claims must still be judged through code, compiler behavior, tracing, testing, or other reproducible evidence.

## Units

| Unit | English | Traditional Chinese | Central focus |
|---|---|---|---|
| F-U01 | [Representation, Types, and Operations](unit-01-representation-types.en.md) | [表示、型別與運算](unit-01-representation-types.zh-TW.md) | binary representation, MSB/LSB, ranges, conversion, formatted output |
| F-U02 | [Complex Control Flow](unit-02-complex-control-flow.en.md) | [複雜控制流程](unit-02-complex-control-flow.zh-TW.md) | branches, sentinels, invariants, boundaries |
| F-U03 | [Arrays](unit-03-arrays.en.md) | [陣列](unit-03-arrays.zh-TW.md) | collections, indexing, traversal, bounds |
| F-U04 | [Strings](unit-04-strings.en.md) | [字串](unit-04-strings.zh-TW.md) | character arrays, null terminator, buffers |
| F-U05 | [Call Stack and Recursion](unit-05-call-stack-recursion.en.md) | [呼叫堆疊與遞迴](unit-05-call-stack-recursion.zh-TW.md) | call frames, scope, lifetime, base cases |
| F-U06 | [Pointers](unit-06-pointers.en.md) | [指標](unit-06-pointers.zh-TW.md) | addresses, indirection, aliases, null pointers |
| F-U07 | [Structures](unit-07-structures.en.md) | [結構](unit-07-structures.zh-TW.md) | heterogeneous records, layout, member access |
| F-U08 | [Dynamic Memory](unit-08-dynamic-memory.en.md) | [動態記憶體](unit-08-dynamic-memory.zh-TW.md) | allocation, ownership, lifetime, release |
| F-U09 | [Files](unit-09-files.en.md) | [檔案](unit-09-files.zh-TW.md) | streams, persistence, EOF, error checking |
| F-U10 | [Modular Programming](unit-10-modular-programming.en.md) | [模組化程式設計](unit-10-modular-programming.zh-TW.md) | interface, implementation, headers, linking |
| F-U11 | [Testing and Debugging](unit-11-testing-debugging.en.md) | [測試、診斷與改善](unit-11-testing-debugging.zh-TW.md) | testing, verification, validation, debugging, regression, refactoring |
| F-U12 | [Integrated Application](unit-12-integrated-application.en.md) | [整合應用程式](unit-12-integrated-application.zh-TW.md) | requirements, data model, memory, files, modules, evidence |

## Recommended Reading Order

Read F-U01 through F-U12 in order. The formal course assumes that the preparatory Units have established:

- source code, compilation, and execution
- data, values, types, variables, and state
- conditions, loops, boundaries, and tracing
- functions, responsibility, parameters, return values, and basic testing

## Completion Standard

Completing a Unit means more than producing one correct output. Students should be able to:

- explain the central Concept
- predict or trace behavior
- implement a minimal case
- reproduce and diagnose a typical error
- test normal and boundary behavior
- modify a requirement and identify affected parts
- support decisions with observable evidence

AI use is not part of the core completion standard. Activities are independent practice unless another official course document explicitly states otherwise.

## Navigation

- [Materials and Activity Resources](../README.en.md)
- [Preparatory Unit P-U04](../preparatory/unit-04-functions-integration.en.md)
- [Instructional Design Workspace](../../design/README.en.md)
- [繁體中文版](README.zh-TW.md)
