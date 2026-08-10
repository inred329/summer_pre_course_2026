# 正式單元 F-U00：按下 Run 之後，到底發生了什麼？

版本：1.1.0  
狀態：正式學生教材  
最後更新：2026-08-10  
對應英文版本：[Formal Unit F-U00: What Actually Happens After You Press Run?](unit-00-build-run-ide.en.md)

正式課程開始以前，先把三個很容易混在一起的詞放回正確位置。

## 0. 先把 program、programming language、programming 分開

- **程式（program）**：交給電腦執行的一套明確工作描述；它可能接收資料、依規則處理，再產生可以觀察的結果。
- **程式語言（programming language）**：用來精確表達資料、操作與控制規則的一套語言；這門課使用 C。
- **程式設計（programming）**：從理解問題、設計解法、用程式語言表達，到執行、測試、診斷與修改的整個過程。寫 code 是其中一部分，不是全部。

所以正式課程不是單純「再學更多 C 語法」。後面我們會一直問：需求怎麼變成可執行的解法？解法用 C 表達後，怎麼知道它真的符合需求？當型別、記憶體、檔案與模組加入時，原本的推理還能不能成立？

你很可能已經使用過 **IDE（Integrated Development Environment，整合式開發環境）**。它把編輯、Build、Run、Debug 與其他開發工作整合在同一個操作環境裡。現在先把它理解成「整合開發工作的介面」；這個 Unit 會把按鈕背後的角色拆開，而不是教你記某一套 IDE 的按鈕位置。

你可能已經寫過程式，也已經習慣按 Run、Build 或 Debug。接下來我們先確認一件更重要的事：當你說「我把程式跑起來了」，中間其實經過了哪些不同步驟？

正式課程會一直使用 compiler、Build、Run、Debug、測試與錯誤訊息。如果這些詞在腦中全部混成同一件事，後面很多問題都會看起來比實際上更神祕。

所以先從一個熟悉的動作開始：

> 你按下 Run，這個整合開發環境到底替你安排了哪些工作？

---

## 1. 先把一個按鈕拆回幾個動作

假設你有：

```c
#include <stdio.h>

int main(void) {
    printf("Hello\n");
    return 0;
}
```

你在 IDE 中按下 Run，看到：

```text
Hello
```

介面上也許只需要一次點擊，但概念上至少要分開：

```text
source code
→ Build / compile-related work
→ executable
→ Run
→ running program
→ output
```

有些 IDE 的 Run 會先自動檢查是否需要 Build；有些工作流程則把 Build 和 Run 分成兩個明確動作。介面可以不同，但這幾個角色不能因此混在一起。

---

## 2. Source code 不是你最後執行的東西

原始碼可能存在：

```text
main.c
```

你真正執行的，則是 Build 後產生的 executable。

所以如果你修改：

```c
printf("Hello\n");
```

變成：

```c
printf("Goodbye\n");
```

但沒有更新 executable，就可能仍然看到舊結果。

這個現象可以用一句很有用的問題重新描述：

> 我現在看的 source，和我現在 run 的 executable，是不是同一輪 Build 的結果？

這比單純問「IDE 為什麼怪怪的」更容易找到問題。

---

## 3. Compiler 和 IDE 是不同角色

IDE 提供的是整合環境。

它可能包含：

```text
editor
build controls
terminal
run controls
debugger
project management
```

Compiler 則負責處理 C 原始碼的一部分建置工作。

所以比較好的模型是：

```text
IDE
  └─ 幫你呼叫與組織 compiler、debugger 與其他工具
```

而不是：

```text
IDE = compiler
```

這個差別在之後換 IDE、換機器、看 CI、處理 build error 時會很重要。

---

## 4. Build 成功，只回答了一部分問題

假設需求是：

```text
輸出 Hello
```

但程式是：

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye\n");
    return 0;
}
```

它仍然可能：

```text
Build succeeded
Run succeeded
```

可是需求沒有被滿足。

所以後面所有 Unit 都可以用這三層來檢查：

```text
1. 工具有沒有接受我的程式？
2. 程式有沒有真的執行到我觀察的位置？
3. 結果有沒有符合需求與我原先的推理？
```

這三層證據不同，不能互相代替。

---

## 5. 用一次「舊 executable」實驗確認自己真的理解

做下面這件事：

1. Build 一個輸出 `Version A` 的程式。
2. Run，確認看到 `Version A`。
3. 把 source 改成輸出 `Version B`。
4. 儲存，但刻意不要重新 Build。
5. 如果你的環境允許，直接執行前一個 executable。
6. 解釋為什麼它仍然可能顯示 `Version A`。
7. 重新 Build，再 Run。
8. 確認這次才變成 `Version B`。

真正重要的不是看到哪一行字，而是你能不能清楚指出：

```text
哪個檔案改了？
哪個檔案被執行？
哪一步讓兩者重新對應？
```

---

## 6. Run 和 Debug 的差別先抓住一件事就好

Run 是讓程式正常往前執行。

Debug 則讓你能在執行途中停下並觀察狀態。

例如：

```c
int a = 5;
int b = 2;
int result = a / b;
```

如果在 `result` 那一行附近設 breakpoint，debugger 可以讓你停下來看：

```text
a = 5
b = 2
```

以及執行前後 `result` 的狀態。

現在不需要把 debugger 的所有功能學完。正式課程 F-U11 會把 debugger 放進完整的測試、診斷與改善流程中。

目前只需要記得：

> Debugger 是用來觀察執行證據的工具，不是另一種神奇的 Run。

---

## 7. Build 裡其實還有更細的步驟，但現在不用一次學完

當程式只有一個 `.c` 檔時，Build 看起來很簡單。

等到程式拆成：

```text
main.c
student.c
student.h
```

你會開始看到 compile、object file、link 等更完整的建置流程。

這些內容會在 F-U10 模組化程式設計時正式處理。現在先保留：

```text
source files
→ Build
→ executable
```

並知道 Build 不是永遠只有一個不可再拆的動作。

---

## 8. 把 IDE 當成「可替換的介面」，不要當成課程本身

如果你今天使用 Visual Studio、VS Code、Code::Blocks、CLion 或其他開發環境，按鈕位置和設定方式都可能不同。

但是下面這些問題不會因 IDE 改變而消失：

- 我正在編輯哪一份 source？
- 哪個 compiler 在處理它？
- Build 成功了嗎？
- 我真正 run 的 executable 是哪一個？
- 我是在正常 Run，還是在 Debug？
- 我看到的 output 能不能支持我的判斷？

能回答這些問題，就比較不會被某一套介面的操作方式綁住。

---

## 9. 離開這個 Unit 前，確認你能解釋而不是只會操作

請不用 IDE 按鈕名稱回答：

- 程式、程式語言、程式設計三者的角色有什麼不同？
- Source file 和 executable 是什麼關係？
- Build 和 Run 為什麼不是同一件事？
- IDE 和 compiler 的角色有什麼不同？
- 修改 source 之後，為什麼可能仍然看到舊 output？
- Build succeeded 為什麼不能證明程式符合需求？
- Run 和 Debug 最重要的差別是什麼？
- 為什麼完整的 compile/link 細節現在可以先不背？

如果你只能說「因為我按這個按鈕」，回到前面的舊 executable 實驗，再用檔案與步驟說一次。

---

## 10. 下一個問題：工具都正常，結果還是可能讓你意外

到這裡，我們先把「程式設計」和「操作工具」分開，也把工具層拆清楚了：source、Build、compiler、executable、Run、Debug 各自有不同角色。

但就算你確定：

```text
Build 沒有失敗
Run 的也是最新 executable
```

程式結果仍然可能和直覺不同。

例如：

```c
int a = 5;
int b = 2;
double result = a / b;
```

為什麼 `result` 可能是 `2.0`，而不是 `2.5`？

這已經不是 IDE 或 Build 的問題了。

下一個 Unit 會開始追問：**表示方式、型別與運算規則，為什麼會改變結果？**

## 導覽

- [下一單元 F-U01：表示、型別與運算為什麼會影響結果？](unit-01-representation-types.zh-TW.md)
- [正式課程學生教材索引](README.zh-TW.md)
- [English version](unit-00-build-run-ide.en.md)
