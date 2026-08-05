# 正式單元 F-U10：程式如何分成可獨立維護的模組？

版本：1.0.1  
狀態：正式學生教材  
最後更新：2026-08-05  
對應英文版本：[Formal Unit F-U10: How Can a Program Be Divided into Independently Maintainable Modules?](unit-10-modular-programming.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能把介面與實作分離，能建立 `.h` 與 `.c` 檔案、理解分開編譯與連結，並能診斷重複定義、缺少宣告、介面使用錯誤與連結錯誤。

## 核心問題

> 如何把介面與實作分開，使不同程式部分可以獨立理解、編譯與替換？

完成本章後，你應能：

1. 區分 module、interface 與 implementation。
2. 建立 header 與 source file。
3. 使用 include guard。
4. 說明 separate compilation 與 linking。
5. 定義並測試介面的前置條件與失敗行為。
6. 診斷常見編譯與連結問題。

---

## 1. 一個檔案開始承擔太多責任

當函數、結構與測試都放在同一檔案，任何修改都需要重新理解整份程式。模組把相關責任組成一個單位，並對外提供清楚介面。

---

## 2. 介面與實作

`score.h`：

```c
#ifndef SCORE_H
#define SCORE_H

int calculate_average(const int values[], int length, double *result);
int is_passing(double average, double threshold);

#endif
```

介面說明 `calculate_average` 透過回傳值表示成功或失敗，且只在成功時透過 `result` 寫入平均值。

`score.c`：

```c
#include "score.h"

int calculate_average(const int values[], int length, double *result) {
    if (values == NULL || result == NULL || length <= 0) {
        return 0;
    }

    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    *result = (double)sum / length;
    return 1;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}
```

`main.c` 只依賴介面：

```c
#include <stdio.h>
#include "score.h"

int main(void) {
    int values[] = {80, 90, 70};
    double average;

    if (!calculate_average(values, 3, &average)) {
        fprintf(stderr, "Cannot calculate average\n");
        return 1;
    }

    printf("Average: %.1f\n", average);
    printf("%s\n", is_passing(average, 60.0) ? "Pass" : "Try again");
    return 0;
}
```

預期輸出：

```text
Average: 80.0
Pass
```

呼叫端不需要知道總和如何計算，只需要知道介面契約與回傳結果。

---

## 3. Include Guard

```c
#ifndef SCORE_H
#define SCORE_H

/* declarations */

#endif
```

同一 header 可能透過不同路徑被多次包含。Include guard 防止同一翻譯單元中的宣告被重複處理。

---

## 4. 分開編譯與連結

```bash
gcc -std=c17 -Wall -Wextra -pedantic -c main.c
gcc -std=c17 -Wall -Wextra -pedantic -c score.c
gcc main.o score.o -o report
./report
```

概念流程：

```text
main.c  ──compile──► main.o
score.c ─compile──► score.o
main.o + score.o ──link──► report
```

編譯處理各翻譯單元；連結把需要的定義組合成可執行檔。

---

## 5. 公開與私有責任

只把呼叫者需要的介面放在 header。模組內部輔助函數可在 `.c` 中使用 `static`：

```c
static int sum_values(const int values[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }
    return sum;
}
```

這降低外部依賴並保留實作替換空間。若使用這個輔助函數，公開函數仍必須先驗證 `values`、`length` 與 `result`。

---

## 6. 錯誤案例

### 無效介面輸入

呼叫 `calculate_average(values, 0, &average)` 時，函數應失敗而不是除以零。輸入或輸出指標為 `NULL` 時，也應失敗且不得解參照。

在信任模組前先測試：

```c
calculate_average(values, 0, &average);   /* failure */
calculate_average(NULL, 3, &average);     /* failure */
calculate_average(values, 3, NULL);       /* failure */
```

### 把函數定義放進 header

若非適當的 `static inline` 設計，多個 `.c` 包含後可能產生重複定義。

### 宣告與定義不一致

```c
/* header */
int calculate_average(const int values[], int length, double *result);

/* source: incorrect */
double calculate_average(int values[], int length) { /* ... */ }
```

介面必須一致，編譯器警告與錯誤是重要證據。

### 忘記連結某個 object file

可能出現 undefined reference。這不是語法錯誤，而是連結階段找不到定義。

### Header 依賴不完整

若 header 使用某型別，應自行包含必要宣告，而不是依賴呼叫者剛好先包含其他檔案。

---

## 7. 引導練習

1. 把 `max_of_two` 分成 `math_utils.h`、`math_utils.c`、`main.c`。
2. 修改 `.c` 實作但不改 header，確認呼叫端不需變動。
3. 故意漏掉 `math_utils.o`，辨識連結錯誤。
4. 為模組介面加入無效輸入測試。

---

## 8. 自主練習：學生資料模組

建立：

```text
student.h
student.c
main.c
```

介面至少提供初始化、更新平均與格式化輸出。只公開呼叫者需要的型別與函數，並定義各函數遇到無效指標或無效筆數時的行為。

---

## 9. 需求修改

新增第二個前端程式 `batch_report.c`，重用同一個 `student` 模組。檢查介面是否足夠通用，避免為單一前端暴露不必要細節，並分別把兩個前端與同一模組編譯連結。

---

## 10. 向 AI 解釋概念

請向 AI 解釋：

> 模組、介面、實作、分開編譯與連結之間有什麼關係？為什麼介面除了成功行為，也必須定義失敗行為？

AI 回應若與編譯指令、檔案依賴、函數契約或可重現錯誤衝突，應以證據重新判斷。

---

## 11. 自我檢核

- 我能區分介面與實作。
- 我能建立 header 與 source file。
- 我能使用 include guard。
- 我能說明編譯與連結階段。
- 我能定義介面的前置條件與失敗行為。
- 我能診斷 undefined reference 與重複定義。
- 我只公開必要介面。

## 12. 本章摘要

模組以清楚介面隔離實作，使不同部分可獨立理解、編譯、測試與替換。可靠介面必須說明有效輸入、失敗行為與輸出責任。分開編譯產生 object files，連結把定義組合成程式。下一章將系統化建立測試、驗證與除錯證據。

## 導覽

- [上一單元：檔案](unit-09-files.zh-TW.md)
- [下一單元：測試、驗證與除錯](unit-11-testing-debugging.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-10-modular-programming.en.md)
