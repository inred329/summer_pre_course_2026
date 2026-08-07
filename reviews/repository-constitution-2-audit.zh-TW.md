# 全庫 Constitution 2.0 符合性審查

版本：1.9.0  
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
| `README.md` | Guide / routing entry | 學生、教師、維護者 | C → A | P0 | 重複評量政策、進度報告與舊 AI 要求 | 重寫為三角色路由入口 | 已完成 |
| `classes/zh/README.md`、`classes/en/README.md` | Material entry | 學生 | D → A | P0 | 早期 TBD 草案與現行課程不符 | 改寫為現行 4×3 與 5×2 小時入口 | 已完成 |
| `design/13-learning-assessment-policy.*` | Official Policy | 學生與教師 | D → A | P0 | 強制 AI 前置成果、摘要、紀錄與普遍 AI 口試能力 | AI 改為選用；未使用不構成缺失 | 已完成 |
| `design/12-constitution-compliance-review.*` | Historical Record | 維護者 | D → H | P0 | 以 Constitution 1.2.0 為現行基準 | 歷史化並加入過時警告 | 已完成 |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | 維護者 | C → A | P0 | 自稱正式優先規則並複製評量政策 | 取消規範效力，只保留遷移說明 | 已完成 |
| `materials/preparatory/unit-01*` 至 `unit-04*` | Student Material | 學生 | B → A | P1 | AI 位於核心主線，形成隱性必做 | 改為可直接跳過的選用延伸 | 已完成 |
| `materials/assignments/*` | Student resources / assessment implementation | 學生、教師 | B → A | P1 | 索引與 rubric 文字可能暗示 AI 為必做 | 作業維持不繳交、不計分；AI 筆記為選用；rubric 只在實際使用時檢查 | 已完成 |
| `materials/README.*`、`materials/TEMPLATE.*` | Role-based index / authoring guide | 學生、教師、維護者 | C → A | P1 | 混合讀者、複製政策、固定 AI 章節與過早完成宣告 | 改寫為角色導覽與目的導向教材寫作指南 | 已完成 |
| `materials/instructor/session-guides.*` | Instructor Guide | 教師、助教 | A | P1 | 節奏、常見錯誤、備援、公平支架與課後紀錄可執行 | 保留；評量仍以 `design/13` 為權威 | 已審查 |
| `materials/formal/README.*`、`materials/formal/unit-01*` 至 `unit-12*` | Student Material | 學生 | B → A | P1 | AI 位於核心路徑，且多處技術契約不足 | AI 改為可直接跳過；補強值域、輸入、生命週期、配置、stream、依賴、溢位與失敗契約 | 已完成 |
| `design/README.*` | Governance index / guide | 所有角色 | C → A | P2 | 將全部設計文件列為同等「正式」、重複政策文字，且下一步已過時 | 重寫權威順序、治理角色、維護流程與現行導覽 | 已完成 |
| `design/01-product-vision.*` | 可修訂的規劃模型 | 設計者、維護者 | C → A | P1 | 自稱上位依據，並把 AI 使用列為所有學生的成功證據 | 改為規劃脈絡；外部協助驗證改為條件式；未使用 AI 不構成缺失 | 已完成 |
| `design/02-requirements-map.*` | 可修訂的規劃與追蹤模型 | 設計者、維護者 | C → A | P1 | 自稱控制基準；把 AI 素養／紀錄列為普遍需求；保留過時線性導覽 | 改為非治理規劃模型；明定上位來源優先；AI 要求改為條件式；移除過時導覽 | 已完成 |
| `design/03-programming-domain-model.*` | 可修訂的規劃模型 | 設計者、維護者 | C → A | P1 | 把 AI 嵌入核心領域；要求普遍揭露；metadata 漂移；建置流程寫得過於實體化 | 外部協助改為選用；揭露改為情境式；同步雙語 metadata；加入 implementation-neutral 工具鏈與 pointer/storage 邊界 | 已完成 |
| `design/04-programming-language-knowledge-graph.*` | 可修訂的規劃與追蹤模型 | 設計者、維護者 | C → A | P1 | 把 AI 判斷當普遍依賴；要求普遍紀錄；保留草案導覽；過度具體化建置階段 | 新增條件式依賴；外部協助分支改為選用；紀錄改為情境式；修正 metadata、導覽與工具鏈例外 | 已完成 |
| `design/05-competency-map.*` | 設計標準 | 設計者、維護者 | B → A | P1 | 需要明確政策邊界與條件式外部協助證據 | 明定治理邊界；EV-AI／PC-A 只在實際使用協助時適用；核心能力不要求 AI | 已完成 |
| `design/06-scope-boundary.*` | 設計標準 | 設計者、維護者 | B → A | P1 | 範圍模型需要明確選用狀態，避免工具使用變成隱性最低交付 | 使用 SB-X 條件式／選用；最低交付不包含 AI；範圍與成熟度不依工具使用決定 | 已完成 |
| `design/07-acceptance-model.*` | 可修訂的規劃與追蹤模型 | 設計者、教師 | B → A | P1 | 候選證據可能被誤認為正式評量政策或普遍工具證據 | 明定正式政策權威；外部協助證據為條件式；不要求 AI／未使用聲明 | 已完成 |
| `design/08-delivery-map.*` | 可修訂的規劃模型 | 設計者、教師 | B → A | P1 | 活動位置可能讓選用工具實質變成必做 | 工具活動改為可直接跳過；共同基線不包含工具使用；政策細節回歸 `design/13` | 已完成 |
| `design/09-risk-register.*` | 可修訂的規劃與追蹤模型 | 設計者、教師、維護者 | B → A | P2 | 工具誤用風險控制需避免轉成強制監控／紀錄 | 以能力證據與驗證處理風險，同時保留選用性、尊嚴與政策權威 | 已完成 |
| `design/10-traceability-matrix.*` | 可修訂的規劃與追蹤模型 | 設計者、維護者 | B → A | P2 | AI 追蹤可能變成普遍依賴路徑 | 外部協助追蹤改為條件式；核心鏈不依賴 AI；明定權威順序 | 已完成 |
| `design/11-terminology-glossary.*` | 設計標準 | 作者、翻譯者、維護者 | B → A | P2 | 術語需補治理角色與精確 C／工具鏈邊界 | 統一治理、Null Pointer、storage duration、stream、verification 與選用外部協助術語 | 已完成 |
| `design/14-programming-concept-tree.*` | 設計標準 | 設計者、維護者 | B → A | P2 | 概念盤點需分離穩定概念、工具選擇與實作慣例 | 外部協助不列核心先備；補強工具鏈／runtime 實作例外與概念邊界 | 已完成 |
| `design/15-programming-concept-registry.*` | 設計標準 | 設計者、維護者 | C → A | P1 | 草案 metadata、本地重定義成熟度、把 AI-assisted programming 列核心、`Null Reference`／stack-storage 與工具鏈假設皆與現行標準衝突 | 啟用為設計標準；成熟度／範圍回歸權威標準；外部協助 Concept 改 X 條件式；修正 C 術語與 runtime 邊界 | 已完成 |
| `design/16-unit-map.*` | 設計標準 | 設計者、維護者 | C → A | P1 | 每個 Unit 原本都要求課後向 AI 解釋，且 compiler／call-stack 文字過於實體化 | 核心證據改為不依外部工具；移除完成條件中的 AI 對話／log／prompt／未使用聲明；工具鏈與 activation model 改為 implementation-neutral | 已完成 |
| `design/17-student-material-outlines.*` | 可修訂的規劃與追蹤模型 | 教材作者、維護者 | C → A | P1 | 每份大綱原本都把 AI 當課後對話對象；舊技術模型可能重新引入 AI 必做與實作 folklore | 以 0.2.0 重寫；核心反思／證據不依工具；外部協助為可直接跳過選用模式；16 Unit 都加入明確技術契約 | 已完成 |

## 三、主要裁決

### 1. AI 活動不得形成隱性必做

AI 可以作為延伸工具，但不得因位於核心章節、完成清單、固定模板、需求基準、領域模型、知識依賴圖、能力欄位、範圍狀態、Unit 骨架、教材大綱或評量欄位而成為隱性必做。不使用 AI 不影響完成、參與或評量。只有在學生實際採用選用外部協助時，才條件式產生理解與技術驗證責任。

### 2. 評量規則維持單一權威來源

`design/13-learning-assessment-policy.*` 是正式評量制度的唯一權威來源。README、作業包、rubric、模板、教師指南、設計標準與規劃模型只能提供導覽、追蹤、定義或執行方式。

### 3. 設計文件不具有相同權威

設計區依序區分 Constitution、正式政策、已核定設計標準、規劃與追蹤模型、執行指南與教材，以及歷史紀錄。下位文件不得覆寫上位來源。

### 4. 學生教材必須揭露技術契約

教材必須交代適用的值域、輸入狀態、終止條件、生命週期、解參考前提、配置大小、ownership／release responsibility、失敗保留、stream 狀態、module 依賴、compile／link 差異與 undefined-behavior 邊界。成功編譯或單次正確輸出不能取代這些契約。

### 5. 概念模型不得被誤認為實作保證

C 標準不要求固定的一組獨立 preprocessor、compiler、assembler、linker、object file、executable file，也不要求唯一的實體 call-stack／heap 表示。當 commands、artifacts、layout 或 runtime behavior 會影響教材時，必須明確指出並驗證目標實作。

### 6. 舊審查只具有歷史效力

舊審查只記錄特定日期與 Constitution 版本下的判斷；現行裁決以 Constitution 2.0 與本 active audit 為準。

## 四、已確認的學生教材品質

前導 P-U01 至 P-U04 與正式 F-U01 至 F-U12 已完成雙語審查。現行教材具備問題導向入口、預測／追蹤、可重現錯誤、測試與回歸、需求修改、技術契約、不依工具的完成路徑與雙語對應。目前沒有已知 P0/P1 問題需要撤下學生教材；P3 文字與節奏仍可在試教後微調。

## 五、現行設計治理分類與審查覆蓋

- Constitution：`CONSTITUTION.*`。
- 正式政策：`design/13-learning-assessment-policy.*`。
- 設計標準：`05`、`06`、`11`、`14`、`15`、`16`。
- 規劃與追蹤模型：`01`、`02`、`03`、`04`、`07`、`08`、`09`、`10`、`17`。
- 歷史紀錄：`12`。
- 治理索引：`design/README.*`。

`design/01–17` 的全部雙語 pair 已完成 Constitution 2.0 治理／AI 政策逐份審查。剩餘全庫工作轉為自動化導覽／技術驗證，以及這些檢查新發現問題的修正。

## 六、剩餘審查範圍

### P2：自動化導覽與雙語檢查

- 驗證應有的中英文配對，找出缺少 counterpart 或孤立文件。
- 搜尋舊 Constitution 版本或已被取代政策文字；歷史紀錄中的刻意引用除外。
- 檢查 Markdown 內部連結並辨識無法由導覽抵達的文件。
- 除檔名／版本 metadata 外，抽樣檢查中英文實質等值。

### P2：技術驗證與 CI

- 盤點可執行 C 範例並建立 compile manifest。
- 在可用環境中，以指定 GCC／Clang 設定建置適用範例。
- 區分刻意的缺陷案例與非預期建置失敗。
- 視需要新增或補強 links、雙語配對、舊治理引用與可編譯範例的 CI 檢查。

## 七、目前結論

文件逐份 Constitution 2.0 審查目前發現的 P0/P1 問題都已修正並提交。前導／正式學生教材與全部 `design/01–17` 雙語 pair 現在都具有一致治理角色與 AI 選用邊界。全庫審查仍未完成，因為自動化導覽、孤立／連結、舊 Constitution、雙語實質等值、compile manifest、compiler coverage 與 CI 驗證尚待完成，因此 PR #10 仍維持 Draft。
