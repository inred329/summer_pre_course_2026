# 前導單元 P-U01：程式開始執行後，敘述怎麼變成結果？

版本：1.2.0  
狀態：學生教材  
最後更新：2026-08-09  
對應英文版本：[Preparatory Unit P-U01: Once a Program Starts Running, How Do Statements Become Results?](unit-01-execution.en.md)

P-U00 已經把工具層拆開了：source file、Build、compiler、executable、Run 和 IDE 各自有不同角色。

這個 Unit 從下一個問題開始：

> **假設我們已經 Build 成功，而且 Run 的也是最新 executable。程式真正開始執行後，裡面的敘述怎麼一步一步變成我們看到的結果？**

我們仍然用一支很小的程式，但這一次不再重學 compiler 或 Build，而是把注意力放到「執行順序、預測、觀察與解釋」。

---

## 1. 先不要執行，從程式文字預測結果

看看：

```c
#include <stdio.h>

int main(void) {
    printf("First\n");
    printf("Second\n");
    return 0;
}
```

先回答三個問題：

1. 哪一行文字會先出現？
2. `Second` 會不會出現在 `First` 前面？
3. `return 0;` 之後，還有本程式中的敘述要執行嗎？

先寫下預測，再 Build 與 Run。

你應該看到：

```text
First
Second
```

這次最重要的不是「成功跑出兩行」，而是你能不能從程式文字提前說出執行順序。

---

## 2. `main` 是我們追蹤執行的起點

在目前這些最小程式裡，可以先把：

```c
int main(void) {
    ...
}
```

理解成程式開始執行後，主要工作從這裡進入。

更完整的函數概念會在 P-U04 再處理。現在只需要知道：當這支程式被啟動後，我們可以從 `main` 裡第一個會執行的敘述開始往下追。

例如：

```c
int main(void) {
    printf("A\n");
    printf("B\n");
    printf("C\n");
    return 0;
}
```

目前可以先用最直接的方式讀：

```text
進入 main
→ 執行第一個 printf
→ 執行第二個 printf
→ 執行第三個 printf
→ 執行 return 0
→ main 結束
```

後面學到條件與迴圈後，執行順序就不一定只是一路往下；但先把最基本的順序執行讀熟，之後才有東西可以比較。

---

## 3. `printf` 做的是一個可觀察的動作

這一行：

```c
printf("Hello, C!\n");
```

要求程式把文字送到標準輸出。

其中：

```text
\n
```

代表換行。

所以：

```c
printf("Hello, ");
printf("C!\n");
```

通常會看到：

```text
Hello, C!
```

而：

```c
printf("Hello,\n");
printf("C!\n");
```

則會看到：

```text
Hello,
C!
```

在 Run 以前先預測這兩種結果，再實際比較。這會是這門課反覆使用的習慣：

```text
先讀程式
→ 建立預期
→ 執行
→ 比較實際結果
```

---

## 4. 把執行過程寫成 trace

對下面這支程式：

```c
#include <stdio.h>

int main(void) {
    printf("One\n");
    printf("Two\n");
    return 0;
}
```

可以用一個很簡單的 trace 表來記錄：

| 順序 | 正要執行的敘述 | 執行後可觀察到什麼 |
|---:|---|---|
| 1 | `printf("One\n");` | 出現 `One` |
| 2 | `printf("Two\n");` | 再出現 `Two` |
| 3 | `return 0;` | `main` 結束 |

Trace 的目的不是抄程式，而是把「哪一步先發生、那一步改變了什麼」說清楚。

到 P-U02 開始有變數之後，trace 會變得更重要，因為除了 output，我們還會追蹤資料與狀態。

---

## 5. `return 0;` 先理解成「這個 main 到這裡結束」

目前看到：

```c
return 0;
```

先不用深入函數回傳值的完整規則。

在這些小程式裡，可以先讀成：

> `main` 在這裡結束，程式正常完成這次執行。

因此：

```c
int main(void) {
    printf("Before\n");
    return 0;
    printf("After\n");
}
```

不要只看有幾個 `printf` 就猜兩行都會出現。先根據執行順序想：當 `return 0;` 執行後，`main` 已經結束，後面的 `printf` 不會成為這次正常執行路徑的一部分。

這裡的重點不是鼓勵你寫 unreachable code，而是開始建立「程式文字存在」和「這次執行真的走到那裡」是兩回事。

---

## 6. Compile error 和 execution behavior 要分開

P-U00 已經知道 Build 和 Run 不同。現在把這個差別拿來讀一個錯誤。

假設少了一個分號：

```c
#include <stdio.h>

int main(void) {
    printf("Hello\n")
    return 0;
}
```

先問：

> 這次新的程式有沒有真的開始執行 `main`？

如果 Build 因語法問題失敗，就沒有進入這次新版本的正常執行流程。

因此看到錯誤時，先分類會比亂改有效：

```text
Build 階段就失敗？
還是程式已經 Run，結果卻和預期不同？
```

如果 compiler 指向某一行，也把它當成診斷線索，不要自動假設真正原因一定就在那個字元。上一行缺少符號時，工具有時要讀到下一行才知道前面無法繼續解析。

---

## 7. 能執行，不代表符合需求

假設需求是：

```text
輸出 Hello, C!
```

但程式是：

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye, C!\n");
    return 0;
}
```

這支程式可以 Build，也可以 Run，而且執行流程很清楚。

但它仍然不符合需求。

因此之後看到「程式會跑」時，至少要分開問：

```text
工具有沒有成功建立它？
↓
這次執行實際走了哪些敘述？
↓
觀察到的結果是否符合需求？
```

P-U00 建立了第一層工具判斷；這個 Unit 開始把第二層的 execution trace 和第三層的 requirement comparison 接上去。

---

## 8. 動手改：先預測，再修改

把這支程式：

```c
#include <stdio.h>

int main(void) {
    printf("Hello, C!\n");
    return 0;
}
```

改成輸出：

```text
Hello, <你的英文名字>!
Welcome to C.
```

先不要立刻寫 code。依序做：

1. 先寫下完整預期輸出。
2. 想清楚需要幾個 `printf`。
3. 決定每個 `\n` 要放在哪裡。
4. 再修改程式。
5. Build、Run。
6. 比較預測與實際結果。

如果結果不同，不要先整支重寫。先沿著 `main` 的執行順序找「第一個和預期不同的地方」。

---

## 9. 做一個只改順序的小實驗

先看：

```c
printf("A\n");
printf("B\n");
printf("C\n");
```

預測 output。

接著只交換第一行和第三行：

```c
printf("C\n");
printf("B\n");
printf("A\n");
```

再預測一次。

這個實驗很小，但它建立一個之後會一直用到的觀念：

> 程式結果不只由「有哪些敘述」決定，也由「這次執行以什麼順序走過它們」決定。

P-U03 加入條件與迴圈後，這個問題會變得更有意思。

---

## 10. 選做：讓 AI 挑戰你的 execution trace

這一節完全可以跳過。

先不用任何工具，自己解釋：

```c
printf("A\n");
printf("B\n");
return 0;
```

為什麼會依序看到 `A`、`B`，然後程式結束？

如果你想多做一次檢查，可以把自己的 trace 交給 AI，請它指出哪一步說得不清楚。你不需要固定 Prompt，也不需要保存或繳交對話。

如果 AI 的說法和你可以實際重現的執行結果衝突，就回到程式與 trace 重新判斷。

---

## 11. 離開這個 Unit 前，確認你真的會追

請找一支本章的程式，不要背教材句子，直接回答：

- 程式開始執行後，我們從哪裡開始追？
- 連續幾個 `printf` 在目前這種程式裡會以什麼順序執行？
- `\n` 改變的是什麼？
- `return 0;` 執行後，這個 `main` 發生什麼事？
- Build 失敗和「程式已經 Run 但結果不對」為什麼要分開？
- 「程式會跑」為什麼仍然不能證明符合需求？
- 你能不能在 Run 前先寫出 output，再用實際結果驗證？

如果答案不確定，就挑兩三行 `printf`，自己換順序、加減 `\n`，再做一次 prediction → Run → compare。

---

## 12. 本章收尾：下一步開始讓程式記住東西

P-U00 先讓我們知道怎麼把 source 變成真正被執行的程式；P-U01 則把注意力放到程式開始執行之後：從 `main` 進入、依序執行敘述、產生 output，並用 prediction 和 trace 解釋結果。

到目前為止，這些程式幾乎只是在「做完一件事，再做下一件事」。

下一個 Unit 會加入一個新的問題：

> **如果程式需要記住一個值，之後再使用或改變它，這個值要放在哪裡？**

這就會帶我們進入資料、型別、變數與程式狀態。

## 導覽

- [上一單元 P-U00：寫好的 C 程式，怎麼真的跑起來？](unit-00-compiler-ide.zh-TW.md)
- [下一單元 P-U02：程式如何記住資料並改變狀態？](unit-02-data-state.zh-TW.md)
- [前導課程學生教材索引](../README.zh-TW.md)
- [English version](unit-01-execution.en.md)
