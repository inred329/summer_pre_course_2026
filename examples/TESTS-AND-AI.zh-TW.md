# C17 範例測試計畫與選用錯誤建議審查

版本：0.2.0  
狀態：教師資源  
最後更新：2026-08-07  
治理說明：本資源不自行建立評量或 AI／工具使用要求；正式規則仍以學習與評量制度為權威來源。  
對應英文版本：[C17 Example Test Plans and Optional Incorrect-Suggestion Review](TESTS-AND-AI.en.md)

## 文件用途

本資源協助教師與助教驗證 `examples/` 下的範例，並規劃預測、追蹤、診斷、修正與回歸活動。

學生應先建立預期結果或技術假設，再觀察 compiler／runtime 證據。AI 特定審查只屬選用延伸；核心活動也可以改由教師提供一段刻意錯誤敘述供學生判斷。

## Unit 1

### `unit-01/hello.c`

預期輸出：

```text
Hello, C!
```

### `unit-01/defects/missing-semicolon.c`

預期：C translation／build 失敗，因此不應執行一個「新建置完成」的程式。符合標準的實作必須對 constraint violation 提供 diagnostic，但訊息文字與標示位置可以不同；不得要求唯一的「missing semicolon」訊息。

選用錯誤建議審查：

> 這是 runtime error，先執行新建置的程式看看完整訊息。

應拒絕此主張，因為目前原始碼沒有成功 translation／build 成預期的新程式。

## Unit 2

### `unit-02/average.c`

輸入契約：兩個十進位整數；`count` 必須大於 0。

| 輸入 | 預期輸出 | 結束方向 |
|---|---|---|
| `5 2` | `Average: 2.50` | success |
| `0 3` | `Average: 0.00` | success |
| `5 0` | `Count must be positive` | failure |
| `5 -2` | `Count must be positive` | failure |
| 非整數輸入 | `Invalid input` | failure |

### `unit-02/defects/integer-division.c`

此程式預期可編譯，但輸出 `Average: 2.00`，因為整數除法先完成，之後才轉成 `double`。

選用錯誤建議審查：

> 只把輸出格式改成 `%.2f`，數學結果就會變成 2.50。

應拒絕此主張：格式只改變顯示方式，不會改變已完成的整數除法結果。

## Unit 3

### `unit-03/score-statistics.c`

輸入契約：以空白分隔的十進位整數；`-1` 是 sentinel；0 到 100 的分數納入統計，其他整數分數忽略。

| 輸入序列 | 預期結果 |
|---|---|
| `80 90 -1` | count 2、sum 170、average 85.00 |
| `0 100 -1` | count 2、sum 100、average 50.00 |
| `-1` | `No valid score` |
| `120 80 -1` | 忽略 120；count 1、sum 80、average 80.00 |

若輸入非整數 token，目前範例會停止掃描並輸出此前累積統計。應把這視為本範例明示的輸入契約，而不是默認它具有 malformed input recovery。

### `unit-03/defects/infinite-loop.c`

預期：原始碼可編譯，但執行後迴圈不終止，因為 `value` 從未更新。核心診斷優先使用靜態追蹤。若教師示範實際執行，應使用環境 timeout 或手動中止；CI 不得在沒有 timeout 的情況下直接執行此程式。

選用錯誤建議審查：

> 把 `while` 改成 `if` 就修好了。

應拒絕此主張，因為這會改變重複執行語意，而不是修正「朝終止條件前進」的缺陷。

## Unit 4

### `unit-04/max-of-three.c`

| 輸入 | 預期輸出 |
|---|---|
| `3 8 5` | `Maximum: 8` |
| `9 9 1` | `Maximum: 9` |
| `-3 -8 -5` | `Maximum: -3` |
| malformed input | `Invalid input` |

### `unit-04/defects/missing-return.c`

缺陷是：一個有回傳值型別的函數到達結尾 `}` 卻沒有回傳值，而 caller 又使用該函數呼叫的結果。依 C17，此執行具有 undefined behavior。開啟警告選項的常見 compiler 通常會對可疑控制路徑提出 warning，但這不是可攜的「必須編譯失敗」案例，也不得要求唯一警告文字。

自動驗證不得把此缺陷程式執行後觀察到的數值當成有意義結果。安全活動是先辨識契約違反、補上必要 `return`，再測試修正後函數。

選用錯誤建議審查：

> 只要其中一次執行印出預期最大值，就不需要補 `return`。

應拒絕此主張，因為當語言層級前提已被破壞時，單次觀察不能證明行為正確。

## 教學規則

- `defects/` 下的檔案刻意含錯，不得當成正確 reference solution。
- 先做預測與技術推理，再進行選用外部建議審查。
- 修正後重新執行適用的正常、邊界、無效與失敗案例。
- 不因學生採用不同做法就扣分；只要符合相同契約與證據期待即可。
- 不要求 AI 使用、AI log、固定 prompt 或未使用聲明。

## 導覽

- [範例索引](README.md)
- [編譯清單](COMPILE-MANIFEST.md)
- [English version](TESTS-AND-AI.en.md)
