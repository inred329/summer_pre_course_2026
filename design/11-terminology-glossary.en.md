# Chinese–English Terminology Glossary

Version: 0.1.1  
Status: Active design standard  
Governance note: This glossary standardizes terminology only. The Constitution and official learning/assessment policy remain authoritative for governance, grading, and tool-use rules.  
Corresponding Chinese version: [中英文術語對照表](11-terminology-glossary.zh-TW.md)

## Document Purpose

This document provides the terminology standard used across course design, student materials, instructor resources, activities, and assessment implementation so that the same concept is not silently renamed or given conflicting meanings.

Its primary readers are instructors, teaching assistants, material authors, translators, and maintainers. Important terminology changes must be made in both language versions and propagated to affected documents.

## Usage Rules

1. Use an approved term consistently when the same concept is intended.
2. Provide both Chinese and English on first introduction when that improves bilingual maintenance or student comprehension.
3. Prefer professional English usage over literal translation.
4. Distinguish language semantics, conceptual teaching models, and implementation-specific behavior in the usage note.
5. C keywords, function names, identifiers, and standard-library names are generally not translated.
6. A glossary entry does not by itself make a topic core, assessed, or mandatory.

---

## Course Design and Governance

| Chinese | English | Usage note |
|---|---|---|
| 課程憲法 | Course Constitution | Highest repository-level governing principles and amendment rules. |
| 正式學習與評量制度 | Official Learning and Assessment Policy | Sole authoritative source in this repository for grading, participation, homework, final oral-exam role, and AI/tool-use policy. |
| 設計標準 | Design Standard | Stable maintenance definition such as competency, scope, terminology, concept, or Unit structure; subordinate to Constitution and official policy. |
| 規劃與追蹤模型 | Planning and Traceability Model | Revisable design rationale, mapping, delivery, risk, or outline document; not an independent policy source. |
| 領域模型 | Domain Model | Describes concepts and relationships; does not define one teaching order. |
| 知識依賴圖 | Knowledge Dependency Graph | Describes strong, supporting, cross-cutting, or conditional dependencies. |
| 能力地圖 | Competency Map | Defines observable programming capabilities, identifiers, evidence expectations, and target maturity relationships. |
| 範圍邊界 | Scope Boundary | Defines what is core, foundation-only, deferred, out of scope, or conditional/optional. |
| 驗收模型 | Acceptance Model | Planning model that maps maturity to candidate evidence/task forms; it does not independently create grading policy. |
| 交付地圖 | Delivery Map | Planning model for pacing and activity placement; it implements rather than defines policy. |
| 風險登錄表 | Risk Register | Records risks, triggers, mitigation, contingency, and accountable roles. |
| 追蹤矩陣 | Traceability Matrix | Connects requirements, concepts, competencies, scope, evidence, Units/materials, and risk. |
| 學習證據 | Learning Evidence | Observable behavior or work that supports a capability claim. |
| 成熟度 | Maturity | Observable degree of capability: recognize, explain, trace, implement, diagnose, transfer. |

### Scope states

| Code | Chinese | English | Meaning |
|---|---|---|---|
| SB-C | 核心交付 | Core Delivery | Required capability at the stated stage/maturity. |
| SB-F | 基礎鋪墊 | Foundation Only | Terminology/model/purpose is established without claiming independent implementation. |
| SB-D | 後續深化 | Deepen Later | Initial capability exists; higher maturity is deferred. |
| SB-I | 延後實作 | Implement Later | Understanding/tracing may occur before full implementation/diagnosis. |
| SB-O | 課程外 | Out of Scope | Not a current core deliverable. |
| SB-X | 條件式／選用 | Conditional / Optional | Applies only when the corresponding optional activity/tool is actually used or explicitly approved as an objective; not a universal completion gate. |

---

## Program Translation and Execution

| Chinese | English | Usage note |
|---|---|---|
| 原始碼 | Source Code | Human-readable program text supplied to an implementation, commonly in `.c`/`.h` files for this course. |
| 前置處理行為 | Preprocessing Behavior | C translation behavior involving directives, file inclusion, macro replacement, and conditional processing. A standalone preprocessor program/file is not guaranteed. |
| 編譯／轉換 | Compilation / Translation | Conceptual responsibility of translating C source/translation units toward executable or lower-level representation. Implementation stages may be fused. |
| 編譯器 | Compiler | Common name for a tool or implementation component that translates source and reports diagnostics; concrete behavior depends on the specified implementation. |
| 組譯 | Assembly | Translation from assembly language to object/machine representation in toolchains that expose such a stage. Not a mandatory standalone C-language stage. |
| 目的碼／目的檔 | Object Code / Object File | Common native-toolchain intermediate representation/file used for linking; not guaranteed as a visible artifact by the C standard. |
| 連結 | Linking | Where applicable, combines translated units/libraries and resolves external references. |
| 連結器 | Linker | Tool or implementation component that performs linking in toolchains exposing a separate linker. |
| 可載入程式映像 | Loadable Program Image | Program representation that the target environment can load or otherwise execute; “executable file” is a common implementation form. |
| 載入／啟動 | Loading / Startup | Target-environment preparation of a program for execution. |
| 程序 | Process | A common operating-system model for a running program and its resources/state; not a universal property of every C execution environment. |
| 診斷 | Diagnostic | Message or other implementation feedback associated with translation/build or execution conditions. |
| 標準函式庫 | Standard Library | Functionality specified by the C standard library and provided by a conforming implementation subject to standard requirements. |

---

## Data, State, Control, and Functions

| Chinese | English | Usage note |
|---|---|---|
| 資料 | Data | Information represented, processed, stored, or communicated. |
| 值 | Value | Information content associated with an expression or object. |
| 型別 | Type | Defines/limits representation, values, operations, conversions, and interpretation according to C semantics. |
| 物件 | Object | Region of data storage in the C abstract machine whose contents can represent values. Do not use “object” to imply C++ object-oriented semantics. |
| 變數 | Variable | Course-friendly term for a named object whose stored value may change; when precision matters, distinguish the identifier/name from the object itself. |
| 識別碼 | Identifier | Name token that can designate program entities according to scope/linkage rules. |
| 常數 | Constant | Context-dependent term. Distinguish literals, enumeration constants, constant expressions, and `const`-qualified objects rather than treating them as identical. |
| 運算式 | Expression | Language construct that is evaluated according to C rules and may produce a value and/or side effects. |
| 指定 | Assignment | Stores a value into a modifiable object subject to type/conversion rules. |
| 狀態 | State | Relevant program/object/stream/control information at a given observation point. |
| 順序 | Sequence | Ordered evaluation/execution relationship. Avoid implying a total order where C leaves evaluation order unspecified. |
| 條件 | Condition | Expression/result used to decide control behavior. |
| 選擇 | Selection | Chooses among execution paths based on conditions, e.g. `if`/`switch`. |
| 重複 | Repetition | Repeated execution under stated continuation/termination rules. |
| 終止條件 | Termination Condition | Condition or state that determines when repetition stops. |
| 不變條件 | Invariant | Property intended to remain true at specified points of a computation, commonly loop reasoning. |
| 函數 | Function | Callable unit with a type/interface and implementation/definition as applicable. |
| 參數 | Parameter | Object/identifier declared in a function definition/declaration that receives call data according to C semantics. |
| 引數 | Argument | Expression supplied in a function call. |
| 回傳值 | Return Value | Value returned by a function whose return type permits a value. |
| 介面 | Interface | Information a caller/user needs: names, types, contracts, preconditions, postconditions, ownership/lifetime rules where relevant. |
| 實作 | Implementation | Internal mechanism that fulfills an interface or language/toolchain realization. |
| 模組化 | Modularization | Organizing responsibilities behind explicit interfaces and source/build boundaries. |
| 遞迴 | Recursion | Direct or indirect function-call recurrence requiring a termination/base condition for intended finite computation. |

---

## Memory and Lifetime

| Chinese | English | Usage note |
|---|---|---|
| 儲存空間／儲存位置 | Storage / Storage Location | Memory/storage associated with objects in the abstract or target machine model. |
| 位址 | Address | Representation/value used to identify or refer to storage/object/function locations under the relevant model. Do not describe every address as a portable integer. |
| 指標 | Pointer | Typed C object/value category capable of representing a pointer to an object/function or a null pointer value as allowed by the type. |
| 空指標 | Null Pointer | Pointer value guaranteed not to point to an object/function; do not call it a “null reference” in C. |
| 取址 | Address-of | `&` operation obtaining a pointer to an eligible object/function subject to C rules. |
| 解參考 | Dereference / Indirection | `*`-based access through a pointer; valid only when the pointer and operation satisfy relevant lifetime, type, alignment, bounds, and other preconditions. |
| 別名 | Aliasing | Multiple access paths designate the same or overlapping stored object; C aliasing/effective-type rules may constrain valid accesses. |
| 範圍 | Scope | Region of program text in which an identifier is visible. |
| 生命週期 | Lifetime | Portion of program execution during which an object exists; distinct from identifier scope. |
| 儲存期 | Storage Duration | C classification controlling minimum lifetime/storage association: automatic, static, thread (if supported), or allocated. |
| 自動儲存期 | Automatic Storage Duration | Storage duration generally associated with block entry/exit; a physical stack is a common implementation, not a language guarantee. |
| 配置儲存期 | Allocated Storage Duration | Course term for storage obtained via allocation functions and lasting until deallocation; use “allocated storage” rather than pretending C defines a language-level `heap`. |
| Call Stack / 呼叫堆疊 | Call Stack | Common implementation/teaching model for nested calls/activation records; useful for reasoning but not mandated as a physical structure by C. |
| Heap | Heap | Informal implementation term for a dynamic-allocation region. Do not confuse with the heap data structure or treat it as C-standard terminology. |
| 所有權／釋放責任 | Ownership / Release Responsibility | Design/API responsibility for who may use, transfer, or release a resource. C has no language-enforced ownership system. |
| 記憶體安全 | Memory Safety | Avoiding invalid lifetime/bounds/access behavior such as out-of-bounds access, dangling use, double free, and related undefined behavior. |

---

## Data Organization and Interaction

| Chinese | English | Usage note |
|---|---|---|
| 序列 | Sequence / Ordered Collection | Collection whose elements have an order/position; distinguish from execution sequence by context. |
| 索引 | Index | Value used to select an element; validity depends on the data structure and bounds. |
| 陣列 | Array | C object type containing a contiguously allocated nonempty set of elements of one element type; classroom examples must state length/bounds. |
| 字串 | String | In C, a contiguous sequence of characters terminated by and including the first null character; not every `char` array is a string. |
| 記錄 | Record | Conceptual grouping of related fields describing one entity. |
| 結構 | Structure / `struct` | C mechanism for a structure type containing named members; a concrete mapping of the record concept. |
| 輸入 | Input | Data supplied from an external source to a program/function. |
| 輸出 | Output | Observable data/result produced for an external destination. |
| 串流 | Stream | C standard-I/O abstraction representing an ordered character sequence associated with an external file/device. |
| 緩衝區 | Buffer | Storage used temporarily for input/output or transformation; its capacity and valid content must be explicit where safety matters. |
| 檔案 | File | External data source/destination as modeled by the environment/C I/O library; distinguish path/name from an opened stream. |
| 輸入結束 | End of Input / End-of-File indication | Condition/results indicating no more input; `EOF` is a macro value used by certain functions, not a character stored in every file. |
| 格式 | Format | Rules for representing/parsing data, including `printf`/`scanf` conversion specifications and file protocols. |
| 協定 | Protocol | Agreed structure/order/meaning for interaction or serialized data. |

---

## Testing, Debugging, and Optional External Assistance

| Chinese | English | Usage note |
|---|---|---|
| 預期結果／預期性質 | Expected Result / Expected Property | Behavior/property derived from requirement/contract before relying on observed output. |
| 實際證據 | Actual Evidence | Observed diagnostics, output, state trace, file content, memory-tool evidence, or other relevant observation. |
| 測試案例 | Test Case | Concrete input/conditions and expected result/property. |
| 正常案例 | Normal Case | Ordinary valid-use case. |
| 邊界案例 | Boundary Case | Case near a defined range/transition/size boundary. |
| 無效輸入案例 | Invalid-Input Case | Input that violates stated input contract and whose required handling must be specified. |
| 失敗案例 | Failure Case | Case exercising a possible operation/resource failure such as allocation, file open, parse, or write failure. |
| 執行／狀態追蹤 | Execution / State Trace | Stepwise record of relevant control, values, calls, streams, objects, or lifetimes. |
| 測試 | Testing | Executing/evaluating selected cases against expected properties. |
| 驗證 | Verification | Gathering evidence that an implementation or claim satisfies a stated technical requirement/contract. |
| 確認需求適切性 | Validation | Gathering evidence that the implemented behavior addresses the intended need/use context; distinguish from “verification.” |
| 除錯 | Debugging | Reproduce, narrow, hypothesize, test the cause, correct, and regress. |
| 回歸驗證 | Regression Verification | Rechecking previously required behavior after a change or correction. |
| 外部協助 | External Assistance | Advice/content from AI, documentation, peers, instructors, tools, or other sources. Core reasoning responsibility remains with the learner. |
| AI 輔助學習 | AI-assisted Learning | Optional use of AI to support learning; not a universal capability, completion gate, or evidence requirement. |
| 人工審查 | Human Review | Learner/instructor checks relevance, assumptions, limitations, and fit of a suggestion before adoption. |
| 技術驗證 | Technical Verification | Reproducible check using programs, tests, diagnostics, reliable references, tracing, or other appropriate evidence. |
| 情境式揭露 | Contextual Disclosure | Tool-use attribution/record required only when a specific approved activity, integrity rule, or assessment condition requires it. Non-use requires no declaration by default. |
| AI 使用紀錄 | AI-use Record | A possible contextual artifact when explicitly required; never assumed to be a universal homework or assessment requirement. |

---

## Maturity Terms

| Level | Chinese | English |
|---|---|---|
| L0 | 尚未建立 | Not Established |
| L1 | 辨識 | Recognize |
| L2 | 解釋 | Explain |
| L3 | 追蹤 | Trace |
| L4 | 實作 | Implement |
| L5 | 診斷 | Diagnose |
| L6 | 遷移 | Transfer |

The Concept Registry must use these maturity meanings or explicitly map any local shorthand to them; it must not silently redefine L1–L6.

## Maintenance Criteria

This glossary is maintained when:

- both language versions are substantively equivalent;
- defined terms are consistent with current C semantics and repository governance;
- conceptual vs implementation-specific terms are marked;
- deprecated or misleading terminology is corrected across dependent documents;
- new terms do not silently create scope, policy, or assessment requirements;
- changes remain traceable through Git history and the active repository audit.

## Related Documents

- [Instructional Design Workspace](README.en.md)
- [Programming Domain Model](03-programming-domain-model.en.md)
- [Programming Competency Map](05-competency-map.en.md)
- [Course Scope Boundary](06-scope-boundary.en.md)
- [Programming Concept Tree](14-programming-concept-tree.en.md)
- [Programming Concept Registry](15-programming-concept-registry.en.md)
- [繁體中文版](11-terminology-glossary.zh-TW.md)
