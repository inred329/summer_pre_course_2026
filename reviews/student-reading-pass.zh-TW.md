# 學生閱讀體驗審查｜Student Reading Pass

版本：2.0.0  
最後更新：2026-08-09  
對應英文版本：[Student Reading Pass](student-reading-pass.en.md)

## 審查目的

逐篇從學生視角閱讀學生教材，檢查開頭動機、概念出現時機、段落銜接、範例作用、治理語氣污染、Unit 間過渡，以及中英文實質等值。

本輪不是再次確認 Constitution 或文件治理，而是把每一份學生 Unit 從第一句讀到最後一個轉場，確認學生能沿著教材本身建立問題、模型、範例與下一步，不需要回頭查閱內部 design／review 文件才知道「為什麼現在要學這件事」。

## 最終進度

| Unit | 中文 | English | 狀態 | 主要處理 |
|---|---|---|---|---|
| P-U01 | 已完成 | 已完成 | 完成 | 以 `hello.c` 實驗取代治理式開場，串起編譯、執行、故障與修改。 |
| P-U02 | 已完成 | 已完成 | 完成 | 以 `score` 狀態變化貫穿；把下一單元概念降為預覽。 |
| P-U03 | 已完成 | 已完成 | 完成 | 直接承接 100 分上限失敗案例，以邊界、狀態與終止建立控制流程。 |
| P-U04 | 已完成 | 已完成 | 完成 | 先建立函數呼叫與直接回傳，延後輸出指標與 `NULL`。 |
| F-U01 | 已完成 | 已完成 | 完成 | 以 `5 / 2` 的意外結果串起表示、型別、格式、近似、邊界與未定義行為。 |
| F-U02 | 已完成 | 已完成 | 完成 | 以「值決定路徑」串起分支、邊界、sentinel、EOF、invariant 與需求修改。 |
| F-U03 | 已完成 | 已完成 | 完成 | 從保留多筆資料建立陣列需求；統一索引、長度、初始化與越界；延後完整指標模型。 |
| F-U04 | 已完成 | 已完成 | 完成 | 從字元陣列建立 `\0`、容量、完整行、殘留輸入與安全走訪主線；修正三格 `"cat"` 初始化的 C 語言說明；避免在 F-U06 前要求完整指標模型。 |
| F-U05 | 已完成 | 已完成 | 完成 | 從既有函數呼叫自然切入每次呼叫的獨立狀態，再串起 call frame、等待關係、scope/lifetime、遞迴終止、結果範圍與迭代比較。 |
| F-U06 | 已完成 | 已完成 | 完成 | 從既有 `scanf(..., &score)` 回收位址問題；依序建立物件／值／位址、解參照、`NULL`、生命週期、aliasing、陣列轉換與 one-past。 |
| F-U07 | 已完成 | 已完成 | 完成 | 從「一位學生的欄位為何散落」建立 `struct` 需求；串起型別／物件、初始化、`.`／`->`、字串欄位、結構複製、比較語意與結構陣列。 |
| F-U08 | 已完成 | 已完成 | 完成 | 重寫成固定容量→配置生命週期→ownership→`realloc` 成長→pointer-to-pointer→失敗契約；為 `int **` 增加 owner pointer 圖與逐層解釋。 |
| F-U09 | 已完成 | 已完成 | 完成 | 從「資料要活過這次執行」自然引出 stream、開檔模式、讀取結果、完整紀錄、file protocol、transactional load 與 write/close failure。 |
| F-U10 | 已完成 | 已完成 | 完成 | 從單一 `main.c` 的修改成本建立模組需求，再串起 interface/implementation、header/source、translation unit、compile/link 與 information hiding。 |
| F-U11 | 已完成 | 已完成 | 完成 | 從前面已做過的邊界與失敗測試收束成 requirement→expected→test→debug hypothesis→minimal fix→regression 的證據鏈，並清楚分離 verification／validation。 |
| F-U12 | 已完成 | 已完成 | 完成 | 以里程碑方式整合 Student、StudentList、ownership、檔案、模組與測試；修正英文舊版規格式結構，重新與中文整合敘事實質對齊。 |

## 主要閱讀決策

P-U01～P-U04 的共同問題原本不是知識缺漏，而是開頭與活動容易像「教材規格」。修正後每一篇都先從學生能立即觀察的程式現象或前一 Unit 留下的問題開始，再逐步引入術語；前導課程不再提前要求輸出指標、`NULL` 或不必要的整數邊界機械細節。

F-U01～F-U04 建立正式課程前半段的連續主線：表示與型別影響結果 → 值如何選擇控制路徑 → 多筆資料為什麼需要陣列 → 字元陣列如何靠 `\0` 形成文字。F-U04 對 `char word[3] = "cat";` 的說明也改為符合 C 規則：它可形成三個已初始化字元，但沒有終止 `\0`，因此不是可直接交給一般字串介面的 terminated C string。

F-U05～F-U07 刻意把抽象名詞放在已有用途之後。F-U05 從學生反覆呼叫過的函數建立 per-call state；F-U06 再回收早已看過的 `&score` 建立位址／指標；F-U07 最後讓 `->` 在 struct 成員已經有意義後才出現。Call stack 保持為 execution reasoning model，不被描述成 C 標準保證的固定實體記憶體配置。

F-U08 是本輪正式課程後半最明顯的閱讀斷點。舊版在可成長陣列後直接出現 `append_value(int **values, ...)`，容易讓學生把 pointer-to-pointer 當成突然多出的符號。本輪改為先走完 allocation lifetime、ownership、`realloc` 與 alias invalidation，再專門回答「為什麼這次要 `int **`」：因為函數要修改的呼叫者物件本身就是 `int *` owner，所以傳入的是 owner pointer 本身的位置 `&values`。接著才展示 unchanged-on-failure 的 append 契約與實作。

F-U09～F-U11 原有版本已具有穩定敘事，不需要為了「有修改」而重寫。F-U09 沿著一筆資料的持久化旅程建立 stream／protocol／transaction；F-U10 從修改成本建立 module boundary，再自然區分 compile 與 link；F-U11 則把前十章已反覆使用的測試習慣收束成一條可重現、可反駁、可回歸的 evidence workflow。

F-U12 發現的是實質雙語不等值，而不是單句翻譯問題。中文版已改成 incremental milestone 敘事：先需求與可觀察證據，再 StudentList invariant、最小生命週期、add、固定資料測試、ownership trace、模組、file protocol、互動輸入、分層測試與最後需求修改；英文版仍是舊版的規格／能力清單結構。本輪已把英文版完整同步成同一教學順序，並保留相同的 failure contract、transactional load、nested ownership 與 final requirement-change reasoning。

## Unit 間閱讀鏈

目前正式課程可以連續讀成：

```text
表示／型別
→ 控制路徑
→ 陣列
→ 字串
→ 函數呼叫狀態／遞迴
→ 位址／指標
→ 結構
→ 動態配置／ownership
→ 檔案持久化
→ 模組邊界
→ testing／debugging／evidence
→ integrated application
```

每一個下一 Unit 的主要問題，都由上一 Unit 已經使用但尚未完整回答的需求或限制引出，而不是靠內部 course-design 文件告訴學生「下一章必須學什麼」。

## 完成判定

Student Reading Pass 已完成目前 repository snapshot 的全體學生 Unit：P-U01～P-U04 與 F-U01～F-U12 均已完成中英文逐篇閱讀；主要治理／規格式語氣、概念過早出現、敘事跳躍與雙語不等值已處理；各 Unit 可由教材本身建立學習動機、主模型、練習與下一單元轉場。

後續若教學試跑、學生回饋或正式 review 發現新的理解障礙，應以新的 reading finding 處理，不需要重新打開已完成的全庫第一輪閱讀審查。