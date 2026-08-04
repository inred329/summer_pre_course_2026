# 程式設計 Concept Registry

版本：0.1.0  
狀態：概念識別與依賴草案  
最後更新：2026-08-04  
對應英文版本：[Programming Concept Registry](15-programming-concept-registry.en.md)

## 文件目的

本文件為 Concept Tree 中的核心概念建立穩定 ID、主要依賴、課程範圍與建議成熟度。Concept Tree 回答「有哪些概念」，本 Registry 回答「每個概念如何被追蹤、依賴與組合」。

本文件尚不直接定義 Unit。Unit 應由本 Registry 中相互依賴且具有共同學習問題的 Concept 組成。

## ID 規則

| 領域 | Prefix |
|---|---|
| Computation | `CT-C` |
| Information | `CT-I` |
| State | `CT-S` |
| Control Flow | `CT-F` |
| Abstraction | `CT-A` |
| Memory | `CT-M` |
| Interaction | `CT-X` |
| Engineering | `CT-E` |
| Composite Concept | `CT-K` |

範圍標記：

- `P-C`：前導課程核心
- `P-F`：前導課程鋪墊
- `F-C`：正式課程核心
- `F-A`：正式課程進階或延後

成熟度：

- `L1`：辨識
- `L2`：在引導下完成
- `L3`：能獨立處理熟悉情境
- `L4`：能在需求修改或新情境中應用
- `L5`：能比較、解釋與評估多種做法

## Computation

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-C01 | Problem | — | P-C | L3 |
| CT-C02 | Requirement | CT-C01 | P-C | L3 |
| CT-C03 | Algorithm | CT-C01, CT-C02 | P-C | L3 |
| CT-C04 | Program | CT-C03 | P-C | L3 |
| CT-C05 | Source Code | CT-C04 | P-C | L3 |
| CT-C06 | Translation | CT-C05 | P-C | L2 |
| CT-C07 | Compiler | CT-C06 | P-C | L2 |
| CT-C08 | Executable | CT-C06, CT-C07 | P-C | L2 |
| CT-C09 | Execution | CT-C08 | P-C | L3 |
| CT-C10 | Process | CT-C09 | P-F | L1 |
| CT-C11 | Termination | CT-C09 | P-C | L2 |

## Information

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-I01 | Data | CT-C04 | P-C | L3 |
| CT-I02 | Value | CT-I01 | P-C | L3 |
| CT-I03 | Representation | CT-I01, CT-I02 | P-F | L2 |
| CT-I04 | Type | CT-I02, CT-I03 | P-C | L3 |
| CT-I05 | Identifier | CT-C05 | P-C | L3 |
| CT-I06 | Constant | CT-I02, CT-I04 | P-C | L2 |
| CT-I07 | Expression | CT-I02, CT-I04, CT-I05 | P-C | L3 |
| CT-I08 | Operator | CT-I07 | P-C | L3 |
| CT-I09 | Evaluation | CT-I07, CT-I08 | P-C | L3 |
| CT-I10 | Conversion | CT-I03, CT-I04, CT-I09 | P-F | L2 |
| CT-I11 | Collection | CT-I01, CT-I04 | F-C | L3 |

## State

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-S01 | State | CT-C09, CT-I02 | P-C | L3 |
| CT-S02 | State Change | CT-S01, CT-I09 | P-C | L3 |
| CT-S03 | Variable | CT-I04, CT-I05, CT-S01 | P-C | L3 |
| CT-S04 | Declaration | CT-I04, CT-I05 | P-C | L3 |
| CT-S05 | Definition | CT-S04 | P-F | L2 |
| CT-S06 | Initialization | CT-S03, CT-S04 | P-C | L3 |
| CT-S07 | Assignment | CT-S02, CT-S03, CT-I07 | P-C | L3 |
| CT-S08 | Update | CT-S07 | P-C | L3 |
| CT-S09 | Scope | CT-I05, CT-S04 | F-C | L3 |
| CT-S10 | Lifetime | CT-S03, CT-M04 | F-C | L3 |
| CT-S11 | Invariant | CT-S01, CT-F05 | F-C | L2 |

## Control Flow

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-F01 | Sequence | CT-C09 | P-C | L3 |
| CT-F02 | Condition | CT-I07, CT-I09 | P-C | L3 |
| CT-F03 | Decision | CT-F02 | P-C | L3 |
| CT-F04 | Branch | CT-F03 | P-F | L2 |
| CT-F05 | Repetition | CT-F02, CT-S02 | P-C | L3 |
| CT-F06 | Iteration | CT-F05, CT-S08 | P-C | L3 |
| CT-F07 | Loop Condition | CT-F02, CT-F05 | P-C | L3 |
| CT-F08 | Boundary | CT-I08, CT-F02 | P-C | L3 |
| CT-F09 | Sentinel | CT-F02, CT-X01 | P-C | L3 |
| CT-F10 | Nested Control | CT-F03, CT-F05 | P-F | L2 |
| CT-F11 | Infinite Execution | CT-F05, CT-F07, CT-S08 | P-C | L3 |

## Abstraction

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-A01 | Decomposition | CT-C01, CT-C03 | P-C | L3 |
| CT-A02 | Responsibility | CT-A01 | P-C | L3 |
| CT-A03 | Function | CT-A01, CT-A02, CT-F01 | P-C | L3 |
| CT-A04 | Interface | CT-A02, CT-A03 | P-F | L2 |
| CT-A05 | Implementation | CT-A03, CT-A04 | P-F | L2 |
| CT-A06 | Parameter | CT-A03, CT-I04, CT-S04 | P-C | L3 |
| CT-A07 | Argument | CT-A03, CT-I07 | P-C | L3 |
| CT-A08 | Return Value | CT-A03, CT-I02 | P-C | L3 |
| CT-A09 | Call | CT-A03, CT-F01 | P-C | L3 |
| CT-A10 | Call Stack | CT-A09, CT-M11 | F-C | L2 |
| CT-A11 | Recursion | CT-A03, CT-A09, CT-F02 | F-A | L3 |
| CT-A12 | Module | CT-A04, CT-A05 | F-C | L3 |

## Memory

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-M01 | Bit | CT-I03 | F-C | L2 |
| CT-M02 | Byte | CT-M01 | F-C | L2 |
| CT-M03 | Address | CT-M02 | F-C | L3 |
| CT-M04 | Object | CT-I02, CT-I04, CT-M02 | P-F | L2 |
| CT-M05 | Layout | CT-M03, CT-M04 | F-C | L3 |
| CT-M06 | Pointer | CT-M03, CT-M04, CT-I04 | F-C | L3 |
| CT-M07 | Indirection | CT-M06 | F-C | L3 |
| CT-M08 | Aliasing | CT-M06, CT-M07 | F-C | L2 |
| CT-M09 | Null Reference | CT-M06 | F-C | L3 |
| CT-M10 | Storage Duration | CT-M04, CT-S10 | F-C | L3 |
| CT-M11 | Stack Storage | CT-M10, CT-A09 | F-C | L2 |
| CT-M12 | Static Storage | CT-M10 | F-C | L2 |
| CT-M13 | Dynamic Allocation | CT-M03, CT-M04, CT-M06 | F-C | L3 |
| CT-M14 | Ownership | CT-M13 | F-C | L3 |
| CT-M15 | Memory Safety | CT-M05, CT-M06, CT-M10, CT-M13 | F-C | L4 |

## Interaction

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-X01 | Input | CT-I01, CT-C09 | P-C | L3 |
| CT-X02 | Output | CT-I01, CT-C09 | P-C | L3 |
| CT-X03 | Stream | CT-X01, CT-X02 | P-F | L2 |
| CT-X04 | Format | CT-I03, CT-X01, CT-X02 | P-C | L3 |
| CT-X05 | Buffer | CT-M04, CT-X03 | F-C | L2 |
| CT-X06 | File | CT-X03 | F-C | L3 |
| CT-X07 | End of Input | CT-X01, CT-X03 | P-F | L2 |
| CT-X08 | Error Channel | CT-X02, CT-X03 | P-F | L1 |
| CT-X09 | Command Line | CT-C09, CT-X01 | F-C | L2 |
| CT-X10 | Protocol | CT-C02, CT-X01, CT-X02 | F-C | L2 |

## Engineering

| ID | Concept | 主要依賴 | 範圍 | 目標成熟度 |
|---|---|---|---|---|
| CT-E01 | Expected Result | CT-C02, CT-I02 | P-C | L4 |
| CT-E02 | Test Case | CT-E01, CT-X01, CT-X02 | P-C | L4 |
| CT-E03 | Testing | CT-E02, CT-C09 | P-C | L4 |
| CT-E04 | Verification | CT-E01, CT-E03 | P-C | L4 |
| CT-E05 | Validation | CT-C01, CT-C02, CT-E04 | P-F | L2 |
| CT-E06 | Debugging | CT-E03, CT-E04 | P-C | L4 |
| CT-E07 | Symptom | CT-E06 | P-C | L3 |
| CT-E08 | Cause | CT-E06, CT-E07 | P-C | L3 |
| CT-E09 | Hypothesis | CT-E07, CT-E08 | P-C | L3 |
| CT-E10 | Regression Testing | CT-E03, CT-E06 | P-C | L3 |
| CT-E11 | Code Reading | CT-C05, CT-I07, CT-F01 | P-C | L3 |
| CT-E12 | Trace | CT-S01, CT-F01, CT-E11 | P-C | L4 |
| CT-E13 | Refactoring | CT-E03, CT-E04, CT-A01 | F-C | L3 |
| CT-E14 | Documentation | CT-C02, CT-A04 | P-F | L2 |
| CT-E15 | Version Control | CT-C05, CT-E14 | F-C | L2 |
| CT-E16 | AI-Assisted Programming | CT-E01, CT-E03, CT-E04, CT-E09 | P-C | L4 |
| CT-E17 | Evidence | CT-E01, CT-E04 | P-C | L4 |
| CT-E18 | Judgment | CT-E04, CT-E05, CT-E17 | P-C | L4 |

## Composite Concepts

| ID | Composite Concept | 組成 Concept | 範圍 | 說明 |
|---|---|---|---|---|
| CT-K01 | Array | CT-I11, CT-M04, CT-M05, CT-F08, CT-F06, CT-M15 | F-C | 固定大小、同型別、連續排列的集合。 |
| CT-K02 | String | CT-I11, CT-I03, CT-K01, CT-F08, CT-X04 | F-C | 以字元集合、終止規則與文字格式共同形成。 |
| CT-K03 | Structure | CT-I11, CT-I04, CT-M04, CT-M05 | F-C | 以不同型別成員組成單一資料物件。 |
| CT-K04 | File I/O | CT-X03, CT-X06, CT-X07, CT-X10, CT-E03 | F-C | 持久化資料的讀寫、格式與錯誤處理。 |
| CT-K05 | Modular Programming | CT-A01, CT-A02, CT-A04, CT-A05, CT-A12, CT-C06 | F-C | 以介面、實作與分離編譯組織大型程式。 |

## 第一批依賴鏈

### 程式如何開始執行

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
```

### 資料與狀態

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-S03 Variable
→ CT-S06 Initialization
→ CT-S07 Assignment
→ CT-S02 State Change
→ CT-E12 Trace
```

### 判斷與重複

```text
CT-I07 Expression
→ CT-I08 Operator
→ CT-F02 Condition
→ CT-F03 Decision
→ CT-F05 Repetition
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Infinite Execution
```

### 函數與分解

```text
CT-C01 Problem
→ CT-A01 Decomposition
→ CT-A02 Responsibility
→ CT-A03 Function
→ CT-A06 Parameter
→ CT-A07 Argument
→ CT-A08 Return Value
→ CT-A09 Call
```

## Unit 組合原則

一個 Unit 應符合以下條件：

1. 由一個可理解的核心問題驅動。
2. 包含一條主要依賴鏈，不只是語法清單。
3. 新 Concept 數量受到控制，必要前置 Concept 已存在或在單元開頭明確補足。
4. 同時包含至少一個 Engineering Concept，例如預測、追蹤、測試、除錯或驗證。
5. C 語法只作為 Concept 的具體映射，不作為 Unit 的唯一組織依據。
6. Unit 可以重用已學 Concept，但必須清楚標示本次新增、深化與整合的內容。

## 待確認事項

- `Requirement` 是否應保留在 Computation，或移至 Engineering。
- `Variable` 是否應留在 State，並以 Information 與 Memory 作為依賴。
- `Declaration` 與 `Definition` 是否需要在前導課程分開教學。
- `Process`、`Error Channel` 與 `Storage Duration` 在前導課程應到何種深度。
- `Ownership` 是否以跨語言概念保留，即使 C 沒有語言層級的所有權系統。

## 導覽

- [程式設計 Concept Tree](14-programming-concept-tree.zh-TW.md)
- [教學內容設計區](README.zh-TW.md)
- [English version](15-programming-concept-registry.en.md)
