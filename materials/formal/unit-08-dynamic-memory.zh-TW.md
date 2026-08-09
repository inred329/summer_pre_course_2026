# 正式單元 F-U08：程式如何在執行期間取得與釋放空間？

版本：1.2.0  
狀態：正式學生教材  
最後更新：2026-08-09  
對應英文版本：[Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?](unit-08-dynamic-memory.en.md)

F-U07 的學生資料可以先寫成：

```c
Student students[10];
```

這個設計很清楚，但它也把一個決定寫死了：最多 10 筆。

現在把需求改成：

> 程式啟動後才知道要保存幾筆資料，而且之後還可能增加。

這時真正改變的不是「我們要學一個比較進階的函式」，而是**空間的大小與生命週期開始由程式自己管理**。

程式要回答：需要多少空間？大小算得安全嗎？配置失敗怎麼辦？誰負責最後釋放？空間成長後舊指標還有效嗎？

這些問題合起來，就是動態配置與 ownership 的主線。

---

## 1. 固定陣列先告訴我們：什麼時候其實不需要動態配置

如果需求真的就是最多 100 個整數：

```c
int values[100];
```

那固定陣列通常更簡單。

動態配置適合的是「大小直到執行時才知道」的情況。例如已經取得元素數量 `count` 後：

```c
int *values = malloc(count * sizeof *values);
```

可以先畫成：

```text
values ─────► 動態配置的區塊
              count 個 int 的空間
```

這裡最重要的第一件事是：`malloc` 接受的是 **byte 數**，不是元素數量。

所以：

```c
count * sizeof *values
```

代表：

```text
元素數量 × 每個元素需要的 byte 數
```

如果 `count` 還沒有被驗證，就不應該急著做這個乘法。

---

## 2. 先驗證元素數量，再驗證 byte 大小

假設數量來自輸入：

```c
int n;

if (scanf("%d", &n) != 1 || n <= 0) {
    fprintf(stderr, "Invalid size\n");
    return 1;
}

size_t count = (size_t)n;
```

現在 `count` 是正數，但還有第二個問題：

> `count * sizeof *values` 能不能由 `size_t` 表示？

在乘法以前檢查：

```c
#include <stdint.h>

if (count > SIZE_MAX / sizeof *values) {
    fprintf(stderr, "Requested size is too large\n");
    return 1;
}
```

這和 F-U01 的邊界原則相同：**先證明運算結果可表示，再做運算。**

如果 byte 數先發生無號回繞，後面的 `malloc` 就算回傳非 `NULL`，也可能只得到一塊比程式以為的小得多的空間。

所以「元素數量合理」和「配置大小能安全算出來」是兩個不同檢查。

---

## 3. 第一次完整追蹤：配置、使用、釋放

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;

    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "Invalid size\n");
        return 1;
    }

    size_t count = (size_t)n;

    if (count > SIZE_MAX / sizeof(int)) {
        fprintf(stderr, "Requested size is too large\n");
        return 1;
    }

    int *values = malloc(count * sizeof *values);
    if (values == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }

    for (size_t i = 0; i < count; i++) {
        values[i] = (int)i;
    }

    free(values);
    values = NULL;
    return 0;
}
```

先不要背函式名稱，把生命週期讀成：

```text
取得元素數量
→ 驗證需求
→ 驗證 byte 大小
→ 配置
→ 檢查配置是否成功
→ 在容量內使用
→ 釋放
→ 停止使用那個配置物件
```

這裡至少有三種不同失敗：輸入不合法、大小算不安全、配置要求無法被滿足。它們不應該被混成同一種「malloc 出問題」。

---

## 4. `free` 結束配置物件的生命週期，不會自動修好所有指標

配置成功後：

```text
values ─────► [ allocation ]
```

執行：

```c
free(values);
```

之後，那個配置物件的生命週期已經結束，所以不能再：

```c
printf("%d\n", values[0]);
```

把 owner 變數設成：

```c
values = NULL;
```

可以避免自己之後又透過 `values` 誤用舊位置。

但如果之前還有另一個 alias：

```c
int *first = values;
```

那麼 `values = NULL` 不會神奇地把 `first` 也改成 `NULL`。

因此真正的規則是：

> 配置一旦被釋放，所有曾經指向它的路徑都必須停止把它當成活著的物件。

這正是 F-U05 的 lifetime 與 F-U06 的 dangling pointer 在動態配置中的版本。

---

## 5. Ownership 是「最後由誰負責 `free`？」

假設有函數：

```c
int *create_values(size_t count);
```

如果它成功配置新空間並回傳指標，介面就需要說清楚：

> 呼叫者是否從現在開始擁有這塊配置，並負責最後的 `free`？

**Ownership（所有權）不是 C 關鍵字。**它是一條設計規則，用來避免兩個相反錯誤：

```text
A 以為 B 會 free
B 以為 A 會 free
→ memory leak
```

以及：

```text
A 覺得自己要 free
B 也覺得自己要 free
→ double free
```

所以看到動態配置指標時，除了「它指到哪裡」，再多問一句：

> 誰負責讓這個生命週期正確結束？

---

## 6. `calloc` 只是另一種建立配置的方式

```c
int *values = calloc(count, sizeof *values);
```

和 `malloc` 相比，`calloc` 把元素數量與元素大小分成兩個參數，成功時還會把配置區塊的 bytes 清成零。

對本章的 `int` 陣列，這會得到初始值為 0 的元素。

但不要把它背成「`calloc` 會替所有型別做正確的預設初始化」。它直接保證的是配置 storage 並把 bytes 清零。

不論用 `malloc` 或 `calloc`，下面三件事都沒有消失：

- 輸入與大小仍要符合需求。
- 回傳值仍要檢查。
- ownership 與最後的釋放責任仍要清楚。

---

## 7. 容量成長時，先保住原 owner

假設目前：

```c
int *values;
size_t capacity;
```

現在需要改成 `new_capacity` 個元素。

先確認新大小可接受：

```c
if (new_capacity == 0 ||
    new_capacity > SIZE_MAX / sizeof *values) {
    return 0;
}
```

再使用 `realloc`：

```c
int *temporary = realloc(values,
                         new_capacity * sizeof *values);

if (temporary == NULL) {
    return 0;
}

values = temporary;
capacity = new_capacity;
```

為什麼不直接寫：

```c
values = realloc(values,
                 new_capacity * sizeof *values);
```

因為對非零大小而言，`realloc` 失敗時，原配置仍然存在。如果直接覆蓋唯一 owner，失敗後 `values` 會變成 `NULL`，程式卻失去找到原配置的最後一條路，形成 leak。

所以 temporary 的作用很簡單：

> 在新配置確定成功以前，不破壞舊配置的 owner。

---

## 8. `realloc` 成功也可能讓舊 alias 失效

成功的 `realloc` 可能原地調整，也可能搬到新的位置。

所以成功後必須以它回傳的新指標為準。

假設成長以前有：

```text
values ───► [ old allocation ]
first  ───► [ old allocation 的第一個元素 ]
```

如果 `realloc` 搬移：

```text
values ───► [ new allocation ]
first  ───► [ 舊位置，不能假設仍有效 ]
```

因此可成長容器比固定陣列多一個問題：

> 哪些指標是 owner？哪些只是暫時 alias，而且可能在成長後失效？

本課程把容量 0 當成明確的「清空」操作：直接 `free` 並更新 owner 狀態，不依賴 `realloc(pointer, 0)` 的特殊情況。

---

## 9. 常見錯誤其實都可以回到三個問題

### Memory leak

配置還活著，但最後一條負責釋放它的路徑失去了。

### Use after free

配置生命週期已結束，卻仍透過舊指標存取。

### Double free

同一個已經結束生命週期的配置又被交給 `free`。

### 配置太小

程式以為自己有 `count` 個元素，但真正配置的 byte 數不足，例如大小公式寫錯或乘法先發生回繞。

與其分開死背名稱，不如一直回到：

```text
這塊配置現在還活著嗎？
誰擁有它？
真正的容量足以支援下一次存取嗎？
```

---

## 10. 先做一個可成長整數清單

需求：

- 初始 `capacity = 4`。
- 使用者持續輸入整數。
- `-1` 表示結束。
- 當 `size == capacity` 時容量加倍。

整個過程維持：

```text
size <= capacity
```

成長以前先確認：

```c
if (capacity > SIZE_MAX / 2) {
    /* capacity * 2 無法安全表示 */
}

size_t new_capacity = capacity * 2;

if (new_capacity > SIZE_MAX / sizeof *values) {
    /* byte 大小無法安全表示 */
}
```

然後才透過 temporary 做 `realloc`。

只有成長成功後才更新 `values` 與 `capacity`。如果失敗，舊資料、舊 `size`、舊 `capacity` 都應保持可用。

這個「失敗時舊狀態仍然完整」的目標，下一節會變成函數介面的核心契約。

---

## 11. 為什麼 `append_value` 需要 `int **values`？

我們希望把 append 包成函數：

```c
int append_value(int **values,
                 size_t *size,
                 size_t *capacity,
                 int value);
```

第一次看到 `int **` 很容易像突然多了一層符號。先不要背它，回到 F-U06 的規則：

> 如果函數要修改呼叫者的一個物件，就把那個物件的位置交給函數。

這次函數想修改的物件，不是一個 `int`，而是呼叫者的 **owner pointer**：

```c
int *values;
```

`values` 本身是一個指標物件。它也有自己的位址：

```c
&values
```

而 `&values` 的型別就是 `int **`。

可以畫成：

```text
append_value 的參數 values
          │
          v
呼叫者的 owner pointer ─────► 動態配置
        int *
```

因此在 `append_value` 裡：

- `values`：指向呼叫者的 owner pointer。
- `*values`：就是呼叫者目前保存的那個 `int *` owner 值。
- 如果 `realloc` 回傳新位置，修改 `*values` 就能把新的 owner 指標交回呼叫者。

`size_t *size` 與 `size_t *capacity` 也是同一個理由：函數成功後要修改呼叫者的 metadata。

所以 `**` 不是另一套魔法；它只是「這次要修改的物件剛好本身是一個指標」。

---

## 12. Append 的重點不是 `realloc`，而是失敗時不要破壞舊狀態

先定義契約：

> 如果 `append_value` 回傳失敗，呼叫者原本的 `*values`、`*size`、`*capacity` 與所有既有元素都仍然有效且不變。

操作順序因此可以讀成：

```text
驗證參數與 size <= capacity
→ 還有空間：直接寫入
→ 需要成長：先安全算新 capacity 與 byte 數
→ temporary = realloc(...)
→ 失敗：原狀態不動
→ 成功：提交新的 owner/capacity
→ 寫入新值
→ 最後增加 size
```

下面是一個骨架：

```c
#include <stdint.h>
#include <stdlib.h>

int append_value(int **values,
                 size_t *size,
                 size_t *capacity,
                 int value) {
    if (values == NULL || size == NULL || capacity == NULL) {
        return 0;
    }

    if (*size > *capacity) {
        return 0;
    }

    if (*capacity > 0 && *values == NULL) {
        return 0;
    }

    if (*size == *capacity) {
        size_t new_capacity;

        if (*capacity == 0) {
            new_capacity = 4;
        } else {
            if (*capacity > SIZE_MAX / 2) {
                return 0;
            }
            new_capacity = *capacity * 2;
        }

        if (new_capacity > SIZE_MAX / sizeof **values) {
            return 0;
        }

        int *temporary = realloc(*values,
                                 new_capacity * sizeof **values);
        if (temporary == NULL) {
            return 0;
        }

        *values = temporary;
        *capacity = new_capacity;
    }

    (*values)[*size] = value;
    (*size)++;
    return 1;
}
```

閱讀這段程式時不要從 `**` 開始。先一路問：

> 哪一個狀態可能失敗？失敗以前哪些舊狀態必須保住？成功後哪些資料才可以一起更新？

這會比背一套 `realloc` 模板更容易移植到其他問題。

---

## 13. 選做：讓 AI 挑戰你的 ownership 圖

這一節完全可以跳過。

先自己畫四個時刻：

```text
配置前
配置後
realloc 成功搬移後
free 後
```

每一張圖都標出 owner、alias 與仍然活著的配置物件。

如果你想多做一次檢查，可以讓 AI 指出哪個轉換最容易產生 leak、dangling alias 或 double free。你不需要固定 Prompt，也不需要保存或繳交對話。

如果它的說法和 `malloc`／`realloc`／`free` 契約、你的配置圖或記憶體檢查工具衝突，就回到可驗證證據重新判斷。

---

## 14. 離開這個 Unit 前，確認你能追蹤整個生命週期

直接回答：

- 為什麼元素數量合法，仍要另外檢查 byte 大小乘法？
- `malloc` 回傳 `NULL` 和大小計算溢位為什麼是不同問題？
- `free(values)` 之後，為什麼其他 alias 不會因 `values = NULL` 自動變安全？
- ownership 主要避免哪兩個相反錯誤？
- 為什麼 `realloc` 通常先存進 temporary？
- `realloc` 成功搬移後，舊 alias 有什麼風險？
- 為什麼修改呼叫者的 `int *values` 需要把 `&values` 傳入 `int **` 參數？
- `append_value` 的「失敗時原狀態不變」為什麼讓呼叫端更容易推理？

如果某題只剩函式名稱或星號數量，重新畫 owner pointer、它自己的位址與配置物件，再走一次生命週期。

---

## 15. 本章收尾

F-U07 讓我們把一筆資料組成 `Student`；F-U08 再讓「要保存幾筆」不必在寫程式時就固定。

代價是責任也跟著增加：**配置以前要安全算大小，配置後要知道誰擁有，成長時要保住舊狀態，釋放後所有路徑都必須停止使用。**

而 `int **` 只是這條主線自然多出的一層：當函數需要修改的「呼叫者物件」本身就是一個指標時，我們就把那個指標物件的位置交給函數。

下一個 Unit 會處理另一種「超過目前執行生命週期」的需求。動態記憶體只能活在程式這次執行期間；如果資料希望程式結束後仍存在，就必須寫到檔案，並面對開啟、讀寫、格式、失敗與部分更新的問題。

## 導覽

- [上一單元：結構](unit-07-structures.zh-TW.md)
- [下一單元：檔案](unit-09-files.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-08-dynamic-memory.en.md)