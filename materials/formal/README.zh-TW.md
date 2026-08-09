# 正式課程學生教材

版本：1.2.0  
狀態：完整雙語學生教材集  
最後更新：2026-08-09  
對應英文版本：[Formal Course Student Materials](README.en.md)

## 正式班從這裡開始

正式課程現在從 F-U00 開始。F-U00 不要求你先走前導課程，而是先把 source、compiler、Build、executable、Run、Debug 這些正式課程會反覆使用的工具角色拆清楚。

**[開始 F-U00：按下 Run 之後，到底發生了什麼？](unit-00-build-run-ide.zh-TW.md)**

前導 Unit 仍然是補充基礎的入口，不是正式班學生的必經閱讀路徑。如果你對變數與狀態、條件與迴圈、函數與參數等基礎概念不熟悉，可以再依需要回到前導教材複習。

## Unit 導覽

| Unit | 中文教材 | English | 核心重點 |
|---|---|---|---|
| F-U00 | [按下 Run 之後，到底發生了什麼？](unit-00-build-run-ide.zh-TW.md) | [What Actually Happens After You Press Run?](unit-00-build-run-ide.en.md) | source、compiler、IDE、Build、Run、Debug、舊 executable |
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

## 閱讀順序

請依 F-U00 至 F-U12 的順序閱讀。每個 Unit 結尾都有「下一單元」連結，因此開始 F-U00 後可以沿著教材一路往下，不需要回到 repository 首頁或其他內部文件尋找下一步。

正式課程會使用以下基礎能力：

- 能編輯、Build 並執行簡單 C 程式，並知道 IDE 不等於 compiler
- 能追蹤變數和值的改變
- 能閱讀基本條件與迴圈
- 能理解函數、參數與回傳值的基本角色

如果後三項其中某項不熟悉，再回到前導課程對應 Unit 複習即可，不需要把整套前導課程當成正式課程的固定前置閱讀清單。

## 完成一個 Unit 時

完成一個 Unit 不只代表產生一次正確輸出。你應該逐漸能夠解釋核心概念、預測或追蹤行為、實作最小案例、重現並診斷典型錯誤、測試正常與邊界行為，並在需求改變時指出受影響的部分。

AI 使用不是核心完成條件。教材中標示為選做的 AI 活動可以直接跳過。

## 導覽

- [學生入口](../STUDENT-START.zh-TW.md)
- [開始 F-U00](unit-00-build-run-ide.zh-TW.md)
- [English version](README.en.md)
