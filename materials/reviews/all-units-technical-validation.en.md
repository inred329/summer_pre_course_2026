# All-Unit Technical Validation Report

Version: 1.0.0  
Status: Completed technical review record  
Last updated: 2026-08-05  
Corresponding Chinese version: [全 Unit 技術驗證報告](all-units-technical-validation.zh-TW.md)

## Purpose

This report records the technical validation of the complete bilingual student materials for P-U01 through P-U04 and F-U01 through F-U12. It checks C17 semantics, input and output contracts, type and arithmetic boundaries, arrays and strings, recursion, pointers, structures, dynamic memory, files, modules, integrated invariants, intentionally incorrect examples, bilingual synchronization, and navigation.

This review distinguishes:

- complete programs intended to compile and run
- partial fragments intended to illustrate one rule
- intentionally incorrect fragments intended to produce a diagnostic, logic failure, undefined behavior, link failure, or resource defect

## Validation Baseline

Correct complete examples are written for C17 and use the warning baseline:

```bash
gcc -std=c17 -Wall -Wextra -Wformat=2 -pedantic source.c -o program
clang -std=c17 -Wall -Wextra -Wformat=2 -pedantic source.c -o program
```

Multi-file examples use separate compilation and linking. Programs using `fabs` may require `-lm` on environments where the math library is linked separately.

The repository currently contains Markdown examples rather than a machine-extracted test harness. Validation therefore combines complete-code review, C17 language-rule review, explicit return-value and boundary contracts, bilingual code comparison, and reproducible test specifications. A later automation may extract complete blocks and compile them continuously, but no unresolved technical defect remains in the reviewed material baseline.

## Validation Matrix

| Unit | Primary technical checks | Result |
|---|---|---|
| P-U01 | minimal program, compile/run distinction, stale executable experiment, compile-error classification | Pass |
| P-U02 | `scanf` result, initialized state, integer division, variadic format mismatch | Pass after correction |
| P-U03 | checked branch input, loop termination, off-by-one, stale/invalid input | Pass after correction |
| P-U04 | function declarations, status/output contracts, signed-addition overflow, division precondition | Pass after correction |
| F-U01 | integer conversion, signed overflow, floating tolerance, character-set assumption, format mismatch | Pass after correction |
| F-U02 | branch order, `switch` fall-through, sentinel vs EOF/invalid text, invariant and zero-count average | Pass after correction |
| F-U03 | array bounds, uninitialized elements, empty maximum, null outputs | Pass after correction |
| F-U04 | terminated strings, `fgets` return, retained newline, logical-line truncation, leftover input | Pass after correction |
| F-U05 | reachable base case, negative domain, result range, checked multiplication, stack/resource classification | Pass after correction |
| F-U06 | null, indeterminate, dangling, one-past pointers, aliases and output contracts | Pass after correction |
| F-U07 | full initialization, null structure pointers, bounded names, non-finite fields, structure comparison | Pass after correction |
| F-U08 | checked input, allocation size, ownership, `realloc`, leak/use-after-free/double-free classification | Pass after correction |
| F-U09 | `fopen`, writes, read stop reason, EOF/format/I/O distinction, `fclose`, file modes | Pass after correction |
| F-U10 | null and empty input, interface/definition agreement, separate compilation, linking and private helpers | Pass after correction |
| F-U11 | boundary-derived tests, reproducible defect, regression, verification/validation distinction | Pass |
| F-U12 | invariant, nullability, `size_t`, capacity/byte overflow, transactional load, empty average, cleanup | Pass after correction |

## Confirmed Corrections

### Input and State

- Every complete `scanf` example now checks conversion success before using the destination.
- Sentinel loops distinguish a sentinel from EOF, invalid text, and out-of-range numeric data.
- Failed input does not leave an indeterminate value or repeatedly process stale state.

### Arithmetic and Representation

- Signed addition and multiplication risks are checked before the operation where the example requires safety.
- Empty averages and zero divisors have explicit failure behavior.
- Variadic format mismatches are classified as undefined behavior rather than merely “wrong output.”
- Floating comparison examples state that tolerance is requirement- and scale-dependent.
- Character numeric values are not assumed to be ASCII without an environment contract.

### Arrays and Strings

- Maximum operations reject null or empty input without reading element zero.
- Reading uninitialized array and structure members is explicitly classified as undefined behavior.
- `fgets` examples distinguish a valid terminated buffer from a complete logical line.
- Overlong input is reported and remaining characters are discarded before another line read.
- Fixed-capacity structure strings use a checked policy instead of unchecked copying.

### Recursion and Pointers

- Recursive factorial rejects negative input and detects result overflow before multiplication.
- Nontermination, stack exhaustion, requirement failure, and signed overflow are classified separately.
- Pointer interfaces define nullability, lifetime, boundaries, output behavior, and aliases.
- One-past pointers may be formed but are never dereferenced.
- Returning an automatic object's address and later dereferencing it is classified as undefined behavior.

### Dynamic Memory and Integrated Capacity

- Allocation input is checked before conversion to `size_t`.
- `realloc` uses a temporary pointer and preserves the original block on failure.
- Integrated list growth checks capacity wraparound and allocation-byte multiplication.
- Count changes only after validation, allocation, and copying succeed.
- List invariants and empty-list behavior are explicit.

### Files and Modules

- File-open, write, read, format, EOF, I/O-error, and close results are distinguished.
- Save success requires both successful writes and successful close.
- Loading into an existing collection uses an explicit transactional replace policy.
- Module examples validate null/empty input and distinguish compile errors from link errors.
- All old F-U02, F-U09, F-U10, and F-U12 filenames in reviewed navigation were replaced with actual paths.

## Incorrect-Example Classification

| Category | Representative examples |
|---|---|
| Compile-time diagnostic / constraint violation | structure `==`, `.` on a structure pointer, declaration-definition mismatch |
| Link error | object file containing a required definition omitted from link command |
| Logic / requirement error | branch order, ignored status, sentinel included in sum, wrong parameter order |
| Undefined behavior | signed overflow, variadic format mismatch, out-of-bounds access, uninitialized read, invalid pointer dereference, integer division by zero |
| Resource / termination defect | unbounded recursion, leak, double free, use after free, failed close, partial load |
| Insufficient evidence | one successful output, missing boundary paths, no regression after correction |

Intentionally incorrect fragments are not presented as safe executable programs. The material now identifies what evidence is appropriate: compiler diagnostic, trace, boundary test, memory model, file test, or link command.

## Bilingual Equivalence

For all 16 Units:

- the Chinese and English files exist
- corrected complete examples use the same interfaces and safety rules
- tests cover the same normal, boundary, invalid, null, and failure cases
- error categories are substantively equivalent
- adjacent-Unit and language-switch navigation use actual filenames

F-U12 previously contained materially different Chinese and English integrated examples. Both versions now use the same `Student`/`StudentList` model, `size_t` counts, invariant, safe growth checks, checked average, and transactional load policy.

## Navigation Validation

The intended chain is valid:

```text
materials/README.*
→ materials/formal/README.* or preparatory Unit files
→ each Unit
→ previous/next Unit
→ corresponding language file
```

Broken legacy references found during technical review were corrected for F-U01, F-U02, F-U03, F-U09, F-U10, and F-U12.

## Final Technical Decision

The reviewed Markdown baseline now has explicit and technically safe contracts for all complete C examples, accurate classification for intentionally incorrect fragments, substantively synchronized bilingual content, and corrected navigation.

> **All 16 Units have completed the current technical validation stage. No known technical defect remains that blocks review of PR #8.**

Remaining work is not a correction blocker for this validation stage:

- automate extraction and compilation of Markdown code blocks
- add CI link checking and bilingual code-block comparison
- run classroom-environment smoke tests on the exact Windows/Linux toolchains used by students

These are continuous verification improvements, not unresolved defects in the current documents.

## Navigation

- [Repository-Wide Constitution Compliance Review](all-documents-constitution-review.en.md)
- [Materials Index](../README.en.md)
- [繁體中文版](all-units-technical-validation.zh-TW.md)
