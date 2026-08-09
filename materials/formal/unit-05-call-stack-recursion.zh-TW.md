# 正式單元 F-U05：函數呼叫如何建立新的執行環境？

版本：1.1.0  
狀態：正式學生教材  
最後更新：2026-08-09  
對應英文版本：[Formal Unit F-U05: How Does a Function Call Create a New Execution Environment?](unit-05-call-stack-recursion.en.md)

前幾個 Unit 已經呼叫過很多函數：`sum_array`、`max_array`、`strlen`、`strcmp`……

我們一直把函數看成「給它資料，它做完工作再回傳」。現在要把鏡頭移到函數裡面：

> 當 `main` 呼叫另一個函數時，呼叫者還沒做完的工作放在哪裡？被呼叫函數的參數與區域變數又怎麼和呼叫者分開？如果函數又呼叫另一個函數，甚至呼叫自己，這些狀態如何不互相混在一起？

這個 Unit 會使用 **call frame** 與 **call stack** 當作追蹤模型。許多實作確實以執行期堆疊保存函數呼叫狀態，但 C 語言標準本身不要求某個固定的實體 stack 配置。因此這裡的圖是幫助推理的模型，不是要求你背某一台機器的記憶體版面。

---

## 1. 一次函數呼叫，至少有一組屬於「這一次」的狀態

先看熟悉的小函數：

```c
int square(int x) {
    int result = x * x;
    return result;
}
```

假設 `main` 執行：

```c
int a = square(5);
```

為了讓這次呼叫能完成，我們至少要能追蹤：

- 這一次的參數 `x` 是 5。
- 這一次的區域變數 `result` 會得到 25。
- `square` 完成後，要回到 `main` 中原本等待結果的位置。

把這一組「屬於某一次呼叫的執行狀態」想成一個 **call frame（呼叫框架）**。

如果之後又執行：

```c
int b = square(8);
```

新的呼叫有自己的 `x` 與 `result`。前一次呼叫的區域狀態不會被拿來當成這一次的區域狀態。

---

## 2. 一個函數呼叫另一個函數時，未完成的工作會形成層次

看：

```c
int double_value(int x) {
    return x * 2;
}

int add_one_then_double(int x) {
    return double_value(x + 1);
}
```

呼叫：

```c
add_one_then_double(4)
```

可以追蹤成：

```text
main
└─ add_one_then_double(4)
   └─ double_value(5)
```

最裡面的 `double_value(5)` 先完成並回傳 10，接著 `add_one_then_double` 才能完成，再回到 `main`。

如果用「call stack」模型表示：

```text
目前最上層：double_value frame
             add_one_then_double frame
             main frame
```

回傳時，最上層那次呼叫先結束，控制權回到等待它的那一層。

這種「最後呼叫、最先完成」的順序，正是理解遞迴時最重要的準備。

---

## 3. 作用域和生命週期不是同一件事

看：

```c
int function(void) {
    int local = 10;
    return local;
}
```

`local` 有兩個不同問題：

### 這個名稱在哪裡能寫？

這是 **作用域（scope）** 的問題。`local` 這個名稱只在它所屬的區塊範圍內可直接使用。

### 這個物件在執行時存在多久？

這是 **生命週期（lifetime）** 的問題。一般自動區域物件在這次區塊執行期間存在；這次呼叫結束後，該次呼叫的 `local` 也結束生命週期。

這兩個概念之後會直接影響指標安全：就算你曾經知道某個物件的位置，也不能在物件生命週期結束後繼續把它當成仍存在的資料。

F-U06 會正式處理這件事；現在先把「名稱可見範圍」和「物件存在時間」分開。

---

## 4. 遞迴只是「函數呼叫自己」，但每一次仍是不同呼叫

先用最小的倒數：

```c
void countdown(int n) {
    if (n == 0) {
        printf("Go!\n");
        return;
    }

    printf("%d\n", n);
    countdown(n - 1);
}
```

呼叫：

```c
countdown(3);
```

追蹤：

```text
countdown(3)
└─ countdown(2)
   └─ countdown(1)
      └─ countdown(0)
         └─ print Go! and return
```

每一層都有自己的參數 `n`：3、2、1、0。

這裡有兩個角色：

- `n == 0`：**base case**，直接結束，不再呼叫自己。
- `countdown(n - 1)`：**recursive case**，把問題改小後再呼叫自己。

只寫出 base case 還不夠。recursive case 還必須真的讓狀態靠近它。

---

## 5. 「有 base case」和「一定會到 base case」是兩件事

例如：

```c
void broken(int n) {
    if (n == 0) {
        return;
    }

    broken(n + 1);
}
```

`n == 0` 的 base case 明明存在，但若從 `broken(3)` 開始，狀態會變成 4、5、6……反而愈來愈遠。

因此判斷遞迴是否可靠時，不只要問：

> Base case 在哪裡？

還要問：

> 每一次 recursive case 是否真的讓問題朝 base case 前進？

如果呼叫無限制地繼續增加，實作必須持續保存更多呼叫狀態，最終可能耗盡可用的執行資源；常見實作會表現成 stack exhaustion／stack overflow。重點不是某個固定 stack 大小，而是：**沒有終止的呼叫鏈需要無限資源，而真實程式沒有無限資源。**

---

## 6. 階乘讓我們同時看見「往下呼叫」與「回來完成工作」

數學上：

```text
4! = 4 × 3 × 2 × 1
```

先寫最直接的遞迴版本：

```c
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }

    return (unsigned long long)n * factorial(n - 1);
}
```

對 `factorial(4)`，往下呼叫時：

```text
factorial(4)
└─ factorial(3)
   └─ factorial(2)
      └─ factorial(1)
```

到 base case 後才開始回來：

```text
factorial(1) = 1
factorial(2) = 2 × 1 = 2
factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
```

所以每一層不只保存自己的 `n`，還保存「等下面那層回來後，我還要乘上自己的 `n`」這件未完成工作。

---

## 7. 能終止，不代表結果一定能放進型別

前面的 `factorial` 還有兩個問題：

1. 負數不是我們這裡定義的有效階乘輸入。
2. 即使遞迴正常終止，數學結果仍可能大到超過 `unsigned long long`。

我們可以利用 F-U02 已學過的 sentinel 思想，設計一個不需要輸出指標的檢查版本：

> 對有效可表示的階乘，結果一定大於 0，所以把回傳值 0 保留成「失敗」訊號。

```c
#include <limits.h>

unsigned long long factorial_checked(int n) {
    if (n < 0) {
        return 0;
    }

    if (n == 0 || n == 1) {
        return 1;
    }

    unsigned long long smaller = factorial_checked(n - 1);
    if (smaller == 0) {
        return 0;
    }

    if (smaller > ULLONG_MAX / (unsigned long long)n) {
        return 0;
    }

    return (unsigned long long)n * smaller;
}
```

這裡把三個問題分開：

- **終止問題**：`n` 是否每次都往 0／1 靠近？
- **輸入問題**：`n < 0` 是否被拒絕？
- **表示範圍問題**：乘法以前是否先確認結果能由 `unsigned long long` 表示？

如果回傳 0，呼叫者知道這不是合法階乘結果，而是「這個介面無法給出有效結果」。

這個 sentinel 設計能成立，是因為數學階乘的合法結果不會是 0。若某個問題本身可能合法回傳 0，就不能隨便把 0 拿來當失敗訊號。

---

## 8. 不要把「遞迴錯誤」全部叫做 stack overflow

幾個例子看起來都可能讓結果失敗，但原因不同。

### 沒有 base case

```c
int countdown(int n) {
    return countdown(n - 1);
}
```

沒有終止分支，呼叫鏈會持續增加，最終可能耗盡執行資源。

### 有 base case，但方向錯

```c
return factorial_checked(n + 1);
```

終止條件存在，卻永遠朝錯方向走。這是邏輯／終止缺陷。

### 負數被錯誤接受

若寫：

```c
if (n <= 1) {
    return 1;
}
```

那 `factorial(-5)` 也會立刻回傳 1。它「會終止」，但違反我們定義的輸入規格。

### 結果超過型別

遞迴路徑完全正確也可能遇到太大的階乘結果。這是表示範圍問題，不是 base case 問題。

所以看到遞迴失敗時，先分類：**沒有終止？方向錯？輸入無效？還是結果範圍不夠？**

---

## 9. 用字串再做一次遞迴，但不提前引入指標運算

F-U04 已經知道字串會在 `\0` 結束。

我們可以用索引寫一個遞迴長度函數：

```c
#include <stddef.h>

size_t recursive_length_at(const char text[], size_t index) {
    if (text[index] == '\0') {
        return 0;
    }

    return 1 + recursive_length_at(text, index + 1);
}
```

呼叫：

```c
size_t length = recursive_length_at("cat", 0);
```

追蹤：

```text
index 0: 'c' → 1 + recursive_length_at(text, 1)
index 1: 'a' → 1 + recursive_length_at(text, 2)
index 2: 't' → 1 + recursive_length_at(text, 3)
index 3: '\0' → 0
回來得到 1 → 2 → 3
```

這個範例仍假設 `text` 是一個有效、可終止的 C 字串。字串參數與指標的完整關係會在下一個 Unit 建立。

---

## 10. 迭代和遞迴：保存狀態的位置不同

手動算字串長度可以寫成迴圈：

```c
size_t length = 0;
while (text[length] != '\0') {
    length++;
}
```

也可以寫成前面的遞迴函數。

兩者都需要保存「現在處理到哪裡」：

- 迭代版把進度明確放在 `length`。
- 遞迴版讓每一次函數呼叫保存自己的 `index`，並等待下一層回來。

遞迴不是「比較高級的迴圈」。選擇哪一種表達方式，要看問題結構、可讀性、資源需求與可驗證性。

---

## 11. 自主練習：`sum_to_n`

建立一個遞迴函數，計算：

```text
1 + 2 + ... + n
```

先不要寫程式，先定義：

- 哪些 `n` 是有效輸入？
- base case 是什麼？
- recursive case 如何確定接近 base case？
- 結果用什麼型別表示？
- 最大允許輸入要怎麼避免超出型別範圍？

如果你選擇用 0 作為失敗 sentinel，先證明所有合法結果都不會是 0；否則就要改用其他介面設計。

至少測試：最小合法輸入、小值、你允許的最大值、超出範圍值與負數。

---

## 12. 修改需求：限制遞迴深度與允許輸入

假設原本允許任何「結果能表示」的 `n`，現在規格另外要求：

> 為了控制遞迴資源，最多只允許到某個明確上限 `MAX_N`。

這會讓你重新區分兩種限制：

- **數學／型別限制**：結果能不能表示？
- **資源／規格限制**：即使結果能表示，我們是否仍選擇限制呼叫深度？

更新輸入檢查與測試，但不要因此把 base case 邏輯改亂。

---

## 13. 選做：讓 AI 挑戰你的遞迴追蹤

這一節完全可以跳過。

先不用任何工具，自己回答：

> 為什麼「有 base case」仍不保證遞迴一定終止？為什麼「一定終止」又不保證輸入有效或結果可表示？

如果你想多做一次檢查，可以把自己的解釋交給 AI，請它設計一個「會終止但結果錯」和一個「有 base case 但走不到」的反例。你不需要固定 Prompt，也不需要保存或繳交對話。

如果 AI 的說法和呼叫追蹤、型別上限或可重現結果衝突，就回到這些證據重新判斷。

---

## 14. 離開這個 Unit 前，確認你能追蹤「哪一次呼叫」

回到本章程式，直接回答：

- 為什麼兩次 `square(...)` 呼叫各自有自己的參數與區域狀態？
- 作用域和生命週期分別回答什麼問題？
- 為什麼 call stack／call frame 在這裡是追蹤模型，而不是 C 標準保證的固定實體配置？
- `countdown(3)` 的每一層 `n` 分別是多少？
- 有 base case 但 recursive case 朝錯方向時，為什麼仍可能不終止？
- `factorial_checked` 為什麼能把 0 保留成失敗 sentinel？
- 為什麼溢位檢查要在乘法發生以前完成？
- 迭代版字串長度和遞迴版分別把「目前位置」保存在哪裡？

如果某一題只能背名詞，就畫出每一次呼叫的參數、等待中的工作與回傳順序。

---

## 15. 本章收尾

這個 Unit 把函數從「黑盒子」打開了一點：每一次呼叫都有屬於那一次的參數、區域狀態與尚未完成工作；巢狀呼叫會形成等待關係，遞迴則讓同一個函數同時存在很多次不同的呼叫狀態。

可靠遞迴至少要分開處理三件事：**能不能走到 base case、輸入是否符合介面、結果是否能由型別表示。**資源限制又是另一層問題。

下一個 Unit 會正式回答前面一直刻意延後的問題：當我們把陣列交給函數、把資料位置傳給 `scanf`，或想讓函數修改呼叫者的資料時，「位置」在 C 裡到底怎麼表示？這就是位址與指標模型。

## 導覽

- [上一單元：字串](unit-04-strings.zh-TW.md)
- [下一單元：指標](unit-06-pointers.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-05-call-stack-recursion.en.md)
