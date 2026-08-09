# 正式單元 F-U12：如何把整門課整合成一個可維護的程式？

版本：1.1.0  
狀態：正式學生教材  
最後更新：2026-08-09  
對應英文版本：[Formal Unit F-U12: How Can the Whole Course Be Integrated into One Maintainable Program?](unit-12-integrated-application.en.md)

前十一個正式 Unit 一直在刻意拆問題：先理解值與型別，再處理控制流程、陣列、字串、函數呼叫、指標、結構、動態記憶體、檔案、模組與測試。

真實程式不會把這些 Concept 分章出現。

一個看似簡單的「成績紀錄管理器」就可能同時需要：

```text
Student 結構
StudentList 動態陣列
指標與 ownership
檔案格式
模組介面
錯誤處理
邊界與回歸測試
```

最後一個 Unit 的目標不是塞進最多功能，而是回答：

> 當很多 Concept 同時存在時，我們能不能仍然清楚說明資料在哪裡、誰負責修改、什麼狀態才有效、哪一步可能失敗，以及用什麼證據確認程式沒有被改壞？

---

## 1. 先不要寫選單，先寫使用者真正看得到的行為

我們要做一個小型成績紀錄管理器。

第一版需求：

1. 新增包含學號、姓名與成績的學生紀錄。
2. 顯示目前所有紀錄。
3. 依學號查詢。
4. 計算平均成績。
5. 儲存到文字檔。
6. 從文字檔載入。
7. 成績只允許 0～100。
8. 無效輸入、配置失敗與檔案格式失敗要能被區分。

在寫函數以前，先替幾條需求寫可觀察證據：

| 需求 | 可以觀察什麼？ |
|---|---|
| 新增有效紀錄 | `count` 增加，而且列表中真的出現該紀錄 |
| 拒絕無效成績 | 清單不變，呼叫者得到失敗 |
| 平均 | 和手算結果一致 |
| 空集合平均 | 回報「沒有結果」，不除以零 |
| 儲存 | 檔案內容符合格式，而且寫入／關閉成功 |
| 載入 | 依明確政策重建資料；失敗時原資料狀態可預測 |

一個函數存在，不代表一項需求已完成。需求要能被實際觀察與測試。

---

## 2. 先決定資料長什麼樣，再談操作

沿用 F-U07：

```c
#include <stddef.h>

#define NAME_SIZE 50

typedef struct {
    int id;
    char name[NAME_SIZE];
    int score;
} Student;
```

現在再建立一個可成長集合：

```c
typedef struct {
    Student *items;
    size_t count;
    size_t capacity;
} StudentList;
```

畫圖：

```text
StudentList
├── items ─────► 動態配置的 Student 陣列
├── count       已經有效的紀錄數
└── capacity    目前實際可容納的元素數
```

這三個欄位不能各自隨便變。

我們先寫出 invariant：

```text
count <= capacity
capacity == 0 時 items == NULL
capacity > 0 時 items 指向至少 capacity 個 Student 的配置
items[0] ... items[count - 1] 都是有效、已初始化紀錄
```

從現在開始，每個操作都要問：

> 成功後 invariant 還成立嗎？失敗後呢？

---

## 3. 第一個里程碑：只有「空清單」和「釋放」

```c
#include <stdlib.h>

int list_init(StudentList *list) {
    if (list == NULL) {
        return 0;
    }

    list->items = NULL;
    list->count = 0;
    list->capacity = 0;
    return 1;
}

void list_destroy(StudentList *list) {
    if (list == NULL) {
        return;
    }

    free(list->items);
    list->items = NULL;
    list->count = 0;
    list->capacity = 0;
}
```

先不要急著新增資料。

先驗證：

```text
init 後是不是空 invariant？
destroy 後是不是又回到空 invariant？
空清單 destroy 是否安全？
NULL list 的政策是否明確？
```

如果最小生命週期都說不清楚，加入更多功能只會讓 ownership 更難追。

---

## 4. 第二個里程碑：新增一筆資料，而且失敗不能破壞舊狀態

```c
#include <stdint.h>
#include <stdlib.h>

int list_add(StudentList *list, const Student *student) {
    if (list == NULL || student == NULL) {
        return 0;
    }

    if (student->score < 0 || student->score > 100) {
        return 0;
    }

    if (list->count > list->capacity) {
        return 0;  /* 進來以前 invariant 已經壞了 */
    }

    if (list->count == list->capacity) {
        size_t new_capacity;

        if (list->capacity == 0) {
            new_capacity = 4;
        } else {
            if (list->capacity > SIZE_MAX / 2) {
                return 0;
            }
            new_capacity = list->capacity * 2;
        }

        if (new_capacity > SIZE_MAX / sizeof *list->items) {
            return 0;
        }

        Student *new_items = realloc(
            list->items,
            new_capacity * sizeof *list->items
        );

        if (new_items == NULL) {
            return 0;
        }

        list->items = new_items;
        list->capacity = new_capacity;
    }

    list->items[list->count] = *student;
    list->count++;
    return 1;
}
```

這段看似把很多 Unit 混在一起，其實可以按順序閱讀：

```text
指標參數有效？             F-U06
Student 內容有效？          F-U07
count/capacity invariant？  F-U03 + F-U08
容量乘法安全？              F-U01 + F-U08
realloc 保留舊 owner？       F-U08
結構值複製？                 F-U07
成功後才增加 count？         F-U02 + invariant reasoning
```

最重要的契約是：

> 只要傳入清單原本符合 invariant，`list_add` 回傳失敗時，原本的清單內容、`items`、`count` 與 `capacity` 都保持可用且不變。

所以可能失敗的成長工作全部先完成，最後才提交新 metadata 與新元素。

---

## 5. 第三個里程碑：先用固定資料做查詢與平均

不要立刻加入鍵盤輸入與檔案。

先在程式裡建立兩筆已驗證資料，測：

```text
list_add
list_find_by_id
list_average
```

平均介面：

```c
int list_average(const StudentList *list, double *average) {
    if (list == NULL || average == NULL || list->count == 0) {
        return 0;
    }

    double sum = 0.0;
    for (size_t i = 0; i < list->count; i++) {
        sum += (double)list->items[i].score;
    }

    *average = sum / (double)list->count;
    return 1;
}
```

這裡的空集合契約很清楚：

```text
count == 0
→ 沒有平均值
→ 回傳失敗
→ 不修改 *average
```

不是讓程式先除以零，再觀察平台會產生什麼。

每筆成績被限制在 0～100，因此使用 `double` 累加避免先在 `int` 中累加造成有號整數溢位。不過真實產品如果允許極大量紀錄，仍要定義可接受的數量與浮點誤差。

---

## 6. 追蹤一次成長，確認 ownership 沒有消失

初始：

```text
items = NULL
count = 0
capacity = 0
```

第一次需要空間：

```text
items ─────► [ Student ][ Student ][ Student ][ Student ]
count = 0
capacity = 4
```

加入一筆：

```text
items ─────► [ valid ][ unused ][ unused ][ unused ]
count = 1
capacity = 4
```

之後若成長到 8，`realloc` 可能搬移：

```text
舊位置 X
新位置 Y ──► [ 8 個 Student 空間 ]
```

所以 `StudentList.items` 是 owner；`main` 不應保存某個元素的長期指標，然後又在清單成長後假設它仍然有效。

這就是跨 Concept 整合真正困難的地方：單獨看「找學生」很簡單，但一旦集合可搬移，F-U06 的 alias lifetime 和 F-U08 的 realloc 規則會一起影響設計。

---

## 7. 第四個里程碑：替程式畫出模組邊界

一個合理的第一版：

```text
student.h / student.c
    建立與驗證 Student
    有界姓名處理

student_list.h / student_list.c
    list ownership
    add / find / average / destroy

storage.h / storage.c
    檔案格式
    save / transactional load

main.c
    使用者輸入
    呼叫模組
    顯示結果
```

`main.c` 不應直接寫：

```c
list.capacity *= 2;
list.items = realloc(...);
```

因為那會繞過 `student_list` 模組負責維持的 invariant。

模組邊界的意義是：

> 誰有權修改哪一段狀態？哪一組規則由哪個模組負責？

---

## 8. 第五個里程碑：先定義檔案 protocol，再實作 save/load

例如第一版格式：

```text
1001,Alice,80
1002,Bob,95
```

先回答：

- 姓名可以包含逗號嗎？
- 空白行允許嗎？
- ID 可以重複嗎？
- 最後一行沒有換行是否接受？
- 成績或欄位格式錯誤時整份 load 怎麼辦？

本章採用 **transactional replace**：

```text
建立空的 temporary list
→ 從檔案逐筆解析／驗證／加入 temporary
→ 任一失敗：destroy temporary，原 list 完全不變
→ 全部成功：destroy 原 list，把 temporary 的 ownership 移交給正式 list
```

這讓 `list_load_replace` 的失敗行為很容易說明：

> 回傳失敗時，呼叫者原本的資料仍然存在。

Ownership 移交後，temporary 必須被重設成空狀態，避免之後再次 destroy 同一塊配置。

儲存成功也必須同時代表：需要的寫入都成功，而且最後 `fclose` 沒有回報失敗。

---

## 9. 第六個里程碑：現在才加入互動式輸入

到這一步，核心資料操作已能用固定測試資料獨立驗證。

`main` 再負責：

```text
讀 command
→ 檢查讀取成功
→ 讀 Student 欄位
→ 驗證
→ 呼叫 list / storage API
→ 根據回傳結果輸出訊息
```

不要把解析、驗證、realloc、檔案格式與 UI 全塞進一個巨大 `switch`。

每次 `scanf`／`fgets` 都遵守之前的規則：**確認讀取成功、確認取得完整資料，再使用輸出。**

一個簡單文字選單就足夠；本章不靠花俏 UI 展示整合能力。

---

## 10. 把整合測試按責任分層

### Student 層

- 0、100 合法。
- -1、101 失敗。
- 姓名容量邊界。
- 過長／未終止字串依 setter 契約拒絕。

### StudentList 層

- 空清單。
- 第一筆加入。
- 超過初始容量後資料仍完整。
- 找得到／找不到 ID。
- 重複 ID 政策。
- 空平均失敗且不修改 output。
- 模擬／推理容量極限時狀態不變。

### Storage 層

- 正常 round trip。
- 檔案不存在。
- 格式錯誤。
- 過長紀錄。
- 最後一行無換行。
- Load 中途失敗時正式清單保持原狀。
- Save 的 write／close 失敗政策。

### 整合／回歸層

- 從新增到儲存、重新載入、再查詢的一條完整使用情境。
- 模組重構後重跑全部案例。
- 需求修改後，同時跑新案例與不應改變的舊案例。

每一筆測試都先寫預期再執行。

---

## 11. 幾個整合 bug，試著指出它破壞哪一層規則

### 直接覆蓋 `realloc` owner

```c
list->items = realloc(list->items, new_size);
```

可能在失敗時失去舊配置 owner。這是 ownership／failure-state defect。

### 成功以前先 `count++`

如果後面配置或複製失敗，`count` 已經宣告一筆不存在的有效元素。這是 invariant defect。

### Load 到一半直接改正式 list

第六行壞掉時前五筆已被替換。若契約說 transactional replace，這是 transaction defect。

### 把 storage parser 寫進 `main`

程式可能還能工作，但第二個前端若也需要載入就得複製規則。這是 module-boundary defect。

### 只修新功能，不跑舊案例

新需求看起來成功，卻不知是否破壞舊 round-trip、空集合或容量邊界。這是 evidence gap。

這些問題來自不同 Unit，但現在都能用同一張應用程式圖定位。

---

## 12. 自主整合練習：完成第一版管理器

建議按 commit／小步驟前進：

```text
1. Student validation
2. empty StudentList lifecycle
3. add fixed records
4. find / average
5. growth boundary
6. module split
7. save
8. transactional load
9. interactive input
10. integrated regression tests
```

每一步都保持程式在一個可以編譯、測試、解釋的狀態。

如果某一步出錯，不要再同時加入兩個新功能；先用 F-U11 的方法找到第一個不一致。

---

## 13. 最後的需求修改：每位學生有多次成績

新需求：

> 每位學生可有 0 筆以上成績，並可顯示個人平均。

不要直接在 `Student` 裡隨便塞 `int scores[100]` 就結束。

先分析：

### 資料模型

成績數量是否固定？需要動態陣列嗎？

### Nested ownership

如果每個 `Student` 自己擁有一個動態配置成績陣列：

```text
StudentList owns Student array
each Student owns score array
```

那麼複製 `Student` 不能再單純依賴結構指定，否則只會複製 pointer value，形成共享 ownership／double-free 風險。

### 空成績

0 筆成績的平均要回報「沒有結果」，不是除以零。

### 檔案格式

舊的每行一個 score 格式不再夠用。新格式如何表示多筆成績？舊檔怎麼轉換？

### 模組介面

哪些新函數需要被公開？Ownership transfer 規則是什麼？

### 測試

至少新增：0 筆、1 筆、多筆、成長失敗、深層複製／釋放、舊檔轉換與 transactional load。

這個修改故意不提供唯一答案。真正要驗證的是你能不能在改 code 前先看到**資料模型改變會沿 ownership、file protocol、API 與 test plan 一路傳播。**

---

## 14. 選做：讓 AI 挑戰你的整合圖

這一節完全可以跳過。

先不用任何工具，自己畫：

```text
使用者
→ main
→ Student / StudentList
→ dynamic storage
→ storage module
→ file
```

再標示 ownership、可能失敗的位置與哪些 test 能觀察結果。

如果你想多做一次檢查，可以讓 AI 找一個你圖上漏掉的 failure path 或 ownership transfer。你不需要固定 Prompt，也不需要保存或繳交對話。

AI 建議如果和實際函數契約、型別範圍、檔案 protocol、記憶體生命週期或可重現測試衝突，仍然回到工程證據判斷。

---

## 15. 離開正式課程教材以前，確認你能回答「為什麼這個程式值得信任」

不要只展示程式能跑。

試著完整說明：

- 使用者需求如何變成可觀察驗收行為？
- `StudentList` invariant 是什麼？哪幾個函數負責維持它？
- 動態配置的 owner 是誰？何時 transfer？何時 free？
- `realloc` 失敗為什麼不會破壞舊清單？
- 空集合平均怎麼定義？
- Load 為什麼使用 temporary list？失敗時正式狀態是什麼？
- 哪些細節留在 module 內，哪些是公開契約？
- 你有哪些 boundary、invalid、transaction 與 regression evidence？
- 當「一個 Student 有多筆成績」加入時，哪些舊假設不再成立？

如果其中一題只能說「因為程式現在會跑」，就回到對應 Unit 的模型再補證據。

---

## 16. 正式課程收尾

這門課一路使用 C，不是要把語法清單背得最長，而是練習一種可以轉移到其他程式與工具的推理方式：

```text
先說清楚需求
→ 建立資料與狀態模型
→ 定義介面與失敗行為
→ 在操作以前確認邊界與前提
→ 追蹤 ownership / lifetime / invariant
→ 把大問題分成可獨立驗證的責任
→ 用測試、錯誤重現與回歸證據支持結論
→ 需求改變時重新檢查受影響的假設
```

如果你能拿一段沒看過的 C 程式，指出它的資料、控制流程、生命週期、介面假設與失敗路徑，並設計實驗驗證自己的判斷，那就已經超過「會不會背某個函式名稱」。

這也是整套教材真正要留下的能力。

## 導覽

- [上一單元：測試、診斷與改善](unit-11-testing-debugging.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [教材總索引](../README.zh-TW.md)
- [English version](unit-12-integrated-application.en.md)
