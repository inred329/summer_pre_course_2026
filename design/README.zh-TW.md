# 教學內容設計區

版本：2.0.0  
狀態：現行設計治理索引  
最後更新：2026-08-07  
重大變更摘要：重新分類設計文件，避免所有文件共享模糊的「正式」地位。現在明確區分 Constitution、正式政策、設計標準、規劃與追蹤模型、執行指南及歷史紀錄。  
對應英文版本：[Instructional Design Workspace](README.en.md)

## 文件目的

本目錄支援 2026 暑期 C 語言前導課程與後續正式課程的設計及維護。這裡不是一組彼此權威相同的文件；每份文件都有明確的治理角色與主要讀者。

## 權威順序

文件內容衝突時，依下列順序判定：

1. `CONSTITUTION.zh-TW.md`：治理原則與修訂規則。
2. `design/13-learning-assessment-policy.zh-TW.md`：唯一正式的學習與評量政策。
3. 已核定的設計標準：維護範圍、能力、術語與教材結構的穩定定義。
4. 規劃與追蹤模型：可隨課程演進修正的操作性設計紀錄。
5. 指南與學生教材：上位規則的實作。
6. 歷史紀錄：保留早期決策證據，但不治理現行工作。

下位文件不得默默覆寫上位來源。發現衝突時，應修正下位文件，並在現行審查紀錄中留下裁決。

## 治理分類

| 文件 | 治理角色 | 主要讀者 | 可決定的內容 |
|---|---|---|---|
| `../CONSTITUTION.zh-TW.md` | Constitution | 所有角色 | 治理原則、不可妥協限制與修訂程序 |
| `13-learning-assessment-policy.zh-TW.md` | 正式政策 | 學生、教師、維護者 | 成績、參與、作業、口試與 AI 使用政策 |
| `05-competency-map.zh-TW.md`、`06-scope-boundary.zh-TW.md`、`11-terminology-glossary.zh-TW.md`、`14-programming-concept-tree.zh-TW.md`、`15-programming-concept-registry.zh-TW.md`、`16-unit-map.zh-TW.md` | 設計標準 | 設計者與維護者 | 在 Constitution 與正式政策限制內，定義穩定的能力、範圍、術語、Concept 與 Unit |
| `01-product-vision.zh-TW.md`、`02-requirements-map.zh-TW.md`、`03-programming-domain-model.zh-TW.md`、`04-programming-language-knowledge-graph.zh-TW.md`、`07-acceptance-model.zh-TW.md`、`08-delivery-map.zh-TW.md`、`09-risk-register.zh-TW.md`、`10-traceability-matrix.zh-TW.md`、`17-student-material-outlines.zh-TW.md` | 規劃與追蹤模型 | 設計者、教師、維護者 | 設計理由、依賴、交付規劃、風險、對應關係與教材草案；不得自行建立評量政策 |
| `12-constitution-compliance-review.zh-TW.md` | 歷史紀錄 | 維護者 | 只保留早期審查證據；Constitution 1.2.0 的判定不再是現行要求 |
| `README.zh-TW.md` | 治理索引／指南 | 所有角色 | 只提供導覽與分類，不自行建立政策 |

## 文件責任

### Constitution 與正式政策

- Constitution 定義治理原則。
- `13-learning-assessment-policy.zh-TW.md` 是唯一可以正式定義成績、參與、作業、口試與 AI 使用規則的文件。
- 其他文件可以摘要或實作政策，但應連結權威來源，避免重新複製整份政策。

### 設計標準

設計標準提供穩定的維護定義。它們必須符合 Constitution 與正式政策；修改時應有明確設計決策，並同步更新雙語版本。

### 規劃與追蹤模型

規劃模型解釋課程為何及如何組織。它們是重要設計證據，但可修訂，也不得被視為獨立政策來源。

### 歷史紀錄

歷史紀錄保留早期推理與遷移脈絡。文件必須明確標示其非規範性，且不得再被引用為現行要求。

## 現行設計原則

- C 是教學語言，核心目標是可遷移的程式設計能力。
- Concept 是知識來源；Unit 組合 Concept 依賴鏈；Lesson 是 Unit 的交付切片。
- 教材以問題脈絡、預測、視覺或執行模型、實作、錯誤診斷、驗證與修改展開。
- 閱讀、預測、修改、測試、除錯與解釋都可作為學習證據。
- AI 使用為選用，不得成為 Unit 完成、課堂參與或評量的前置條件。
- 每個 Unit 應提供可重現錯誤、技術契約、邊界案例與回歸檢查。
- 中文授課與英文授課班可調整節奏及語言支架，但必須維持等值的核心能力與評量期待。

## 維護流程

1. 先辨識規範此次修改的最高權威來源。
2. 同步更新中英文配對文件。
3. 更新相依的標準、規劃模型、指南與教材，避免不必要地複製政策全文。
4. 驗證連結、雙語配對、術語與可執行技術範例。
5. 將教材治理變更記錄於 `reviews/repository-constitution-2-audit.*`。
6. 保留歷史紀錄，但明確維持其非規範性。

## 導覽

- [課程 Constitution](../CONSTITUTION.zh-TW.md)
- [正式學習與評量政策](13-learning-assessment-policy.zh-TW.md)
- [教材與活動資源](../materials/README.zh-TW.md)
- [現行 Constitution 2.0 審查](../reviews/repository-constitution-2-audit.zh-TW.md)
- [返回倉庫首頁](../README.md)
- [English version](README.en.md)
