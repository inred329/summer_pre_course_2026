# 課程交付地圖

版本：0.2.1  
狀態：可修訂的規劃模型  
治理說明：本文件規劃授課節奏與活動配置；作業、課堂參與、出席、成績結構、最終口試與 AI／工具規則，以[學習與評量制度](13-learning-assessment-policy.zh-TW.md)為權威來源。  
對應英文版本：[Course Delivery Map](08-delivery-map.en.md)

## 文件目的

本文件規劃三條相互銜接的交付路徑：中文前導班 4 × 3 小時、英文前導班 5 × 2 小時，以及銜接的正式 C 程式設計課程。

典型課堂循環如下：

```text
適用時討論前次自主練習
→ 本堂核心問題與心智模型
→ 預測或追蹤
→ 最小實作／推理
→ 測試、除錯與需求修改
→ 自主延伸練習
```

正式學習與評量制度決定自主作業是否繳交／計分、課堂參與如何觀察，以及最終口試的角色。本交付地圖只負責落實該制度，不重新定義政策。

## 一、共同交付原則

- 兩個前導語言班維持相同核心能力與技術深度，但可採不同節奏與語言支架。
- 中文班較多的時數用於增加追蹤、討論、補救與診斷，不增加核心要求。
- 每堂課應提供符合正式政策的多種參與方式。
- 自主練習討論優先處理真實錯誤、不同解法、邊界案例與測試盲點，不以單一標準答案取代推理。
- 每個單元應提供預測、觀察、診斷、修正、修改與驗證的機會。
- AI 與其他外部工具預設為選用；選用工具活動必須可直接跳過，且不影響核心完成或參與證據。

## 二、共同前導能力基線

兩個前導班結束時，學生應能：

- 以適當概念層次說明 C 原始碼在指定環境中如何經翻譯／建置後執行。
- 追蹤基本資料／狀態、條件與迴圈行為。
- 完成並解釋小型輸入—處理—輸出程式。
- 說明函數責任並進行簡單分解。
- 建立預期結果，以及正常、邊界與適用的無效／失敗案例。
- 重現、診斷、修正並重新測試至少一個缺陷。
- 修改一項小型需求並說明受影響部分。

學生若選擇使用 AI 或其他外部協助，仍須對採用結果的理解與驗證負責；「使用工具」本身不屬於共同前導能力基線。

## 三、中文前導班：4 堂 × 3 小時

### 第 1 堂：程式如何開始執行

- 入口：介紹課程導覽、指定環境與現行學習／評量制度。
- 核心：翻譯／建置的概念責任、指定工具鏈、最小程式、預測與基本診斷判讀。
- 自主練習：從原始碼到執行。

### 第 2 堂：資料、型別與程式狀態

- 有適合素材時，討論前次練習的代表性問題。
- 核心：值、物件／變數、型別、運算式、輸入輸出、狀態追蹤與輸入假設。
- 自主練習：資料與狀態追蹤。

### 第 3 堂：條件、迴圈與可靠終止

- 討論前次練習的代表性問題。
- 核心：條件、迴圈狀態、終止、邊界、off-by-one 與不終止診斷。
- 自主練習：條件與迴圈。

### 第 4 堂：函數與整合驗證

- 討論前次練習的代表性問題。
- 核心：函數責任、問題分解、需求修改、測試、除錯與回歸驗證。
- 自主練習：函數／整合練習與小型整合開發循環。
- 選用延伸：審查一項 AI 或其他外部建議，並以可重現證據驗證被採用的技術主張。跳過此延伸仍完成相同核心課程。

## 四、英文前導班：5 堂 × 2 小時

### Session 1: Execution and First Program

- Introduce course navigation, the specified environment, and the current learning/assessment policy.
- Core: conceptual translation/build responsibilities, the specified toolchain, a minimal program, prediction, and basic diagnostics.
- Follow-up practice: execution and first-program work.

### Session 2: Data, Types, and Program State

- Discuss representative issues from previous practice.
- Core: values, objects/variables, types, expressions, input/output, and state tracing.
- Follow-up practice: data and state.

### Session 3: Conditions and Repetition

- Discuss representative issues from previous practice.
- Core: conditions, loop state, termination, boundaries, and defect diagnosis.
- Follow-up practice: conditions and loops.

### Session 4: Functions and Decomposition

- Discuss representative issues from previous practice.
- Core: function responsibility, interfaces, calls, decomposition, and small caller-side tests.
- Follow-up practice: functions and decomposition.

### Session 5: Integrated Development Cycle

- Discuss representative issues from previous practice.
- Core: requirement change, integrated reasoning, testing, debugging, regression verification, and reflection.
- Follow-up practice: integrated development-cycle work.
- Optional extension: review an AI or other external suggestion and verify any adopted claim. Skipping this extension does not affect core completion.

## 五、自主練習討論流程

可採用的實作模式：

```text
學生提出問題、缺陷或匿名卡點
→ 教師挑選代表案例
→ 全班先預測或追蹤
→ 比較測試、解法或診斷
→ 學生修正推理
→ 教師把證據連回本堂新概念
```

正式政策目前建議保留專門的討論時間；具體分鐘數屬於政策與教師執行層，而不是本規劃模型的獨立規範。

## 六、課堂參與交付

教師或助教可依正式政策保留輕量證據紀錄，例如：

- 提出具體問題或卡點。
- 參與追蹤、測試、除錯或比較。
- 分享錯誤、測試、修正或不同解法。
- 修正自己先前的說明。
- 以書面、圖示、程式操作、匿名輸入或小組方式貢獻。

本地圖不把出席、發言速度或特定文件轉換成評分規則。

## 七、銜接正式課程

正式課程可沿用相同學習循環，並把能力提升到實作、診斷、遷移、模組化推理、記憶體／生命週期責任與更完整測試。

除非透過 repository 治理程序正式修改權威評量政策，正式課程交付設計必須持續符合相同的正式學習與評量制度。本交付地圖不得自行建立衝突的第二套評量制度。

## 八、最終一對一口試銜接

正式學習與評量制度已定義最終一對一口試的角色。交付教材應讓學生能對自己的工作進行解釋、追蹤、修改、測試、診斷與理由說明。

本規劃模型不自行設定口試日期、時間、題數、可用資源、補考方式或評分方法；這些細節應由日後核定的雙語口試程序定義。

## 維護規則

修改本交付地圖時：

1. 維持兩個語言班與中英文文件的實質等值。
2. 新增核心內容前先檢查能力地圖與範圍邊界。
3. 修改作業、參與、出席、口試或工具使用敘述前先檢查正式評量制度。
4. AI／工具選用活動必須明確標示為條件式且可直接跳過。
5. 具體 compiler／toolchain 敘述要依指定環境驗證。
6. 重大治理發現記錄到進行中的全庫審查。

## 相關文件

- [能力驗收模型](07-acceptance-model.zh-TW.md)
- [學習與評量制度](13-learning-assessment-policy.zh-TW.md)
- [課程範圍邊界](06-scope-boundary.zh-TW.md)
- [教材索引](../materials/README.zh-TW.md)
- [教學內容設計區](README.zh-TW.md)
- [English version](08-delivery-map.en.md)
