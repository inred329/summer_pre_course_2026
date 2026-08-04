# Concept 驅動的 Unit Map

版本：0.1.0  
狀態：Unit 組合草案  
最後更新：2026-08-04  
對應英文版本：[Concept-Driven Unit Map](16-unit-map.en.md)

## 文件目的

本文件依據 Concept Tree 與 Concept Registry，將跨語言的程式設計 Concept 組合成可教學、可閱讀、可追蹤的 Unit。

Unit 不是章節名稱或語法清單，而是由以下元素構成：

1. 一個學生能理解的核心問題。
2. 一條主要 Concept 依賴鏈。
3. 少量首次引入的 Concept。
4. 需要深化或重用的既有 Concept。
5. 至少一項預測、追蹤、測試、除錯或驗證活動。
6. 對應的 C 語言工具與語法。

本文件先定義 Unit 骨架，不決定每週節奏，也不取代最終學生教材。

## Unit 組合標記

- `N`：本 Unit 首次引入的新 Concept。
- `D`：本 Unit 深化的 Concept。
- `R`：本 Unit 重用的 Concept。
- `P`：前導課程範圍。
- `F`：正式課程範圍。

---

# 前導課程 Unit

## P-U01　程式如何從文字變成執行結果？

核心問題：**人類可讀的程式文字，如何變成電腦真正執行的行為？**

主要 Concept 鏈：

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

Concept 使用：

- `N`：Problem、Requirement、Program、Source Code、Translation、Compiler、Executable、Execution、Output、Expected Result
- `D`：Algorithm
- `R`：無

C 語言映射：

- 最小 `main` 程式
- `#include <stdio.h>`
- `printf`
- GCC／Clang 編譯指令
- 可執行檔與終端機執行
- `return 0`

學生必須經歷：

- 執行前預測輸出
- 區分編譯與執行
- 製造並診斷一個編譯錯誤
- 修改原始碼後比較「未重新編譯」與「重新編譯」的差異

---

## P-U02　程式如何記住資料並改變狀態？

核心問題：**程式如何保存目前的資料，並在每一步執行後產生新的狀態？**

主要 Concept 鏈：

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

Concept 使用：

- `N`：Data、Value、Type、State、Variable、Initialization、Assignment、Update、Expression、Evaluation
- `D`：Expected Result、Output
- `R`：Program、Execution

C 語言映射：

- `int`、`double`、`char`
- 變數宣告與初始化
- 指派運算子
- 算術運算子
- `scanf` 與 `printf`
- 整數除法與型別轉換的初步觀察

學生必須經歷：

- 建立變數狀態表
- 逐行追蹤舊值與新值
- 預測運算式結果
- 比較整數與浮點表示
- 診斷未初始化、型別不合或錯誤格式的案例

---

## P-U03　程式如何選擇與重複？

核心問題：**當不同狀況需要不同動作，或同一動作需要重複時，程式如何決定下一步？**

主要 Concept 鏈：

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

Concept 使用：

- `N`：Sequence、Condition、Decision、Repetition、Iteration、Loop Condition、Boundary、Infinite Execution
- `D`：Expression、Evaluation、State Change、Update
- `R`：Input、Output、Expected Result

C 語言映射：

- 比較與邏輯運算子
- `if`、`else`
- `while`、`for`
- `break`、`continue` 作為延伸映射
- 計數器、累加器與 sentinel

學生必須經歷：

- 預測分支路徑
- 逐次追蹤迴圈狀態
- 比較 `<` 與 `<=` 的邊界差異
- 診斷無窮迴圈與 off-by-one
- 修改需求後進行回歸檢查

---

## P-U04　如何把一個大問題拆成可理解的工作？

核心問題：**當程式開始變長時，如何把責任分開，讓每一部分可以理解、測試與修改？**

主要 Concept 鏈：

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

- `N`：Decomposition、Responsibility、Function、Interface、Parameter、Argument、Return Value、Call
- `D`：Test Case、Testing、Verification、Requirement
- `R`：State、Decision、Repetition、Expected Result

C 語言映射：

- 函數宣告、定義與呼叫
- 參數與回傳值
- 區域變數
- 函數原型
- 小型整合程式

學生必須經歷：

- 為函數寫一句責任說明
- 預測參數與回傳值
- 追蹤呼叫前後狀態
- 為函數設計正常、邊界與回歸案例
- 驗證一個看似合理但錯誤的 AI 函數建議

---

# 正式課程 Unit

正式課程不重置前導課程。前導 Concept 會持續深化並與新的 Concept 組合。

## F-U01　表示、型別與運算為什麼會影響結果？

核心問題：**同一個數值或運算，為什麼可能因表示方式與型別而產生不同結果？**

主要 Concept：Representation、Type、Operator、Evaluation、Conversion、Format。

深化：Value、Expression、Expected Result、Testing。

C 映射：整數範圍、浮點誤差、字元編碼、隱式與顯式轉換、格式化輸出。

---

## F-U02　如何建立可靠的多分支與重複流程？

核心問題：**當條件、邊界與重複規則變複雜時，如何仍能證明流程正確？**

主要 Concept：Branch、Nested Control、Sentinel、Invariant。

深化：Decision、Repetition、Boundary、State Change、Verification。

C 映射：`switch`、巢狀控制、複合條件、sentinel loop、loop invariant。

---

## F-U03　資料如何形成有順序的集合？

核心問題：**當多個同類資料需要一起保存與處理時，程式如何組織、定位與走訪它們？**

主要 Concept：Collection、Object、Layout、Boundary、Iteration、Memory Safety。

組合 Concept：`CT-K01 Array`。

C 映射：一維陣列、索引、長度、走訪、越界、陣列作為函數參數。

---

## F-U04　文字資料如何被表示與處理？

核心問題：**電腦如何把文字保存成資料，又如何知道文字在哪裡結束？**

主要 Concept：Representation、Collection、Layout、Sentinel、Buffer、Format。

組合 Concept：`CT-K02 String`。

C 映射：`char` 陣列、空字元、字串常值、`fgets`、字串函式與緩衝區安全。

---

## F-U05　函數呼叫如何建立新的執行環境？

核心問題：**函數呼叫時，參數、區域狀態與未完成工作如何被保存？**

主要 Concept：Call Stack、Scope、Lifetime、Stack Storage、Recursion。

深化：Function、Call、Parameter、Return Value、Invariant。

C 映射：自動區域變數、呼叫框架、遞迴、base case、stack overflow 概念。

---

## F-U06　如何透過位址間接操作資料？

核心問題：**程式如何用一個值指向另一個物件，並透過位址存取或修改它？**

主要 Concept：Address、Pointer、Indirection、Aliasing、Null Reference、Lifetime、Memory Safety。

C 映射：`&`、`*`、pointer parameter、null pointer、pointer arithmetic 的受限使用。

---

## F-U07　資料結構如何由多個不同欄位組成？

核心問題：**當一個實體包含多種不同資料時，如何把它們組合成一個有意義的物件？**

主要 Concept：Collection、Object、Layout、Type、Interface。

組合 Concept：`CT-K03 Structure`。

C 映射：`struct`、member access、nested structure、structure assignment、`typedef`。

---

## F-U08　程式如何在執行期間取得與釋放空間？

核心問題：**當資料大小或生命週期無法預先固定時，程式如何管理儲存空間？**

主要 Concept：Dynamic Allocation、Ownership、Lifetime、Pointer、Memory Safety。

C 映射：`malloc`、`calloc`、`realloc`、`free`、memory leak、dangling pointer、double free。

---

## F-U09　程式如何與檔案及持久資料互動？

核心問題：**當資料需要在程式結束後仍存在，程式如何讀取、寫入並判斷錯誤？**

主要 Concept：Stream、File、End of Input、Format、Buffer、Protocol、Error Channel。

組合 Concept：`CT-K04 File I/O`。

C 映射：`FILE *`、`fopen`、`fclose`、文字檔讀寫、EOF、函式回傳值檢查。

---

## F-U10　程式如何分成可獨立維護的模組？

核心問題：**如何把介面與實作分開，使不同程式部分可以獨立理解、編譯與替換？**

主要 Concept：Module、Interface、Implementation、Translation、Compiler、Responsibility。

組合 Concept：`CT-K05 Modular Programming`。

C 映射：`.h`、`.c`、include guard、separate compilation、linking。

---

## F-U11　如何系統化地證明、診斷與改善程式？

核心問題：**除了看到正確輸出之外，還需要什麼證據才能信任程式？**

主要 Concept：Testing、Verification、Validation、Debugging、Error Diagnosis、Regression、Refactoring、Code Reading、Code Review。

C 映射：測試表、錯誤重現、逐步縮小範圍、修正後回歸、程式比較與重構。

---

## F-U12　如何負責任地與 AI 協作？

核心問題：**當 AI 可以快速提出程式與解釋時，學生如何保留判斷責任並建立可信證據？**

主要 Concept：AI Collaboration、Expected Result、Testing、Verification、Error Diagnosis、Documentation。

C 映射：AI 程式審查、錯誤建議驗證、測試補強、解法比較與決策紀錄。

---

## F-U13　如何完成跨 Concept 的整合程式？

核心問題：**如何從需求出發，整合資料、流程、函數、記憶體、互動與工程能力？**

主要 Concept：Requirement、Algorithm、Decomposition、Module、Protocol、Testing、Validation、Maintenance。

此 Unit 不新增大量語法，而是要求學生整合、修改、診斷、驗證與解釋。

---

## Unit 與 Lesson 的關係

Unit 不等於一次上課。Lesson 是 Unit 的交付切片。

同一 Unit 可以：

- 在中文班以較長時間整合教學。
- 在英文班拆成較多 Lesson，加入術語、閱讀與表達支架。
- 在正式課程中跨週深化。

Lesson 不得改變 Unit 的核心問題、Concept 鏈或能力標準。

## 第一版數量結論

目前建議：

- 前導課程：4 個 Unit。
- 正式課程：13 個 Unit。
- 合計：17 個 Unit 骨架。

此數量不是憲法固定值。後續可依 Concept 邊界、試教結果與課程時數合併或拆分，但不得直接以週數取代 Concept 推導。

## 下一步

1. 對每個 Unit 檢查 Concept 依賴是否完整。
2. 確認每個 Unit 的新 Concept 數量是否適合初學者。
3. 對照現有前導單元 1–4，決定保留、拆分或重寫方式。
4. 為每個 Unit 建立學生教材大綱。
5. 最後才排定中文班、英文班與正式課程 Lesson。

## 導覽

- [Programming Concept Tree](14-programming-concept-tree.zh-TW.md)
- [Programming Concept Registry](15-programming-concept-registry.zh-TW.md)
- [教學內容設計區](README.zh-TW.md)
- [English version](16-unit-map.en.md)
