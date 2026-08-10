# 多角度學生閱讀體驗審查

版本：1.0.0  
狀態：本輪完成  
最後更新：2026-08-10  
對應英文版本：[Multi-Angle Student Reading Experience Review](multi-angle-reading-experience-pass.en.md)

## 審查目的

本輪不是再次檢查單純的文法、技術正確性或 Unit 是否存在，而是從不同學生的理解方式重新閱讀學生主線，特別檢查：

- 文章語氣是否像在引導理解，而不是命令、糾正或規格書；
- 同一個核心概念是否只有單一路徑，還是能從需求、程式、圖像、trace、反例、實驗、測試或需求修改等不同角度建立；
- 多種角度是否真的互補，而不是為了形式重複同一句話；
- 類比是否必要且有邊界，不因追求親切而引入錯誤模型；
- 第一次學 C、已使用過 IDE、偏好視覺追蹤、偏好實際實驗、偏好從錯誤反推原因的學生，是否都有可進入理解的入口；
- 中英文是否保留相同的教學角度與語氣強度。

## 整體結論

目前學生教材的多角度教學已具有穩定基礎，不需要把所有 Unit 機械式改成相同模板。中後段教材尤其常以「需求動機 → 最小程式 → 圖／trace → 邊界或錯誤 → 實驗／測試 → 需求修改」形成互補理解。

本輪發現最值得修正的是 P-U00。原版本雖然技術流程清楚，但仍較像由作者指定一條理解路徑。對第一次碰開發環境的學生而言，有人會先從 IDE 按鈕理解，有人喜歡看到實際檔案與 terminal 指令，也有人是在「程式改了但輸出沒變」時才真正理解 Build 與 executable 的差別。

P-U00 已修成三種合法入口：

```text
IDE-first
terminal / file-first
failure-first
```

三種入口最後收斂到同一模型：

```text
source → Build → executable → Run
```

同時調整部分命令式語氣，改成邀請學生預測、選擇較有感的理解方式、再把自己的操作對回模型。

## Unit-by-Unit 多角度檢查

### P-U00

主要角度：

- IDE 按下 Run 的熟悉經驗；
- `hello.c`、Build 指令與 executable 的實體檔案路徑；
- stale executable 的故障情境；
- IDE 組成圖；
- Run / Debug 的 breakpoint 觀察；
- Build 成功與需求正確的層次區分。

本輪修正：新增 IDE-first、terminal/file-first、failure-first 三入口，補一個有明確限制的播放類比來理解 Run / Debug，並柔化多個「不要……」句型。

### P-U01

主要角度：

- 從程式文字預測輸出；
- `main` 的順序流程；
- `printf` 可觀察結果；
- trace 表；
- `return` 造成可達／不可達差異；
- compile failure 與 execution mismatch 分類；
- 交換輸出順序的小實驗。

判定：角度足夠，語氣雖有明確指令，但大多立即提供操作理由與可驗證行動，未形成治理式語氣。

### P-U02

主要角度：

- `score = score + 5` 的直覺衝突；
- data / value / type / variable / state 分解；
- 狀態表；
- 輸入使外部資料進入狀態；
- integer division 與 format mismatch 的結果反例；
- 需求增加上限後自然導向控制流程。

判定：適合偏抽象、偏追蹤與偏實驗的不同學生。

### P-U03

主要角度：

- 成績上限需求引出選路；
- boundary table；
- `if/else` flowchart；
- 需求語句對照比較運算；
- 多分支順序反例；
- `while` 的四問題模型與狀態表；
- off-by-one 與不終止案例。

判定：同一控制流程概念有圖、表、程式與邊界值多入口。

### P-U04

主要角度：

- `main` 做太多工作的維護痛點；
- 一件容易命名的責任；
- argument → parameter → return 的資料流圖；
- 單次呼叫 trace；
- 「這個函數負責＿＿」的語意檢查；
- 介面與需求修改。

判定：函數不是以語法表起頭，對不同理解方式友善。

### F-U00

主要角度：

- 熟悉的 Run 按鈕反拆流程；
- source 與 executable 的 artifact 差異；
- stale executable 實驗；
- IDE / compiler 角色分離；
- Build success 與 requirement success 分層；
- breakpoint 觀察；
- 為 F-U10 compile/link 與 F-U11 debugging 留下明確伏筆。

判定：正式班入口適合已有操作經驗但工具模型不完整的學生。

### F-U01

主要角度：

- `5 / 2` 的結果驚訝；
- bit pattern / representation；
- LSB/MSB 權重；
- operand-type data flow；
- format string type contract；
- floating-point experiment；
- signed/unsigned boundary behavior；
- defined-vs-undefined error classification。

判定：抽象 representation/type 有數值、位元、I/O 與錯誤分類多條入口。

### F-U02

主要角度：

- grade classification trace；
- boundary-value table；
- `switch` 對照離散選項；
- nested-path table；
- sentinel 與 EOF / invalid input 三路徑；
- 控制流程與測試覆蓋互相連接。

判定：不是只增加語法，路徑模型清楚。

### F-U03

主要角度：

- 五個／五十個變數的規模痛點；
- array box diagram；
- index/value 分離；
- loop trace table；
- out-of-bounds 反例；
- initialized-vs-addressable distinction；
- 三種不同 traversal 任務；
- 需求修改。

判定：多角度表現良好。

### F-U04

主要角度：

- `char` array 與 text 的差異；
- `"cat"` 格子圖；
- character array vs terminated string 對照；
- capacity / visible length / required storage 三數字模型；
- `fgets` truncation 實驗；
- newline / EOF / overlong-line 分類；
- parser contract。

判定：對字串這個常見高認知負荷主題提供足夠不同切入方式。

### F-U05

主要角度：

- 熟悉函數呼叫的「這一次」狀態；
- nested call tree；
- call-stack reasoning model；
- scope vs lifetime 對照；
- countdown recursion；
- wrong-direction recursion 反例；
- factorial 的下降與回傳展開；
- 字串索引遞迴。

判定：遞迴同時有結構圖、數學展開、錯誤方向與不同資料例子。

### F-U06

主要角度：

- 從熟悉 `scanf(..., &score)` 回收概念；
- object / value / address 四項分離；
- pointer diagram；
- `&` / `*` 操作流程；
- 修改 caller object；
- NULL；
- lifetime / dangling；
- aliasing；
- array decay / pointer arithmetic / one-past；
- 四問題安全檢查。

判定：是全套教材中多角度建立抽象概念最完整的 Unit 之一。

### F-U07

主要角度：

- 同一學生欄位分散的資料組織問題；
- struct tree diagram；
- type vs object；
- field initialization validity；
- `.` 與 `->` 的等價關係；
- value vs pointer passing；
- 後續 copy / array-of-records 需求。

判定：struct 由「資料屬於同一實體」引出，不是語法清單。

### F-U08

主要角度：

- fixed array limitation；
- element count vs byte count；
- allocation lifecycle trace；
- `free` 後 alias 仍存在；
- ownership 的 leak / double-free 對照；
- realloc growth；
- pointer-to-pointer 的 caller-owner diagram；
- unchanged-on-failure contract。

判定：同時服務偏資料結構、偏生命週期與偏介面推理的學生。

### F-U09

主要角度：

- process lifetime vs persistence 的需求；
- stream lifecycle；
- file mode 作為資料政策；
- `fscanf` return-driven loop 與 `feof` 反例；
- EOF / format / I/O error 分類；
- `fgets` complete-record 問題；
- file format as protocol；
- transactional load；
- write/close failure path。

判定：檔案不是 API 函式清單，而是一筆資料完整旅程。

### F-U10

主要角度：

- all-in-one `main.c` 的 change-cost 痛點；
- interface vs implementation；
- header/source 實例；
- failure contract；
- include dependency diagram；
- compile → object → link pipeline；
- compile error vs link error；
- information hiding；
- second frontend 作為 module-boundary test。

判定：模組概念有維護視角與工具鏈視角，不只檔案拆分。

### F-U11

主要角度：

- requirement-derived tests；
- boundary table；
- failure vs root cause；
- debugging hypothesis loop；
- reproducible bug report；
- regression；
- verification vs validation；
- test expectation itself can be wrong；
- refactoring protection；
- evidence-based code review。

判定：同一個「可信度」概念有多層證據角度。

### F-U12

主要角度：

- observable requirements；
- data-model diagram + invariant；
- milestone-by-milestone implementation；
- ownership growth trace；
- module boundary；
- file protocol and transactional load；
- interactive layer added after core tests；
- layered testing；
- final multi-score requirement change propagating through ownership/API/protocol/tests。

判定：整合章雖資訊量大，但採里程碑敘事避免規格書式一次灌入。

## 語氣檢查

整體教材常使用「先預測」「先分類」「不要只……」等句型。這些句型在技術教材中有明確教學功能，但若密度過高，會累積成糾正式語氣。

本輪採取的原則是：

- 保留真正能阻止常見誤解的提醒；
- 能改成「可以試著……」「如果這個角度較有感……」「換一個角度看……」時，優先使用邀請式語氣；
- 不把「不要背」本身當成口號，後面必須提供可操作的理解方式；
- 不因追求親切而降低技術精確性；
- 不大量加入擬人或生活類比，以免學生記住類比卻誤解 C 的實際規則。

P-U00 已依此原則做成對修正。其餘 Unit 目前的提醒語句多半緊接著原因、trace、測試或替代策略，尚未形成需要全面重寫的語氣污染。

## 本輪完成判定

- P-U00～P-U04：多角度與語氣檢查完成。
- F-U00～F-U12：多角度與語氣檢查完成。
- 中英文新修 P-U00：實質等值。
- 主要抽象概念皆至少有兩種以上實質不同的理解入口；不是依賴定義重述。
- 沒有要求每個 Unit 使用固定教學裝置；角度選擇依概念需要而定。
- 本輪未發現需要大規模重寫的學生閱讀障礙。
