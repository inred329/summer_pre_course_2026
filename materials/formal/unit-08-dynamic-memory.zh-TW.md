# 正式單元 F-U08：程式如何在執行期間取得與釋放空間？

版本：1.1.0  
狀態：正式學生教材  
最後更新：2026-08-09  
對應英文版本：[Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?](unit-08-dynamic-memory.en.md)

F-U07 的 `Student students[10]` 有一個很明確的假設：最多就是 10 筆。

但如果需求變成：

> 程式啟動後才由使用者告訴我們要保存幾筆資料，而且之後還可能增加呢？

這時固定陣列不一定適合。程式需要在**執行期間**取得一塊大小合適的儲存空間，使用完後再明確交還。

這就是動態配置。

動態記憶體不是「比較進階所以比較好」。它只是把原本由語言與作用域幫我們處理的一部分工作，交給程式自己負責：大小計算、配置失敗、誰擁有這塊空間、何時釋放，以及釋放後誰都不能再使用。

---

## 1. 從「使用者決定元素數量」開始

固定版本：

```c
int values[100];
```

如果 `100` 是需求的一部分，這很簡單也很好。

如果元素數量直到執行時才知道，就可以先取得數量，再配置：

```c
int *values = malloc(count * sizeof *values);
```

概念圖：

```text
values ─────► 動態配置的區塊
              count 個 int 的空間
```

`malloc` 的參數不是「元素數量」，而是 **byte 數**。

因此 `count * sizeof *values` 的意思是：

```text
元素數量 × 每個元素需要的 byte 數
```

---

## 2. 配置以前，先確認「我要幾格」和「總 byte 數」都合理

假設元素數量來自輸入：

```c
int n;

if (scanf("%d", &n) != 1) {
    fprintf(stderr, "Invalid input\n");
    return 1;
}

if (n <= 0) {
    fprintf(stderr, "Size must be positive\n");
    return 1;
}
```

先處理輸入，再轉成 `size_t`：

```c
size_t count = (size_t)n;
```

接著不能直接假設：

```c
count * sizeof(int)
```

一定能由 `size_t` 表示。

在乘法發生以前檢查：

```c
#include <stdint.h>

if (count > SIZE_MAX / sizeof(int)) {
    fprintf(stderr, "Requested size is too large\n");
    return 1;
}
```

這和 F-U01 的整數邊界原則完全相同：**先證明運算可表示，再做運算。**

如果 byte 數先發生無號回繞，之後即使 `malloc` 回傳非 `NULL`，也可能只配置到比程式以為的小得多的區塊。

---

## 3. 第一次完整走完「配置 → 使用 → 釋放」

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

把主線讀成：

```text
取得元素數量
→ 驗證需求
→ 驗證 byte 大小
→ malloc
→ 檢查是否成功
→ 在界限內使用
→ free
→ 不再使用原物件
```

這裡有三種不同失敗，不要混在一起：

1. 輸入本身不合法。
2. 所需 byte 數無法安全計算。
3. 大小合法，但配置要求仍無法被滿足。

---

## 4. `free` 結束的是動態物件的生命週期

配置成功後，`values` 指向一個動態配置物件。

當：

```c
free(values);
```

執行後，那個配置物件的生命週期結束。

所以不能再：

```c
printf("%d\n", values[0]);
```

這是 use after free。

把 owner 指標設成：

```c
values = NULL;
```

可以幫助避免之後不小心再次透過這個變數使用舊位置，但要注意：如果還有其他 alias 曾指向同一塊配置，**它們不會跟著自動變成 `NULL`**。

因此真正的安全規則是：

> 一旦配置物件被釋放，所有曾用來指向它的路徑都必須停止把它當成活著的物件。

---

## 5. Ownership 回答「最後誰負責 free？」

假設有函數：

```c
int *create_values(size_t count);
```

如果它成功配置一塊新空間並回傳指標，介面必須說明：

> 呼叫者是否從這一刻開始取得所有權，並負責最後的 `free`？

這裡的 **ownership（所有權）** 不是 C 語法關鍵字，而是一種設計規則，用來避免兩種相反錯誤：

```text
A 以為 B 會 free
B 也以為 A 會 free
→ leak
```

或：

```text
A 覺得自己要 free
B 也覺得自己要 free
→ double free
```

所以看到動態配置指標時，不只問「它指到哪裡」，還要問：

> 誰對這塊配置的最終釋放負責？

---

## 6. `calloc` 是「配置並把 bytes 清成零」

```c
int *values = calloc(count, sizeof *values);
```

`calloc` 把元素數量與元素大小分開傳入，成功時會配置所需空間並把配置的 bytes 設為零。

對本章的整數陣列而言，這會讓初始整數值為 0。

但不要把它背成：

> `calloc` 對所有 C 型別都等同於「語意上的預設初始化」。

它直接保證的是配置 storage 並將 bytes 清零。即使使用 `calloc`，你仍然要：

- 確認 `count` 符合需求。
- 檢查回傳值是否為 `NULL`。
- 明確管理所有權與 `free`。

---

## 7. 如果容量要成長，`realloc` 不能直接覆蓋唯一 owner

假設目前有：

```c
int *values;
size_t capacity;
```

需要改成 `new_count` 個元素。

先驗證新容量：

```c
if (new_count == 0 ||
    new_count > SIZE_MAX / sizeof *values) {
    /* 不支援這個容量 */
}
```

再寫：

```c
int *temporary = realloc(values,
                         new_count * sizeof *values);

if (temporary == NULL) {
    /* values 仍然指向原本有效的配置 */
    return 0;
}

values = temporary;
```

為什麼需要 `temporary`？

因為對非零大小的要求，`realloc` 失敗時原配置仍然存在；我們不想把唯一能找到它的指標覆蓋掉。

危險模式：

```c
values = realloc(values,
                 new_count * sizeof *values);
```

若失敗，`values` 會被 `NULL` 覆蓋，原配置卻仍存在，程式就可能失去最後一個可用 owner 指標，造成 leak。

---

## 8. `realloc` 成功後，位址可能完全不同

成功的 `realloc` 可能：

- 在原位置調整空間。
- 搬到另一個位置並回傳新位址。

所以成功之後要以新的回傳指標為準。

如果其他 alias 還保存舊配置中的位置，它們不能被假設仍然有效。

這使「可成長陣列」比固定陣列多一個重要設計問題：

> 成長操作期間，哪些指標是 owner？哪些外部 alias 可能因搬移而失效？

本課程也把容量 0 當成獨立操作：需要清空時明確 `free(values)` 並更新 owner 狀態，而不是依賴 `realloc(pointer, 0)` 的特殊情況。

---

## 9. 四種常見錯誤其實都在破壞生命週期或所有權

### Memory leak

配置還活著，但程式已經失去負責釋放它的最後一條路。

### Use after free

物件生命週期已結束，卻仍透過舊指標存取。

### Double free

同一個已結束生命週期的配置又被交給 `free`。

### 配置太小

例如本來要 `int` 元素，大小計算卻寫錯，或 `count * sizeof *values` 在未檢查前發生回繞。程式之後會按照「以為的容量」走訪，實際配置卻沒有那麼大。

這些名稱不需要分開死背。可以一直回到三個問題：

```text
這塊配置現在還活著嗎？
誰擁有它？
實際容量真的足以支援接下來的存取嗎？
```

---

## 10. 自主練習：做一個可成長整數清單

需求：

- 初始 `capacity = 4`。
- 使用者持續輸入整數。
- `-1` 表示結束。
- 當 `size == capacity` 時，容量加倍。

整個過程維持：

```text
size <= capacity
```

每次成長以前都要先證明：

1. `capacity * 2` 本身可表示。
2. 新容量換算成 byte 數可表示。
3. `realloc` 成功以前，原 owner 與 metadata 不被破壞。

只有在重新配置成功後才更新：

```c
capacity = new_capacity;
```

若失敗，原資料、原 `size`、原 `capacity` 都應仍然可用，讓呼叫者可以決定要終止、重試或保存目前結果。

---

## 11. 修改需求：把 append 包成一個函數

現在希望呼叫：

```c
int append_value(int **values,
                 size_t *size,
                 size_t *capacity,
                 int value);
```

這個介面看起來比前面複雜，因為函數不只可能修改元素，還可能因 `realloc` 改變 owner 指標本身。

在寫實作以前，先定義失敗契約：

> 如果 `append_value` 回傳失敗，呼叫者原本的 `*values`、`*size`、`*capacity` 與所有既有元素都保持有效且不變。

接著才能安排操作順序：

```text
驗證參數與 invariant
→ 若仍有容量，直接寫入
→ 若需要成長，先安全算新容量與 byte 數
→ 用 temporary 執行 realloc
→ 成功後才提交新的 pointer/capacity
→ 寫入 value
→ 最後增加 size
```

這是一個很重要的設計模式：**先完成可能失敗的工作，成功後才一次提交新狀態。**

---

## 12. 選做：讓 AI 挑戰你的 ownership 圖

這一節完全可以跳過。

先自己畫一個可成長陣列在：

```text
配置前
配置後
realloc 成功搬移後
free 後
```

四個時刻的 owner 與 alias。

如果你想多做一次檢查，可以讓 AI 指出哪一個時刻最容易產生 leak、dangling alias 或 double free。你不需要固定 Prompt，也不需要保存或繳交對話。

如果它的說法和 `malloc`／`realloc`／`free` 契約、配置圖或記憶體檢查工具衝突，就回到可驗證證據重新判斷。

---

## 13. 離開這個 Unit 前，確認你能追蹤整個生命週期

直接回答：

- 為什麼元素數量合法，仍要另外檢查 byte 大小乘法？
- `malloc` 回傳 `NULL` 和大小計算溢位為什麼是不同問題？
- `free(values)` 之後，為什麼其他 alias 不會因 `values = NULL` 自動變安全？
- ownership 主要要避免哪兩個相反錯誤？
- 為什麼 `realloc` 通常先存進 temporary？
- `realloc` 成功搬移後，舊 alias 有什麼風險？
- 可成長清單為什麼只能在配置成功後更新 `capacity`？
- `append_value` 的「失敗時原狀態不變」為什麼能讓呼叫端更容易推理？

如果某題只剩函式名稱，重新畫出 owner 箭頭與配置物件的生命週期。

---

## 14. 本章收尾

F-U07 讓我們把一筆資料組成 `Student`；F-U08 再讓「要保存幾筆」不必在寫程式時就固定。

代價是責任也跟著增加：**配置以前要安全算大小，配置後要知道誰擁有，成長時要保留失敗前狀態，釋放後所有路徑都必須停止使用。**

下一個 Unit 會處理另一種「超過程式生命週期」的需求。動態記憶體只能活到程式執行期間；如果資料希望程式結束後仍存在，就必須寫到檔案，並面對開啟、讀寫、格式、失敗與部分更新的問題。

## 導覽

- [上一單元：結構](unit-07-structures.zh-TW.md)
- [下一單元：檔案](unit-09-files.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-08-dynamic-memory.en.md)
