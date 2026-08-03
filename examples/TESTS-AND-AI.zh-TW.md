# C17 範例測試與錯誤 AI 建議

版本：0.1.0  
狀態：正式教學資源  
最後更新：2026-08-03  
對應英文版本：[C17 Example Tests and Incorrect AI Suggestions](TESTS-AND-AI.en.md)

## 文件用途

供教師與助教搭配 `examples/` 使用。所有案例先要求學生預測，再編譯、執行、比較與說明。

## 單元 1

### `unit-01/hello.c`

預期輸出：

```text
Hello, C!
```

### `unit-01/defects/missing-semicolon.c`

預期：編譯失敗；程式尚未執行。不同編譯器訊息文字可不同，但應指出 `printf` 附近需要 `;`。

錯誤 AI 建議：

> 這是執行期錯誤，先執行程式看看完整訊息。

學生應拒絕，因為編譯失敗時沒有新的程式執行。

## 單元 2

### `unit-02/average.c`

| 輸入 | 預期輸出 |
|---|---|
| `5 2` | `Average: 2.50` |
| `0 3` | `Average: 0.00` |
| `5 0` | `Count must be positive` |

### `unit-02/defects/integer-division.c`

輸入 `5 2` 時，錯誤結果可能為 `2.00`。原因是整數除法先完成，再轉成 `double`。

錯誤 AI 建議：

> 把輸出格式改成 `%.2f` 就會得到 2.50。

學生應拒絕；格式只能改變顯示方式，不能修正已經發生的整數除法。

## 單元 3

### `unit-03/score-statistics.c`

| 輸入序列 | 預期結果 |
|---|---|
| `80 90 -1` | count 2、sum 170、average 85.00 |
| `0 100 -1` | count 2、sum 100、average 50.00 |
| `-1` | `No valid score` |
| `120 80 -1` | 忽略 120，只計算 80 |

### `unit-03/defects/infinite-loop.c`

預期：輸入後迴圈不終止，因為控制變數沒有更新。

錯誤 AI 建議：

> 把 `while` 改成 `if` 就能修好。

學生應先指出這會改變需求，不能取代「重複直到終止」的迴圈。

## 單元 4

### `unit-04/max-of-three.c`

| 輸入 | 預期輸出 |
|---|---|
| `3 8 5` | `Maximum: 8` |
| `9 9 1` | `Maximum: 9` |
| `-3 -8 -5` | `Maximum: -3` |

### `unit-04/defects/missing-return.c`

預期：編譯器應提出非 `void` 函數可能未回傳值的警告；實際結果不可信。

錯誤 AI 建議：

> 只要目前測試輸出正確，就不必補 `return`。

學生應拒絕；函數契約要求所有可達路徑都提供回傳值。

## 教學規則

- 缺陷檔不得當成正確範例。
- 錯誤 AI 建議先讓學生預測，不直接公布判斷。
- 修正後必須重新執行正常、邊界與必要異常案例。
- 不因學生採用不同合理解法而扣分。

## 導覽

- [範例索引](README.md)
- [English version](TESTS-AND-AI.en.md)
