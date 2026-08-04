# Concept 驅動的 Unit Map

版本：0.2.0  
狀態：完整 Unit 組合草案  
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
7. 一個簡短的課後概念解釋活動。

本文件先定義 Unit 骨架，不決定每週節奏，也不取代最終學生教材。

## AI 的定位

AI 不是獨立 Unit，也不是教材主體。

每個 Unit 結尾只安排一個簡短活動：請學生用自己的話，向 AI 解釋本 Unit 的核心 Concept，並從對話中確認自己的理解是否清楚。

此活動：

- 不提供固定 Prompt。
- 不要求繳交對話紀錄。
- 不要求使用特定 AI 工具。
- 不取代執行前預測、程式實作、測試、除錯與驗證。
- 不要求 AI 直接提供答案或程式。

核心原則是：**學生向 AI 解釋，而不是先請 AI 替學生解釋。**

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

課後概念解釋：

> 請向 AI 解釋原始碼、編譯器、可執行檔與執行之間的關係。

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

課後概念解釋：

> 請向 AI 解釋變數、值、型別與狀態之間的關係。

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

課後概念解釋：

> 請向 AI 解釋條件判斷與重複執行的差異，以及兩者如何一起控制程式流程。

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
- 比較不同函數切分方式

課後概念解釋：

> 請向 AI 解釋函數為什麼能幫助我們分解問題，以及參數與回傳值各自扮演什麼角色。

---

# 正式課程 Unit

正式課程不重置前導課程。前導 Concept 會持續深化並與新的 Concept 組合。

## F-U01　表示、型別與運算為什麼會影響結果？

核心問題：**同一個數值或運算，為什麼可能因表示方式與型別而產生不同結果？**

主要 Concept：Representation、Type、Operator、Evaluation、Conversion、Format。

深化：Value、Expression、Expected Result、Testing。

C 映射：整數範圍、二進位表示、MSB、LSB、浮點誤差、字元編碼、隱式與顯式轉換、格式化輸出。

學生必須經歷：

- 比較十進位與二進位表示
- 判斷 MSB 與 LSB 的位置與意義
- 預測整數與浮點運算結果
- 觀察轉型與格式化造成的差異
- 用邊界值驗證型別假設

課後概念解釋：

> 請向 AI 解釋 MSB 與 LSB 是什麼，以及兩者的差異。

---

## F-U02　如何建立可靠的多分支與重複流程？

核心問題：**當條件、邊界與重複規則變複雜時，如何仍能證明流程正確？**

主要 Concept：Branch、Nested Control、Sentinel、Invariant。

深化：Decision、Repetition、Boundary、State Change、Verification。

C 映射：`switch`、巢狀控制、複合條件、sentinel loop、loop invariant。

學生必須經歷：

- 繪製複合流程路徑
- 建立迴圈不變量的初步描述
- 比較不同 sentinel 設計
- 尋找邊界與路徑遺漏
- 修改流程後重新驗證

課後概念解釋：

> 請向 AI 解釋 sentinel、迴圈條件與邊界之間的關係。

---

## F-U03　資料如何形成有順序的集合？

核心問題：**當多個同類資料需要一起保存與處理時，程式如何組織、定位與走訪它們？**

主要 Concept：Collection、Object、Layout、Boundary、Iteration、Memory Safety。

組合 Concept：`CT-K01 Array`。

C 映射：一維陣列、索引、長度、走訪、越界、陣列作為函數參數。

學生必須經歷：

- 繪製陣列元素與索引關係
- 預測走訪順序
- 比較有效與無效索引
- 診斷越界與 off-by-one
- 修改陣列長度後重新測試

課後概念解釋：

> 請向 AI 解釋陣列、索引、長度與邊界之間的關係。

---

## F-U04　文字資料如何被表示與處理？

核心問題：**電腦如何把文字保存成資料，又如何知道文字在哪裡結束？**

主要 Concept：Representation、Collection、Layout、Sentinel、Buffer、Format。

組合 Concept：`CT-K02 String`。

C 映射：`char` 陣列、空字元、字串常值、`fgets`、字串函式與緩衝區安全。

學生必須經歷：

- 畫出字串在陣列中的配置
- 說明空字元的作用
- 比較字元數與陣列空間
- 診斷缺少終止字元與緩衝區不足
- 以輸入案例驗證字串處理

課後概念解釋：

> 請向 AI 解釋字元陣列與 C 字串的差異，以及空字元為什麼重要。

---

## F-U05　函數呼叫如何建立新的執行環境？

核心問題：**函數呼叫時，參數、區域狀態與未完成工作如何被保存？**

主要 Concept：Call Stack、Scope、Lifetime、Stack Storage、Recursion。

深化：Function、Call、Parameter、Return Value、Invariant。

C 映射：自動區域變數、呼叫框架、遞迴、base case、stack overflow 概念。

學生必須經歷：

- 繪製函數呼叫堆疊
- 追蹤參數與區域變數
- 比較 scope 與 lifetime
- 辨認遞迴 base case
- 診斷無限遞迴

課後概念解釋：

> 請向 AI 解釋函數呼叫堆疊、scope 與 lifetime 之間的關係。

---

## F-U06　如何透過位址間接操作資料？

核心問題：**程式如何用一個值指向另一個物件，並透過位址存取或修改它？**

主要 Concept：Address、Pointer、Indirection、Aliasing、Null Reference、Lifetime、Memory Safety。

C 映射：`&`、`*`、pointer parameter、null pointer、pointer arithmetic 的受限使用。

學生必須經歷：

- 畫出物件、位址與指標關係
- 預測解參照結果
- 比較指標本身與指向物件
- 觀察 aliasing 導致的共享修改
- 診斷 null、dangling 與無效解參照

課後概念解釋：

> 請向 AI 解釋位址、指標、解參照與指向物件之間的關係。

---

## F-U07　資料結構如何由多個不同欄位組成？

核心問題：**當一個實體包含多種不同資料時，如何把它們組合成一個有意義的物件？**

主要 Concept：Collection、Object、Layout、Type、Interface。

組合 Concept：`CT-K03 Structure`。

C 映射：`struct`、member access、nested structure、structure assignment、`typedef`。

學生必須經歷：

- 從需求辨認資料欄位
- 比較多個獨立變數與一個 structure
- 觀察成員配置
- 傳遞與修改 structure
- 為 structure 設計有效資料條件

課後概念解釋：

> 請向 AI 解釋 structure 如何把不同型別的欄位組成一個有意義的物件。

---

## F-U08　程式如何在執行期間取得與釋放空間？

核心問題：**當資料大小或生命週期無法預先固定時，程式如何管理儲存空間？**

主要 Concept：Dynamic Allocation、Ownership、Lifetime、Pointer、Memory Safety。

C 映射：`malloc`、`calloc`、`realloc`、`free`、memory leak、dangling pointer、double free。

學生必須經歷：

- 繪製配置、使用與釋放流程
- 判斷資源 ownership
- 檢查配置失敗
- 診斷 leak、dangling pointer 與 double free
- 修改容量需求後重新驗證

課後概念解釋：

> 請向 AI 解釋動態記憶體、ownership、lifetime 與 `free` 之間的關係。

---

## F-U09　程式如何與檔案及持久資料互動？

核心問題：**當資料需要在程式結束後仍存在，程式如何讀取、寫入並判斷錯誤？**

主要 Concept：Stream、File、End of Input、Format、Buffer、Protocol、Error Channel。

組合 Concept：`CT-K04 File I/O`。

C 映射：`FILE *`、`fopen`、`fclose`、文字檔讀寫、EOF、函式回傳值檢查。

學生必須經歷：

- 區分 stream 與 file
- 檢查開檔與讀寫結果
- 追蹤讀取位置與 EOF
- 診斷格式或檔案錯誤
- 驗證關閉資源與資料保存

課後概念解釋：

> 請向 AI 解釋 stream、file、EOF 與錯誤檢查之間的關係。

---

## F-U10　程式如何分成可獨立維護的模組？

核心問題：**如何把介面與實作分開，使不同程式部分可以獨立理解、編譯與替換？**

主要 Concept：Module、Interface、Implementation、Translation、Compiler、Responsibility。

組合 Concept：`CT-K05 Modular Programming`。

C 映射：`.h`、`.c`、include guard、separate compilation、linking。

學生必須經歷：

- 區分 interface 與 implementation
- 建立 header 與 source file
- 追蹤分別編譯與 linking
- 診斷 declaration、definition 與 linker 錯誤
- 替換實作而不改變使用者程式

課後概念解釋：

> 請向 AI 解釋 module、interface、implementation 與 linking 之間的關係。

---

## F-U11　如何系統化地證明、診斷與改善程式？

核心問題：**除了看到正確輸出之外，還需要什麼證據才能信任程式？**

主要 Concept：Testing、Verification、Validation、Debugging、Error Diagnosis、Regression、Refactoring、Code Reading、Code Review。

C 映射：測試表、錯誤重現、逐步縮小範圍、修正後回歸、程式比較與重構。

學生必須經歷：

- 先寫 expected result
- 設計正常、邊界與錯誤案例
- 重現並縮小問題
- 修正後執行 regression
- 比較重構前後行為

課後概念解釋：

> 請向 AI 解釋 testing、verification、validation 與 debugging 的差異。

---

## F-U12　如何完成跨 Concept 的整合程式？

核心問題：**如何把需求、資料、流程、函數、記憶體、互動與工程方法整合成一個可驗證的程式？**

主要 Concept：Requirement、Algorithm、Decomposition、Module、Protocol、Testing、Validation、Maintenance。

本 Unit 不大量引入新語法，而要求學生整合、修改、診斷、驗證與解釋。

學生必須經歷：

- 將需求轉成可觀察行為
- 建立資料、流程與模組設計
- 逐步完成最小可執行版本
- 建立測試與回歸案例
- 處理修改需求
- 解釋設計與驗證證據

課後概念解釋：

> 請向 AI 解釋你的整合程式如何把需求、資料、流程、函數、記憶體與測試連結起來。

---

## Unit 與 Lesson 的關係

Unit 不等於一堂課。Lesson 是 Unit 的授課切片。

同一個 Unit 可以：

- 在中文班以較長的整合區塊教學。
- 在英文班拆成更多 Lesson，增加術語、閱讀與表達支架。
- 在正式課程跨多週逐步深化。

Lesson 不得改變 Unit 的核心問題、Concept 鏈或能力標準。

## 完整數量結論

目前建議：

- 前導課程：4 個 Unit。
- 正式課程：12 個 Unit。
- 合計：16 個 Unit 骨架。

AI 不另設 Unit。它只以簡短課後概念解釋活動，低比重地出現在各 Unit 中。

此數量並非憲法固定。後續仍可依 Concept 邊界、試教結果與課程時數合併或拆分，但不得以週數取代 Concept 推導。

## 下一步

1. 檢查每個 Unit 的 Concept 依賴鏈是否完整。
2. 確認每個 Unit 的新 Concept 數量適合初學者。
3. 對照目前前導 Unit 1–4，決定保留、拆分、合併或重寫內容。
4. 為全部 16 個 Unit 建立雙語學生教材大綱。
5. 從 P-U01 開始撰寫可獨立閱讀的正式學生教材。
6. 最後才切分中文班、英文班與正式課程的 Lessons。

## 導覽

- [程式設計 Concept Tree](14-programming-concept-tree.zh-TW.md)
- [程式設計 Concept Registry](15-programming-concept-registry.zh-TW.md)
- [教學內容設計區](README.zh-TW.md)
- [English version](16-unit-map.en.md)
