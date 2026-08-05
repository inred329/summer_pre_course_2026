# 正式單元 F-U09：程式如何與檔案及持久資料互動？

版本：1.0.1  
狀態：正式學生教材  
最後更新：2026-08-05  
對應英文版本：[Formal Unit F-U09: How Does a Program Interact with Files and Persistent Data?](unit-09-files.en.md)

## 文件用途與完成標準

本章供學生獨立閱讀、練習與複習。完成本章代表你能開啟、讀寫與關閉文字檔，能檢查 I/O 回傳值與 EOF，並能診斷模式、格式、寫入、關閉與資源釋放錯誤。

## 核心問題

> 當資料需要在程式結束後仍存在，程式如何讀取、寫入並判斷錯誤？

完成本章後，你應能：

1. 說明 stream、file 與持久資料。
2. 使用 `fopen`、`fprintf`、`fscanf`、`fgets` 與 `fclose`。
3. 檢查開檔、讀取、寫入與關閉結果。
4. 區分 EOF、格式錯誤與真正 I/O 錯誤。
5. 設計可重現的檔案測試。

---

## 1. 檔案讓資料跨越程式生命週期

變數通常在程式結束後消失。檔案把資料交給作業系統保存，使下一次執行仍可讀取。

```mermaid
flowchart LR
    P[程式] -->|write| F[檔案]
    F -->|read| P
```

---

## 2. 開啟、寫入與關閉

```c
#include <stdio.h>

int main(void) {
    FILE *file = fopen("scores.txt", "w");
    if (file == NULL) {
        perror("scores.txt");
        return 1;
    }

    if (fprintf(file, "%d\n", 80) < 0) {
        fprintf(stderr, "Write failed\n");
        fclose(file);
        return 1;
    }

    if (fclose(file) == EOF) {
        fprintf(stderr, "Close failed\n");
        return 1;
    }

    return 0;
}
```

模式：

- `"r"`：讀取既有檔案
- `"w"`：寫入並截斷既有內容
- `"a"`：附加到尾端

模式是需求的一部分，選錯模式可能造成資料遺失。`fopen` 成功不代表後續寫入或關閉一定成功。

---

## 3. 讀取文字資料並判斷停止原因

```c
#include <stdio.h>

int main(void) {
    FILE *file = fopen("scores.txt", "r");
    if (file == NULL) {
        perror("scores.txt");
        return 1;
    }

    int score;
    int result;

    while ((result = fscanf(file, "%d", &score)) == 1) {
        printf("%d\n", score);
    }

    if (result == EOF) {
        if (ferror(file)) {
            fprintf(stderr, "Read error\n");
            fclose(file);
            return 1;
        }
        /* normal end of file */
    } else {
        fprintf(stderr, "Invalid score format\n");
        fclose(file);
        return 1;
    }

    if (fclose(file) == EOF) {
        fprintf(stderr, "Close failed\n");
        return 1;
    }

    return 0;
}
```

不要使用 `while (!feof(file))` 作為主要讀取模式。應以讀取函數是否成功取得資料控制迴圈，再檢查停止原因。

---

## 4. EOF、格式錯誤與 I/O 錯誤

對 `fscanf(file, "%d", &score)`：

- 回傳 `1`：成功讀入一個整數
- 回傳 `EOF`：在取得數值前遇到 EOF 或輸入錯誤
- 回傳 `0`：檔案中仍有資料，但不符合整數格式

當結果為 `EOF` 時，再用 `ferror(file)` 區分真正 I/O 錯誤與正常 EOF。

---

## 5. 逐行讀取

```c
char line[100];
while (fgets(line, sizeof line, file) != NULL) {
    printf("%s", line);
}

if (ferror(file)) {
    fprintf(stderr, "Read error\n");
}
```

逐行讀取適合保留格式或再自行解析。若一行超過緩衝區，同一個實體行可能分成多次 `fgets` 才讀完。

---

## 6. 結構化文字格式

例如：

```text
1001 Amy 87.5
1002 Ben 91.0
```

格式就是一種 protocol。寫入端與讀取端必須對欄位順序、分隔方式、型別與錯誤處理有共同規則。

若姓名可能包含空白，空白分隔格式就不再足夠，應重新設計格式。

---

## 7. 錯誤案例

### 未檢查 `fopen`

直接使用 `NULL` 的 `FILE *` 是無效操作。

### 忽略 `fprintf` 或 `fclose`

成功開檔不保證緩衝資料最後真的寫入儲存裝置。應檢查寫入操作與最後關閉結果。

### 使用 `"w"` 覆蓋資料

原本想附加卻使用 `"w"`，既有內容會被截斷。先建立測試檔副本。

### `while (!feof(file))`

EOF 只有在讀取嘗試失敗後才被設定，可能導致重複處理最後資料。以讀取結果控制迴圈。

### 把格式錯誤當成 EOF

遇到無法轉成整數的文字時，`fscanf` 可能回傳 `0`。錯誤字元仍留在輸入中；若直接重試相同轉換而不處理或回報，可能形成無窮迴圈。

### 未關閉檔案

資源可能未及時釋放，緩衝資料也可能未完整寫出。確保每條成功開啟路徑都有對應且被檢查的關閉。

---

## 8. 引導練習

1. 寫入三個整數，檢查每次寫入與最後關閉。
2. 讀回資料並加總，同時判斷讀取為何停止。
3. 比較 `"w"` 與 `"a"`。
4. 加入一行格式錯誤資料，確認程式回報格式錯誤而非正常 EOF。

---

## 9. 自主練習：成績檔案報告

從文字檔讀取多筆學號、姓名與成績，輸出筆數、平均與最高分。

必測：

- 檔案不存在
- 空檔案
- 正常多筆資料
- 一筆格式錯誤
- 一行超過緩衝區
- 最後一行沒有換行

請明確定義遇到錯誤紀錄時要停止、略過還是回報，不要讓行為隱含不明。

---

## 10. 需求修改

新增輸出檔 `report.txt`，保存分析結果。請決定覆蓋或附加模式，並定義開檔、寫入與關閉失敗時程式如何回報。

---

## 11. 向 AI 解釋概念

請向 AI 解釋：

> Stream、檔案模式、EOF、格式與錯誤檢查之間有什麼關係？為什麼不應只用 `feof` 控制讀取？

AI 回應若與函式回傳規格或可重現檔案測試衝突，應以證據重新判斷。

---

## 12. 自我檢核

- 我能選擇正確開檔模式。
- 我會檢查 `fopen`、寫入結果與 `fclose`。
- 我以讀取結果控制迴圈。
- 我能區分 EOF、格式錯誤與 I/O 錯誤。
- 我能在每條成功開啟路徑關閉檔案。
- 我能設計空檔案、錯誤格式與超長輸入測試。

## 13. 本章摘要

檔案讓資料在程式結束後仍存在。可靠檔案處理需要明確格式、正確模式、檢查開啟／讀取／寫入／關閉結果、理解 EOF，並確實釋放資源。下一章將把介面與實作分開，建立可獨立維護的模組。

## 導覽

- [上一單元：動態記憶體](unit-08-dynamic-memory.zh-TW.md)
- [下一單元：模組化程式設計](unit-10-modular-programming.zh-TW.md)
- [正式課程索引](README.zh-TW.md)
- [English version](unit-09-files.en.md)
