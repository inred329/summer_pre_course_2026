# 中英文術語對照表

版本：0.1.1  
狀態：現行設計標準  
治理說明：本詞彙表只標準化術語；治理、評分與工具使用規則仍以 Constitution 與正式學習／評量制度為權威來源。  
對應英文版本：[Chinese–English Terminology Glossary](11-terminology-glossary.en.md)

## 文件目的

本文件提供課程設計、學生教材、教師資源、活動與評量實作共用的術語標準，避免同一概念在不同文件被任意改名或賦予衝突意義。

主要讀者為教師、助教、教材作者、翻譯者與維護者。重要術語變更必須同步中英文版本，並更新受影響文件。

## 使用規則

1. 表達同一概念時使用已核定術語。
2. 首次介紹重要術語時，若有助於雙語維護或學生理解，可同時提供中英文。
3. 英文優先採專業慣用法，不追求逐字翻譯。
4. 說明欄必須區分語言語意、概念教學模型與實作相依行為。
5. C 關鍵字、函式名稱、識別碼與標準函式庫名稱原則上不翻譯。
6. 術語出現在詞彙表中，不代表它自動成為核心、必評或必做內容。

---

## 課程設計與治理

| 中文 | English | 使用說明 |
|---|---|---|
| 課程憲法 | Course Constitution | Repository 層級最高治理原則與修訂規則。 |
| 正式學習與評量制度 | Official Learning and Assessment Policy | 本 repository 中評分、參與、作業、最終口試角色與 AI／工具使用政策的唯一正式權威來源。 |
| 設計標準 | Design Standard | 用於維護能力、範圍、術語、Concept 或 Unit 結構的穩定定義；受 Constitution 與正式政策約束。 |
| 規劃與追蹤模型 | Planning and Traceability Model | 可修訂的設計理由、對應、交付、風險或大綱文件；不具獨立政策效力。 |
| 領域模型 | Domain Model | 描述概念及關係，不定義唯一授課順序。 |
| 知識依賴圖 | Knowledge Dependency Graph | 描述強依賴、支援依賴、橫向依賴或條件式依賴。 |
| 能力地圖 | Competency Map | 定義可觀察程式能力、識別碼、證據期待與成熟度關係。 |
| 範圍邊界 | Scope Boundary | 定義核心、基礎、延後、課程外與條件式／選用內容。 |
| 驗收模型 | Acceptance Model | 將成熟度對應到候選證據／任務形式的規劃模型；不自行建立評分政策。 |
| 交付地圖 | Delivery Map | 規劃節奏與活動位置；負責實作政策而不是定義政策。 |
| 風險登錄表 | Risk Register | 記錄風險、觸發、緩解、應變與責任角色。 |
| 追蹤矩陣 | Traceability Matrix | 連結需求、概念、能力、範圍、證據、Unit／教材與風險。 |
| 學習證據 | Learning Evidence | 支持能力判定的可觀察行為或作品。 |
| 成熟度 | Maturity | 可觀察能力程度：辨識、解釋、追蹤、實作、診斷、遷移。 |

### 範圍狀態

| Code | 中文 | English | 意義 |
|---|---|---|---|
| SB-C | 核心交付 | Core Delivery | 指定階段／成熟度下必須達成的能力。 |
| SB-F | 基礎鋪墊 | Foundation Only | 建立名詞／模型／目的，不宣稱可獨立實作。 |
| SB-D | 後續深化 | Deepen Later | 已有初步能力，更高成熟度延後。 |
| SB-I | 延後實作 | Implement Later | 可先理解／追蹤，完整實作／診斷延後。 |
| SB-O | 課程外 | Out of Scope | 不屬於目前核心交付。 |
| SB-X | 條件式／選用 | Conditional / Optional | 只有對應選用活動／工具實際被使用，或被明確核准為活動目標時才適用；不是普遍完成門檻。 |

---

## 程式轉換與執行

| 中文 | English | 使用說明 |
|---|---|---|
| 原始碼 | Source Code | 提供給實作處理的人類可閱讀程式文字；本課常見為 `.c`／`.h`。 |
| 前置處理行為 | Preprocessing Behavior | C 翻譯過程中的指令、檔案引入、巨集替換與條件處理；不保證存在獨立 preprocessor 程式／檔案。 |
| 編譯／轉換 | Compilation / Translation | 將 C 原始碼／translation unit 轉向可執行或較低階表示的概念責任；實作可合併不同階段。 |
| 編譯器 | Compiler | 常用來稱呼翻譯原始碼並產生診斷的工具／實作元件；具體行為依指定實作而異。 |
| 組譯 | Assembly | 在暴露該階段的工具鏈中，將 assembly language 轉成 object／machine representation；不是 C 語言保證存在的獨立階段。 |
| 目的碼／目的檔 | Object Code / Object File | 常見原生工具鏈用於連結的中介表示／檔案；C 標準不保證它一定可見。 |
| 連結 | Linking | 適用時組合翻譯單元／函式庫並解析外部參照。 |
| 連結器 | Linker | 在有獨立連結階段的工具鏈中執行 linking 的工具／實作元件。 |
| 可載入程式映像 | Loadable Program Image | 目標環境可載入或以其他方式執行的程式表示；「可執行檔」是常見實作形式之一。 |
| 載入／啟動 | Loading / Startup | 目標環境將程式準備為可執行狀態的過程。 |
| 程序 | Process | 常見作業系統對執行中程式及資源／狀態的模型；不是每個 C 執行環境都必然存在。 |
| 診斷 | Diagnostic | 實作針對翻譯／建置或執行條件提供的訊息或其他回饋。 |
| 標準函式庫 | Standard Library | C 標準所規範並由符合要求的實作提供之函式庫功能。 |

---

## 資料、狀態、控制與函數

| 中文 | English | 使用說明 |
|---|---|---|
| 資料 | Data | 被表示、處理、儲存或傳遞的資訊。 |
| 值 | Value | 與運算式或物件相關的資訊內容。 |
| 型別 | Type | 依 C 語意定義／限制表示、值集合、操作、轉換與解讀方式。 |
| 物件 | Object | C abstract machine 中的資料儲存區域，其內容可表示值；不得讓學生誤以為是 C++ 物件導向概念。 |
| 變數 | Variable | 課程友善用語，指可改變儲存值的具名物件；精確討論時應區分 identifier／名稱與 object 本身。 |
| 識別碼 | Identifier | 依 scope／linkage 規則可用來指定程式實體的名稱 token。 |
| 常數 | Constant | 依語境而異；應區分 literal、enumeration constant、constant expression 與 `const`-qualified object，不能視為同一件事。 |
| 運算式 | Expression | 依 C 規則求值的語言構造，可產生值與／或 side effect。 |
| 指定 | Assignment | 在型別／轉換規則下把值存入可修改物件。 |
| 狀態 | State | 某觀察點下相關程式／物件／stream／控制資訊。 |
| 順序 | Sequence | 求值／執行的有序關係；C 若未規定完整 evaluation order，不得暗示一定存在全序。 |
| 條件 | Condition | 用於決定控制行為的運算式／結果。 |
| 選擇 | Selection | 根據條件選擇執行路徑，例如 `if`／`switch`。 |
| 重複 | Repetition | 在明確持續／終止規則下反覆執行。 |
| 終止條件 | Termination Condition | 決定重複何時停止的條件或狀態。 |
| 不變條件 | Invariant | 在計算特定觀察點應維持成立的性質，常用於 loop reasoning。 |
| 函數 | Function | 具型別／介面與適用定義／實作的可呼叫單位。 |
| 參數 | Parameter | 函數宣告／定義中依 C 語意接收呼叫資料的物件／識別碼。 |
| 引數 | Argument | 函數呼叫時提供的運算式。 |
| 回傳值 | Return Value | 回傳型別允許時，由函數傳回給呼叫端的值。 |
| 介面 | Interface | 呼叫者／使用者需要知道的名稱、型別、契約、前置／後置條件及適用的所有權／生命週期規則。 |
| 實作 | Implementation | 滿足介面的內部機制，或語言／工具鏈的具體實現。 |
| 模組化 | Modularization | 以明確介面與 source／build 邊界組織責任。 |
| 遞迴 | Recursion | 直接或間接重複函數呼叫；若預期有限計算，需要可到達的終止／base case。 |

---

## 記憶體與生命週期

| 中文 | English | 使用說明 |
|---|---|---|
| 儲存空間／儲存位置 | Storage / Storage Location | 與 abstract／target machine 中物件相關的儲存。 |
| 位址 | Address | 在相關模型中用於識別／指向儲存、物件或函數位置的表示／值；不能把所有位址都當成可攜整數。 |
| 指標 | Pointer | 具型別的 C 物件／值類別，可依型別表示物件／函數指標或 null pointer value。 |
| 空指標 | Null Pointer | 保證不指向物件／函數的指標值；C 不宜稱為「null reference」。 |
| 取址 | Address-of | 以 `&` 取得符合 C 規則之物件／函數指標的操作。 |
| 解參考 | Dereference / Indirection | 透過 `*` 由指標間接存取；只有在生命週期、型別、alignment、邊界與其他前提都成立時才有效。 |
| 別名 | Aliasing | 多個存取路徑指定同一或重疊儲存物件；C aliasing／effective-type 規則可能限制合法存取。 |
| 範圍 | Scope | 識別碼在程式文字中可見的區域。 |
| 生命週期 | Lifetime | 物件存在於程式執行中的時間範圍；與 identifier scope 不同。 |
| 儲存期 | Storage Duration | C 對物件儲存／最低生命週期的分類：automatic、static、thread（若支援）或 allocated。 |
| 自動儲存期 | Automatic Storage Duration | 通常與 block 進出相關；實體 stack 是常見實作，但不是語言保證。 |
| 配置儲存期 | Allocated Storage Duration | 課程用語，表示由配置函式取得並持續到 deallocation 的儲存；比把「heap」當成 C 標準術語更精確。 |
| 呼叫堆疊 | Call Stack | 常見 nested call／activation record 的實作與教學模型；C 不強制特定實體結構。 |
| Heap | Heap | 動態配置區域的非正式實作用語；不得與 heap 資料結構混淆，也不得當成 C 標準術語。 |
| 所有權／釋放責任 | Ownership / Release Responsibility | API／設計層級對誰可使用、轉移或釋放資源的責任；C 沒有語言層級強制 ownership system。 |
| 記憶體安全 | Memory Safety | 避免越界、懸空使用、double free 等無效生命週期／邊界／存取及相關 undefined behavior。 |

---

## 資料組織與互動

| 中文 | English | 使用說明 |
|---|---|---|
| 序列 | Sequence / Ordered Collection | 元素具有順序／位置的集合；與 execution sequence 需依語境區分。 |
| 索引 | Index | 用來選取元素的值；合法性取決於資料結構與邊界。 |
| 陣列 | Array | C 中由同一元素型別組成的連續配置 object type；教材範例必須交代長度／邊界。 |
| 字串 | String | C 中由字元組成且以第一個 null character 終止的連續序列；不是每個 `char` array 都是 string。 |
| 記錄 | Record | 將描述同一實體的欄位概念性群組。 |
| 結構 | Structure / `struct` | C 用來定義具名 member 之 structure type 的機制，是 record 概念的具體映射。 |
| 輸入 | Input | 從外部來源提供給程式／函數的資料。 |
| 輸出 | Output | 程式對外部目的地產生的可觀察資料／結果。 |
| 串流 | Stream | C standard I/O 對與外部 file／device 關聯之有序字元序列的抽象。 |
| 緩衝區 | Buffer | 暫存輸入／輸出或轉換資料的空間；安全相關時必須明確容量與有效內容。 |
| 檔案 | File | 環境／C I/O library 所建模的外部資料來源／目的地；應區分 path／name 與已開啟 stream。 |
| 輸入結束 | End of Input / End-of-File indication | 表示沒有更多輸入的條件／函式結果；`EOF` 是某些函式使用的 macro value，不是每個檔案實際存的一個字元。 |
| 格式 | Format | 表示／解析資料的規則，包含 `printf`／`scanf` conversion specification 與檔案協定。 |
| 協定 | Protocol | 互動或序列化資料的共同結構、順序與意義規則。 |

---

## 測試、除錯與選用外部協助

| 中文 | English | 使用說明 |
|---|---|---|
| 預期結果／預期性質 | Expected Result / Expected Property | 在依賴實際輸出前，依需求／契約推導的行為或性質。 |
| 實際證據 | Actual Evidence | 觀察到的診斷、輸出、狀態追蹤、檔案內容、memory-tool 證據或其他相關觀察。 |
| 測試案例 | Test Case | 明確輸入／條件與預期結果／性質。 |
| 正常案例 | Normal Case | 一般合法使用案例。 |
| 邊界案例 | Boundary Case | 靠近已定義範圍、轉折或大小邊界的案例。 |
| 無效輸入案例 | Invalid-Input Case | 違反已述輸入契約的資料；需要先定義應如何處理。 |
| 失敗案例 | Failure Case | 觸發可能操作／資源失敗，如 allocation、file open、parse、write failure。 |
| 執行／狀態追蹤 | Execution / State Trace | 逐步記錄相關控制、值、呼叫、stream、物件或生命週期。 |
| 測試 | Testing | 使用選定案例對照預期性質進行執行／評估。 |
| 驗證 | Verification | 蒐集證據確認實作或技術主張滿足明確需求／契約。 |
| 需求適切性確認 | Validation | 蒐集證據確認實作行為解決實際需求／使用情境；應與 verification 區分。 |
| 除錯 | Debugging | 重現、縮小範圍、提出假設、驗證原因、修正並回歸。 |
| 回歸驗證 | Regression Verification | 修改／修正後重新檢查先前必要行為。 |
| 外部協助 | External Assistance | 來自 AI、文件、同儕、教師、工具或其他來源的建議／內容；核心推理責任仍在學生。 |
| AI 輔助學習 | AI-assisted Learning | 選用 AI 支援學習；不是普遍能力、完成門檻或證據要求。 |
| 人工審查 | Human Review | 學生／教師在採用建議前檢查相關性、假設、限制與適用性。 |
| 技術驗證 | Technical Verification | 以程式、測試、診斷、可靠來源、追蹤或其他適當可重現證據檢查。 |
| 情境式揭露 | Contextual Disclosure | 只有特定核准活動、誠信規則或評量條件要求時才需要工具使用標註／紀錄；預設未使用時不需聲明。 |
| AI 使用紀錄 | AI-use Record | 明確被要求時可能使用的情境式 artifact；不得默認為所有作業或評量的普遍要求。 |

---

## 成熟度術語

| Level | 中文 | English |
|---|---|---|
| L0 | 尚未建立 | Not Established |
| L1 | 辨識 | Recognize |
| L2 | 解釋 | Explain |
| L3 | 追蹤 | Trace |
| L4 | 實作 | Implement |
| L5 | 診斷 | Diagnose |
| L6 | 遷移 | Transfer |

Concept Registry 必須使用這套成熟度意義，或明確提供任何局部簡寫與本標準的對應，不能私自重新定義 L1–L6。

## 維護條件

本詞彙表維護到位時：

- 中英文版本實質等值。
- 定義符合現行 C 語意與 repository 治理。
- 概念與實作相依術語有清楚標示。
- 過時或誤導術語會同步修正到相依文件。
- 新術語不會默默建立範圍、政策或評量要求。
- 變更可透過 Git 歷史與進行中的全庫審查追蹤。

## 相關文件

- [教學內容設計區](README.zh-TW.md)
- [程式設計領域模型](03-programming-domain-model.zh-TW.md)
- [程式設計能力地圖](05-competency-map.zh-TW.md)
- [課程範圍邊界](06-scope-boundary.zh-TW.md)
- [程式設計 Concept Tree](14-programming-concept-tree.zh-TW.md)
- [程式設計 Concept Registry](15-programming-concept-registry.zh-TW.md)
- [English version](11-terminology-glossary.en.md)
