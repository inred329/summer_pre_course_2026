# 正式單元 F-U06：如何透過位址間接操作資料？

版本：1.0.0  
狀態：正式學生教材  
最後更新：2026-08-04  
對應英文版本：[Formal Unit F-U06: How Can Data Be Manipulated Indirectly Through Addresses?](unit-06-pointers.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能說明位址、指標與解參照的關係，能用記憶體圖追蹤間接修改，並能診斷 null pointer、dangling pointer 與錯誤別名問題。

## 核心問題

> 程式如何用一個值指向另一個物件，並透過位址存取或修改它？

完成本章後，你應能：

1. 區分物件、值、位址與指標。
2. 使用 `&` 取得位址，使用 `*` 解參照。
3. 追蹤指標參數如何修改呼叫者資料。
4. 說明 aliasing、null pointer 與 lifetime。
5. 避免解參照無效位址。

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

## 4. 指標參數

```c
void add_bonus(int *score, int bonus) {
    *score = *score + bonus;
}

int main(void) {
    int value = 80;
    add_bonus(&value, 5);
    printf("%d\n", value);
}
```

呼叫者傳入位址，因此函數可修改呼叫者的物件。

介面責任應清楚：此函數會修改傳入物件，而非只回傳新值。

---

## 5. 兩個指標可指向同一物件

```c
int value = 10;
int *a = &value;
int *b = &value;
```

`a` 與 `b` 是別名（aliases）。透過 `*a` 修改後，`*b` 讀到同一個新值。

Aliasing 會增加追蹤難度，因為不同名稱可能影響同一狀態。

---

## 6. Null Pointer

```c
int *p = NULL;
```

`NULL` 表示目前不指向有效物件。可以比較：

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

`local` 在函數回傳後生命週期結束，回傳的位址成為 dangling pointer。位址數字可能仍存在，但不再代表可合法使用的物件。

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

指標算術必須保持在同一陣列範圍內或恰好尾端之外；不可任意跨越記憶體。

---

## 9. 錯誤案例

### 未初始化指標

```c
int *p;
*p = 10;
```

`p` 沒有可靠指向，解參照屬未定義行為。

### 解參照 NULL

```c
int *p = NULL;
printf("%d\n", *p);
```

先檢查有效性。

### 把 `*` 的兩種位置混淆

```c
int *p;   /* 宣告指標 */
*p = 5;   /* 解參照 */
```

語法相似，但角色不同；以記憶體圖解讀。

---

## 10. 引導練習

1. 畫出 `value`、`p`、`*p` 的關係。
2. 建立 `swap(int *a, int *b)`，先追蹤兩個位址與值。
3. 比較「回傳新值」與「透過指標修改」兩種介面。

---

## 11. 自主練習：找出最小與最大值

建立函數：

```c
int find_min_max(const int values[], int length, int *min, int *max);
```

成功時透過指標輸出最小與最大值；若長度不合法則回傳失敗。先定義 null pointer 與空陣列的行為。

---

## 12. 需求修改

新增規則：`min` 或 `max` 任一為 `NULL` 時不得寫入。更新前置條件、回傳規則與測試。

---

## 13. 向 AI 解釋概念

請向 AI 解釋：

> 位址、指標與解參照之間有什麼關係？為什麼 lifetime 會決定一個位址是否仍可使用？

AI 回應若與記憶體圖、函數介面或可重現結果衝突，應以證據重新判斷。

---

## 14. 自我檢核

- 我能區分物件、值、位址與指標。
- 我能使用 `&` 與 `*`。
- 我能追蹤指標參數修改。
- 我能說明 aliasing。
- 我不會解參照 NULL 或未初始化指標。
- 我能說明 dangling pointer 與 lifetime。

## 15. 本章摘要

指標保存物件位址，解參照讓程式透過位址存取或修改物件。可靠使用指標需要明確指向、有效生命週期、null 檢查與邊界控制。下一章將用結構把多個不同欄位組成一個資料物件。

## 導覽

- [上一單元：呼叫堆疊與遞迴](unit-05-call-stack-recursion.zh-TW.md)
- [下一單元：結構](unit-07-structures.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-06-pointers.en.md)
