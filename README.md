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

課程憲法是本倉庫的最高指導文件。繁體中文版與英文版具有同等效力，並須同步維護。

The Course Constitution is the highest governing document of this repository. Its Traditional Chinese and English versions have equal authority and must be maintained together.

### 教學設計｜Instructional Design

教學內容以需求工程與系統設計的方式建立，先定義願景、需求與知識依賴，再建立能力、範圍、課程節奏及教材。

Instructional content is designed through a requirements-engineering and system-design approach: vision, requirements, and knowledge dependencies are defined before competencies, scope, delivery, and teaching materials.

- [教學內容設計區（繁體中文）](design/README.zh-TW.md)
- [Instructional Design Workspace (English)](design/README.en.md)

目前可由設計區導覽至：

The design workspace currently provides navigation to:

1. 課程產品願景｜Course Product Vision
2. 教學需求地圖｜Instructional Requirements Map
3. 程式語言知識圖｜Programming Language Knowledge Graph

### 既有課程與執行規劃｜Existing Course and Operational Planning

以下文件為較早期建立的規劃內容，後續仍須依憲法完成雙語化、一致性與導覽檢查：

The following files were created during an earlier planning stage and still require bilingual completion, consistency review, and navigation review under the Constitution:

- `docs/course-overview.md`：共用課程目標與設計決策
- `classes/zh/README.md`：中文班規劃
- `classes/en/README.md`：英文班規劃
- `planning/timeline.md`：籌備時程
- `planning/checklist.md`：執行檢查清單

在完成上述要求前，這些文件視為待整理內容，而非目前正式基準。

Until those requirements are satisfied, these files are treated as materials awaiting normalization rather than current official baselines.

---

## 核心設計理念｜Core Design Philosophy

本課程不把 C 視為需要死背的語法集合，而是用 C 幫助學生理解程式語言如何解決問題。

The course does not treat C as a collection of syntax to memorize. It uses C to help students understand how programming languages solve problems.

每個主要概念應依下列邏輯展開：

Each major concept should be developed through this sequence:

> 需求｜Need → 設計目的｜Design Purpose → 語言邏輯｜Language Logic → 語法｜Syntax → 實作｜Implementation → 驗證｜Verification

課程目前以以下知識面向組織：

The current knowledge architecture includes:

- 程式轉換與執行｜Program Translation and Execution
- 資料與狀態｜Data and State
- 流程與控制｜Flow and Control
- 函數與抽象｜Functions and Abstraction
- 記憶體模型｜Memory Model
- 資料組織｜Data Organization
- 測試、除錯與驗證｜Testing, Debugging, and Verification
- AI 輔助學習與人工驗證｜AI-assisted Learning and Human Verification

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
   Include purposeful visuals whenever visualization materially improves understanding.
5. 具有清楚目的、讀者、先備條件與完成標準。  
   State a clear purpose, audience, prerequisites, and completion criteria.
6. 能由本 README 經直接或間接導覽鏈抵達。  
   Be reachable from this README through a direct or indirect navigation path.

單一語言、未完成審核或未納入導覽的文件，均不得視為正式發布版本。

A single-language, unreviewed, or unnavigated document is not considered an officially published version.

---

## 目前工作階段｜Current Work Stage

目前已完成：

Completed:

- 課程憲法｜Course Constitution
- 課程產品願景｜Course Product Vision
- 教學需求地圖｜Instructional Requirements Map
- 程式語言知識圖｜Programming Language Knowledge Graph

下一階段將把知識節點轉換成可觀察、可驗收的能力地圖，之後再切分前導課程與正式課程範圍。

The next stage is to transform knowledge nodes into an observable and assessable competency map, followed by defining the scope boundary between the preparatory and formal courses.
