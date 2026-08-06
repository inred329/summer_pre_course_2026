# 正式單元 F-U07：資料結構如何由多個不同欄位組成？

版本：1.0.2  
狀態：正式學生教材  
最後更新：2026-08-06  
對應英文版本：[Formal Unit F-U07: How Can One Data Object Contain Different Fields?](unit-07-structures.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能用 `struct` 表示具有多個欄位的實體，能追蹤成員存取與結構指定，並能為結構介面明確定義初始化、指標、字串容量與欄位驗證契約。

本章核心完成標準不要求使用 AI。文末的 AI 活動是可直接跳過的選用延伸；未使用 AI 不影響本章完成、課堂參與或評量。

## 核心問題

> 當一個實體包含多種不同資料時，如何把它們組合成一個有意義的物件？

完成本章後，你應能：

1. 說明結構、欄位與物件。
2. 定義與初始化 `struct`。
3. 使用 `.` 與 `->` 存取成員。
4. 比較結構值傳遞與指標傳遞。
5. 在不超出容量的情況下複製字串欄位。
6. 設計結構陣列與欄位驗證。

---

## 1. 一個學生不是三個無關變數

```c
char name[20];
int id;
double average;
```

這些資料共同描述一個學生。若有多位學生，分散變數容易失去對應關係。

---

## 2. 結構模型

```c
struct Student {
    char name[20];
    int id;
    double average;
};
```

```text
Student
├── name
├── id
└── average
```

`struct Student` 定義一種資料型別；實際變數才是物件。

```c
struct Student s;
```

這個宣告本身不會初始化欄位。在初始化前讀取 `s.id`、`s.average`，或把 `s.name` 當成字串使用都不合法；純量成員具有 indeterminate value，而字元陣列也可能沒有終止符。

---

## 3. 初始化與成員存取

```c
struct Student s = {"Amy", 1001, 87.5};

printf("%s\n", s.name);
printf("%d\n", s.id);
printf("%.1f\n", s.average);
```

`.` 表示從一個結構物件中存取成員。

```c
s.average = 90.0;
```

若物件稍後才逐欄填入，可先使用零初始化：

```c
struct Student empty = {0};
```

這會把純量欄位設為 0，並讓 `name[0] == '\0'`，形成空字串。

---

## 4. `typedef` 簡化名稱

```c
typedef struct {
    char name[20];
    int id;
    double average;
} Student;

Student s = {"Amy", 1001, 87.5};
```

`typedef` 建立型別別名，不會自動建立物件。

---

## 5. 結構介面需要契約

值傳遞：

```c
void print_student(Student s) {
    printf("%s %d %.1f\n", s.name, s.id, s.average);
}
```

具驗證的指標傳遞：

```c
#include <math.h>

int update_average(Student *s, double value) {
    if (s == NULL || !isfinite(value) || value < 0.0 || value > 100.0) {
        return 0;
    }

    s->average = value;
    return 1;
}
```

`p->member` 等價於 `(*p).member`。函數不應修改資料時可使用 `const Student *s`，但仍要定義是否允許 `NULL`。

---

## 6. 安全設定固定容量姓名

```c
#include <stdio.h>

int set_name(Student *s, const char *name) {
    if (s == NULL || name == NULL) {
        return 0;
    }

    int written = snprintf(s->name, sizeof s->name, "%s", name);
    if (written < 0 || (size_t)written >= sizeof s->name) {
        s->name[0] = '\0';
        return 0;
    }

    return 1;
}
```

此函數不會默默保存被截斷的姓名；若來源太長則回報失敗，並把 `name` 留成空字串。其他政策也可以，但必須明確寫出並測試。

---

## 7. 結構指定

```c
Student a = {"Amy", 1001, 87.5};
Student b = a;
```

結構指定會複製各欄位的值，也會複製陣列成員中的每個元素。之後修改 `b.average` 或 `b.name[0]` 都不會改變 `a`。

若欄位本身是指標，複製的是指標值；所有權問題會在動態記憶體單元深化。

C 不提供結構的 `a == b`。應逐一比較需求指定的欄位；字串內容使用 `strcmp`。

---

## 8. 結構陣列

```c
Student students[3] = {
    {"Amy", 1001, 87.5},
    {"Ben", 1002, 91.0},
    {"Cara", 1003, 78.0}
};
```

```c
for (int i = 0; i < 3; i++) {
    printf("%s %.1f\n", students[i].name, students[i].average);
}
```

陣列邊界規則仍然適用。函數應同時取得陣列與長度，並定義空集合行為。

---

## 9. 錯誤案例與分類

### 讀取未初始化結構

```c
Student s;
printf("%d\n", s.id);
```

讀取 indeterminate scalar member 屬未定義行為。

### 對指標使用 `.`

```c
Student *p = &s;
printf("%d\n", p.id);
```

這是編譯期型別錯誤。應使用 `p->id` 或 `(*p).id`。

### 解參照空結構指標

```c
Student *p = NULL;
printf("%d\n", p->id);
```

程式可編譯，但求值 `p->id` 會解參照 null pointer，屬未定義行為。

### 忽略字串容量

```c
strcpy(s.name, source);
```

若 `source` 太長，會寫出陣列邊界並造成未定義行為。應使用具有明確截斷政策的 checked interface。

### 使用 `==` 比較結構

```c
if (a == b) { /* ... */ }
```

結構運算元不支援 `==`，這是編譯期 constraint violation。應比較指定成員。

---

## 10. 引導練習

1. 定義 `Point`，包含 `x`、`y`，並提供零初始化。
2. 建立函數計算兩點距離，並定義 null pointer 行為。
3. 定義 `Book`，包含書名、頁數與價格，並建立 checked setter。
4. 建立結構陣列並找出最高價格，包含空陣列行為。

---

## 11. 自主練習：學生資料分析

建立最多 10 位學生的結構陣列，輸出平均最高者、全班平均與指定學號資料。

定義並測試：

- 找不到學號
- 空集合
- 相同最高分
- 過長姓名
- 無效或非有限平均
- 若輔助函數使用輸出指標，測試 null output pointer

---

## 12. 需求修改

新增欄位 `char grade`，由平均成績計算。請指出哪些初始化、驗證函數、介面、輸出、結構比較與測試需要更新。

---

## 13. 選用延伸：使用 AI 檢查自己的解釋

這一節可直接跳過。未使用 AI 不影響本章完成、課堂參與或評量。

若你選擇使用 AI，可先用自己的話解釋：

> 結構如何把多個欄位組成一個資料物件？為什麼初始化、字串容量、nullability 與欄位驗證仍是不同契約？

不需要固定 Prompt，也不需要保存、繳交對話或提出未使用聲明。AI 回應若與成員追蹤、函數介面、編譯器診斷或可重現結果衝突，應以證據重新判斷。

---

## 14. 自我檢核

- 我能定義並完整初始化結構。
- 我能區分型別與物件。
- 我能在有效物件與指標上使用 `.` 與 `->`。
- 我能說明結構指定，包括陣列與指標成員。
- 我能安全設定固定容量字串欄位。
- 我能驗證結構欄位與空集合。

## 15. 本章摘要

結構把描述同一實體的不同欄位組成一個型別，讓資料關係、介面與走訪更清楚。可靠使用結構仍需要完整初始化、有效指標、有界字串操作、欄位驗證與明確比較規則。下一章將在執行期間配置空間，並處理所有權與生命週期。

## 導覽

- [上一單元：指標](unit-06-pointers.zh-TW.md)
- [下一單元：動態記憶體](unit-08-dynamic-memory.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-07-structures.en.md)
