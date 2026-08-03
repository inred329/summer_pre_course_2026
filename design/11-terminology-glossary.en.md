# Chinese–English Terminology Glossary

Version: 0.1.0  
Status: Official design baseline  
Last updated: 2026-08-03  
Major change summary: Established the shared Chinese–English terminology baseline for course design, materials, activities, and assessment.  
Corresponding Chinese version: [中英文術語對照表](11-terminology-glossary.zh-TW.md)

## Document Purpose

This document provides the terminology baseline used across official course documents so that the domain model, knowledge dependencies, competencies, scope, acceptance, delivery, risks, materials, and assessment use consistent names.

Its primary readers are instructors, teaching assistants, material authors, translators, and maintainers. When an important term is added or revised, both language versions and affected documents must be updated together.

## Usage Rules

1. Important terms should include both Chinese and English when first introduced, where appropriate.
2. The same concept must not be renamed arbitrarily across documents.
3. English wording should follow professional conventions rather than literal translation.
4. When one English term has different meanings in different contexts, the notes column must distinguish them.
5. Check for an existing approved term before adding a new one.
6. Program identifiers, function names, and C keywords are generally not translated.

## Core Course Terminology

| Chinese | English | Usage Note |
|---|---|---|
| 程式設計 | Programming | The activity and capability of using a programming language to construct an executable solution. |
| 領域模型 | Domain Model | Describes which concepts exist and how they relate; it does not define teaching order. |
| 知識依賴圖 | Knowledge Dependency Graph | Describes prerequisite knowledge usually needed before another concept. |
| 能力地圖 | Competency Map | Describes what students must be able to do and the target maturity. |
| 範圍邊界 | Scope Boundary | Defines core delivery, foundations, deferrals, and out-of-scope content. |
| 驗收模型 | Acceptance Model | Defines tasks, evidence, and passing criteria needed to establish capability. |
| 交付地圖 | Delivery Map | Arranges competencies, maturity, and evidence into course stages and units. |
| 風險登錄表 | Risk Register | Records risks, triggers, mitigation, contingency, and accountable roles. |
| 追蹤矩陣 | Traceability Matrix | Connects requirements, concepts, competencies, acceptance, delivery, and risk. |
| 成熟度 | Maturity | Observable degree of capability: recognize, explain, trace, implement, diagnose, and transfer. |
| 學習證據 | Learning Evidence | Observable work or behavior supporting a capability claim. |
| 核心交付 | Core Delivery | Capability that must be achieved and formally evidenced by the end of a course stage. |
| 基礎鋪墊 | Foundation Only | Establishes terminology, purpose, and models without claiming independent implementation. |
| 延後深化 | Deepen Later | An initial capability exists, while higher maturity is deferred. |
| 延後實作 | Implement Later | Understanding or tracing is possible, while full implementation and diagnosis are intentionally deferred. |
| 課程外 | Out of Scope | Not part of the current course’s core delivery. |

## Program Execution and Toolchain

| Chinese | English | Usage Note |
|---|---|---|
| 原始碼 | Source Code | Human-written program text processed by the toolchain. |
| 前置處理器 | Preprocessor | Handles `#include`, macros, and conditional compilation. |
| 編譯器 | Compiler | Translates high-level language and performs syntax and semantic checks. |
| 組譯器 | Assembler | Converts assembly language into object code. |
| 目的檔 | Object File | Output awaiting linking after compilation and assembly. |
| 連結器 | Linker | Combines object files and libraries into an executable. |
| 可執行檔 | Executable | A program image that can be loaded by the operating system. |
| 載入器 | Loader | Maps an executable into a running process. |
| 程序 | Process | A running program together with its resources and state. |
| 標準函式庫 | Standard Library | The standard set of functionality provided by the C environment. |

## Data, Control, and Functions

| Chinese | English | Usage Note |
|---|---|---|
| 值 | Value | Information content processed by a program. |
| 型別 | Type | Constrains representation, range, and permitted operations. |
| 變數 | Variable | A named data entity referring to mutable state. |
| 常數 | Constant | A value that should not change within a stated semantic context. |
| 運算式 | Expression | A combination of values, names, and operators that can be evaluated. |
| 指定 | Assignment | Writes a result into a data location and changes state. |
| 狀態 | State | The data situation of a program at a given execution moment. |
| 順序 | Sequence | Statements execute in temporal order. |
| 條件 | Condition | Produces a true-or-false judgment from current data. |
| 選擇 | Selection | Chooses an execution path based on a condition. |
| 重複 | Repetition | Repeats under a condition with state updates. |
| 終止條件 | Termination Condition | Determines when repetition stops. |
| 函數 | Function | A callable unit that encapsulates one named responsibility. |
| 參數 | Parameter | A named input declared by a function interface. |
| 引數 | Argument | The actual value or expression supplied in a function call. |
| 回傳值 | Return Value | A result returned through the function interface. |
| 作用域 | Scope | The program region in which a name may be used. |
| 生命週期 | Lifetime | The period in which a data entity exists and remains valid. |
| 模組化 | Modularization | Organizes related responsibilities and implementations through explicit interfaces. |
| 遞迴 | Recursion | A problem representation in which a function directly or indirectly calls itself. |

## Memory and Data Organization

| Chinese | English | Usage Note |
|---|---|---|
| 儲存位置 | Storage Location | The memory region in which a data entity resides. |
| 位址 | Address | A value identifying a storage location. |
| 指標 | Pointer | A typed variable that stores an address. |
| 取址 | Address-of | The operation of obtaining an object’s address. |
| 解參考 | Dereference | Accessing a target object through an address. |
| 別名 | Alias | A relationship in which multiple names or pointers refer to one data location. |
| 自動儲存期 | Automatic Storage Duration | Storage duration commonly associated with blocks and function calls. |
| 動態儲存期 | Dynamic Storage Duration | Storage acquired and released during execution. |
| 呼叫堆疊 | Call Stack | The execution structure that preserves function-call and return information. |
| Heap | Heap | The English term is retained in Chinese materials to avoid confusion with the heap data structure. |
| 序列 | Sequence | Multiple elements organized by position or order. |
| 索引 | Index | A method of locating data by position or key. |
| 字串 | String | Text represented as a sequence of characters. |
| 記錄 | Record | A group of fields describing one entity. |
| 結構 | Structure / `struct` | The C language mechanism for creating record-shaped data. |
| 搜尋 | Search | An operation that locates data satisfying a condition. |
| 重新排列 | Rearrangement | Changes element order according to a rule; a specific sorting algorithm is not necessarily core. |

## Testing, Debugging, and AI

| Chinese | English | Usage Note |
|---|---|---|
| 預期結果 | Expected Result | A result derived from the requirement before execution. |
| 實際結果 | Actual Result | The observed result after execution. |
| 測試案例 | Test Case | A concrete statement of input, conditions, and expected result. |
| 正常案例 | Normal Case | Verifies ordinary use. |
| 邊界案例 | Boundary Case | Verifies thresholds, ranges, and transition points. |
| 異常案例 | Exceptional Case | Verifies invalid or unexpected input when applicable. |
| 執行追蹤 | Execution Trace | Step-by-step recording of data, control, calls, or memory changes. |
| 除錯 | Debugging | Uses evidence to reproduce, narrow, hypothesize, and verify a cause. |
| 回歸測試 | Regression Testing | Confirms that a correction did not break previously correct behavior. |
| AI 輔助學習 | AI-assisted Learning | Uses AI for explanation, hints, testing, and debugging without replacing core thinking. |
| 人工審查 | Human Review | A learner or teacher evaluates whether an AI suggestion is appropriate. |
| 技術驗證 | Technical Verification | Confirms claims through documentation, compilation, execution, tracing, and testing. |
| AI 使用紀錄 | AI-use Record | Records the goal, prior state, suggestion summary, verification, decision, and reason. |

## Maturity Terms

| Level | Chinese | English |
|---|---|---|
| L0 | 尚未建立 | Not Established |
| L1 | 辨識 | Recognize |
| L2 | 解釋 | Explain |
| L3 | 追蹤 | Trace |
| L4 | 實作 | Implement |
| L5 | 診斷 | Diagnose |
| L6 | 遷移 | Transfer |

## Maintenance and Completion Criteria

This glossary is complete only when:

- Both language versions exist and are substantively equivalent.
- Every official material and assessment uses consistent terms.
- Each new term includes a definition or usage note.
- Potentially confusing terms are explicitly distinguished.
- Changes remain traceable through a Git commit, Issue, or PR.

## Navigation

- [Previous stage: Course Design Traceability Matrix](10-traceability-matrix.en.md)
- [Back to Instructional Design Workspace](README.en.md)
- [繁體中文版](11-terminology-glossary.zh-TW.md)
