# 正式單元 F-U07：資料結構如何由多個不同欄位組成？

版本：1.0.0  
狀態：正式學生教材  
最後更新：2026-08-04  
對應英文版本：[Formal Unit F-U07: How Can One Data Object Contain Different Fields?](unit-07-structures.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能用 `struct` 表示具有多個欄位的實體，能追蹤成員存取與結構指定，並能設計清楚的資料介面與測試。

## 核心問題

> 當一個實體包含多種不同資料時，如何把它們組合成一個有意義的物件？

完成本章後，你應能：

1. 說明結構、欄位與物件。
2. 定義與初始化 `struct`。
3. 使用 `.` 與 `->` 存取成員。
4. 比較結構值傳遞與指標傳遞。
5. 設計結構陣列與欄位驗證。

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

---

## 3. 初始化與成員存取

```c
struct Student s = {"Amy", 1001, 87.5};

printf("%s\n", s.name);
printf("%d\n", s.id);
printf("%.1f\n", s.average);
```

`.` 表示從一個結構物件中存取成員。

指定成員：

```c
s.average = 90.0;
```

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

## 5. 結構作為函數參數

值傳遞：

```c
void print_student(Student s) {
    printf("%s %d %.1f\n", s.name, s.id, s.average);
}
```

指標傳遞：

```c
void update_average(Student *s, double value) {
    s->average = value;
}
```

`p->member` 等價於 `(*p).member`。

若函數不應修改資料，可使用：

```c
void print_student(const Student *s);
```

---

## 6. 結構指定

```c
Student a = {"Amy", 1001, 87.5};
Student b = a;
```

結構指定會複製各欄位的值。之後修改 `b.average` 不會改變 `a.average`。

但若欄位本身是指標，複製的是位址；所有權問題會在動態記憶體單元深化。

---

## 7. 結構陣列

```c
Student students[3] = {
    {"Amy", 1001, 87.5},
    {"Ben", 1002, 91.0},
    {"Cara", 1003, 78.0}
};
```

走訪：

```c
for (int i = 0; i < 3; i++) {
    printf("%s %.1f\n", students[i].name, students[i].average);
}
```

---

## 8. 錯誤案例

### 欄位彼此不同步

若姓名、編號、平均分別放在三個平行陣列，排序其中一個陣列時可能破壞對應。結構陣列把同一實體欄位綁在一起。

### 對指標使用 `.`

```c
Student *p = &s;
printf("%d\n", p.id);
```

應使用 `p->id` 或 `(*p).id`。

### 不檢查字串容量

把過長名字寫入固定陣列可能越界。輸入與複製仍需遵守容量與終止符規則。

---

## 9. 引導練習

1. 定義 `Point`，包含 `x`、`y`。
2. 建立函數計算兩點距離。
3. 定義 `Book`，包含書名、頁數與價格。
4. 建立結構陣列並找出最高價格。

---

## 10. 自主練習：學生資料分析

建立最多 10 位學生的結構陣列，輸出：

- 平均最高者
- 全班平均
- 指定學號的學生資料

先定義找不到學號、空集合與相同最高分的行為。

---

## 11. 需求修改

新增欄位 `char grade`，由平均成績計算。請指出哪些初始化、函數介面、輸出與測試需要更新。

---

## 12. 向 AI 解釋概念

請向 AI 解釋：

> 結構如何把多個欄位組成一個資料物件？`.`、`->`、值傳遞與指標傳遞有什麼差異？

AI 回應若與成員追蹤、函數介面或可重現結果衝突，應以證據重新判斷。

---

## 13. 自我檢核

- 我能定義與初始化結構。
- 我能區分型別與物件。
- 我能使用 `.` 與 `->`。
- 我能說明結構指定。
- 我能選擇值傳遞或指標傳遞。
- 我能建立與走訪結構陣列。

## 14. 本章摘要

結構把描述同一實體的不同欄位組成一個型別，讓資料關係、介面與走訪更清楚。下一章將在執行期間配置空間，並處理所有權與生命週期。

## 導覽

- [上一單元：指標](unit-06-pointers.zh-TW.md)
- [下一單元：動態記憶體](unit-08-dynamic-memory.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-07-structures.en.md)
