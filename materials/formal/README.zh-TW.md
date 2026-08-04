# 正式課程學生教材

版本：1.0.1  
狀態：完整雙語學生教材集  
最後更新：2026-08-05  
對應英文版本：[Formal Course Student Materials](README.en.md)

## 文件用途

本目錄收錄接續四個前導 Unit 的十二個正式課程學生 Unit。每份教材都可供學生獨立閱讀、複習、實驗、診斷與說明。

教材以 C 作為教學語言，但核心目標是建立可遷移的程式設計 Concept。每個 Unit 都包含核心問題、心智模型、最小範例、預測或追蹤、可重現錯誤、練習、需求修改、簡短的 AI 概念解釋、自我檢核與摘要。

AI 只是一個低比重的對話工具，不取代預測、實作、測試、除錯或以證據判斷。

## Unit 導覽

| Unit | 中文教材 | English | 核心重點 |
|---|---|---|---|
| F-U01 | [表示、型別與運算](unit-01-representation-types.zh-TW.md) | [Representation, Types, and Operations](unit-01-representation-types.en.md) | 二進位表示、MSB／LSB、範圍、轉換、格式化輸出 |
| F-U02 | [複雜控制流程](unit-02-complex-control-flow.zh-TW.md) | [Complex Control Flow](unit-02-complex-control-flow.en.md) | 分支、sentinel、invariant、邊界 |
| F-U03 | [陣列](unit-03-arrays.zh-TW.md) | [Arrays](unit-03-arrays.en.md) | 集合、索引、走訪、邊界 |
| F-U04 | [字串](unit-04-strings.zh-TW.md) | [Strings](unit-04-strings.en.md) | 字元陣列、空字元、緩衝區 |
| F-U05 | [呼叫堆疊與遞迴](unit-05-call-stack-recursion.zh-TW.md) | [Call Stack and Recursion](unit-05-call-stack-recursion.en.md) | 呼叫框架、作用域、生命週期、base case |
| F-U06 | [指標](unit-06-pointers.zh-TW.md) | [Pointers](unit-06-pointers.en.md) | 位址、間接存取、別名、空指標 |
| F-U07 | [結構](unit-07-structures.zh-TW.md) | [Structures](unit-07-structures.en.md) | 異質欄位、配置、成員存取 |
| F-U08 | [動態記憶體](unit-08-dynamic-memory.zh-TW.md) | [Dynamic Memory](unit-08-dynamic-memory.en.md) | 配置、ownership、生命週期、釋放 |
| F-U09 | [檔案](unit-09-files.zh-TW.md) | [Files](unit-09-files.en.md) | stream、持久資料、EOF、錯誤檢查 |
| F-U10 | [模組化程式設計](unit-10-modular-programming.zh-TW.md) | [Modular Programming](unit-10-modular-programming.en.md) | 介面、實作、標頭檔、linking |
| F-U11 | [測試與除錯](unit-11-testing-debugging.zh-TW.md) | [Testing and Debugging](unit-11-testing-debugging.en.md) | testing、verification、validation、debugging、regression、refactoring |
| F-U12 | [整合應用程式](unit-12-integrated-application.zh-TW.md) | [Integrated Application](unit-12-integrated-application.en.md) | 需求、資料模型、記憶體、檔案、模組、證據 |

## 建議閱讀順序

請依 F-U01 至 F-U12 的順序閱讀。正式課程假設前導 Unit 已建立：

- 原始碼、編譯與執行
- 資料、值、型別、變數與狀態
- 條件、迴圈、邊界與追蹤
- 函數、責任、參數、回傳值與基本測試

## 完成標準

完成一個 Unit 不只代表產生一次正確輸出。學生應能：

- 解釋核心 Concept
- 預測或追蹤行為
- 實作最小案例
- 重現並診斷典型錯誤
- 測試正常與邊界行為
- 修改需求並指出受影響部分
- 以可觀察證據支持判斷

除非其他正式課程文件另有明確規定，教材中的活動皆為自主練習，不需繳交。

## 導覽

- [教材與活動資源](../README.zh-TW.md)
- [前導單元 P-U04](../preparatory/unit-04-functions-integration.zh-TW.md)
- [教學內容設計區](../../design/README.zh-TW.md)
- [English version](README.en.md)
