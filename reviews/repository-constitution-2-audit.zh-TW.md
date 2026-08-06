# 全庫 Constitution 2.0 符合性審查

版本：0.3.0  
狀態：進行中審查紀錄  
最後更新：2026-08-06  
權威基準：`CONSTITUTION.zh-TW.md` 2.0.0  
主要讀者：課程設計者、授課教師與維護者  
規範效力：本文件只記錄審查結果與修正建議，不自行建立新規範

## 一、審查目的

本審查依 Constitution 2.0 重新檢視本倉庫所有正式文件，記錄文件層級、主要讀者、權威角色、雙語等值、學生閱讀品質、技術可驗證性，以及 AI 與評量規則是否一致。

符合性判定：A 符合、B 小幅修正、C 結構性修正、D 不符合、H 歷史化。  
優先級：P0 立即修正、P1 高優先、P2 中優先、P3 一般改善。

## 二、已完成審查矩陣

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | 學生、教師、設計維護者 | C → A | P0 | 重複評量政策、設計理念、進度報告與舊 AI 要求 | 重寫為三角色路由入口 | 已完成 |
| `classes/zh/README.md` | Material entry | 中文班學生 | D → A | P0 | 早期 TBD 草案與現行課程不符 | 改寫為 4×3 小時現行入口 | 已完成 |
| `classes/en/README.md` | Material entry | 英文班學生 | D → A | P0 | 早期 TBD 草案與現行課程不符 | 改寫為 5×2 小時現行入口 | 已完成 |
| `design/13-learning-assessment-policy.*` | Official Policy | 學生與教師 | D → A | P0 | 強制 AI 使用前成果、摘要、紀錄與普遍 AI 口試能力 | AI 改為選用；未使用不構成缺失 | 已完成 |
| `design/12-constitution-compliance-review.*` | Historical Record | 設計維護者 | D → H | P0 | 以 Constitution 1.2.0 為現行基準 | 歷史化並加入過時警告 | 已完成 |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | 維護者 | C → A | P0 | 自稱正式優先規則並複製評量政策 | 取消規範效力，只保留舊措辭遷移說明 | 已完成 |
| `materials/preparatory/unit-01-execution.*` | Student Material | 學生 | B → A | P1 | AI 活動位於核心編號主線，形成隱性必做 | 標示為可跳過的選用延伸；完成標準不依賴 AI | 已完成 |
| `materials/preparatory/unit-02-data-state.*` | Student Material | 學生 | B → A | P1 | AI 活動位於核心編號主線，形成隱性必做 | 標示為可跳過的選用延伸；完成標準不依賴 AI | 已完成 |
| `materials/preparatory/unit-03-control-flow.*` | Student Material | 學生 | B → A | P1 | AI 活動位於核心編號主線，形成隱性必做 | 標示為可跳過的選用延伸；完成標準不依賴 AI | 已完成 |
| `materials/preparatory/unit-04-functions-integration.*` | Student Material | 學生 | B → A | P1 | AI 活動位於核心編號主線，形成隱性必做 | 標示為可跳過的選用延伸；完成標準不依賴 AI | 已完成 |
| `materials/assignments/ai-use-log.*` | Optional Learning Resource | 學生 | A | P1 | 已明確為選用、不繳交、不評分，未使用無須聲明 | 保留；後續確認索引不將其列為必備 | 已審查 |
| `materials/assignments/preparatory-assignments.*` | Student Task Pack | 學生、教師 | A | P1 | 作業不繳交、不計分；AI 僅為選用，核心任務不依賴 AI | 保留 | 已審查 |
| `materials/assignments/rubric.*` | Assessment Standard | 教師、助教 | A | P1 | AI 只在實際使用時檢查說明與驗證；未使用不影響評分 | 保留 | 已審查 |
| `materials/assignments/grading-guide.*` | Instructor Guide | 教師、助教 | A | P1 | AI／外部建議不是固定活動；參與與評量方式符合多元證據原則 | 保留 | 已審查 |

## 三、第二批裁決

### 1. AI 活動的學生教材位置

AI 可以作為延伸工具，但不得因位於核心章節主線、完成清單或評量欄位而形成隱性必做。Unit 1–4 已明確標示 AI 段落可跳過，且未使用 AI 不影響完成、參與或評量。

### 2. AI 驗證筆記的角色

`ai-use-log.*` 只是一份學生可自行選用的複習模板。它不得成為作業附件、口試必要證據、未使用聲明或教師逐份檢查項目。

### 3. 評量規則的單一權威來源

`design/13-learning-assessment-policy.*` 是正式評量制度的唯一權威來源。作業包、rubric 與教師指南可以將制度轉成對應任務和觀察方式，但不得重新定義成績結構或建立相衝突的 AI 義務。

## 四、已確認的學生教材品質

前導 Unit 1–4 目前均具備：

- 以問題脈絡進入概念，而非先列語法。
- 執行前預測、狀態或流程追蹤。
- 可重現錯誤、診斷與回歸驗證。
- 需求修改與多種測試案例。
- 不以編譯成功、單一輸出或工具判斷取代理解。
- 清楚的前置知識、完成標準與雙語對應。

這些文件仍可在後續試教後進行 P3 文字與節奏微調，但本輪未發現需要停止使用的 P0/P1 技術或教學問題。

## 五、下一批審查範圍

### P1：教材入口與模板

- `materials/README.*`
- `materials/TEMPLATE.*`
- 是否把內部治理欄位、能力 ID 或 AI 模板暴露為學生必讀內容。
- 學生、教師與維護者入口是否清楚分離。

### P1：教師文件邊界

- `materials/instructor/*`
- 是否可直接執行，又不重寫學生教材。
- 是否包含教師提示、常見誤解、備援活動與公平支架。

### P2：設計文件治理層級

重新判定 `design/01–11`、Concept Tree、Registry、Unit Map、Traceability、Acceptance、Risk 與 Delivery 文件的權威角色，避免多份文件同時宣稱為同一規則的正式基準。

### P2：技術與導覽自動檢查

- 中英文配對與實質等值。
- 舊憲法版本引用。
- 失效連結與孤立文件。
- 可編譯程式清單、GCC／Clang 差異與 CI 覆蓋範圍。

## 六、本輪結論

目前已發現的 P0 問題均已修復。Unit 1–4 與作業／評量文件中的 AI 定位已完成審查並符合 Constitution 2.0。全庫審查尚未完成，下一批將處理教材入口、模板、教師文件與設計治理層級，因此 PR 仍維持 Draft。
