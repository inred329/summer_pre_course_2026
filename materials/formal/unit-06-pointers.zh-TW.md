# 正式單元 F-U06：如何透過位址間接操作資料？

版本：1.0.1  
狀態：正式學生教材  
最後更新：2026-08-05  
對應英文版本：[Formal Unit F-U06: How Can Data Be Manipulated Indirectly Through Addresses?](unit-06-pointers.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能說明位址、指標與解參照的關係，能用記憶體圖追蹤間接修改，並能為指標介面明確定義 nullability、lifetime、boundary 與 aliasing 契約。

## 核心問題

> 程式如何用一個值指向另一個物件，並透過位址存取或修改它？

完成本章後，你應能：

1. 區分物件、值、位址與指標。
2. 使用 `&` 取得位址，使用 `*` 解參照。
3. 追蹤指標參數如何修改呼叫者資料。
4. 說明 aliasing、null pointer 與 lifetime。
5. 定義指標參數是否可為 `NULL` 或彼此為別名。
6. 避免解參照無效位址。

---

## 1. 變數除了值還有位址

```c
int score = 80;
int *p = &score;
```

概念圖：

```text
p ──────► score
          value: 80
```

`score` 是物件，`80` 是目前值，`&score` 是位址，`p` 保存該位址。

---

## 2. `&` 與 `*`

```c
printf("%d\n", *p);
*p = 90;
```

- `&score`：取得 `score` 的位址。
- `*p`：存取 `p` 指向的物件。

`*p = 90` 不是改變指標值，而是透過指標修改 `score`。

---

## 3. 間接修改追蹤

```c
int score = 80;
int *p = &score;
*p = *p + 5;
```

```text
讀取 p 保存的位址
→ 找到 score
→ 讀取 80
→ 計算 85
→ 寫回 score
```

最後 `score == 85`。

---

## 4. 指標參數需要契約

```c
int add_bonus(int *score, int bonus) {
    if (score == NULL) {
        return 0;
    }

    *score = *score + bonus;
    return 1;
}

int main(void) {
    int value = 80;

    if (!add_bonus(&value, 5)) {
        return 1;
    }

    printf("%d\n", value);
    return 0;
}
```

呼叫者傳入位址，因此函數可修改呼叫者的物件。介面明確要求 `score` 必須指向仍在生命週期內的 `int`；若為 `NULL`，函數回傳失敗且不解參照。

這個範例仍假設 `int` 加法結果可表示。若需求允許極端 bonus，介面還必須在指定前檢查溢位。

---

## 5. 兩個指標可指向同一物件

```c
int value = 10;
int *a = &value;
int *b = &value;
```

`a` 與 `b` 是別名（aliases）。透過 `*a` 修改後，`*b` 讀到同一個新值。

Aliasing 行為應寫進函數契約。例如以下 swap 即使兩個參數指向同一物件仍合法：

```c
int swap(int *a, int *b) {
    if (a == NULL || b == NULL) {
        return 0;
    }

    int temporary = *a;
    *a = *b;
    *b = temporary;
    return 1;
}
```

若 `a == b`，物件值維持不變；這是合法 no-op，不是錯誤。其他介面也可以禁止別名，但必須明確寫出並測試。

---

## 6. Null Pointer

```c
int *p = NULL;
```

`NULL` 表示目前不指向有效物件。

```c
if (p != NULL) {
    printf("%d\n", *p);
}
```

不可解參照 `NULL`。

---

## 7. Lifetime 與 Dangling Pointer

```c
int *bad_pointer(void) {
    int local = 10;
    return &local;
}
```

`local` 在函數回傳後生命週期結束。回傳指標不能再用來合法存取該物件；之後解參照屬未定義行為。不能因位址數字看似未變就認為可用。

---

## 8. 指標與陣列

```c
int values[3] = {10, 20, 30};
int *p = values;
```

在許多運算式中，陣列名稱會轉成第一個元素位址。

```c
*p        /* 10 */
*(p + 1)  /* 20 */
```

指標算術必須位於同一陣列物件內，或恰好指向尾端之外一格。尾端之外一格的指標可建立與比較，但不可解參照。

---

## 9. 錯誤案例與分類

### 未初始化指標

```c
int *p;
*p = 10;
```

`p` 具有 indeterminate value，解參照屬未定義行為。

### 解參照 NULL

```c
int *p = NULL;
printf("%d\n", *p);
```

程式可編譯，但解參照 null pointer 屬未定義行為。

### 解參照尾端之外一格

```c
int values[3] = {10, 20, 30};
int *end = values + 3;
printf("%d\n", *end);
```

建立 `end` 合法；解參照它則越界並屬未定義行為。

### 對指標使用 `.`

```c
/* 假設 p 是結構指標 */
p.member
```

這是編譯期型別錯誤。應使用 `p->member` 或 `(*p).member`。

---

## 10. 引導練習

1. 畫出 `value`、`p`、`*p` 的關係。
2. 以不同物件、同一物件與各種 `NULL` 參數測試 `swap`。
3. 比較「回傳新值」與「透過指標修改」兩種介面。
4. 說明為什麼尾端之外一格可比較但不可解參照。

---

## 11. 自主練習：找出最小與最大值

建立函數：

```c
int find_min_max(const int values[], int length, int *min, int *max);
```

建議契約：

- `values`、`min` 或 `max` 為 `NULL` 時失敗
- `length <= 0` 時失敗
- 失敗時不修改任何輸出物件
- 成功時寫入兩個結果
- 允許 `min == max`；先在區域變數計算兩個結果，再依順序寫入同一物件

測試空陣列、null 參數、單一元素、全部相同與輸出指標別名。

---

## 12. 需求修改

新規則：允許 `min` 或 `max` 任一為 `NULL`，表示不需要該結果；但兩者不可同時為 `NULL`。更新契約、實作與測試，且不得解參照被省略的輸出。

---

## 13. 向 AI 解釋概念

請向 AI 解釋：

> 位址、指標與解參照之間有什麼關係？為什麼指標介面必須定義 nullability、lifetime、boundary 與 aliasing？

AI 回應若與記憶體圖、函數介面或可重現結果衝突，應以證據重新判斷。

---

## 14. 自我檢核

- 我能區分物件、值、位址與指標。
- 我能使用 `&` 與 `*`。
- 我能追蹤指標參數修改。
- 我能說明 aliasing，並定義介面是否允許別名。
- 我不會解參照 null、indeterminate、dangling 或 one-past 指標。
- 我能說明 lifetime 如何決定指標是否有效。

## 15. 本章摘要

指標保存物件位址，解參照讓程式透過位址存取或修改物件。可靠的指標介面必須定義有效目標、生命週期、nullability、陣列邊界、輸出行為與 aliasing。下一章將用結構把多個不同欄位組成一個資料物件。

## 導覽

- [上一單元：呼叫堆疊與遞迴](unit-05-call-stack-recursion.zh-TW.md)
- [下一單元：結構](unit-07-structures.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-06-pointers.en.md)
