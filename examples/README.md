# C17 Examples and Defect Cases

Version: 0.3.0  
Status: Instructor verification resource  
Last updated: 2026-08-07  
Governance note: This directory provides technical examples and defect cases. It does not create grading, homework, participation, or AI/tool-use policy; those rules remain governed by the official learning and assessment policy.

## Purpose

These files support prediction, tracing, implementation, testing, debugging, requirement modification, regression verification, and discussion of technical evidence for Preparatory Units 1–4.

AI or other external-suggestion review may be offered as an optional extension. The core example path never requires AI use, an AI log, a fixed prompt, or a non-use declaration.

## Target Compilation

For the current native-host classroom path, compile ordinary correct examples with a C17-capable GCC or Clang configuration equivalent to:

```bash
$CC -std=c17 -Wall -Wextra -pedantic <file>.c -o <program>
```

where `$CC` is the compiler selected for the target environment, commonly `gcc` or `clang`.

Concrete diagnostics, generated artifacts, executable formats, and the visibility of separate preprocessing/assembly/linking stages are implementation-specific. Students should classify the observed build evidence rather than memorize one compiler's wording or one physical pipeline.

Windows PowerShell commonly runs a generated native executable with:

```powershell
.\<program>.exe
```

A Unix-like shell commonly uses:

```bash
./<program>
```

These commands describe the specified host environment, not a universal C-language execution model.

## Example Inventory

### Correct examples

- `unit-01/hello.c` — minimal output and source/build/execution distinction.
- `unit-02/average.c` — input contract, positive count, explicit floating conversion, and two-decimal output.
- `unit-03/score-statistics.c` — sentinel-controlled input, accepted score range, accumulation, and two-decimal average.
- `unit-04/max-of-three.c` — function responsibility, input validation, and return-value contract.

### Intentional defect cases

- `unit-01/defects/missing-semicolon.c` — translation constraint violation; expected to require a diagnostic.
- `unit-02/defects/integer-division.c` — compiles successfully but contains an intentional numeric-logic defect.
- `unit-03/defects/infinite-loop.c` — compiles successfully but intentionally does not make progress toward loop termination; do not run in CI without a timeout.
- `unit-04/defects/missing-return.c` — intentionally violates the value-returning function contract; using the resulting call value after reaching the closing brace has undefined behavior, so automated verification must not treat an observed runtime value as meaningful.

See [Compile Manifest](COMPILE-MANIFEST.md) for expected build/runtime treatment.

## Test Plans and Optional Incorrect-Suggestion Review

- [測試計畫與選用錯誤建議審查（繁體中文）](TESTS-AND-AI.zh-TW.md)
- [Test Plans and Optional Incorrect-Suggestion Review (English)](TESTS-AND-AI.en.md)

These files define expected outputs, input contracts, boundary cases, and intentionally incorrect claims for review. An instructor may present the claims without AI, or optionally use an AI-generated suggestion as the claim source. The learning target is prediction, diagnosis, and technical verification—not tool use itself.

## Verification Rules

- Correct examples should compile cleanly under the selected warning flags and satisfy their documented test cases.
- Intentional defect examples have per-file expectations; “defect” does not mean “must fail compilation.”
- Never execute the intentional infinite loop in unattended automation without a timeout.
- Never use runtime output from the missing-return defect as correctness evidence because the relevant execution has undefined behavior.
- Diagnostic wording is compiler-specific; verify the technical category/cause instead of exact text.
- When the target compiler/environment changes, record the configuration and rerun the relevant compile/test manifest.

## Learning and Assessment Boundary

Use the [official learning and assessment policy](../design/13-learning-assessment-policy.en.md) for homework, participation, grading, final-oral, and AI/tool rules. This examples directory intentionally does not duplicate those policies.

## Current Verification Status

- Correct and defect source files for Preparatory Units 1–4 are inventoried.
- Test plans are synchronized with current source outputs/contracts.
- AI-specific review has been made explicitly optional.
- A compile manifest documents which files must compile, which intentionally fail translation, and which must not be executed automatically.
- GCC/Clang execution in the actual classroom/CI environment still needs to be recorded by automated verification.

## Navigation

- [Compile Manifest](COMPILE-MANIFEST.md)
- [Materials Index](../materials/README.en.md)
- [教材索引](../materials/README.zh-TW.md)
