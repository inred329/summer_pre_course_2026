# 全庫 Constitution 2.0 符合性審查

版本：2.0.0  
狀態：PR #10 正式審查快照之已完成審查紀錄  
最後更新：2026-08-07  
權威基準：`CONSTITUTION.zh-TW.md` 2.0.0  
主要讀者：課程設計者、授課教師與維護者  
規範效力：本文件只記錄審查與驗證結果，不自行建立新規範

## 一、目的與判定

本審查依 Constitution 2.0 檢查治理層級、權威來源、評量與 AI 規則、學生教材可讀性、教師文件邊界、雙語實質等值及技術可驗證性。

判定：A 符合、B 小幅修正、C 結構性修正、D 不符合、H 歷史化。優先級：P0 立即、P1 高、P2 中、P3 一般改善。「已完成」表示已識別問題已修正並重新檢查，不排除未來 P3 教學或文字改善。

## 二、完成審查矩陣

| 範圍 | 治理角色 | 優先級 | 主要發現與修正 | 狀態 |
|---|---|---:|---|---|
| `README.md`、`classes/*/README.md` | 導覽／教材入口 | P0 | 移除重複政策、舊 AI 要求與過時 TBD；改為現行角色與班別入口 | A／完成 |
| `design/13-learning-assessment-policy.*` | 唯一正式評量政策 | P0 | 移除普遍 AI 紀錄與 AI 口試能力要求；AI 預設選用，未使用不構成缺失 | A／完成 |
| `design/12-constitution-compliance-review.*` | 歷史紀錄 | P0 | Constitution 1.2.0 審查明確歷史化，不再作現行依據 | H／完成 |
| `materials/preparatory/ASSESSMENT-NOTE.*` | 遷移說明 | P0 | 移除自稱優先政策的效力，只保留遷移說明 | A／完成 |
| P-U01–P-U04 中英文教材 | 學生教材 | P1 | AI 從核心路徑移為可直接跳過的選用延伸；補強可讀性與技術契約 | A／完成 |
| F-U01–F-U12 中英文教材 | 學生教材 | P1 | 移除核心路徑中的 AI 必做暗示；補值域、輸入、生命週期、配置、stream、依賴、溢位、失敗與 UB 邊界 | A／完成 |
| `materials/assignments/*` | 學習／評量實作資源 | P1 | 作業不繳交、不直接計分；rubric 只在實際採用 AI 時檢查相關責任 | A／完成 |
| `materials/README.*`、`materials/TEMPLATE.*` | 導覽／作者指南 | P1 | 分離讀者角色、移除複製政策與固定 AI 章節 | A／完成 |
| `materials/instructor/session-guides.*` | 教師執行指南 | P1 | 保留節奏、常見錯誤、備援與公平支架；不得覆蓋 `design/13` | A／已審查 |
| `design/README.*` | 治理索引 | P2 | 建立 Constitution → 正式政策 → 設計標準 → 規劃模型 → 指南／教材 → 歷史紀錄的權威順序 | A／完成 |
| `design/01–04` 中英文 pair | 可修訂規劃／追蹤模型 | P1 | 移除上位／控制基準宣稱、普遍 AI 依賴與紀錄；修正工具鏈與 runtime 過度實體化 | A／完成 |
| `design/05–06` 中英文 pair | 設計標準 | P1 | 能力與範圍不以 AI 使用為最低門檻；外部協助證據採條件式 | A／完成 |
| `design/07–10` 中英文 pair | 可修訂規劃／追蹤模型 | P1/P2 | 驗收、delivery、risk、traceability 不得把選用工具轉成隱性必做或監控要求 | A／完成 |
| `design/11` 中英文 pair | 術語設計標準 | P2 | 統一治理、null pointer、storage duration、stream、verification 與外部協助術語 | A／完成 |
| `design/14–16` 中英文 pair | 設計標準 | P1/P2 | 外部協助排除於核心先備；修正 C／runtime 術語；Unit 核心證據不依 AI | A／完成 |
| `design/17` 中英文 pair | 可修訂規劃／追蹤模型 | P1 | 教材大綱改為工具無關核心證據＋可直接跳過的選用外部協助模式 | A／完成 |
| Repository 導覽／雙語結構 | 機械驗證 | P2 | 中英配對、版本、內部連結、舊 Constitution 引用與孤立 Markdown 已自動檢查 | A／完成 |
| `examples/`、validation fixtures | 技術驗證 | P2 | 正確範例與刻意缺陷已分類；建立 compile manifest、runtime／defect 驗證 | A／完成 |
| `.github/workflows/*validation*` | CI 驗證 | P2 | 文件／治理、GCC／Clang C17 與範例驗證已可重複執行 | A／完成 |

以上矩陣涵蓋本次 Constitution 2.0 審查中的既有文件區域；各 `design/01–17` 雖在表中依治理角色分組，均已逐份完成中英文審查。

## 三、主要裁決

### 1. AI 不得形成隱性必做

AI 可作選用延伸，但不得因位於核心章節、完成清單、模板、需求、能力、範圍、Unit 骨架、教材大綱或評量欄位而變成必做。不使用 AI 不影響完成、參與或評量。只有實際採用外部協助時，才產生相應的理解與技術驗證責任。

### 2. 評量只有一個權威來源

`design/13-learning-assessment-policy.*` 是正式評量制度唯一權威來源。README、作業包、rubric、模板、教師指南、設計標準與規劃模型只能提供導覽、追蹤、定義或執行方式。

### 3. 低層文件不得覆蓋高層來源

權威順序為 Constitution → 正式學習與評量制度 → 已核准設計標準 → 規劃與追蹤模型 → 執行指南與教材 → 歷史紀錄。

### 4. 技術敘述必須可驗證

相關教材必須說明必要的值域、輸入狀態、終止條件、生命週期、解參照前提、配置大小、ownership／釋放責任、失敗保留、stream 狀態、模組依賴、compile/link 差異與 undefined-behavior 邊界。成功編譯或單一正確輸出不能取代技術契約。

### 5. 概念模型不是實作保證

C 標準不要求固定的實體 preprocessor／compiler／assembler／linker 流程，也不要求單一實體 call-stack／heap 表示。當指令、產物、配置或 runtime 行為重要時，教材必須指出並驗證目標實作環境。

## 四、人工審查涵蓋範圍

逐份人工審查已涵蓋 P-U01–P-U04、F-U01–F-U12 的中英文教材，作業／rubric、教材索引／模板、教師指南、`design/01–17` 全部雙語 pair，以及 repository／治理入口與歷史紀錄邊界。

人工審查檢查權威來源、評量與 AI 規則、學生可讀性、教師文件邊界、雙語實質等值與技術敘述。未來課堂使用仍可能產生 P3 文字或節奏改善；除非發現實質衝突，否則不因此重開已完成的 P0/P1 審查。

## 五、自動化與技術驗證紀錄

在本 2.0.0 矩陣更新前的 PR #10 審查快照中：

- `scripts/validate_repository.py --skip-c`：114 份 Markdown，通過。
- GCC repository validation：114 份 Markdown、8 個一般 C translation units，通過。
- Clang repository validation：114 份 Markdown、8 個一般 C translation units，通過。
- `validation/check_materials.py`：114 份 Markdown；未發現孤立／未引用 Markdown 候選；navigation／bilingual／former-Constitution 檢查通過。
- `validation/run_validation.py`：GCC 與 Clang 均通過。
- `examples/verify.sh`：GCC 13.3.0 與 Clang 18.1.3 均通過，包含 `missing-return.c` 的 diagnostic-only 契約。
- GitHub Actions 的 `Technical Validation`、`Repository validation`、`Verify C17 examples` 在該審查快照均成功完成。

自動檢查驗證結構與可執行技術契約，不取代上述人工內容審查。

## 六、目前結論

PR #10 範圍內的全庫 Constitution 2.0 審查已完成。所有本輪識別的 P0/P1 已修復；雙語審查矩陣已涵蓋審查區域；學生教材、設計文件、導覽與技術驗證均已完成相應檢查。

因此 PR #10 可進入正式 review，而非維持 draft-only audit 狀態。後續 reviewer 或 CI 新發現應記為新的 finding；P2/P3 編輯或課堂改善可持續進行，但不與本次完成快照矛盾。
