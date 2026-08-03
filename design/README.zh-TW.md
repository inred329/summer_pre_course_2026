# 教學內容設計區

版本：0.8.0  
狀態：規劃中  
對應英文版本：[Instructional Design Workspace](README.en.md)

## 文件目的

本目錄以需求工程與系統設計方式規劃 2026 暑期 C 語言前導課程及後續 16 週正式課程。

設計順序為：

1. 教育願景與問題。
2. 利害關係人及需求。
3. 程式設計領域中的核心概念與關係。
4. 理解這些概念所需的知識依賴。
5. 學生應具備的能力與成熟度。
6. 前導課程與正式課程的範圍邊界。
7. 可觀察、可驗收的學習證據。
8. 中文班、英文班與正式課程的交付節奏。
9. 設計與執行風險。
10. 需求、能力、範圍、驗收、交付與風險的追蹤關係。
11. 教材、活動、作業與評量。

## 憲法遵循

本目錄內所有正式文件，在撰寫、修改或翻譯前，均須先參考：

- [課程憲法（繁體中文）](../CONSTITUTION.zh-TW.md)
- [Course Constitution (English)](../CONSTITUTION.en.md)

每份文件至少必須：

- 促進真正理解，而非只完成產出。
- 以雙語成對建立並實質一致。
- 為能力提供先備條件與驗收方式。
- 控制初學者認知負荷。
- 同等重視閱讀、修改、測試、除錯、解釋與從零撰寫。
- 對適合視覺化的概念與關係提供圖形。
- 讓 AI 協助學習，而非取代核心思考。
- 使前導課程與正式課程形成連續能力發展。
- 能由根 README 經直接或間接導覽鏈抵達。

## 正式設計文件

| 階段 | 文件 | 用途 |
|---|---|---|
| 01 | [課程產品願景](01-product-vision.zh-TW.md) | 定義教育問題、產品定位與成功條件。 |
| 02 | [教學需求地圖](02-requirements-map.zh-TW.md) | 定義教育需求、能力需求與橫向要求。 |
| 03 | [程式設計領域模型](03-programming-domain-model.zh-TW.md) | 定義程式設計領域中存在的概念及其關係。 |
| 04 | [程式語言知識依賴圖](04-programming-language-knowledge-graph.zh-TW.md) | 定義理解核心概念時的主要先備知識與依賴。 |
| 05 | [程式設計能力地圖](05-competency-map.zh-TW.md) | 將概念與依賴轉換為學生可展現的能力、成熟度與證據。 |
| 06 | [課程範圍邊界](06-scope-boundary.zh-TW.md) | 定義前導與正式課程的核心交付、鋪墊、延後與排除範圍。 |
| 07 | [能力驗收模型](07-acceptance-model.zh-TW.md) | 定義成熟度最低證據、標準驗收任務、AI 邊界與通過判準。 |
| 08 | [課程交付地圖](08-delivery-map.zh-TW.md) | 將共同能力、成熟度與驗收證據安排到兩個前導班及 16 週正式課程。 |
| 09 | [課程風險登錄表](09-risk-register.zh-TW.md) | 定義風險優先級、觸發條件、緩解措施、應變與責任角色。 |

英文導覽：[Instructional Design Workspace](README.en.md)

## 設計文件架構

```text
design/
├── README.zh-TW.md
├── README.en.md
├── 01-product-vision.zh-TW.md
├── 01-product-vision.en.md
├── 02-requirements-map.zh-TW.md
├── 02-requirements-map.en.md
├── 03-programming-domain-model.zh-TW.md
├── 03-programming-domain-model.en.md
├── 04-programming-language-knowledge-graph.zh-TW.md
├── 04-programming-language-knowledge-graph.en.md
├── 05-competency-map.zh-TW.md
├── 05-competency-map.en.md
├── 06-scope-boundary.zh-TW.md
├── 06-scope-boundary.en.md
├── 07-acceptance-model.zh-TW.md
├── 07-acceptance-model.en.md
├── 08-delivery-map.zh-TW.md
├── 08-delivery-map.en.md
├── 09-risk-register.zh-TW.md
└── 09-risk-register.en.md
```

後續預計增加：

```text
10-traceability-matrix.*
```

## 三份核心模型的分工

| 文件 | 回答的問題 |
|---|---|
| 領域模型 | 程式設計世界有哪些概念？它們如何關聯？ |
| 知識依賴圖 | 理解某概念前通常需要理解什麼？ |
| 能力地圖 | 學生必須能做到什麼，做到什麼程度？ |

三者不得混用：領域關係不等於學習順序，知識依賴不等於週次，能力成熟度也不等於主題是否曾經介紹。

## 目前核心假設

- 教學語言為 C，但核心目標是程式設計能力與 C 的語言邏輯。
- 每個概念依「需求 → 設計目的 → 語言邏輯 → 語法 → 實作 → 驗證」展開。
- 程式設計以資料與狀態、流程與控制、函數與抽象為基本支柱。
- 工具鏈、記憶體模型、資料組織、測試除錯與 AI 素養為必要面向。
- 資料組織目前維持在序列、記錄、索引與操作的抽象層，不預設進階資料結構為課程核心。
- 能力成熟度分為辨識、解釋、追蹤、實作、診斷與遷移。
- 範圍狀態分為核心交付、基礎鋪墊、延後深化、延後實作與課程外。
- 核心能力驗收至少需要理解型與行動型兩種互補證據。
- 英文前導班共 10 小時；中文前導班共 12 小時；正式課程共 48 小時。
- 兩個前導班的共同核心學習成果與驗收標準一致。
- 中文班額外 2 小時用於更多追蹤、補救、診斷與驗收，不提高核心標準。
- 高優先風險不得透過降低驗收、擴張範圍或加入進階資料結構處理。

## 下一步

建立 `10-traceability-matrix`，把需求、領域概念、知識節點、能力、範圍狀態、驗收任務、交付階段與風險 ID 串成可檢查的追蹤關係。

## 導覽

- [返回倉庫首頁](../README.md)
- [English version](README.en.md)
