# 全庫 Constitution 2.0 符合性審查

版本：1.0.0  
狀態：進行中審查紀錄  
最後更新：2026-08-06  
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
| `classes/zh/README.md` | Material entry | 中文班學生 | D → A | P0 | 早期 TBD 草案與現行課程不符 | 改寫為 4×3 小時現行入口 | 已完成 |
| `classes/en/README.md` | Material entry | 英文班學生 | D → A | P0 | 早期 TBD 草案與現行課程不符 | 改寫為 5×2 小時現行入口 | 已完成 |
| `design/13-learning-assessment-policy.*` | Official Policy | 學生與教師 | D → A | P0 | 強制 AI 使用前成果、摘要、紀錄與普遍 AI 口試能力 | AI 改為選用；未使用不構成缺失 | 已完成 |
| `design/12-constitution-compliance-review.*` | Historical Record | 設計維護者 | D → H | P0 | 以 Constitution 1.2.0 為現行基準 | 歷史化並加入過時警告 | 已完成 |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | 維護者 | C → A | P0 | 自稱正式優先規則並複製評量政策 | 取消規範效力，只保留遷移說明 | 已完成 |
| `materials/preparatory/unit-01*` 至 `unit-04*` | Student Material | 學生 | B → A | P1 | AI 活動位於核心主線，形成隱性必做 | 改為可跳過選用延伸；完成標準不依賴 AI | 已完成 |
| `materials/assignments/ai-use-log.*` | Optional Learning Resource | 學生 | A | P1 | 已為選用、不繳交、不評分，未使用無須聲明 | 保留；索引不得列為必備 | 已審查 |
| `materials/assignments/preparatory-assignments.*` | Student Task Pack | 學生、教師 | A | P1 | 作業不繳交、不計分；AI 不屬核心完成條件 | 保留 | 已審查 |
| `materials/assignments/rubric.*` | Assessment Standard | 教師、助教 | A | P1 | AI 只在實際使用時檢查說明與驗證 | 保留 | 已審查 |
| `materials/assignments/grading-guide.*` | Instructor Guide | 教師、助教 | A | P1 | 支援多元參與證據；不把 AI 當固定活動 | 保留 | 已審查 |
| `materials/README.*` | Role-based materials index | 學生、教師、作者維護者 | C → A | P1 | 混合讀者、複製政策、宣稱審查完成、把 AI 列為共同標準 | 改寫為角色入口並只連結權威政策 | 已完成 |
| `materials/TEMPLATE.*` | Authoring Standard / Guide | 教材作者與維護者 | C → A | P1 | 固定要求 AI 章節與機械式同構 | 改為目的導向建議模板；AI 僅可作選用延伸 | 已完成 |
| `materials/instructor/session-guides.*` | Instructor Guide | 教師、助教 | A | P1 | 節奏、常見錯誤、備援、公平支架與課後紀錄可執行 | 保留；評量仍以 `design/13` 為權威 | 已審查 |
| `materials/formal/README.*` | Student-material index | 學生 | C → A | P1 | 宣稱每個 Unit 固定包含 AI 解釋 | 改寫學習路徑；AI 不影響完成、參與或評量 | 已完成 |
| `materials/formal/unit-01-representation-types.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；完成標準未排除 AI | AI 改為可跳過延伸；新增非 AI 完成標準 | 已完成 |
| `materials/formal/unit-02-complex-control-flow.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；未明示無須紀錄或聲明 | 改為選用延伸並補非 AI 完成標準 | 已完成 |
| `materials/formal/unit-03-arrays.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；累加範圍與輸入契約不足 | 補可表示範圍、輸入驗證與空集合契約 | 已完成 |
| `materials/formal/unit-04-strings.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；固定長度輸入未充分說明截斷、殘留輸入與終止字元風險 | AI 改為選用；補行截斷偵測、緩衝區與 `\0` 契約 | 已完成 |
| `materials/formal/unit-05-call-stack-recursion.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；遞迴深度與結果可表示範圍未形成完整契約 | AI 改為選用；補基底案例、深度、堆疊與結果範圍限制 | 已完成 |
| `materials/formal/unit-06-pointers.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；生命週期、空指標、one-past 與別名界線需更明確 | AI 改為選用；補有效生命週期、可解參照範圍與別名契約 | 已完成 |
| `materials/formal/unit-07-structures.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；未明示未使用 AI 不影響完成 | AI 改為可直接跳過的選用延伸；補非 AI 完成標準與無紀錄／聲明要求 | 已完成 |
| `materials/formal/unit-08-dynamic-memory.*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線；配置大小溢位、零容量成長、alias 生命週期與 `realloc` metadata 契約不完整 | AI 改為選用；補元素數量轉 byte 溢位檢查、明確零容量處理、alias 失效與失敗保留原資料契約 | 已完成 |

## 三、主要裁決

### 1. AI 活動不得形成隱性必做

AI 可以作為延伸工具，但不得因位於核心章節、完成清單、固定模板或評量欄位而成為隱性必做。所有已審查的前導 Unit、正式課程索引與 F-U01 至 F-U08 均已改為可直接跳過的選用延伸。

### 2. 評量規則維持單一權威來源

`design/13-learning-assessment-policy.*` 是正式評量制度的唯一權威來源。README、作業包、rubric、模板與教師指南只能提供導覽或執行方式。

### 3. 學生教材必須揭露技術契約

涉及陣列、字串、遞迴、指標、結構與動態記憶體時，教材必須清楚交代值域、輸入狀態、終止條件、生命週期、可解參照範圍、配置大小計算、所有權、釋放責任、失敗保留與未定義行為；成功編譯或單次正確輸出不能取代這些契約。

### 4. 舊審查只具有歷史效力

舊審查只記錄特定日期與憲法版本下的判斷。現行裁決以 Constitution 2.0 與本審查為準。

## 四、已確認的學生教材品質

前導 Unit 1–4 與正式課程 F-U01 至 F-U08 目前均具備：

- 以問題脈絡進入概念，而非先列語法。
- 執行前預測、狀態／流程／記憶體追蹤。
- 可重現錯誤、診斷與回歸驗證。
- 需求修改與多類測試。
- 不以編譯成功、單一輸出或工具判斷取代理解。
- 清楚的前置知識、完成標準與雙語對應。
- AI 不構成核心完成條件。
- 技術邊界與失敗條件可被操作與驗證。

這些文件仍可在試教後進行 P3 文字與節奏微調，但本輪未發現需要停止使用的 P0/P1 問題。

## 五、下一批審查範圍

### P1：正式課程學生教材

- `materials/formal/unit-09*` 至 `unit-12*`
- AI 是否仍位於核心完成主線。
- 是否混入內部治理欄位、教師提示或評量行政。
- Concept-first、依賴順序、錯誤診斷與技術可驗證性。

### P2：設計文件治理層級

重新判定 `design/01–11`、Concept Tree、Registry、Unit Map、Traceability、Acceptance、Risk 與 Delivery 的權威角色，避免多份文件同時宣稱同一規則的正式基準。

### P2：技術與導覽自動檢查

- 中英文配對與實質等值。
- 舊憲法版本引用。
- 失效連結與孤立文件。
- 可編譯程式清單、GCC／Clang 差異與 CI 覆蓋範圍。

## 六、本輪結論

目前已發現的 P0 問題均已修復。正式課程索引與 F-U01 至 F-U08 已完成審查；F-U08 已把 AI 移出核心路徑，並建立元素數量驗證、配置大小溢位、所有權、alias、釋放、零容量處理與 `realloc` 失敗保留原資料等可操作契約。全庫審查尚未完成，下一批將處理 F-U09 至 F-U12、設計治理層級與自動驗證，因此 PR 仍維持 Draft。