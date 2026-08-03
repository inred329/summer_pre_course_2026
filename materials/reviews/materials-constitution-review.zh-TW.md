# 前導教材憲法遵循審查

版本：0.1.0  
狀態：正式審查紀錄  
最後更新：2026-08-03  
重大變更摘要：完成所有前導單元、作業、rubric、AI 紀錄與教師指引的憲法逐項檢查。  
對應英文版本：[Preparatory Materials Constitution Compliance Review](materials-constitution-review.en.md)

## 審查範圍

- `materials/TEMPLATE.*`
- `materials/preparatory/unit-01-execution.*`
- `materials/preparatory/unit-02-data-state.*`
- `materials/preparatory/unit-03-control-flow.*`
- `materials/preparatory/unit-04-functions-integration.*`
- `materials/assignments/preparatory-assignments.*`
- `materials/assignments/rubric.*`
- `materials/assignments/ai-use-log.*`
- `materials/assignments/grading-guide.*`
- `materials/README.*`

## 審查基準

重新讀取並對照：

- `CONSTITUTION.zh-TW.md` 1.2.0
- `CONSTITUTION.en.md` 1.2.0

## 結果摘要

| 憲法要求 | 結果 | 說明 |
|---|---|---|
| 雙語成對與實質一致 | 通過 | 所有正式教材與教師文件都有中英文版本，核心結構、程式、測試與標準一致。 |
| 文件目的與可獨立閱讀 | 通過 | 教材說明讀者、目標、前置、工具、任務、完成與補驗標準。 |
| 導覽可發現性 | 通過 | 根 README 經教材索引可抵達所有正式教材。 |
| 術語一致 | 通過 | 使用 `design/11-terminology-glossary` 的正式術語。 |
| 結構一致 | 通過 | 四個單元依共用模板建立；作業與 rubric 採固定結構。 |
| 程式與文字一致 | 通過 | 範例使用 C17、GCC/Clang 指令、相同中英文程式與測試資料。 |
| 視覺化 | 通過 | 工具鏈、狀態、控制流程與責任分解均提供對應圖或追蹤表。 |
| 認知負荷 | 通過 | 每單元限制新概念並明列可延後內容；不加入進階資料結構。 |
| 理解優先 | 通過 | 所有作業均要求預測、追蹤、測試、修改、除錯或口試。 |
| 錯誤與測試核心化 | 通過 | 每單元含可重現錯誤與正常、邊界、必要異常案例。 |
| 多元合理解法 | 通過 | rubric 明確禁止因與範例不同而扣分。 |
| AI 不取代思考 | 通過 | 每份教材與作業明列允許、禁止、必須保留與驗證責任。 |
| 雙語公平 | 通過 | 核心能力與通過標準相同；只允許節奏與語言支架差異。 |
| 補驗針對能力 | 通過 | 補驗對應缺失能力，不要求無差別重做。 |
| 版本與變更追蹤 | 通過 | 所有新增正式文件都有版本、日期、重大變更與對應語言。 |

## 審查中修正

發現整合作業的「刪除最低分後重算平均」可能讓學生誤以為需要尚未教授的陣列。已同步修改中英文作業包，明確規定：

- 使用三個獨立成績變數即可。
- 可用三數總和減最低分，再除以 2。
- 不要求也不鼓勵陣列或其他尚未教授的資料結構。

## 剩餘限制

- 教材中的程式碼為人工審查的短小 C17 範例；倉庫目前尚未建立自動編譯 CI。發布前仍須由教師在指定環境實際編譯。
- 作業截止日期與實際班級行事曆尚未填入；在班級發布版本中必須同步補上中英文相同條件。
- 教師提供的缺陷程式與錯誤 AI 建議需在實際授課前建立雙語等值版本。

上述為執行前待辦，不構成目前教材內容與憲法的衝突。

## 最終結論

目前所有已建立的前導課程教材、作業與評量文件均符合課程憲法，可作為後續課堂版本與發布版本的正式基準。

## 導覽

- [教材索引](../README.zh-TW.md)
- [English version](materials-constitution-review.en.md)
