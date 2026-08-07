# 全庫 Constitution 2.0 符合性審查

版本：1.6.0  
狀態：進行中審查紀錄  
最後更新：2026-08-07  
權威基準：`CONSTITUTION.zh-TW.md` 2.0.0  
主要讀者：課程設計者、授課教師與維護者  
規範效力：本文件只記錄審查結果與修正建議，不自行建立新規範

## 一、審查目的與判定方式

本審查依 Constitution 2.0 檢視文件層級、主要讀者、權威角色、雙語等值、學生閱讀品質、技術可驗證性，以及 AI 與評量規則是否一致。

符合性判定：A 符合、B 小幅修正、C 結構性修正、D 不符合、H 歷史化。  
優先級：P0 立即修正、P1 高優先、P2 中優先、P3 一般改善。

## 二、已完成審查矩陣

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | 學生、教師、設計維護者 | C → A | P0 | 重複評量政策、進度報告與舊 AI 要求 | 重寫為三角色路由入口 | 已完成 |
| `classes/zh/README.md`、`classes/en/README.md` | Material entry | 學生 | D → A | P0 | 早期 TBD 草案與現行課程不符 | 改寫為現行 4×3 與 5×2 小時入口 | 已完成 |
| `design/13-learning-assessment-policy.*` | Official Policy | 學生與教師 | D → A | P0 | 強制 AI 前置成果、摘要、紀錄與普遍 AI 口試能力 | AI 改為選用；未使用不構成缺失 | 已完成 |
| `design/12-constitution-compliance-review.*` | Historical Record | 設計維護者 | D → H | P0 | 以 Constitution 1.2.0 為現行基準 | 歷史化並加入過時警告 | 已完成 |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | 維護者 | C → A | P0 | 自稱正式優先規則並複製評量政策 | 取消規範效力，只保留遷移說明 | 已完成 |
| `materials/preparatory/unit-01*` 至 `unit-04*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線，形成隱性必做 | 改為可跳過選用延伸 | 已完成 |
| `materials/assignments/*` | Student resources / assessment implementation | 學生、教師 | B → A | P1 | 索引與 rubric 文字可能暗示 AI 為必做 | 作業維持不繳交、不計分；AI 筆記為選用；rubric 只在實際使用 AI 時檢查 | 已完成 |
| `materials/README.*`、`materials/TEMPLATE.*` | Role-based index / authoring guide | 學生、教師、維護者 | C → A | P1 | 混合讀者、複製政策、固定 AI 章節與過早完成宣告 | 改寫為角色導覽與目的導向教材寫作指南 | 已完成 |
| `materials/instructor/session-guides.*` | Instructor Guide | 教師、助教 | A | P1 | 節奏、常見錯誤、備援、公平支架與課後紀錄可執行 | 保留；評量仍以 `design/13` 為權威 | 已審查 |
| `materials/formal/README.*`、`materials/formal/unit-01*` 至 `unit-12*` | Student Material | 學生 | B → A | P1 | AI 位於核心路徑，且多處技術契約不足 | AI 改為可直接跳過；補強值域、輸入、生命週期、配置、stream、依賴、溢位與失敗契約 | 已完成 |
| `design/README.*` | Governance index / guide | 所有角色 | C → A | P2 | 將全部設計文件列為同等「正式」、重複政策文字，且下一步已過時 | 重寫權威順序、治理角色、維護流程與現行導覽 | 已完成 |
| `design/01-product-vision.*` | 可修訂的規劃模型 | 課程設計者與維護者 | C → A | P1 | 自稱上位依據，並把 AI 使用列為所有學生的成功證據 | 改為規劃脈絡；外部協助驗證改為條件式；明定未使用 AI 不構成缺失 | 已完成 |

## 三、主要裁決

### 1. AI 活動不得形成隱性必做

AI 可以作為延伸工具，但不得因位於核心章節、完成清單、固定模板或評量欄位而成為隱性必做。所有前導與正式 Unit 均已改為可直接跳過的選用延伸；不使用 AI 不影響完成、參與或評量。

### 2. 評量規則維持單一權威來源

`design/13-learning-assessment-policy.*` 是正式評量制度的唯一權威來源。README、作業包、rubric、模板與教師指南只能提供導覽或執行方式。

### 3. 設計文件不具有相同權威

設計區現在依序區分 Constitution、正式政策、已核定設計標準、規劃與追蹤模型、執行指南與教材，以及歷史紀錄。下位文件不得覆寫上位來源。

### 4. 學生教材必須揭露技術契約

教材必須交代值域、輸入狀態、終止條件、生命週期、可解參照範圍、配置大小、所有權、失敗保留、stream 狀態、模組依賴、編譯／連結階段與未定義行為。成功編譯或單次正確輸出不能取代這些契約。

### 5. 舊審查只具有歷史效力

舊審查只記錄特定日期與憲法版本下的判斷。現行裁決以 Constitution 2.0 與本審查為準。

## 四、已確認的學生教材品質

前導 Unit 1–4 與正式課程 F-U01 至 F-U12 目前均具備：

- 以問題脈絡進入概念，而非先列語法。
- 執行前預測與狀態、流程、記憶體、stream 或模組依賴追蹤。
- 可重現錯誤、診斷與回歸驗證。
- 需求修改與正常、邊界、無效及失敗案例。
- 不以編譯成功、單一輸出或工具判斷取代理解。
- 清楚的完成標準與雙語對應。
- AI 不構成核心完成條件。
- 技術邊界與失敗條件可操作、可驗證。

本輪未發現需要停止使用的 P0/P1 問題；試教後仍可進行 P3 文字與節奏微調。

## 五、現行設計治理分類

- Constitution：`CONSTITUTION.*`。
- 正式政策：`design/13-learning-assessment-policy.*`。
- 設計標準：能力、範圍、術語、Concept Tree、Concept Registry 與 Unit Map。
- 規劃與追蹤模型：願景、需求、領域模型、知識圖、驗收、交付、風險、追蹤與學生教材大綱。
- 歷史紀錄：`design/12-constitution-compliance-review.*`。
- 治理索引：`design/README.*`。

`design/01-product-vision.*` 已符合此分類。下一批設計治理工作須套用 `design/02–04` 已記錄的修正，並繼續逐份檢查其餘文件是否仍重複宣稱規範效力、保留過時 metadata 或存在雙語不等值。

## 六、下一批審查範圍

### P1：已記錄的設計文件修正

套用 `design/02–04` 現有雙語發現，包括權威衝突、普遍 AI 要求、強制 AI 紀錄、領域模型混雜、過時狀態文字與雙語 metadata 差異。

### P2：個別設計文件

審查 `design/05–11` 與 `14–17` 是否仍有重複政策、衝突的權威宣告、過時狀態、陳舊下一步及雙語不等值。

### P2：技術與導覽自動檢查

- 中英文配對與實質等值。
- 舊憲法版本引用。
- 失效連結與孤立文件。
- 可編譯程式清單、GCC／Clang 差異與 CI 覆蓋範圍。

## 七、本輪結論

目前已發現的 P0 問題均已修復。前導教材與正式課程 F-U01 至 F-U12 已完成雙語審查，`design/01` 的雙語 P1 問題也已解決。`design/02–04` 仍有已記錄但尚未套用的 P1 修正，全庫審查尚未完成；仍需逐份清理設計文件、擴充審查矩陣並補上自動驗證，因此 PR #10 繼續維持 Draft。
