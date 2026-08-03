# 課程交付地圖

版本：0.2.0  
狀態：正式交付基準  
最後更新：2026-08-03  
重大變更摘要：加入每堂前次作業討論、課堂參與觀察與一次最終一對一口試，移除逐堂微型口試作為正式驗收。  
對應英文版本：[Course Delivery Map](08-delivery-map.en.md)

## 文件目的

本文件安排三條交付路徑：中文前導班 4×3 小時、英文前導班 5×2 小時，以及正式課程 16×3 小時。

每堂課都遵循共同循環：

```text
前次作業討論 15–25 分鐘
→ 本堂核心問題
→ 視覺模型與預測
→ 最小實作
→ 測試、除錯與修改
→ 指定下次自主作業
```

平時作業不繳交、不計分；課堂追問是形成性學習活動；只有最終一對一口試是總結性驗收。

## 一、共同交付原則

- 兩個語言班具有相同核心能力、成熟度與最終口試標準。
- 中文班多出的 2 小時用於更多追蹤、討論、補救與診斷，不增加核心要求。
- 不點名計分；出席不等於參與。
- 每堂課保留多元參與方式，包括口頭、書面、匿名提問、圖表、程式操作與小組紀錄。
- 作業討論優先處理學生真實錯誤、不同解法與測試盲點，不公布單一標準答案取代推理。
- 每個單元刻意包含可重現、可診斷、可修正的錯誤案例。

## 二、共同前導能力基線

兩班結束時均應能：

- 說明原始碼、編譯與執行的關係。
- 追蹤基本資料、條件與迴圈狀態。
- 完成小型輸入—處理—輸出程式。
- 說明函數責任並進行簡單分解。
- 建立正常、邊界與必要異常測試。
- 重現、診斷並修正一個缺陷。
- 驗證 AI 建議而非直接接受。

這些能力由自主作業累積，於課堂參與中形成性觀察，並在最終口試綜合驗證。

## 三、中文前導班：4 堂 × 3 小時

### 第 1 堂：程式如何開始執行

- 本堂沒有前次作業討論，先介紹學習與評量制度。
- 核心：工具鏈、最小程式、預測、編譯錯誤。
- 指定作業：作業 1「從原始碼到執行」。

### 第 2 堂：資料、型別與程式狀態

- 開始 15–25 分鐘討論作業 1。
- 核心：值、變數、型別、運算式、輸入輸出與狀態追蹤。
- 指定作業：作業 2「資料與狀態追蹤」。

### 第 3 堂：條件、迴圈與可靠終止

- 開始 15–25 分鐘討論作業 2。
- 核心：條件、迴圈四要素、邊界、off-by-one 與無窮迴圈。
- 指定作業：作業 3「條件與迴圈」。

### 第 4 堂：函數、整合與 AI 驗證

- 開始 15–25 分鐘討論作業 3。
- 核心：函數責任、分解、需求修改、回歸測試與 AI 建議審查。
- 指定作業：作業 4 與整合作業，作為最終口試準備。
- 課程結束前說明如何整理自主作業與學習紀錄，不在本堂進行正式口試。

## 四、英文前導班：5 堂 × 2 小時

### Session 1: Execution and First Program

- Introduce the learning and assessment policy.
- Core: toolchain, minimal program, prediction, and compile errors.
- Assign Homework 1.

### Session 2: Data, Types, and Program State

- Discuss Homework 1 for 15–25 minutes.
- Core: values, variables, types, expressions, input/output, and state tracing.
- Assign Homework 2.

### Session 3: Conditions and Repetition

- Discuss Homework 2 for 15–25 minutes.
- Core: conditions, loop elements, boundaries, and defect diagnosis.
- Assign Homework 3.

### Session 4: Functions and Decomposition

- Discuss Homework 3 for 15–25 minutes.
- Core: function responsibility, interfaces, calls, and decomposition.
- Assign Homework 4.

### Session 5: Integrated Cycle and AI Verification

- Discuss Homework 4 for 15–25 minutes.
- Core: integrated development cycle, requirement change, regression testing, and AI review.
- Assign the integrated practice as final oral-exam preparation.
- Explain how students should organize their saved work; no formal oral examination occurs during this session.

## 五、每堂作業討論的建議流程

```text
學生提出問題或匿名卡點
→ 教師挑選代表性錯誤
→ 全班先預測與追蹤
→ 比較不同解法或測試
→ 學生修正自己的理解
→ 教師連結到本堂新概念
```

建議時間：15–25 分鐘。若問題較多，優先處理會影響後續學習的概念缺口，而不是逐題講解完整答案。

## 六、課堂參與交付

教師或助教只需保留輕量觀察紀錄，例如：

- 提出具體問題。
- 參與追蹤、測試或除錯。
- 分享錯誤與修正。
- 補充、修正或比較解法。
- 使用非口頭方式提供可見貢獻。

不得以點名表或單純出席率取代參與證據，也不得要求每位學生每堂都公開發言。

## 七、正式 16 週課程

正式課程沿用同一學習循環與評量哲學，但能力成熟度逐步提高至 L4–L6。每週仍可用前次自主練習或專題進度作為開場討論素材；是否同樣只使用一次最終口試，需由正式課程評量制度另行確認，不由本前導交付地圖擅自推定。

## 八、最終口試銜接

前導課程結束後另行安排一次最終一對一口試。題型、時間、抽題、資源使用、補考與評分一致性由後續正式文件定義。

## 導覽

- [能力驗收模型](07-acceptance-model.zh-TW.md)
- [學習與評量制度](13-learning-assessment-policy.zh-TW.md)
- [教材索引](../materials/README.zh-TW.md)
- [English version](08-delivery-map.en.md)
