# 正式單元 F-U10：程式如何分成可獨立維護的模組？

版本：1.1.0  
狀態：正式學生教材  
最後更新：2026-08-09  
對應英文版本：[Formal Unit F-U10: How Can a Program Be Divided into Independently Maintainable Modules?](unit-10-modular-programming.en.md)

到 F-U09 為止，我們已經有學生資料、動態陣列、檔案讀寫、分析函數與錯誤處理。

如果全部繼續放在同一個 `main.c`，程式仍然可以運作，但每次修改都會出現新的負擔：

> 我只是想改平均計算，為什麼還要重新翻過檔案解析？我只是想做另一個前端，為什麼要複製同一批學生函數？

模組化要解決的不是「檔案太長看起來不好看」，而是**讓不同責任可以透過穩定介面彼此合作，而不必知道所有內部細節。**

---

## 1. 先把「呼叫者需要知道什麼」和「內部怎麼做」分開

假設平均計算對外提供：

```c
int calculate_average(const int values[],
                      int length,
                      double *result);
```

呼叫者真正需要知道的是：

- 要提供哪些資料？
- 哪些輸入有效？
- 成功時得到什麼？
- 失敗時哪些東西不會被修改？

它不需要知道內部是 `for` 還是 `while`，也不需要知道模組是否使用額外 helper。

這些「呼叫者需要依賴的承諾」就是**介面（interface）**。

實際完成工作的程式碼則是**實作（implementation）**。

---

## 2. Header 保存公開介面，source 保存實作

`score.h`：

```c
#ifndef SCORE_H
#define SCORE_H

int calculate_average(const int values[],
                      int length,
                      double *result);
int is_passing(double average, double threshold);

#endif
```

`score.c`：

```c
#include <stddef.h>
#include "score.h"

int calculate_average(const int values[],
                      int length,
                      double *result) {
    if (values == NULL || result == NULL || length <= 0) {
        return 0;
    }

    double sum = 0.0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    *result = sum / (double)length;
    return 1;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}
```

`main.c`：

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
    printf("%s\n",
           is_passing(average, 60.0) ? "Pass" : "Try again");
    return 0;
}
```

呼叫者只 include `score.h`，依賴的是介面承諾。

`score.c` 自己也 include `score.h` 很重要：如果實作函數型別和公開宣告不一致，編譯器就有機會直接指出衝突，而不是讓兩份描述各自漂移。

---

## 3. 一個好的介面不只描述成功，也描述失敗

例如 `calculate_average` 的第一版契約可以是：

```text
values 指向至少 length 個可讀 int
length > 0
result != NULL
成功：回傳 1，寫入 *result
失敗：回傳 0，不修改 *result
```

這些規則比「函數叫 calculate_average」更重要。

因為呼叫者可以依契約寫：

```c
if (!calculate_average(values, length, &average)) {
    /* 不使用 average 當成新結果 */
}
```

而模組內部也能改寫演算法，只要仍然遵守同一個公開契約。

本例用 `double` 累加，避免先在 `int` 中把許多值相加而發生有號溢位；但這不代表任意資料量都具有無限精度。真正的應用仍應由需求決定可接受範圍與誤差。

---

## 4. Include guard 解決「同一個 header 可能沿不同路徑被包含」

```c
#ifndef SCORE_H
#define SCORE_H

/* declarations and type definitions */

#endif
```

大型程式可能出現：

```text
main.c
├── includes a.h
│   └── includes score.h
└── includes b.h
    └── includes score.h
```

Include guard 讓同一個 header 的內容在一個 translation unit 中只展開一次。

這對 typedef、struct definition 等特別重要，也讓 header 可以被安全地從不同依賴路徑使用。

一個實用原則是：

> Header 應該自己包含它公開介面真正需要的型別宣告，不要要求使用者「剛好先 include 某個別的 header」才編得過。

---

## 5. `#include` 之後，各 `.c` 會形成自己的 translation unit

編譯：

```bash
gcc -std=c17 -Wall -Wextra -pedantic -c main.c
gcc -std=c17 -Wall -Wextra -pedantic -c score.c
```

得到：

```text
main.c  ──compile──► main.o
score.c ─compile──► score.o
```

接著：

```bash
gcc main.o score.o -o report
```

連結：

```text
main.o + score.o ──link──► report
```

這讓我們第一次可以非常清楚地區分兩類錯誤。

### Compile-stage 問題

例如 `main.c` 看不到函數宣告、型別不相容、語法錯誤。

### Link-stage 問題

例如 `main.c` 已經知道有 `calculate_average` 這個函數，也能成功編譯，但最後忘了把提供定義的 `score.o` 放進 linker：

```text
undefined reference to calculate_average
```

這不是語法錯誤，而是「需要的定義最後沒有被接進程式」。

---

## 6. 公開的東西越少，模組越容易改

假設平均計算內部想使用：

```c
static double sum_values(const int values[], int length) {
    double sum = 0.0;

    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    return sum;
}
```

如果只有 `score.c` 需要它，就沒有必要放進 `score.h`。

把它留在 implementation 內，並使用適當的 internal linkage，呼叫者就不會開始依賴這個 helper。

未來你可以：

- 改名。
- 移除。
- 改用另一個演算法。

而不需要修改所有使用 `score` 模組的程式。

這就是「資訊隱藏」最實際的價值：**不是把東西藏起來顯得神祕，而是減少外部必須跟著改的依賴。**

---

## 7. 三種錯誤可以直接用模組邊界來診斷

### 宣告和定義不一致

Header：

```c
int calculate_average(const int values[],
                      int length,
                      double *result);
```

Source 卻寫成另一種函數型別。因為 `score.c` include 自己的 header，編譯器應能指出衝突。

### 把一般外部函數定義直接放在 header

若多個 `.c` 都 include 這個 header，最後可能產生多個外部定義並在 link 階段衝突。

不要因此背成「header 永遠不能有 function body」；像適當設計的 `static inline` 有不同規則。現在先抓住目的：**不要無意間讓每個 translation unit 都產生同一個外部定義。**

### 忘記 link 某個 object file

每個 `.c` 都成功 compile，最後仍可能因缺少定義而 link 失敗。

所以看到錯誤訊息先問：

> 問題發生在某個 translation unit 自己，還是發生在把多個 object files 組合起來時？

---

## 8. 自主練習：把學生資料拆成真正可重用的模組

建立：

```text
student.h
student.c
main.c
```

`student` 模組至少處理：

- `Student` 公開型別或呼叫端需要的等價介面。
- 初始化。
- 更新平均。
- 格式化／輸出所需資料。

不要一開始把每個 helper 都公開。

先從兩個角度畫邊界：

```text
呼叫者一定要知道什麼？
只有 student.c 自己需要知道什麼？
```

再為公開函數寫至少一個正常案例與一個失敗案例。

---

## 9. 修改需求：再加入一個前端，但不複製模組

新增：

```text
batch_report.c
```

現在有兩個前端：

```text
main.c
batch_report.c
```

它們都使用同一個 `student` 模組。

分別編譯／連結：

```text
main.o + student.o         → interactive_app
batch_report.o + student.o → batch_report
```

如果為了第二個前端，你必須進入 `student.c` 抄一份內部細節到外面，表示公開介面可能不夠合適。

反過來，如果你為了任何可能需求都把內部 helper 公開，介面又可能過大。

這個練習要找的是：**足以支援真實呼叫者，但不暴露不必要實作細節的邊界。**

---

## 10. 選做：讓 AI 挑戰你的模組邊界

這一節完全可以跳過。

先不用任何工具，自己回答：

> `score.h` 和 `score.c` 分別應該承擔什麼？如果我改寫平均計算演算法但不改介面契約，為什麼 `main.c` 理論上不需要跟著修改？

如果你想多做一次檢查，可以請 AI 指出一個「不應該公開卻被放進 header」或「呼叫者需要但介面沒有表達」的例子。你不需要固定 Prompt，也不需要保存或繳交對話。

如果它的說法和實際 include 依賴、編譯／連結結果或函數契約衝突，就回到證據重新判斷。

---

## 11. 離開這個 Unit 前，確認你能找到錯誤發生在哪一層

直接回答：

- 介面和實作分別是誰的承諾與誰的細節？
- 為什麼 `score.c` 也應 include `score.h`？
- Include guard 解決的是哪一種重複包含問題？
- `.c` 經過 compile 後產生什麼？Linker 又做什麼？
- 為什麼 `undefined reference` 可能出現在所有 `.c` 都成功編譯之後？
- 為什麼內部 helper 不一定應放在 header？
- 「失敗時不修改輸出」為什麼也是公開介面的一部分？
- 第二個前端如何幫你測試模組邊界是否真的可重用？

如果只會背 `.h`／`.c`，就畫出兩個 translation units 和最後 linker 的流程。

---

## 12. 本章收尾

F-U09 讓資料跨越程式執行；F-U10 則讓程式本身在成長時還能維持可理解的邊界。

模組化的核心不是「每幾百行就切一個檔」，而是：**公開穩定契約，把內部實作留在邊界內，讓每個 translation unit 可以獨立檢查，再由 linker 組成完整程式。**

下一個 Unit 會把「我覺得這個模組應該可以」變成更有系統的證據。我們會把前面一路使用的邊界測試、錯誤案例、回歸測試與診斷方法整理成完整的 testing、verification 與 debugging 流程。

## 導覽

- [上一單元：檔案](unit-09-files.zh-TW.md)
- [下一單元：測試、驗證與除錯](unit-11-testing-debugging.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-10-modular-programming.en.md)
