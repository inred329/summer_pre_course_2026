# 教材與活動資源

版本：1.2.0  
狀態：前導教材、評量制度與教師執行包完成  
最後更新：2026-08-03  
重大變更摘要：新增雙語教師執行指引與教材評量優先規則，完成可直接授課的前導課程執行基準。  
對應英文版本：[Materials and Activity Resources](README.en.md)

## 文件目的

本目錄提供中文與英文前導班的教材、活動、自主作業、課堂討論、參與觀察、AI 紀錄、教師執行及最終口試準備資源。

所有正式教材必須：

- 由根 README 與本索引抵達。
- 同時提供繁體中文與英文版本。
- 引用需求 ID、能力 ID、成熟度、範圍狀態與驗收任務。
- 將閱讀、預測、實作、修改、測試、除錯與說明納入學習循環。
- 明確說明 AI 允許、禁止與必須保留的證據。
- 不把作業繳交、點名或單次輸出當成能力證據。

## 正式前導教材

| 單元 | 中文教材 | 英文教材 | 核心交付 |
|---|---|---|---|
| 1 | [程式如何開始執行](preparatory/unit-01-execution.zh-TW.md) | [How a Program Begins to Run](preparatory/unit-01-execution.en.md) | 工具鏈、最小程式、預測與錯誤分類 |
| 2 | [資料、型別與程式狀態](preparatory/unit-02-data-state.zh-TW.md) | [Data, Types, and Program State](preparatory/unit-02-data-state.en.md) | 值、型別、狀態追蹤、輸入輸出與需求修改 |
| 3 | [條件、迴圈與控制流程](preparatory/unit-03-control-flow.zh-TW.md) | [Conditions, Loops, and Control Flow](preparatory/unit-03-control-flow.en.md) | 路徑、終止、邊界測試與錯誤診斷 |
| 4 | [函數、整合開發與 AI 驗證](preparatory/unit-04-functions-integration.zh-TW.md) | [Functions, Integrated Development, and AI Verification](preparatory/unit-04-functions-integration.en.md) | 函數責任、整合循環、回歸與 AI 審查 |

中文班以四堂交付；英文班將單元 4 拆成 Session 4 與 Session 5。核心能力、難度與評量標準相同。

## 教師執行資源

- [前導課程教師執行指引](instructor/session-guides.zh-TW.md)
- [Preparatory Course Instructor Implementation Guide](instructor/session-guides.en.md)
- [前導教材評量制度補充規則](preparatory/ASSESSMENT-NOTE.zh-TW.md)
- [Preparatory Material Assessment Override](preparatory/ASSESSMENT-NOTE.en.md)

教師執行指引已包含：

- 中文四堂與英文五堂的節奏配置。
- 每堂課前次作業討論時間。
- 必備錯誤案例與錯誤 AI 建議。
- 課堂參與觀察點。
- 時間不足與工具故障時的備援策略。

教材中若仍出現「提交、補驗、微型口試」等舊措辭，以評量制度補充規則與 `design/07`、`design/13` 為準。

## 自主作業與評量資源

- [自主作業與口試準備包](assignments/preparatory-assignments.zh-TW.md)
- [Independent Homework and Oral Preparation Pack](assignments/preparatory-assignments.en.md)
- [課堂參與與最終口試評分規準](assignments/rubric.zh-TW.md)
- [Classroom Participation and Final Oral Examination Rubric](assignments/rubric.en.md)
- [AI 使用紀錄模板](assignments/ai-use-log.zh-TW.md)
- [AI Use Log Template](assignments/ai-use-log.en.md)
- [作業討論與課堂參與觀察指引](assignments/grading-guide.zh-TW.md)
- [Assignment Discussion and Participation Observation Guide](assignments/grading-guide.en.md)

## 正式制度

- 作業不繳交、不計分、不逐份批改。
- 每堂課開始保留 15–25 分鐘討論前次作業。
- 不點名計分；出席不等於參與。
- 課堂參與允許口頭、書面、匿名提問、程式操作與小組紀錄。
- 最終一次一對一口試是唯一總結性評量。
- 作業與學習紀錄由學生自行保存，作為討論及口試準備素材。

## 教材模板

- [單元教材模板](TEMPLATE.zh-TW.md)
- [Unit Material Template](TEMPLATE.en.md)

## 審查紀錄

- [前導教材憲法遵循審查](reviews/materials-constitution-review.zh-TW.md)
- [Preparatory Materials Constitution Review](reviews/materials-constitution-review.en.md)

## 下一階段

- 建立各單元可直接編譯的 C17 範例與缺陷程式。
- 在實際教室環境驗證 GCC／Clang 與 Windows／Linux 指令。
- 建立雙語等值的錯誤 AI 建議案例庫。
- 逐份清理單元教材中的舊評量措辭。
- 待後續討論後，建立最終一對一口試的正式雙語內容與流程文件。

## 導覽

- [學習與評量制度](../design/13-learning-assessment-policy.zh-TW.md)
- [返回倉庫首頁](../README.md)
- [教學內容設計區](../design/README.zh-TW.md)
- [English version](README.en.md)
