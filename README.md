# 2026 大專暑期前導課程｜2026 Summer Preparatory Course

本倉庫用於規劃 2026 大專暑期 C 語言前導課程，以及與其銜接的 16 週正式程式設計課程。

This repository contains the design of the 2026 Summer C Programming Preparatory Course and the connected 16-week formal programming course.

課程包含兩個前導班別：

The preparatory course includes two tracks:

- 中文班：4 堂，每堂 3 小時，共 12 小時
- English-taught class: five 2-hour sessions, totaling 10 hours

兩班具有相同的核心學習成果、難度與評量標準，只以不同節奏交付共同能力。

Both classes share the same core outcomes, difficulty, and assessment standards, delivered through different pacing.

---

## 文件導覽｜Document Navigation

### 最高規範｜Governing Documents

- [課程憲法（繁體中文）](CONSTITUTION.zh-TW.md)
- [Course Constitution (English)](CONSTITUTION.en.md)

### 教學設計基準｜Instructional Design Baseline

- [教學內容設計區（繁體中文）](design/README.zh-TW.md)
- [Instructional Design Workspace (English)](design/README.en.md)
- [學習與評量制度](design/13-learning-assessment-policy.zh-TW.md)
- [Learning and Assessment Policy](design/13-learning-assessment-policy.en.md)

正式設計基準包含 `01–13`：願景、需求、領域模型、知識依賴、能力、範圍、驗收、交付、風險、追蹤矩陣、術語、憲法審查，以及學習與評量制度。

The official design baseline includes stages `01–13`: vision, requirements, domain model, knowledge dependencies, competencies, scope, acceptance, delivery, risks, traceability, terminology, constitutional review, and the learning and assessment policy.

### 教材、自主作業與評量｜Materials, Independent Homework, and Assessment

- [教材與活動資源（繁體中文）](materials/README.zh-TW.md)
- [Materials and Activity Resources (English)](materials/README.en.md)
- [自主作業與口試準備包](materials/assignments/preparatory-assignments.zh-TW.md)
- [Independent Homework and Oral Preparation Pack](materials/assignments/preparatory-assignments.en.md)
- [課堂參與與最終口試評分規準](materials/assignments/rubric.zh-TW.md)
- [Classroom Participation and Final Oral Examination Rubric](materials/assignments/rubric.en.md)

## 正式學習與評量制度｜Official Learning and Assessment Policy

- 每次課後都有自主作業，但不繳交、不計分、不逐份批改。
- 下一堂課保留 15–25 分鐘討論前次作業、錯誤、測試與不同解法。
- 不以點名或出席率計分；出席不等於參與。
- 課堂參與可透過提問、回答、追蹤、測試、除錯、書面、匿名提問、程式操作或小組紀錄展現。
- 不以發言次數排名，亦不要求每位學生每堂公開發言。
- 正式成績只由課堂參與與一次最終一對一口試構成。
- 建議比例範圍：課堂參與 20–30%，最終口試 70–80%。
- 口試內容與流程將在後續討論後另立雙語正式文件。

- Independent homework follows each class but is not submitted, graded, or individually marked.
- The next class reserves 15–25 minutes to discuss the previous homework, errors, tests, and alternative solutions.
- Roll call and attendance percentage are not graded; attendance is not participation.
- Participation may be demonstrated through questions, answers, tracing, testing, debugging, writing, anonymous questions, program operation, or group records.
- Speaking frequency is not ranked, and students are not required to speak publicly in every class.
- The official grade consists only of classroom participation and one final one-on-one oral examination.
- Recommended range: participation 20–30%; final oral examination 70–80%.
- Detailed oral content and procedure will be defined in a later bilingual official document after further discussion.

---

## 核心設計理念｜Core Design Philosophy

本課程不把 C 視為需要死背的語法集合，而是用 C 幫助學生建立可遷移的程式設計能力。

The course does not treat C as a collection of syntax to memorize. It uses C to build transferable programming competency.

每個主要概念依下列邏輯展開：

Each major concept develops through:

> 需求｜Need → 設計目的｜Design Purpose → 語言邏輯｜Language Logic → 語法｜Syntax → 實作｜Implementation → 驗證｜Verification

教材與活動同等重視：

Materials and activities give equal importance to:

- 閱讀與預測｜Reading and prediction
- 狀態與流程追蹤｜State and flow tracing
- 實作與需求修改｜Implementation and requirement modification
- 測試、除錯與回歸驗證｜Testing, debugging, and regression verification
- 說明、反思與解法比較｜Explanation, reflection, and solution comparison
- AI 建議的技術驗證｜Technical verification of AI suggestions

每個單元應刻意設計可犯錯、可重現、可診斷與可修正的學習機會。正確輸出、成功編譯、OJ 通過或 AI 的正面評價都不能單獨證明能力。

Every unit should deliberately provide opportunities to make, reproduce, diagnose, and correct errors. Correct output, successful compilation, passing OJ, or positive AI feedback cannot independently establish capability.

資料組織維持在前導課程所需的抽象層，不預設進階資料結構為核心內容。

Data organization remains at the abstraction level needed by the preparatory course; advanced data structures are not presumed core content.

---

## 目前工作階段｜Current Work Stage

已完成：

Completed:

- 課程憲法與 `01–13` 正式設計鏈
- 雙語前導單元 1–4
- 自主作業與口試準備包
- 課堂參與與最終口試 rubric
- 作業討論與參與觀察教師指引
- AI 使用紀錄模板
- 教材憲法遵循審查

- Course Constitution and the official `01–13` design chain
- Bilingual Preparatory Units 1–4
- Independent homework and oral-preparation pack
- Classroom-participation and final-oral rubric
- Assignment-discussion and participation-observation guide
- AI-use log template
- Materials constitution review

下一階段是在後續討論後建立最終一對一口試的正式雙語內容與流程文件。發布前仍須在實際教室環境編譯所有 C17 範例，並建立雙語等值的缺陷程式與錯誤 AI 建議。

The next stage is to create the formal bilingual final one-on-one oral-examination content and procedure after further discussion. Before release, all C17 examples must still be compiled in the actual classroom environment, and bilingual-equivalent defective programs and incorrect AI suggestions must be prepared.
