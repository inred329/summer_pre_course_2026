# 正式單元 F-U08：程式如何在執行期間取得與釋放空間？

版本：1.0.1  
狀態：正式學生教材  
最後更新：2026-08-05  
對應英文版本：[Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?](unit-08-dynamic-memory.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能使用 `malloc`、`calloc`、`realloc` 與 `free` 管理動態空間，能說明所有權與生命週期，並能診斷 memory leak、dangling pointer 與 double free。

## 核心問題

> 當資料大小或生命週期無法預先固定時，程式如何管理儲存空間？

完成本章後，你應能：

1. 區分自動儲存與動態配置。
2. 配置、檢查、使用與釋放空間。
3. 說明所有權與釋放責任。
4. 安全使用 `realloc`。
5. 診斷常見生命週期錯誤。

---

## 1. 為什麼需要動態配置？

```c
int values[100];
```

固定陣列要求容量在編譯時或進入區塊時決定。若使用者輸入資料筆數，或物件必須跨越目前函數生命週期，就可能需要動態空間。

---

## 2. 配置模型

```c
int *values = malloc(n * sizeof *values);
```

```text
values ─────► 動態配置區塊
              n 個 int
```

`malloc` 回傳起始位址；配置失敗時回傳 `NULL`。

```c
if (values == NULL) {
    return 1;
}
```

---

## 3. 完整生命週期

```c
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

    int *values = malloc((size_t)n * sizeof *values);
    if (values == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        values[i] = i * 10;
    }

    free(values);
    values = NULL;
    return 0;
}
```

流程：

```text
讀取並驗證大小
→ 配置
→ 檢查
→ 初始化／使用
→ 釋放
→ 不再使用
```

輸入檢查是程式契約的一部分。若 `scanf` 失敗，`n` 就沒有可供後續判斷使用的有效值。

---

## 4. `calloc`

```c
int *values = calloc(n, sizeof *values);
```

`calloc` 配置多個元素並把位元清為零。不要把這推廣成所有型別的語意初始化保證；應理解它做的是 zero-initialized storage。

---

## 5. 所有權

所有權回答：誰負責釋放這塊空間？

```c
int *create_values(int n);
```

若函數回傳新配置空間，介面應說明呼叫者取得所有權並負責 `free`。

避免兩個模組都以為對方會釋放，或兩者都釋放同一區塊。

---

## 6. `realloc`

```c
int *temporary = realloc(values, new_size * sizeof *values);
if (temporary != NULL) {
    values = temporary;
}
```

不要直接寫：

```c
values = realloc(values, new_size * sizeof *values);
```

若失敗，原位址可能因被覆蓋而遺失，造成 leak。使用暫存指標保留原區塊。

---

## 7. 錯誤案例

### Memory Leak

配置後失去最後一個位址，或函數結束前未釋放不再需要的區塊。

### Dangling Pointer

```c
free(values);
printf("%d\n", values[0]);
```

釋放後物件生命週期結束，不能再解參照。

### Double Free

```c
free(values);
free(values);
```

同一區塊不可重複釋放。釋放後設為 `NULL` 有助於降低部分風險，但不能取代所有權設計。

### 錯誤大小

```c
malloc(n * sizeof(int *))
```

若要配置 `int`，應使用 `sizeof *values`，讓型別變更時仍一致。

---

## 8. 引導練習

1. 動態配置 `n` 個整數並計算總和。
2. 畫出配置前、配置後與釋放後的指標圖。
3. 將固定容量陣列改成由輸入決定大小。

---

## 9. 自主練習：可成長整數清單

從容量 4 開始讀入整數；滿時把容量加倍。輸入 `-1` 結束。

必須保存：

- `size` 與 `capacity`
- 每次成長前後位址與容量
- `realloc` 失敗處理
- 最後一次 `free`

---

## 10. 需求修改

新增函數：

```c
int append_value(int **values, int *size, int *capacity, int value);
```

請定義所有權、成功／失敗回傳、哪些參數會被修改，以及失敗時原資料是否仍有效。

---

## 11. 向 AI 解釋概念

請向 AI 解釋：

> 動態配置、所有權、生命週期與 `free` 之間有什麼關係？為什麼 `realloc` 常需要暫存指標？

AI 回應若與配置圖、函式規格或記憶體檢查結果衝突，應以證據重新判斷。

---

## 12. 自我檢核

- 我能檢查輸入與配置失敗。
- 我能配對每次成功配置與釋放責任。
- 我能說明所有權。
- 我不會在 `free` 後使用物件。
- 我能診斷 leak、dangling pointer 與 double free。
- 我能安全處理 `realloc` 失敗。

## 13. 本章摘要

動態記憶體讓程式在執行期間決定大小與生命週期，但也把所有權與釋放責任交給程式設計者。可靠管理需要明確介面、輸入與配置失敗檢查、正確釋放與不再使用。下一章將把資料寫入檔案，使其在程式結束後仍可保存。

## 導覽

- [上一單元：結構](unit-07-structures.zh-TW.md)
- [下一單元：檔案](unit-09-files.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-08-dynamic-memory.en.md)
