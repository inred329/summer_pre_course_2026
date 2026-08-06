# 正式單元 F-U08：程式如何在執行期間取得與釋放空間？

版本：1.0.2  
狀態：正式學生教材  
最後更新：2026-08-06  
對應英文版本：[Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?](unit-08-dynamic-memory.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能使用 `malloc`、`calloc`、`realloc` 與 `free` 管理動態空間，能說明所有權與生命週期、避免配置大小計算溢位，並能診斷 memory leak、dangling pointer 與 double free。

AI 使用不屬於本章完成標準。接近章末的 AI 選用延伸可直接跳過，不影響完成、課堂參與或評量。

## 核心問題

> 當資料大小或生命週期無法預先固定時，程式如何管理儲存空間？

完成本章後，你應能：

1. 區分自動儲存與動態配置。
2. 在計算配置大小前驗證元素數量。
3. 配置、檢查、使用與釋放空間。
4. 說明所有權與釋放責任。
5. 在 `realloc` 失敗時保留原區塊。
6. 診斷常見生命週期錯誤。

---

## 1. 為什麼需要動態配置？

```c
int values[100];
```

固定陣列要求容量在執行工作前決定。若資料筆數由使用者輸入，或物件必須跨越目前函數生命週期，就可能需要動態空間。

動態配置不一定比固定陣列更好。它同時帶來失敗處理、所有權、生命週期與釋放責任。只有在需求真的需要執行期間決定大小或生命週期時才使用。

---

## 2. 配置模型

```c
int *values = malloc(count * sizeof *values);
```

```text
values ─────► 動態配置區塊
              count 個 int
```

`malloc` 接受以 byte 為單位的大小。成功時回傳具有適當 alignment 的區塊起始位址；無法滿足要求時回傳 `NULL`。

配置前必須先回答兩個問題：

1. 元素數量是否符合程式需求？
2. `count * sizeof *values` 是否能由 `size_t` 表示？

```c
if (count > SIZE_MAX / sizeof *values) {
    fprintf(stderr, "Requested size is too large\n");
    return 1;
}
```

必須在乘法發生前檢查。若 byte 數計算發生 wraparound，程式可能取得比後續假設更小的區塊。

---

## 3. 完整生命週期

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;

    if (scanf("%d", &n) != 1) {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }

    if (n <= 0) {
        fprintf(stderr, "Size must be positive\n");
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

流程：

```text
讀取並驗證元素數量
→ 驗證 byte 大小計算
→ 配置
→ 檢查配置結果
→ 在界限內初始化／使用
→ 恰好釋放一次
→ 所有指向該物件的指標都停止使用
```

輸入檢查是程式契約的一部分。若 `scanf` 失敗，`n` 就沒有可供後續判斷使用的有效值。

大小檢查保護的是配置契約。配置失敗與大小乘法溢位是不同問題，不應混為一談。

---

## 4. `calloc`

```c
int *values = calloc(count, sizeof *values);
```

`calloc` 接受元素數量與每個元素大小。它要嘛配置足以容納乘積的空間，要嘛失敗；成功時也會把配置的 bytes 清為零。

應把它理解成 zeroed storage，而不是所有可能 C 型別的通用語意初始化保證。對本課程使用的整數陣列而言，全零位元表示整數零。

即使使用 `calloc`，程式仍須確認 `count` 符合需求，並檢查回傳指標。

---

## 5. 所有權

所有權回答：誰負責釋放這塊空間？

```c
int *create_values(size_t count);
```

若函數回傳新配置空間，介面應說明：

- 呼叫者是否取得所有權
- 最終由哪一方呼叫 `free`
- `NULL` 是否表示失敗
- 是否還有其他 alias 存在

避免兩個模組都以為對方會釋放，或兩者都釋放同一區塊。

釋放後只把其中一個指標設為 `NULL`，不會同步更新其他 alias。所有曾指向該物件的指標都不能再用來解參照、當作有效物件位址比較，或再次 `free`。

---

## 6. `realloc`

`realloc` 成功時可能回傳原位址，也可能把物件移到新位址。成功後不得再使用舊指標值。對非零大小要求而言，若 `realloc` 失敗，原配置仍然有效且內容不變。

先驗證新的元素數量與 byte 大小：

```c
if (new_count == 0 || new_count > SIZE_MAX / sizeof *values) {
    /* 處理無效或不支援的容量 */
}
```

再保留原指標，直到確認成功：

```c
int *temporary = realloc(values, new_count * sizeof *values);
if (temporary == NULL) {
    /* values 仍擁有原區塊 */
    return 0;
}

values = temporary;
```

避免直接指定：

```c
values = realloc(values, new_count * sizeof *values); /* 不安全模式 */
```

若失敗，直接指定可能覆蓋唯一的原位址，造成 memory leak。

本課程把容量變成零視為獨立操作：明確呼叫 `free(values)`，再把 owner 指標設成 `NULL`。不要依賴 `realloc(pointer, 0)` 在不同實作間可能不同的行為。

---

## 7. 錯誤案例

### Memory Leak

配置後失去最後一個位址，或不再需要區塊後沒有任何負責的 owner 釋放它。

### Use After Free 與 Dangling Pointer

```c
free(values);
printf("%d\n", values[0]);
```

物件生命週期在 `free` 時結束，之後不能再解參照。指向同一物件的其他 alias 也同樣成為 dangling pointer。

### Double Free

```c
free(values);
free(values);
```

同一區塊不可重複釋放。釋放後立即把 owner 指標設為 `NULL`，可降低部分風險，因為 `free(NULL)` 是允許的；但這不會修復其他 dangling alias，也不能取代所有權設計。

### 錯誤配置型別大小

```c
malloc(count * sizeof(int *))
```

若要配置 `int` 元素，應使用 `sizeof *values`，讓表示式與指標目標型別維持一致。

### 配置大小溢位

```c
malloc(count * sizeof *values)
```

只有在先確認下列條件後，這個表示式才安全：

```c
count <= SIZE_MAX / sizeof *values
```

即使 `malloc` 回傳非 `NULL`，也不能證明未檢查的乘法代表了原本想要的大小。

---

## 8. 引導練習

1. 動態配置 `n` 個整數並計算總和，同時避免配置大小乘法溢位。
2. 畫出配置前、配置後與釋放後的 owner 指標與 alias。
3. 將固定容量陣列改成由已驗證輸入決定大小。
4. 說明配置失敗時哪些敘述會執行，以及為什麼不能再存取元素。

---

## 9. 自主練習：可成長整數清單

從容量 4 開始讀入整數；滿時把容量加倍。輸入 `-1` 結束。

追蹤：

- `size` 與 `capacity`
- invariant：`size <= capacity`
- 容量加倍以及換算 byte 數是否可表示
- 成長成功前後的位址
- `realloc` 失敗時原區塊仍有效
- 最終負責一次 `free` 的 owner

只有在重新配置成功後，才能更新 `capacity`。

---

## 10. 需求修改

新增函數：

```c
int append_value(int **values, size_t *size, size_t *capacity, int value);
```

請定義：

- 呼叫前後的所有權
- 成功／失敗回傳規則
- 哪些輸出參數可能改變
- `size` 與 `capacity` 的 invariant
- 容量成長時的 overflow 處理
- 失敗時原資料是否仍有效

一個清楚的失敗契約是：函數回報失敗時，原指標、`size`、`capacity` 與既有元素仍然有效且不變。

---

## 11. 選用延伸：評估 AI 解釋

本節可直接跳過。AI 不是必要工具，也不要求固定 Prompt、保存對話、留下筆記、繳交內容或聲明未使用。

若你選擇使用 AI，先用自己的話解釋：

> 動態配置、所有權、生命週期、配置大小計算與 `free` 之間有什麼關係？為什麼 `realloc` 常需要暫存指標？

再以配置圖、C 函式庫契約、編譯器診斷、測試，以及可用時的記憶體檢查工具評估回應。不要因為說法看起來有自信就直接接受。

---

## 12. 自我檢核

- 我能驗證輸入並拒絕不支援的元素數量。
- 我能在進行配置大小乘法前先檢查是否可表示。
- 我能在存取元素前檢查配置失敗。
- 我能把每次成功配置配對到一個釋放責任。
- 我能說明所有權與 alias 的影響。
- 我不會透過任何指標在 `free` 後繼續使用物件。
- 我能診斷 leak、use after free、dangling pointer 與 double free。
- 我能在 `realloc` 失敗時保留原區塊與 metadata。
- 我能說明為什麼零容量處理與一般成長分開。

## 13. 本章摘要

動態記憶體讓程式在執行期間決定大小與生命週期，但也把大小計算、所有權與釋放責任交給程式設計者。可靠管理需要驗證元素數量、防止 byte 大小溢位、檢查配置結果、定義所有權、恰好釋放一次，並在之後停止所有使用。安全成長會在 `realloc` 成功前保留原物件。下一章將把資料寫入檔案，使其在程式結束後仍可保存。

## 導覽

- [上一單元：結構](unit-07-structures.zh-TW.md)
- [下一單元：檔案](unit-09-files.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-08-dynamic-memory.en.md)