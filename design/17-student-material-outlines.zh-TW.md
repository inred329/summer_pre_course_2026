# 16 個 Unit 的學生教材大綱

版本：0.2.0  
狀態：可修訂的規劃與追蹤模型  
最後更新：2026-08-07  
治理說明：本文件規劃學生教材結構，不自行建立評分、完成、AI／工具使用或繳交規則。若有衝突，以 Constitution、正式學習與評量制度、設計標準與現行學生教材為準。  
對應英文版本：[Student Material Outlines for 16 Units](17-student-material-outlines.en.md)

## 文件目的

本文件依據 [Concept 驅動的 Unit Map](16-unit-map.zh-TW.md)，整理 4 個前導 Unit 與 12 個正式課程 Unit 的可維護教材大綱。它是規劃模型，不是學生教材本身的權威來源。

每個大綱原則上支援學生獨立閱讀，常見結構為：

> 核心問題 → 預測 → 視覺／執行模型 → Concept 與 C 映射 → 追蹤／實作 → 錯誤診斷 → 測試／修改 → 核心反思 → 摘要

若不同結構更有利於閱讀，可調整章節數量；但核心學習證據必須在不依賴 AI 或其他外部協助的情況下仍可完成。

## Constitution 2.0 對齊原則

- AI 與其他外部協助預設為選用。
- 任何大綱都不得把 AI 對話、固定 Prompt、保存對話、AI 使用紀錄或未使用聲明列為核心完成條件。
- 核心反思要求學生用自己的話說明核心關係，並以程式、追蹤、圖示、測試或其他證據支持；不需要外部工具也能完成。
- 若提供外部協助延伸，必須可直接跳過；只有在學生實際採用外部建議時，才需要理解、審查與技術驗證。
- 具體 C／工具鏈敘述必須交代必要技術契約，並區分語言保證與實作相依行為。
- 中英文版本使用相同 Unit ID、核心問題、技術深度與證據方向。

## 共通教材撰寫要求

完成版學生 Unit 在適用時應清楚呈現：

1. 學生在觀察結果前應先預測什麼；
2. 正確推理所需的輸入／狀態／流程／生命週期／stream／module 技術契約；
3. 至少一個可重現的錯誤或失敗案例；
4. 與主題相符的正常、邊界、無效或失敗測試；
5. 一個需求修改或程式修改任務；
6. 哪些證據支持目前信心，以及仍有哪些限制；
7. 一條不依賴選用外部工具的核心完成路徑。

---

# 前導課程

## P-U01 — 程式文字如何變成執行結果？

核心問題：**人類可讀的程式文字，如何在指定環境中變成電腦可執行的行為？**

大綱重點：

- Problem、Requirement、Algorithm／Design、Source Code、translation/build、diagnostic、executable/loadable representation、execution、output；
- 最小 `main`、`stdio`、return status，以及經驗證的建置／執行指令；
- 執行前預測與 translation/build 缺陷診斷；
- 明確區分概念性的建置責任模型與目標工具鏈實際暴露的步驟／產物。

核心證據：輸出預測、建置／執行觀察、診斷分類、修改原始碼後重新建置，以及對實際 source-to-execution 流程的說明。

核心反思：說明原始碼、translation/build、目標程式表示、執行與可觀察證據之間的關係。

---

## P-U02 — 程式如何記住資料並改變狀態？

核心問題：**程式如何保存目前資料，並在每一步執行後產生新的狀態？**

大綱重點：

- Data、Value、Type、Object／Name、Initialization、Assignment、Expression、Evaluation、Input／Output、State Change；
- 狀態表與執行前預期結果；
- 基本型別／值域／格式假設與輸入狀態邊界；
- 以安全且契約明確的例子診斷未初始化、轉換、輸入或格式錯誤。

核心證據：逐步狀態追蹤、運算式結果預測、錯誤修正，以及小型需求修改與重新測試。

核心反思：說明值、型別、具名物件、運算式求值與狀態改變之間的關係。

---

## P-U03 — 程式如何選擇與重複？

核心問題：**當不同狀況需要不同動作，或同一動作需要重複時，程式如何決定下一步？**

大綱重點：

- Sequence、Condition、Selection、Repetition、Loop State、Update、Boundary、Termination／Nontermination；
- `if`／`else`、`while`、`for` 與範圍明確的流程轉移；
- 分支預測、逐次迴圈追蹤、off-by-one 與終止條件；
- 邊界或需求改變後的回歸驗證。

核心證據：路徑追蹤、迴圈狀態表、邊界測試、非終止／off-by-one 診斷，以及修正後驗證。

核心反思：說明條件、狀態更新、重複、邊界與終止如何共同作用。

---

## P-U04 — 如何把大問題拆成可理解的工作？

核心問題：**當程式變長時，如何分離責任，使各部分可以理解、測試與修改？**

大綱重點：

- Decomposition、Responsibility、Function、Interface、Parameter、Argument、Return Value、Call；
- caller／callee 狀態與基本函數契約；
- 小函數的正常／邊界測試；
- 比較不同分解方式，並在不重寫無關責任的前提下修改需求。

核心證據：責任描述、呼叫追蹤、經測試的函數、分解比較，以及需求修改。

核心反思：說明責任、介面、參數、引數、回傳值與測試證據如何連結。

---

# 正式課程

## F-U01 — 表示、型別與運算為什麼會影響結果？

核心問題：**同一個數學想法或原始碼運算式，為什麼會因表示、型別與轉換而產生不同程式行為？**

大綱重點：整數範圍、bit／byte、signed／unsigned 邊界、字元表示、浮點近似、型別轉換與格式化 I/O。必須區分可攜的 C 保證與 implementation-defined／implementation-specific 觀察。

核心證據：結果預測、適合目標實作的邊界實驗、轉換／格式錯誤診斷，以及表示限制的說明。

核心反思：說明表示、型別、轉換與運算規則如何限制可觀察結果。

---

## F-U02 — 如何建立可靠的多分支與重複流程？

核心問題：**當條件、邊界與重複規則變複雜時，如何仍能證明流程正確？**

大綱重點：多路選擇、巢狀控制、sentinel、invariant、路徑覆蓋、複合條件，以及控制流程修改後的回歸。

核心證據：路徑表／圖、不變量或迴圈狀態說明、邊界／sentinel 測試、邏輯錯誤診斷，以及修正後驗證。

核心反思：說明路徑覆蓋、迴圈條件、邊界、sentinel 與 invariant 如何提供互補證據。

---

## F-U03 — 資料如何形成有順序的集合？

核心問題：**當多個相關值需要一起保存與處理時，如何安全地組織、定位與走訪它們？**

大綱重點：Array、Index、Length／Capacity、連續元素配置、Traversal、函數參數中的陣列行為，以及越界風險。

核心證據：索引／配置圖、走訪追蹤、有效／無效邊界案例、安全的索引錯誤診斷，以及大小修改後重新測試。

核心反思：說明陣列配置、索引、有效邊界與迭代之間的關係。

---

## F-U04 — 文字資料如何被表示與處理？

核心問題：**C 如何表示文字，又如何知道有效內容與容量邊界？**

大綱重點：`char` 陣列、null termination、string literal、容量與長度、`fgets`、輸入換行／狀態、選定字串函式與 buffer 邊界。

核心證據：字元陣列／字串圖、容量／終止測試、截斷或輸入處理問題診斷，以及修正後重新測試。

核心反思：說明為什麼不是每個 `char` 陣列都是有效 C 字串，以及容量與終止為何是不同問題。

---

## F-U05 — 巢狀與遞迴函數呼叫期間有哪些狀態？

核心問題：**在巢狀或遞迴呼叫中，如何理解參數、區域物件、回傳位置、scope 與 lifetime，而不把單一實體 runtime 表示當成語言保證？**

大綱重點：Activation Model、Scope、Lifetime、Automatic Storage Duration、Nested Calls、Recursion、Base／Termination Condition 與資源影響。Call-stack 圖可以作為特定實作／教學模型，但不得表述為 C 語言保證。

核心證據：activation／lifetime 追蹤、scope 與 lifetime 比較、遞迴追蹤，以及非終止或錯誤生命週期推理的診斷。

核心反思：說明 scope、物件 lifetime、activation state 與目標實作可能使用的 call-stack 視覺化有何不同。

---

## F-U06 — 如何透過指標值間接存取資料？

核心問題：**指標值如何指向物件，又必須滿足哪些前提才能合法地間接存取？**

大綱重點：Object、Address、Pointer Type／Value、Null Pointer、Dereference Preconditions、Aliasing、Pointer Parameter、Lifetime、Bounds 與有限的 Array 關係。

核心證據：物件－指標圖、aliasing 追蹤、有效／無效前提分類、透過 pointer parameter 修改 caller 資料，以及 null／dangling／out-of-bounds 風險的安全診斷。

核心反思：說明 pointer type／value、被指向物件、lifetime、bounds 與 dereference 前提如何連結。

---

## F-U07 — 一個資料物件如何包含不同欄位？

核心問題：**當一個實體包含多種不同資料時，如何把欄位表示並操作成一個有意義的 record？**

大綱重點：從需求辨識欄位、`struct` 型別／物件、member access、initialization、assignment、passing、nested structure、layout caveat 與 record validity。

核心證據：依需求設計 record、member 更新、函數互動、無效資料測試，以及兩種資料設計比較。

核心反思：說明 structure type、structure object、members 與圍繞該 record 的 interface responsibility 有何不同。

---

## F-U08 — 程式如何管理執行期間才決定大小或生命週期的儲存空間？

核心問題：**當所需空間無法事先固定時，如何安全處理配置、調整大小、ownership／release responsibility、失敗與 lifetime？**

大綱重點：`malloc`、`calloc`、`realloc`、`free`、size arithmetic、allocation failure、保留舊指標的 resize 模式、ownership／release responsibility、dangling use、leak 與 double release。

核心證據：配置／使用／釋放圖、大小／邊界推理、明確失敗路徑、ownership 說明、安全 resize 實作，以及容量修改後回歸。

核心反思：說明配置成功、pointer ownership、lifetime、resize 與 release responsibility 如何連結。

---

## F-U09 — 程式如何與檔案及持久資料互動？

核心問題：**從外部檔案讀寫資料時，程式如何區分有效資料、輸入結束與失敗，同時維持正確資源狀態？**

大綱重點：pathname／file 與 opened stream 的差異、`FILE *`、open／read／write／close 結果、end-of-input indication、stream error state、text format／protocol，以及適用時的 transactional／failure-preserving loading。

核心證據：狀態／錯誤追蹤、open／read／write 失敗案例、持久資料驗證、資源關閉推理，以及格式／錯誤處理修正。

核心反思：說明 pathname／file、opened stream、end-of-input indication 與 error state 有何不同。

---

## F-U10 — 如何把程式分成可獨立維護的模組？

核心問題：**如何分離 interface 與 implementation，使程式各部分能以明確依賴被修改與建置？**

大綱重點：header／source、declaration／definition、include guard、translation unit、目標工具鏈建置步驟、適用時的 linkage、dependency tracing，以及 compile 與 link 證據。

核心證據：interface／implementation 分離、dependency graph、目標工具鏈建置、declaration／definition／linkage 問題診斷，以及在穩定介面下替換 implementation。

核心反思：說明 interface、implementation、translation unit、dependency 與 linkage／build evidence 有何不同。

---

## F-U11 — 如何系統化測試、診斷與改善程式？

核心問題：**除了單次正確輸出之外，還需要哪些證據才能信任程式或技術主張？**

大綱重點：Expected Result、正常／邊界／無效／失敗測試、Reproducibility、Symptom／Cause／Hypothesis、Debugging、Verification、Validation、Regression、Refactoring、Evidence Quality 與 Confidence Limit。

核心證據：先寫預期結果的測試設計、可重現錯誤、假設驗證、修正、回歸，以及證據強度比較。

核心反思：說明 Testing、Verification、Validation、Debugging 與 Regression Verification 的差異與關係。

---

## F-U12 — 如何整合整門課的程式設計 Concept？

核心問題：**如何把需求、資料、流程、函數、memory／lifetime、interaction 與 engineering evidence 整合成一個可維護程式？**

大綱重點：Requirement Contract、Decomposition、Data／Control／Module Design、Incremental Implementation、Failure Handling、Testing、Modification、Validation、Maintenance 與 Trade-off Explanation。

核心證據：從 requirement 到 implementation／test evidence 的端到端追蹤、需求修改、已診斷的 defect 或 failure path、regression verification，以及剩餘限制說明。

核心反思：說明 requirement、design、implementation、tests、failure handling 與 maintenance evidence 如何形成一個完整開發循環。

---

## 選用外部協助延伸模式

Unit 可以在核心路徑之後選擇加入短延伸，例如：

1. 學生先陳述自己的推理或預期結果；
2. 學生選擇是否取得外部建議；
3. 找出值得檢查的主張；
4. 以程式、測試、diagnostics、可靠參考資料、追蹤或其他可重現方式驗證；
5. 接受、修改或拒絕該建議。

此模式永遠不是普遍必做。除非特定已核准活動或學術誠信規則明確要求，否則不要求固定 Prompt、完整對話紀錄、前後版本工件、AI 摘要或未使用聲明。

## 維護規則

修改本規劃模型時：

- 中英文版本必須一起更新；
- 保留 Unit ID 與現行 Unit Map 的核心問題／證據方向；
- 在宣稱實作完成前，必須把大綱變更與目前實際學生教材比對；
- 不重複正式評量政策；
- 選用外部協助必須可直接跳過；
- 具體技術敘述必須依指定 C 標準／工具鏈／環境驗證；
- 重要治理修正必須記錄於現行 Constitution 2.0 審查。

## 相關文件

- [Concept 驅動的 Unit Map](16-unit-map.zh-TW.md)
- [程式設計 Concept Registry](15-programming-concept-registry.zh-TW.md)
- [正式學習與評量制度](13-learning-assessment-policy.zh-TW.md)
- [正式學生教材](../materials/formal/README.zh-TW.md)
- [前導學生教材](../materials/preparatory/)
- [教學內容設計區](README.zh-TW.md)
- [English version](17-student-material-outlines.en.md)
