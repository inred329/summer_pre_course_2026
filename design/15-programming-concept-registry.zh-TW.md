# 程式設計 Concept Registry

版本：0.1.1  
狀態：現行設計標準  
治理說明：本標準為 Concept 指派穩定 ID 與依賴／範圍 metadata；能力成熟度由 `05-competency-map.*` 與 `06-scope-boundary.*` 定義，本 Registry 不重新定義 L1–L6，也不建立評量／工具政策。  
對應英文版本：[Programming Concept Registry](15-programming-concept-registry.en.md)

## 文件目的

Concept Tree 回答「有哪些概念？」；本 Registry 為這些概念建立穩定識別碼、主要先備關係與粗粒度課程位置，讓 Units 與教材能一致引用。

一般文字修訂應保留 Concept ID。若刻意將概念改名、拆分或合併，必須在同一批變更中同步更新相依 Unit／教材與 active traceability／audit 紀錄。

## ID Prefix

| 領域 | Prefix |
|---|---|
| Computation | `CT-C` |
| Information | `CT-I` |
| State | `CT-S` |
| Control Flow | `CT-F` |
| Abstraction | `CT-A` |
| Memory and Lifetime | `CT-M` |
| Interaction | `CT-X` |
| Engineering and Verification | `CT-E` |
| Composite Concept | `CT-K` |

## 課程位置 Marker

以下只作 Registry 導覽，不重新定義成熟度：

- `P-C`：前導核心概念。
- `P-F`：前導基礎鋪墊，可於正式課程深化／實作。
- `F-C`：正式課程核心概念。
- `F-A`：正式課程進階／延後概念；是否納入仍須通過範圍理由。
- `X`：條件式／選用概念；只有對應選用活動／工具實際使用時才適用。

實際成熟度意義使用 `05-competency-map.*`／`11-terminology-glossary.*` 的標準 `L0–L6`；核心／選用決策以 `06-scope-boundary.*` 為準。

---

## Computation

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-C01 | Problem | — | P-C |
| CT-C02 | Requirement | CT-C01 | P-C |
| CT-C03 | Algorithm / Design Procedure | CT-C01、CT-C02 | P-C |
| CT-C04 | Program | CT-C03 | P-C |
| CT-C05 | Source Code | CT-C04 | P-C |
| CT-C06 | C Translation | CT-C05 | P-C |
| CT-C07 | C Implementation / Compiler Tool | CT-C06 | P-C |
| CT-C08 | Executable / Loadable Program Representation | CT-C06、CT-C07 | P-C |
| CT-C09 | Execution | CT-C08 | P-C |
| CT-C10 | Process / Runtime Instance | CT-C09 | P-F |
| CT-C11 | Termination | CT-C09 | P-C |
| CT-C12 | Diagnostic | CT-C06 | P-C |

`CT-C06–C08` 描述概念責任。除非目標工具鏈實際暴露，不推定一定存在獨立 preprocessor、assembler、linker、object file 或特定 OS executable 格式。

---

## Information

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-I01 | Data | CT-C04 | P-C |
| CT-I02 | Value | CT-I01 | P-C |
| CT-I03 | Representation | CT-I01、CT-I02 | P-F |
| CT-I04 | Type | CT-I02、CT-I03 | P-C |
| CT-I05 | Identifier | CT-C05 | P-C |
| CT-I06 | Literal / Constant Form | CT-I02、CT-I04 | P-C |
| CT-I07 | Expression | CT-I02、CT-I04、CT-I05 | P-C |
| CT-I08 | Operator | CT-I07 | P-C |
| CT-I09 | Evaluation | CT-I07、CT-I08 | P-C |
| CT-I10 | Conversion | CT-I03、CT-I04、CT-I09 | P-F |
| CT-I11 | Collection | CT-I01、CT-I04 | F-C |

---

## State

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-S01 | State | CT-C09、CT-I02 | P-C |
| CT-S02 | State Change | CT-S01、CT-I09 | P-C |
| CT-S03 | Variable / Named Object | CT-I04、CT-I05、CT-S01 | P-C |
| CT-S04 | Declaration | CT-I04、CT-I05 | P-C |
| CT-S05 | Definition | CT-S04 | P-F |
| CT-S06 | Initialization | CT-S03、CT-S04 | P-C |
| CT-S07 | Assignment | CT-S02、CT-S03、CT-I07 | P-C |
| CT-S08 | Update | CT-S07 | P-C |
| CT-S09 | Scope | CT-I05、CT-S04 | F-C |
| CT-S10 | Lifetime | CT-S03、CT-M04 | F-C |
| CT-S11 | Invariant | CT-S01、CT-F05 | F-C |

---

## Control Flow

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-F01 | Sequence | CT-C09 | P-C |
| CT-F02 | Condition | CT-I07、CT-I09 | P-C |
| CT-F03 | Selection / Decision | CT-F02 | P-C |
| CT-F04 | Branch / Transfer | CT-F03 | P-F |
| CT-F05 | Repetition | CT-F02、CT-S02 | P-C |
| CT-F06 | Iteration | CT-F05、CT-S08 | P-C |
| CT-F07 | Loop Condition | CT-F02、CT-F05 | P-C |
| CT-F08 | Boundary | CT-I08、CT-F02 | P-C |
| CT-F09 | Sentinel / End Condition | CT-F02、CT-X01 | P-C |
| CT-F10 | Nested Control | CT-F03、CT-F05 | P-F |
| CT-F11 | Nontermination | CT-F05、CT-F07、CT-S08 | P-C |

---

## Abstraction

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-A01 | Decomposition | CT-C01、CT-C03 | P-C |
| CT-A02 | Responsibility | CT-A01 | P-C |
| CT-A03 | Function | CT-A01、CT-A02、CT-F01 | P-C |
| CT-A04 | Interface | CT-A02、CT-A03 | P-F |
| CT-A05 | Implementation | CT-A03、CT-A04 | P-F |
| CT-A06 | Parameter | CT-A03、CT-I04、CT-S04 | P-C |
| CT-A07 | Argument | CT-A03、CT-I07 | P-C |
| CT-A08 | Return Value | CT-A03、CT-I02 | P-C |
| CT-A09 | Call | CT-A03、CT-F01 | P-C |
| CT-A10 | Activation Model | CT-A09、CT-M04、CT-S10 | F-C |
| CT-A11 | Recursion | CT-A03、CT-A09、CT-F02、CT-C11 | F-A |
| CT-A12 | Module | CT-A04、CT-A05 | F-C |

`CT-A10` 可依目標實作用 call stack 視覺化，但實體 stack representation 不是 C 語言保證。

---

## Memory and Lifetime

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-M01 | Bit | CT-I03 | F-C |
| CT-M02 | Byte | CT-M01 | F-C |
| CT-M03 | Address | CT-M02、CT-M04 | F-C |
| CT-M04 | Object / Storage | CT-I02、CT-I04 | P-F |
| CT-M05 | Layout | CT-M03、CT-M04 | F-C |
| CT-M06 | Pointer | CT-M03、CT-I04 | F-C |
| CT-M07 | Indirection / Dereference | CT-M06 | F-C |
| CT-M08 | Aliasing | CT-M06、CT-M07 | F-C |
| CT-M09 | Null Pointer | CT-M06 | F-C |
| CT-M10 | Storage Duration | CT-M04 | F-C |
| CT-M11 | Automatic Storage / Call-Lifetime Model | CT-M10、CT-A09 | F-C |
| CT-M12 | Static Storage | CT-M10 | F-C |
| CT-M13 | Allocated Storage / Dynamic Allocation | CT-M03、CT-M04、CT-M06 | F-C |
| CT-M14 | Ownership / Release Responsibility | CT-M13、CT-S10 | F-C |
| CT-M15 | Memory Safety | CT-M05、CT-M06、CT-M10、CT-M13 | F-C |

「heap」與實體「stack」是常見實作／教學用語，不是 C abstract machine 必須具有的區域。語言層級需要精確時，優先使用 `allocated storage` 與 `automatic storage duration`。

---

## Interaction

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-X01 | Input | CT-I01、CT-C09 | P-C |
| CT-X02 | Output | CT-I01、CT-C09 | P-C |
| CT-X03 | Stream | CT-X01、CT-X02 | P-F |
| CT-X04 | Format | CT-I03、CT-X01、CT-X02 | P-C |
| CT-X05 | Buffer | CT-M04、CT-X03 | F-C |
| CT-X06 | File | CT-X03 | F-C |
| CT-X07 | End of Input | CT-X01、CT-X03 | P-F |
| CT-X08 | Error Channel / Error State | CT-X02、CT-X03 | P-F |
| CT-X09 | Command-Line Input | CT-C09、CT-X01 | F-C |
| CT-X10 | Protocol | CT-C02、CT-X01、CT-X02 | F-C |

---

## Engineering and Verification

| ID | Concept | 主要依賴 | Placement |
|---|---|---|---|
| CT-E01 | Expected Result / Property | CT-C02、CT-I02 | P-C |
| CT-E02 | Test Case | CT-E01、CT-X01、CT-X02 | P-C |
| CT-E03 | Testing | CT-E02、CT-C09 | P-C |
| CT-E04 | Verification | CT-E01、CT-E03 | P-C |
| CT-E05 | Validation | CT-C01、CT-C02、CT-E04 | P-F |
| CT-E06 | Debugging | CT-E03、CT-E04 | P-C |
| CT-E07 | Symptom | CT-E06 | P-C |
| CT-E08 | Cause | CT-E06、CT-E07 | P-C |
| CT-E09 | Hypothesis | CT-E07、CT-E08 | P-C |
| CT-E10 | Regression Verification | CT-E03、CT-E06 | P-C |
| CT-E11 | Code Reading | CT-C05、CT-I07、CT-F01 | P-C |
| CT-E12 | Trace | CT-S01、CT-F01、CT-E11 | P-C |
| CT-E13 | Refactoring | CT-E03、CT-E04、CT-A01 | F-C |
| CT-E14 | Documentation | CT-C02、CT-A04 | P-F |
| CT-E15 | Version Control | CT-C05、CT-E14 | F-C |
| CT-E16 | External Assistance | CT-E01、CT-E04、CT-E09 | X |
| CT-E17 | Evidence | CT-E01、CT-E04 | P-C |
| CT-E18 | Judgment | CT-E04、CT-E05、CT-E17 | P-C |
| CT-E19 | Human Review of External Suggestions | CT-E16、CT-E18 | X |
| CT-E20 | Contextual Disclosure | CT-E16、CT-E17 | X |

`CT-E16`、`CT-E19`、`CT-E20` 都是條件式，不推定 AI 必用、固定 prompt、log、before/after artifact 或未使用聲明。學生若實際採用外部協助，核心 verification／evidence Concept 仍然適用。

---

## Composite Concepts

| ID | Composite Concept | Component concepts | Placement | 說明 |
|---|---|---|---|---|
| CT-K01 | Array | CT-I11、CT-M04、CT-M05、CT-F08、CT-F06、CT-M15 | F-C | 同元素型別陣列，需明確 index／bounds／lifetime 推理。 |
| CT-K02 | String | CT-I11、CT-I03、CT-K01、CT-F08、CT-X04、CT-X05 | F-C | Null-terminated character sequence，加上 capacity／format 邊界。 |
| CT-K03 | Structure / Record | CT-I11、CT-I04、CT-M04、CT-M05 | F-C | 將相關欄位組成 structure object／type。 |
| CT-K04 | File I/O | CT-X03、CT-X06、CT-X07、CT-X10、CT-E03 | F-C | 包含 stream state、format、error 與 resource lifetime 的外部／持久資料互動。 |
| CT-K05 | Modular Programming | CT-A01、CT-A02、CT-A04、CT-A05、CT-A12、CT-C06 | F-C | 跨 translation／build 邊界的 interface／implementation 組織。 |

---

## 代表性依賴鏈

### 從程式到可觀察證據

```text
CT-C01 Problem
→ CT-C02 Requirement
→ CT-C03 Algorithm / Design
→ CT-C04 Program
→ CT-C05 Source Code
→ CT-C06 C Translation
→ CT-C08 Executable / Loadable Representation
→ CT-C09 Execution
→ CT-E01 Expected Result / Property
→ CT-E04 Verification
```

### 資料與狀態

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-S03 Variable / Named Object
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
→ CT-F03 Selection
→ CT-F05 Repetition
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Nontermination
```

### 函數與分解

```text
CT-C01 Problem
→ CT-A01 Decomposition
→ CT-A02 Responsibility
→ CT-A03 Function
→ CT-A04 Interface
→ CT-A06 Parameter
→ CT-A07 Argument
→ CT-A08 Return Value
→ CT-A09 Call
```

### 條件式外部協助

```text
Relevant Core Understanding
→ CT-E16 External Assistance（選用）
→ CT-E19 Human Review
→ CT-E04 Verification
→ CT-E18 Judgment
→ CT-E20 只有明確要求時才做 Contextual Disclosure
```

未使用外部協助的學生完全不需要經過這條條件式鏈。

---

## Unit 組合規則

一個 Unit 應：

1. 由學生可理解的核心問題驅動。
2. 以一條連貫主要依賴鏈組織，而不是語法清單。
3. 控制新概念數量，必要先備要預先建立或在開頭補齊。
4. 至少包含 Expected Result、Trace、Testing、Debugging 或 Verification 等 Engineering Concept。
5. 把 C syntax 當具體映射，而不是唯一組織原則。
6. 清楚指出 newly introduced、deepened、reused Concept。
7. `X` Concept 維持選用／條件式，除非經核准活動明確以它為學習目標，否則不得進入核心完成鏈。

## 維護規則

- 除非有記錄的 migration 必要，保留穩定 ID。
- 中英文版本維持實質等值。
- 不在本 Registry 私自重新定義成熟度。
- ID 意義改變時檢查 `05`、`06`、`11`、`14`、`16` 與相依教材。
- 重大變更記錄到 active repository audit。

## 相關文件

- [程式設計 Concept Tree](14-programming-concept-tree.zh-TW.md)
- [程式設計能力地圖](05-competency-map.zh-TW.md)
- [課程範圍邊界](06-scope-boundary.zh-TW.md)
- [中英文術語對照表](11-terminology-glossary.zh-TW.md)
- [Concept 驅動的 Unit Map](16-unit-map.zh-TW.md)
- [教學內容設計區](README.zh-TW.md)
- [English version](15-programming-concept-registry.en.md)
