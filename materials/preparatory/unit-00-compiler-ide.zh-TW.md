# 前導單元 P-U00：寫好的 C 程式，怎麼真的跑起來？

版本：1.0.0  
狀態：學生教材  
最後更新：2026-08-09  
對應英文版本：[Preparatory Unit P-U00: How Does the C Code You Write Actually Start Running?](unit-00-compiler-ide.en.md)

你可能已經看過別人按下 IDE 裡的綠色三角形，程式就出現結果。也可能第一次打開開發環境時，畫面上同時有編輯器、終端機、Build、Run、Debug，一時不知道哪些東西其實在做不同的工作。

在開始學 C 語法以前，我們先把這件事弄清楚。

這個 Unit 不要求你背工具名稱或按鈕位置。真正要建立的是一條之後會一直用到的路徑：

```text
你寫的 C 原始碼
→ compiler 讀取原始碼
→ 產生可以執行的程式
→ 作業系統啟動它
→ 程式執行並產生可觀察結果
```

IDE 會讓這些步驟操作起來比較方便，但 IDE 本身不是這整條流程的同義詞。

---

## 1. 先從一個普通文字檔開始

建立一個檔案，名稱叫做：

```text
hello.c
```

內容是：

```c
#include <stdio.h>

int main(void) {
    printf("Hello, C!\n");
    return 0;
}
```

現在先不要急著按 Run。

這個 `hello.c` 此刻是一份 **source file（原始檔）**。裡面的內容是 **source code（原始碼）**。

你可以打開它、閱讀它、修改它，但光是儲存這份文字，不代表電腦已經開始執行裡面的 C 程式。

這是第一個要分清楚的事情：

```text
我把程式碼寫進檔案
```

和

```text
電腦正在執行這支程式
```

不是同一件事。

---

## 2. Compiler 做的是什麼？

C 原始碼是寫給人類與 C 工具理解的文字。要真正執行，必須先經過編譯工具處理。

如果你的環境使用 GCC，可以在終端機輸入：

```text
gcc hello.c -o hello
```

不同作業系統、compiler 或課堂環境的指令可能不同；如果老師指定其他指令，就使用老師提供的版本。現在重要的不是背 `gcc`，而是觀察這個動作的角色。

成功之後，目錄裡會多出一個可以執行的結果。在不同系統上，它可能叫做 `hello`、`hello.exe`，或由開發環境放在某個 build 目錄中。

可以先把流程想成：

```text
hello.c
  │
  │ compiler
  ▼
executable
```

這個過程叫做 **compile（編譯）**。

如果原始碼不符合 compiler 能接受的 C 規則，例如少了一個分號，compiler 可能就不會成功產生新的 executable。

---

## 3. Compile 和 Run 是兩件不同的事

現在才執行剛剛產生的程式。

在某些終端機環境中可能是：

```text
./hello
```

在 Windows 環境中則可能執行：

```text
hello.exe
```

你會看到：

```text
Hello, C!
```

剛才其實做了兩件事情：

```text
Compile
hello.c → executable

Run
executable → running program → output
```

所以：

- Compile 是把原始碼轉成可以執行的結果。
- Run 是啟動已經存在的 executable。

之後看到 Build、Run、Debug 等按鈕時，不要先把它們全部理解成「讓程式跑」。先問：**現在到底正在做哪一個階段？**

---

## 4. 一個很重要的小實驗：改了原始碼，但先不要重新編譯

把原始碼改成：

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye, C!\n");
    return 0;
}
```

儲存 `hello.c`。

現在先不要重新 compile，直接執行剛才那個 executable。

先預測會看到：

```text
Hello, C!
```

還是：

```text
Goodbye, C!
```

如果你執行的仍然是上一輪編譯出的 executable，就會看到舊的結果：

```text
Hello, C!
```

原因不是電腦「沒有看到你存檔」，而是：

```text
你改的是 hello.c
但你執行的是先前產生的 executable
```

兩者不是同一個檔案。

現在重新 compile，再執行一次，才會看到：

```text
Goodbye, C!
```

這個實驗之後會非常有用。當你遇到「明明改了程式，結果怎麼沒變」時，可以先問：

> 我真的重新 build／compile 了嗎？我現在執行的是最新產生的 executable 嗎？

---

## 5. 那 IDE 到底是什麼？

IDE 是 **Integrated Development Environment（整合式開發環境）**。

它通常把很多開發時常用的功能放在同一個介面裡，例如：

```text
IDE
├─ editor：編輯原始碼
├─ build integration：呼叫 compiler 與相關工具
├─ run：啟動程式
├─ terminal：直接輸入指令
└─ debugger：暫停並觀察程式執行
```

不同 IDE 的畫面與按鈕位置會不同，但這些角色比按鈕長什麼樣子更重要。

所以不要把：

```text
IDE = compiler
```

當成同一件事。

比較準確的理解是：

> IDE 幫你把編輯、建置、執行、除錯與其他開發工作整合在一起；真正進行 C 編譯的仍然是 compiler 與其相關工具。

這也是為什麼有些編輯器可以打開 `.c` 檔，卻不代表電腦已經具備可用的 C compiler。

---

## 6. Build 和 Compile 為什麼有時看起來不完全一樣？

在只有一個很小的 `hello.c` 時，可以先把 Build 理解成「讓目前的原始碼變成最新可執行結果所需要的工作」。

對非常小的程式來說，你看到的主要工作通常就是編譯。

但是以後程式變大、拆成多個檔案之後，一次 Build 可能會包含不只單一編譯動作。正式課程後面的模組化 Unit 會再把 compile 與 link 拆開來看。

現在只需要保留這個模型：

```text
Edit source
→ Build
→ 得到最新可執行結果
→ Run
```

不要急著把後面所有建置細節一次背完。

---

## 7. Run 和 Debug 也不是同一件事

Run 的目標通常是直接執行程式。

Debug 模式則讓你有機會在程式執行途中停下來觀察。

例如 IDE 常提供 **breakpoint（中斷點）**。你可以在某一行設下 breakpoint，讓程式執行到那裡先暫停。

假設之後有這樣的程式：

```c
int a = 5;
int b = 2;
int sum = a + b;
```

Debugger 可以讓你在某一行停下來，看當時的 `a`、`b`、`sum` 是多少。

現在不需要學會所有 debugger 功能，只需要知道：

```text
Run：直接讓程式往前執行
Debug：讓你在執行途中停下、一步一步走、觀察狀態
```

後面的課程會再把 debugger 放進真正的測試與除錯流程中。

---

## 8. 不要把「成功 Build」當成「程式一定正確」

看這支程式：

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye, C!\n");
    return 0;
}
```

它可能成功 compile，也能成功 run。

但如果需求是：

```text
輸出 Hello, C!
```

它仍然做錯了事情。

因此之後我們會一直區分：

```text
原始碼能不能被 compiler 接受？
↓
程式能不能被啟動並執行？
↓
實際結果有沒有符合需求？
```

這三題不能互相取代。

---

## 9. 試著自己走一次完整流程

建立：

```text
intro.c
```

讓它輸出兩行：

```text
My name is <你的英文名字>.
I am learning C.
```

這次不要只按一個按鈕就結束。每一步都試著說出自己現在在做什麼：

1. 我正在編輯哪一個 source file？
2. 我什麼時候儲存了它？
3. 我什麼時候 build／compile？
4. Build 成功後產生或更新了什麼？
5. 我真正 run 的是哪一個程式？
6. Output 是否符合我原本預期？

如果使用 IDE，也試著找出 editor、terminal、Build、Run、Debug 分別在哪裡。

---

## 10. 離開這個 Unit 前，確認你能從實際操作回答

不要背定義，直接從剛才的 `hello.c` 回答：

- `hello.c` 和 executable 是同一個檔案嗎？
- 修改 `hello.c` 後，為什麼舊 executable 不會自動改變？
- Compile 和 Run 各自在做什麼？
- IDE 和 compiler 為什麼不能直接畫上等號？
- Build 成功為什麼不能證明結果符合需求？
- Run 和 Debug 的目的有什麼不同？
- 如果你改了原始碼，但執行結果仍然是舊的，第一批應該檢查什麼？

如果其中一題只能背一句話，就回到實際檔案再做一次「修改但不重新編譯」的小實驗。

---

## 11. 接下來：開始讀真正執行中的程式

現在我們已經知道一支 C 程式不是「寫完文字、按一個神奇按鈕」就完成了。

你有 source file；compiler 會處理它；Build 會產生最新可執行結果；Run 才真正啟動程式；IDE 則把這些工作整合在一起。

下一個 Unit 不再把重點放在工具，而會開始追蹤：**當程式真的執行時，`main` 裡的敘述怎麼一步一步變成我們看到的結果？**

## 導覽

- [下一單元 P-U01：程式如何從文字變成執行結果？](unit-01-execution.zh-TW.md)
- [前導課程學生教材索引](../README.zh-TW.md)
- [English version](unit-00-compiler-ide.en.md)
