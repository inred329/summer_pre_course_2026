# Formal Course Student Materials

Version: 1.2.0  
Status: Complete bilingual student-material set  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式課程學生教材](README.zh-TW.md)

## Formal-course students start here

The formal course now starts with F-U00. F-U00 does not require you to take the preparatory path first; it separates the roles of source code, compiler, Build, executable, Run, and Debug that the formal course will keep using.

**[Start F-U00: What Actually Happens After You Press Run?](unit-00-build-run-ide.en.md)**

The preparatory Units remain available for foundation review, not as a required reading path for formal-course students. If variables and state, conditions and loops, or basic functions and parameters feel unfamiliar, return to the relevant preparatory Unit only when you need it.

## Units

| Unit | English | Traditional Chinese | Central focus |
|---|---|---|---|
| F-U00 | [What Actually Happens After You Press Run?](unit-00-build-run-ide.en.md) | [按下 Run 之後，到底發生了什麼？](unit-00-build-run-ide.zh-TW.md) | source, compiler, IDE, Build, Run, Debug, stale executables |
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

## Reading order

Read F-U00 through F-U12 in order. Each Unit ends with a link to the next one, so after starting F-U00 you can follow the learning path forward without returning to the repository home page or opening internal course documents to find the next step.

The formal course uses these basic capabilities:

- edit, Build, and run a simple C program while understanding that the IDE is not the compiler
- trace changes in variables and values
- read basic conditions and loops
- understand the basic roles of functions, parameters, and return values

If one of the last three foundations feels unfamiliar, review the corresponding preparatory Unit when needed. The preparatory course is not a fixed prerequisite reading list for the formal-course path.

## Completing a Unit

Completing a Unit means more than producing one correct output. You should gradually be able to explain the central concept, predict or trace behavior, implement a minimal case, reproduce and diagnose a typical error, test normal and boundary behavior, and identify affected parts when a requirement changes.

AI use is not part of the core completion standard. Any AI activity explicitly marked optional may be skipped.

## Navigation

- [Student entry](../STUDENT-START.en.md)
- [Start F-U00](unit-00-build-run-ide.en.md)
- [繁體中文版](README.zh-TW.md)
