# 全 Unit 技術驗證報告

版本：1.0.0  
狀態：完成技術審查紀錄  
最後更新：2026-08-05  
對應英文版本：[All-Unit Technical Validation Report](all-units-technical-validation.en.md)

## 文件目的

本報告記錄 P-U01 至 P-U04 與 F-U01 至 F-U12 雙語學生教材的完整技術驗證。檢查範圍包括 C17 語意、輸入輸出契約、型別與運算邊界、陣列與字串、遞迴、指標、結構、動態記憶體、檔案、模組、整合 invariant、故意錯誤範例、雙語同步與導覽。

本審查區分：

- 預期可編譯並執行的完整程式
- 只用來說明單一規則的片段
- 故意產生診斷、邏輯失敗、未定義行為、連結失敗或資源缺陷的錯誤片段

## 驗證基準

正確完整範例以 C17 撰寫，警告基準為：

```bash
gcc -std=c17 -Wall -Wextra -Wformat=2 -pedantic source.c -o program
clang -std=c17 -Wall -Wextra -Wformat=2 -pedantic source.c -o program
```

多檔案範例使用分開編譯與 linking。使用 `fabs` 的程式在部分環境可能需要額外加入 `-lm`。

目前倉庫中的程式碼位於 Markdown，而非已抽取的機器測試 harness。因此本次驗證結合完整程式碼審查、C17 語言規則、明確回傳值與邊界契約、雙語程式碼比較及可重現測試規格。未來可再自動抽取並持續編譯，但目前教材基準沒有已知未解決技術缺陷。

## 驗證矩陣

| Unit | 主要技術檢查 | 結果 |
|---|---|---|
| P-U01 | 最小程式、編譯／執行差異、舊執行檔實驗、編譯錯誤分類 | 通過 |
| P-U02 | `scanf` 回傳、初始化狀態、整數除法、variadic 格式不匹配 | 修正後通過 |
| P-U03 | 分支輸入檢查、迴圈終止、off-by-one、stale／invalid input | 修正後通過 |
| P-U04 | 函數宣告、狀態／輸出契約、有號加法溢位、除法前置條件 | 修正後通過 |
| F-U01 | 整數轉型、有號溢位、浮點誤差、字元集假設、格式不匹配 | 修正後通過 |
| F-U02 | 分支順序、`switch` fall-through、sentinel 與 EOF／無效文字、invariant、零筆平均 | 修正後通過 |
| F-U03 | 陣列邊界、未初始化元素、空集合最大值、null output | 修正後通過 |
| F-U04 | 終止字串、`fgets` 回傳、換行、邏輯行截斷、殘留輸入 | 修正後通過 |
| F-U05 | 可到達 base case、負數範圍、結果範圍、乘法檢查、stack／resource 分類 | 修正後通過 |
| F-U06 | null、indeterminate、dangling、one-past 指標、別名與輸出契約 | 修正後通過 |
| F-U07 | 完整初始化、空結構指標、有界姓名、非有限欄位、結構比較 | 修正後通過 |
| F-U08 | 輸入檢查、配置大小、所有權、`realloc`、leak／use-after-free／double-free 分類 | 修正後通過 |
| F-U09 | `fopen`、寫入、讀取停止原因、EOF／格式／I/O、`fclose`、模式 | 修正後通過 |
| F-U10 | null／空輸入、介面與定義一致、分開編譯、linking、private helper | 修正後通過 |
| F-U11 | 邊界導向測試、可重現缺陷、回歸、verification／validation | 通過 |
| F-U12 | invariant、nullability、`size_t`、容量／位元組溢位、transactional load、空平均、cleanup | 修正後通過 |

## 已確認修正

### 輸入與狀態

- 每個完整 `scanf` 範例都在使用目標變數前檢查轉換成功。
- Sentinel 迴圈區分 sentinel、EOF、無效文字與超出範圍數值。
- 輸入失敗不會使用 indeterminate value 或重複處理 stale state。

### 運算與表示

- 需要安全保證的範例會在有號加法與乘法前檢查溢位。
- 空集合平均與零除數都有明確失敗行為。
- Variadic format mismatch 明確分類為未定義行為，而非僅描述成「輸出錯誤」。
- 浮點比較說明誤差門檻取決於需求與尺度。
- 未在沒有環境契約時假設字元數值一定是 ASCII。

### 陣列與字串

- 最大值函數拒絕 null 或空輸入，不讀取第 0 個元素。
- 讀取未初始化陣列與結構成員明確分類為未定義行為。
- `fgets` 範例區分合法終止緩衝區與完整邏輯輸入行。
- 過長輸入會回報並清除剩餘字元，再進行下一次讀取。
- 固定容量結構字串使用 checked policy，不使用無界複製。

### 遞迴與指標

- 階乘遞迴拒絕負數，並在乘法前檢查結果溢位。
- 不終止、stack exhaustion、需求失敗與有號溢位分開分類。
- 指標介面定義 nullability、lifetime、boundary、輸出行為與 aliasing。
- One-past pointer 可以建立，但不會被解參照。
- 回傳自動儲存物件位址後再解參照明確分類為未定義行為。

### 動態記憶體與整合容量

- 在轉成 `size_t` 前先檢查配置輸入。
- `realloc` 使用暫存指標，失敗時保留原區塊。
- 整合清單成長會檢查容量回繞與配置位元組乘法。
- `count` 只在驗證、配置與複製成功後才改變。
- List invariant 與空集合行為已明確定義。

### 檔案與模組

- 開檔、寫入、讀取、格式、EOF、I/O error 與關閉結果分開處理。
- 儲存成功必須同時確認寫入與關閉成功。
- 載入既有集合採用明確的 transactional replace policy。
- 模組範例檢查 null／空輸入，並區分編譯錯誤與連結錯誤。
- 技術審查中發現的 F-U02、F-U09、F-U10 與 F-U12 舊檔名導覽已全部修正。

## 故意錯誤範例分類

| 類別 | 代表範例 |
|---|---|
| 編譯期診斷／constraint violation | 結構 `==`、對結構指標使用 `.`、宣告與定義不一致 |
| Link error | 連結命令漏掉提供必要定義的 object file |
| 邏輯／需求錯誤 | 分支順序、忽略狀態、sentinel 被加入總和、參數順序錯誤 |
| 未定義行為 | 有號溢位、variadic format mismatch、越界、未初始化讀取、無效指標解參照、整數除零 |
| 資源／終止缺陷 | 無界遞迴、leak、double free、use after free、關閉失敗、部分載入 |
| 證據不足 | 單一成功輸出、未測邊界、修正後沒有 regression |

故意錯誤片段不會被描述為安全可執行程式。教材現在會指出應使用何種證據：編譯器診斷、追蹤、邊界測試、記憶體模型、檔案測試或 linking command。

## 雙語等值

16 個 Unit 都已確認：

- 中英文檔案同時存在
- 修正後完整範例使用相同介面與安全規則
- 測試涵蓋相同正常、邊界、無效、null 與失敗案例
- 錯誤分類實質一致
- 前後 Unit 與語言切換使用實際檔名

F-U12 原先中英文整合範例實質不同。現在兩版都使用相同 `Student`／`StudentList` 模型、`size_t` 筆數、invariant、安全成長檢查、checked average 與 transactional load policy。

## 導覽驗證

預期導覽鏈已有效：

```text
materials/README.*
→ materials/formal/README.* 或前導 Unit
→ 各 Unit
→ 上一／下一 Unit
→ 對應語言版本
```

技術審查中發現的 F-U01、F-U02、F-U03、F-U09、F-U10 與 F-U12 舊連結均已修正。

## 最終技術結論

目前 Markdown 教材基準已為所有完整 C 範例建立明確且技術安全的契約，為故意錯誤片段提供正確分類，完成雙語實質同步並修正導覽。

> **全部 16 個 Unit 已完成目前技術驗證階段，沒有已知技術缺陷會阻擋 PR #8 進入審查。**

以下屬持續驗證改善，不是本階段未解決缺陷：

- 自動抽取與編譯 Markdown 程式碼區塊
- 建立 CI 連結檢查與雙語 code-block 比較
- 在學生實際使用的 Windows／Linux toolchain 執行教室環境 smoke test

## 導覽

- [全文件憲法遵循重審](all-documents-constitution-review.zh-TW.md)
- [教材索引](../README.zh-TW.md)
- [English version](all-units-technical-validation.en.md)
