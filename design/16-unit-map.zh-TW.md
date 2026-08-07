# Concept 驅動的 Unit Map

版本：0.2.1  
狀態：現行設計標準  
治理說明：本標準定義 Unit 識別碼、核心問題、Concept 組合與核心證據方向；不自行定義評分、週次或工具必用規則。  
對應英文版本：[Concept-Driven Unit Map](16-unit-map.en.md)

## 文件目的

本文件將 Concept Tree 與 Concept Registry 中的穩定 Concept 組合成前導與銜接正式 C 課程的可教學、可閱讀、可追蹤 Units。

一個 Unit 應包含：

1. 一個學生能理解的核心問題。
2. 一條連貫的主要 Concept chain／cluster。
3. 受控制數量的首次引入 Concept。
4. 需要深化或重用的既有 Concept。
5. 至少一項預測、追蹤、測試、除錯、修改或驗證活動。
6. 技術邊界明確的 C 具體映射。
7. 不依賴選用外部工具的核心完成／證據方向。

Unit 不自動等於一堂課或一週；實際 delivery slice 另由交付規劃決定。

## Constitution 2.0 對齊原則

- Unit 由 Concept、依賴、範圍與能力證據產生，不只依語法章節順序。
- 學生教材可比本骨架更長或更短，但必須保留核心問題、技術契約與能力方向。
- AI 與其他外部協助預設為選用。核心完成不得要求 AI 對話、AI 概念解釋、AI log、固定 prompt 或未使用聲明。
- 學生若實際使用選用外部協助，仍須自己理解並技術驗證被採用結果。
- 具體工具鏈／runtime 主張必須指出目標環境，不能把常見實作模型寫成 C 語言保證。

## 組合 Marker

- `N`：本 Unit 首次引入。
- `D`：本 Unit 深化。
- `R`：本 Unit 重用。
- `P`：前導課程範圍。
- `F`：正式課程範圍。
- `X`：選用／條件式外部協助活動；不屬普遍完成條件。

---

# 前導課程 Units

## P-U01 — 程式文字如何成為執行結果？

核心問題：**人類可閱讀的程式文字，如何在指定環境中成為電腦可執行的行為？**

主要 Concept chain：

```text
CT-C01 Problem
→ CT-C02 Requirement
→ CT-C03 Algorithm / Design Procedure
→ CT-C04 Program
→ CT-C05 Source Code
→ CT-C06 C Translation
→ CT-C07 C Implementation / Compiler Tool
→ CT-C08 Executable / Loadable Program Representation
→ CT-C09 Execution
→ CT-X02 Output
→ CT-E01 Expected Result / Property
→ CT-E04 Verification
```

Concept 使用：

- `N`：Problem、Requirement、Program、Source Code、C Translation、C Implementation／Compiler Tool、Executable／Loadable Representation、Execution、Output、Expected Result／Property、Diagnostic。
- `D`：Algorithm／Design Procedure。
- `R`：無。

C 映射與技術邊界：

- 最小 `main` 程式。
- `#include <stdio.h>`、`printf` 與 return status。
- 課程指定環境實際使用的 GCC／Clang 或其他建置命令。
- 實際觀察到的 diagnostics 與產物。
- 明確指出不同實作可能以不同方式暴露 preprocessing／compilation／code generation／assembly／linking。

核心證據：

- 執行前預測輸出。
- 區分 source text、translation／build、產生的 program representation 與 execution。
- 重現並診斷一個 translation／build error。
- 解釋修改 source 後，為何已建置的程式在重新建置前不會自行改變。
- 比較 expected 與 actual evidence。

---

## P-U02 — 程式如何表示資料並改變狀態？

核心問題：**程式如何表示目前資料，又如何在每個相關執行步驟後產生新狀態？**

主要 chain：

```text
CT-I01 Data
→ CT-I02 Value
→ CT-I04 Type
→ CT-M04 Object / Storage
→ CT-S01 State
→ CT-S03 Variable / Named Object
→ CT-S06 Initialization
→ CT-S07 Assignment
→ CT-S02 State Change
→ CT-I07 Expression
→ CT-I09 Evaluation
→ CT-E12 Trace
```

Concept 使用：

- `N`：Data、Value、Type、Object／Storage、State、Variable／Named Object、Initialization、Assignment、State Change、Expression、Evaluation、Trace。
- `D`：Expected Result／Property、Output。
- `R`：Program、Execution。

C 映射：

- `int`、`double`、`char`。
- declaration 與 initialization。
- assignment 與 arithmetic expressions。
- 基本 standard input／output 與 format／type matching。
- 入門 integer division 與 conversion 觀察。

核心證據：

- 建立 state table。
- 逐行追蹤 old／new value。
- 執行前預測 expression result。
- 指出 invalid／uninitialized-state assumption 與 input／format 問題。
- 只在明確值域契約內比較 integer 與 floating behavior。

---

## P-U03 — 程式如何可靠地選擇與重複？

核心問題：**當不同情況需要不同動作，或工作需要反覆進行時，程式如何決定下一步並知道何時停止？**

主要 chain：

```text
CT-F01 Sequence
→ CT-F02 Condition
→ CT-F03 Selection / Decision
→ CT-F05 Repetition
→ CT-F06 Iteration
→ CT-F07 Loop Condition
→ CT-F08 Boundary
→ CT-F11 Nontermination
→ CT-E03 Testing
→ CT-E10 Regression Verification
```

Concept 使用：

- `N`：Sequence、Condition、Selection／Decision、Repetition、Iteration、Loop Condition、Boundary、Nontermination。
- `D`：Expression、Evaluation、State Change、Update、Testing。
- `R`：Input、Output、Expected Result／Property。

C 映射：

- relational／logical operators。
- `if`、`else`、`while`、`for`。
- 只有在符合控制目的時使用 `break`／`continue`。
- counter、accumulator、sentinel／end condition。

核心證據：

- 預測 branch path。
- 逐 iteration 追蹤 loop state。
- 比較 `<` 與 `<=` 等 boundary choice。
- 診斷 nontermination 與 off-by-one defect。
- 修改需求後重跑相關 regression check。

---

## P-U04 — 較大的問題如何拆成可理解的工作？

核心問題：**當程式變大時，如何分離責任，讓每一部分都能被理解、測試與修改？**

主要 chain：

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

Concept 使用：

- `N`：Decomposition、Responsibility、Function、Interface、Parameter、Argument、Return Value、Call。
- `D`：Test Case、Testing、Verification、Requirement。
- `R`：State、Selection、Repetition、Expected Result／Property。

C 映射：

- function declaration／prototype、definition、call。
- parameters 與 return values。
- local objects 與基本 scope。
- 小型整合程式及 caller-side tests。

核心證據：

- 用一句話說明 function responsibility。
- 預測 argument、parameter 與 return value。
- 追蹤 call 前／中／後的相關 state。
- 依情境設計 normal、boundary、invalid 或 failure cases。
- 比較不同 decomposition 並修改需求。

選用 `X` 延伸：學生若自行使用 AI 或其他外部協助，以同一套核心 testing／trace evidence 驗證被採用建議；跳過此延伸不改變核心完成要求。

---

# 正式課程 Units

正式課程深化前導 Concept，而不是從零重置。現行 F-U01–F-U12 學生教材是這些 Unit skeleton 的具體實作，可包含額外已驗證細節。

## F-U01 — 為什麼表示、型別與操作會影響結果？

核心問題：**為什麼同一數學想法，會因資料表示、型別與操作規則得到不同程式結果？**

主要 Concepts：CT-I03 Representation、CT-I04 Type、CT-I08 Operator、CT-I09 Evaluation、CT-I10 Conversion、CT-X04 Format、CT-E01 Expected Result／Property。

C 映射：

- 以 `<limits.h>` 說明 integer range，而不是假設固定 bit width。
- 使用 binary example 時明確指定 width。
- 只有在 representation 已指定時談 MSB／LSB 位置。
- floating-point approximation 與 `<float.h>`／目標環境觀察。
- character representation 與 conversions。
- 正確 formatted I/O specifier。

核心證據：

- 在明確契約內預測 type／conversion 結果。
- 區分數學預期與可表示 domain 行為。
- 測試 boundary values 與 formatting assumptions。
- 指出哪些主張由標準保證，哪些屬 implementation-specific。

---

## F-U02 — 複雜控制流程如何維持可解釋與可測試？

核心問題：**當條件、邊界與重複變複雜時，需要什麼證據支持正確性？**

主要 Concepts：CT-F03 Selection、CT-F05 Repetition、CT-F09 Sentinel／End Condition、CT-F10 Nested Control、CT-S11 Invariant、CT-E03 Testing、CT-E10 Regression Verification。

C 映射：`switch`、nested control、compound conditions、sentinel／end-condition loops、以 invariant 作為 reasoning tool。

核心證據：畫／追蹤 path、找出 missing／overlapping case、提出適當 invariant、測試 boundaries、需求變更後重新驗證。

---

## F-U03 — 資料如何形成有順序的集合？

核心問題：**需要一起保存與處理多個相關值時，如何組織、索引並維持有效邊界？**

主要 Concepts：CT-I11 Collection、CT-M04 Object／Storage、CT-M05 Layout、CT-F08 Boundary、CT-F06 Iteration、CT-M15 Memory Safety；Composite CT-K01 Array。

C 映射：one-dimensional arrays、indexes、明確 length／capacity contract、traversal、arrays passed to functions、範圍允許時的 introductory multidimensional arrays。

核心證據：追蹤 element／index relationship、測試 valid／invalid bounds、診斷 out-of-bounds／off-by-one、修改 length／capacity requirement 並重新驗證。

---

## F-U04 — 文字如何被表示與處理成 C 資料？

核心問題：**C 如何表示 string、如何判定其結束，又需要哪些 capacity／boundary 條件才能安全操作？**

主要 Concepts：CT-I03 Representation、CT-K01 Array、CT-K02 String、CT-F09 Sentinel／End Condition、CT-X05 Buffer、CT-X04 Format、CT-M15 Memory Safety。

C 映射：`char` arrays、null terminator、string literals、`fgets`、選定 `<string.h>` functions、明確 capacity／length contract。

核心證據：區分 character array 與 valid string、追蹤 terminator／capacity state、測試 input boundary、診斷 unterminated／insufficient-buffer case；談 multibyte encoding 時說明 byte-vs-character 限制。

---

## F-U05 — 函數呼叫如何形成暫時執行狀態？

核心問題：**在 nested／recursive calls 中，parameter、local object、control return、scope 與 lifetime 如何互相作用？**

主要 Concepts：CT-A09 Call、CT-A10 Activation Model、CT-S09 Scope、CT-S10 Lifetime、CT-M10 Storage Duration、CT-M11 Automatic Storage、CT-A11 Recursion。

C 映射：automatic local objects、nested calls、recursion、base／termination conditions。

核心證據：

- 追蹤 implementation-neutral activation model。
- 區分 scope 與 lifetime。
- 推理 recursive progress／termination。
- 診斷 invalid returned address 或 nonterminating recursion。
- 只有目標實作確實使用時，才把 physical call stack／stack overflow 連結到具體環境。

---

## F-U06 — 如何透過指標間接存取資料？

核心問題：**pointer 如何指定另一個 object，又需要哪些條件才可有效進行 indirect access？**

主要 Concepts：CT-M03 Address、CT-M06 Pointer、CT-M07 Indirection／Dereference、CT-M08 Aliasing、CT-M09 Null Pointer、CT-S10 Lifetime、CT-M15 Memory Safety。

C 映射：`&`、`*`、pointer parameters、null pointer values、array／pointer relationship 與 array object 規則內的有限 pointer arithmetic。

核心證據：畫 pointer／object relationship、預測 alias effect、指出 dereference preconditions、診斷 null、dangling、one-past misuse 與 invalid access。

---

## F-U07 — 一個實體如何包含不同欄位？

核心問題：**當一個實體需要多種不同資料時，如何把欄位建模成一個有意義的 record？**

主要 Concepts：CT-I11 Collection、CT-M04 Object／Storage、CT-M05 Layout、CT-I04 Type、CT-A04 Interface；Composite CT-K03 Structure／Record。

C 映射：`struct`、member access、initialization／assignment、structure pointers、nested structures、arrays of structures、提高 interface clarity 時的 `typedef`。

核心證據：從 requirement 推導 fields、比較 separate variables 與 record、區分 semantic field 與 implementation padding／layout、透過清楚 interface 修改 structure、測試 validity constraint。

---

## F-U08 — 程式如何管理執行時才決定大小或生命週期的儲存空間？

核心問題：**當需求無法在 translation time 固定時，如何安全取得、調整、管理與釋放 storage？**

主要 Concepts：CT-M13 Allocated Storage／Dynamic Allocation、CT-M14 Ownership／Release Responsibility、CT-S10 Lifetime、CT-M06 Pointer、CT-M15 Memory Safety。

C 映射：`malloc`、`calloc`、`realloc`、`free`、overflow-safe size reasoning、allocation failure、leak／dangling／double-free prevention。

核心證據：畫 allocate-use-resize-release path、`realloc` failure 時保留原 allocation、指出 ownership／release responsibility、測試 failure path、診斷 lifetime error。

---

## F-U09 — 程式如何與檔案及持久資料互動？

核心問題：**資料需要跨一次執行保存時，程式如何讀寫，又如何區分正常 input end、error 與 malformed data？**

主要 Concepts：CT-X03 Stream、CT-X06 File、CT-X07 End of Input、CT-X04 Format、CT-X05 Buffer、CT-X10 Protocol、CT-X08 Error State；Composite CT-K04 File I/O。

C 映射：`FILE *`、`fopen`、`fclose`、text I/O、return-value check、只有依 API 語意使用 `feof`／`ferror`、partial failure 重要時採 transactional loading。

核心證據：檢查 open／read／write／close state、區分 EOF 與 error、測試 malformed／missing data、失敗載入時維持 invariant、驗證 persisted results。

---

## F-U10 — 程式如何拆成可獨立維護的模組？

核心問題：**如何分離 interface 與 implementation，讓各部分能在受控 dependency 下被理解、翻譯、連結、測試與替換？**

主要 Concepts：CT-A12 Module、CT-A04 Interface、CT-A05 Implementation、CT-C06 C Translation、CT-A02 Responsibility、CT-E14 Documentation；Composite CT-K05 Modular Programming。

C 映射：`.h`／`.c`、declaration vs definition、include guard、direct standard-library dependencies、separate translation、適用的 linkage、compile-vs-link diagnostics。

核心證據：設計 interface、拆分 source、建置所有必要 translation units、診斷 declaration／definition／link error、在 client contract 不變下替換 implementation。

---

## F-U11 — 如何系統化測試、診斷與改善程式？

核心問題：**除了單一次正確輸出之外，需要什麼證據才能信任程式或技術主張？**

主要 Concepts：CT-E01 Expected Result／Property、CT-E02 Test Case、CT-E03 Testing、CT-E04 Verification、CT-E05 Validation、CT-E06 Debugging、CT-E10 Regression Verification、CT-E11 Code Reading、CT-E13 Refactoring、CT-E17 Evidence、CT-E18 Judgment。

C 映射／活動：test table／harness、diagnostics、defect reproduction／narrowing、behavior-preserving refactoring、適當 compiler warning 與其他 tool。

核心證據：先定義 expectation、設計 normal／boundary／invalid／failure cases、以證據縮小 fault、執行 regression verification、說明目前信心的限制。

選用 `X` 延伸：實際使用外部協助時，條件式加入 CT-E16／19／20 並驗證被採用主張；未使用者不需任何外部協助 artifact。

---

## F-U12 — 如何把全課程 Concept 整合成一個可驗證程式？

核心問題：**如何整合 requirement、data、control、function、memory／lifetime、interaction、module 與 verification，又不失去清楚 responsibility 或 evidence？**

主要 Concepts：CT-C02 Requirement、CT-C03 Algorithm／Design、CT-A01 Decomposition、CT-A12 Module、CT-X10 Protocol、CT-E03 Testing、CT-E05 Validation、CT-E10 Regression Verification、CT-E18 Judgment。

本 Unit 幾乎不引入新 syntax，而是透過 requirement clarification、architecture／data-flow decision、incremental implementation、failure handling、change impact、testing、diagnosis 與 explanation 整合既有能力。

核心證據：

- 把 requirement 轉成 observable behavior 與 technical contract。
- 設計 data／control／module responsibility。
- 逐步建立 minimal working slice。
- 建立並執行相關 normal／boundary／invalid／failure／regression cases。
- 處理 changed requirement 又不破壞未受影響行為。
- 說明 design decision、assumption、limitation 與 verification evidence。

---

## Unit 與 Delivery 的關係

Unit 是 capability／concept skeleton，不是固定 class meeting。

- 中文前導班可把一個 Unit 放在較長 block。
- 英文前導班可使用較多 delivery slice 與語言支架。
- 正式 Unit 可依核定交付規劃跨一週以上。
- Delivery slice 可調整 example 與 pacing，但不得默默改變 Unit core question、technical standard 或 core evidence expectation。

## Unit Set

目前核定 skeleton：

- 前導課程：P-U01 至 P-U04。
- 正式課程：F-U01 至 F-U12。
- 合計：16 個 Unit identifier。

此數量是可維護的設計決策，不是 constitution 常數。任何 merge／split 都必須同步 Concept Registry reference、scope／competency traceability、material path、中英文版本與 active audit。

## 維護規則

1. 中英文版本維持實質等值。
2. Unit identifier 保持穩定，除非執行有文件紀錄的 migration。
3. 變更核心 Unit 內容時檢查 Concept Registry dependency 與 competency／scope standard。
4. AI／external-assistance activity 維持可直接跳過；除非明確核准活動本身就是 tool judgment 目標。
5. 具體 C／toolchain／runtime 敘述依指定 standard 與 target environment 驗證。
6. 對應學生教材持續保持可讀、技術可測試且沒有過時 Unit requirement。
7. 實質變更記錄到 repository-wide active audit。

## 相關文件

- [程式設計 Concept Tree](14-programming-concept-tree.zh-TW.md)
- [程式設計 Concept Registry](15-programming-concept-registry.zh-TW.md)
- [程式設計能力地圖](05-competency-map.zh-TW.md)
- [課程範圍邊界](06-scope-boundary.zh-TW.md)
- [課程交付地圖](08-delivery-map.zh-TW.md)
- [正式教材索引](../materials/formal/README.zh-TW.md)
- [前導教材索引](../materials/preparatory/README.zh-TW.md)
- [教學內容設計區](README.zh-TW.md)
- [English version](16-unit-map.en.md)
