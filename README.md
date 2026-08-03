# 2026 大專暑期前導課程｜2026 Summer Preparatory Course

本倉庫用於規劃 2026 大專暑期 C 語言前導課程，以及與其銜接的 16 週正式程式設計課程。

This repository contains the design of the 2026 Summer C Programming Preparatory Course and the connected 16-week formal programming course.

課程包含兩個前導班別：

The preparatory course includes two tracks:

- 中文班：4 堂，每堂 3 小時，共 12 小時
- English-taught class: five 2-hour sessions, totaling 10 hours

兩班具有相同的核心學習成果、難度與驗收標準，只以不同節奏交付共同能力。

Both classes share the same core learning outcomes, difficulty, and acceptance standards, delivered through different pacing.

---

## 文件導覽｜Document Navigation

本 README 是倉庫內所有正式文件的根導覽入口。每份正式文件都必須能由此處透過直接連結或具明確語意的間接導覽鏈抵達。

This README is the root navigation entry for every official document in the repository. Each official document must be reachable from here through either a direct link or a semantically clear indirect navigation path.

### 最高規範｜Governing Documents

- [課程憲法（繁體中文）](CONSTITUTION.zh-TW.md)
- [Course Constitution (English)](CONSTITUTION.en.md)

### 教學設計基準｜Instructional Design Baseline

- [教學內容設計區（繁體中文）](design/README.zh-TW.md)
- [Instructional Design Workspace (English)](design/README.en.md)

目前正式設計基準包含 `01–12`：願景、需求、領域模型、知識依賴、能力、範圍、驗收、交付、風險、追蹤矩陣、術語表及憲法遵循審查。

The official design baseline includes stages `01–12`: vision, requirements, domain model, knowledge dependencies, competencies, scope, acceptance, delivery, risks, traceability, terminology, and constitutional review.

### 教材、作業與評量｜Materials, Assignments, and Assessment

- [教材與活動資源（繁體中文）](materials/README.zh-TW.md)
- [Materials and Activity Resources (English)](materials/README.en.md)
- [單元教材模板（繁體中文）](materials/TEMPLATE.zh-TW.md)
- [Unit Material Template (English)](materials/TEMPLATE.en.md)

前導課程正式基準已包含：

The preparatory-course baseline now includes:

- 四個雙語能力單元｜Four bilingual capability units
- 四份形成性作業｜Four formative assignments
- 一份整合作業｜One integrated assignment
- 共用雙語評分規準｜Shared bilingual rubric
- AI 使用紀錄模板｜AI-use log template
- 教師與助教批改指引｜Instructor and TA grading guide
- 教材憲法遵循審查｜Materials Constitution review

所有教材均要求預測、追蹤、實作、測試、除錯、修改、回歸驗證、說明與 AI 技術驗證；正確輸出、編譯成功或 OJ 通過不能單獨證明能力。

All materials require prediction, tracing, implementation, testing, debugging, modification, regression verification, explanation, and technical verification of AI suggestions. Correct output, successful compilation, or passing OJ cannot independently establish capability.

---

## 核心設計理念｜Core Design Philosophy

本課程不把 C 視為需要死背的語法集合，而是用 C 幫助學生理解程式語言如何解決問題。

The course does not treat C as a collection of syntax to memorize. It uses C to help students understand how programming languages solve problems.

每個主要概念依下列邏輯展開：

Each major concept develops through:

> 需求｜Need → 設計目的｜Design Purpose → 語言邏輯｜Language Logic → 語法｜Syntax → 實作｜Implementation → 驗證｜Verification

設計文件中的三個核心模型具有不同責任：

The three core design models have distinct responsibilities:

- 領域模型：有哪些概念與關係。
- 知識依賴圖：理解某概念前通常需要理解什麼。
- 能力地圖：學生必須能做到什麼，以及做到什麼程度。

- Domain model: which concepts and relationships exist.
- Knowledge dependency graph: what usually must be understood before another concept.
- Competency map: what students must be able to do and to what maturity.

資料組織目前維持在序列、記錄、索引與操作的抽象層，不預設進階資料結構為課程核心。

Data organization remains at the abstraction level of sequences, records, indexing, and operations; advanced data structures are not presumed core course content.

能力驗收至少需要互補證據；正確輸出、成功編譯、OJ 通過或 AI 的正面評價都不能單獨證明學生已建立能力。

Competency acceptance requires complementary evidence; correct output, successful compilation, passing OJ, or positive AI feedback cannot independently establish capability.

兩個前導班採不同節奏但相同核心標準；中文班額外 2 小時用於更多追蹤、補救、診斷與驗收，而不是新增核心能力。

The two preparatory tracks use different pacing but the same core standard; the Chinese-taught track's additional two hours support tracing, remediation, diagnosis, and acceptance rather than additional core capability.

高優先風險不得以降低驗收、擴張範圍、全面禁止 AI 或加入進階資料結構處理。

High-priority risks must not be treated by lowering acceptance, expanding scope, banning AI outright, or adding advanced data structures.

每項核心需求、能力、驗收與交付位置都必須能雙向追蹤；沒有需求來源、驗收證據或交付位置的項目不得列為正式核心內容。

Every core requirement, competency, acceptance task, and delivery location must support bidirectional traceability; an item without a requirement source, acceptance evidence, or delivery location may not be official core content.

---

## 文件完成條件｜Document Completion Conditions

所有正式文件均須：

Every official document must:

1. 同時提供繁體中文版與英文版。  
   Be available in both Traditional Chinese and English.
2. 中英文內容實質一致並同步維護。  
   Maintain substantive equivalence and synchronized updates.
3. 在撰寫與修改前參考課程憲法。  
   Be drafted and revised with reference to the Course Constitution.
4. 在適合視覺化時提供具有教學目的的圖形。  
   Include purposeful visuals when visualization materially improves understanding.
5. 具有清楚目的、讀者、先備條件與完成標準。  
   State a clear purpose, audience, prerequisites, and completion criteria.
6. 能由本 README 經直接或間接導覽鏈抵達。  
   Be reachable from this README through a direct or indirect navigation path.
7. 使用正式術語並保留版本、日期與重大變更摘要。  
   Use approved terminology and retain version, date, and major-change summary.

單一語言、未完成審核或未納入導覽的文件，不得視為正式發布版本。

A single-language, unreviewed, or unnavigated document is not an officially published version.

---

## 目前工作階段｜Current Work Stage

已完成：

Completed:

- 課程憲法與完整設計鏈
- 中英文術語與憲法遵循審查
- 雙語教材模板與教材索引
- 前導單元 1–4 雙語教材
- 前導作業包、rubric、AI 紀錄與教師批改指引
- 所有前導教材的憲法重讀與內容審查

- Course Constitution and complete design chain
- Bilingual terminology and constitutional review
- Bilingual material template and index
- Bilingual Preparatory Units 1–4
- Assignment pack, rubric, AI-use log, and grading guide
- Constitutional re-read and content review of all preparatory materials

發布前仍需在實際教室環境編譯範例、加入班級日期，並準備雙語等值的教師缺陷程式與錯誤 AI 建議。

Before classroom release, instructors must still compile examples in the actual environment, add class dates, and prepare bilingual-equivalent defective programs and sample incorrect AI suggestions.
