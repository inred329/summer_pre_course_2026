# Formal Unit F-U10: How Can a Program Be Divided into Independently Maintainable Modules?

Version: 1.0.2  
Status: Official student material  
Last updated: 2026-08-06  
Corresponding Chinese version: [正式單元 F-U10：程式如何分成可獨立維護的模組？](unit-10-modular-programming.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can separate interfaces from implementations, create `.h` and `.c` files, explain separate compilation and linking, and diagnose duplicate definitions, missing declarations, invalid interface use, and link errors.

AI use is not part of the chapter's core completion standard. The AI activity near the end is a directly skippable optional extension; not using AI does not affect completion, participation, or assessment.

## Core Question

> How can interface and implementation be separated so different program parts can be understood, compiled, and replaced independently?

After completing this chapter, you should be able to:

1. Distinguish module, interface, and implementation.
2. Create headers and source files.
3. Use include guards.
4. Explain separate compilation and linking.
5. Define and test interface preconditions and failure behavior.
6. Diagnose common compile and link failures.

---

## 1. One File Begins to Carry Too Many Responsibilities

When functions, structures, and tests all live in one file, every change requires understanding the entire program. A module groups related responsibility and exposes a clear interface.

---

## 2. Interface and Implementation

`score.h`:

```c
#ifndef SCORE_H
#define SCORE_H

int calculate_average(const int values[], int length, double *result);
int is_passing(double average, double threshold);

#endif
```

The interface states that `calculate_average` reports success or failure through its return value and writes the average through `result` only on success.

`score.c`:

```c
#include <stddef.h>
#include "score.h"

int calculate_average(const int values[], int length, double *result) {
    if (values == NULL || result == NULL || length <= 0) {
        return 0;
    }

    double sum = 0.0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    *result = sum / length;
    return 1;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}
```

Accumulating in `double` avoids signed overflow from first summing many or extreme values in `int`. This does not mean arbitrary input sizes have unlimited precision; the interface should still define acceptable data size and precision for its application.

`main.c` depends only on the interface:

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

Expected output:

```text
Average: 80.0
Pass
```

The caller does not know how the sum is calculated. It knows only the interface contract and the reported result.

---

## 3. Include Guards

```c
#ifndef SCORE_H
#define SCORE_H

/* declarations */

#endif
```

A header may be included through several paths. Include guards prevent its declarations from being processed repeatedly in one translation unit.

---

## 4. Separate Compilation and Linking

```bash
gcc -std=c17 -Wall -Wextra -pedantic -c main.c
gcc -std=c17 -Wall -Wextra -pedantic -c score.c
gcc main.o score.o -o report
./report
```

```text
main.c  ──compile──► main.o
score.c ─compile──► score.o
main.o + score.o ──link──► report
```

Compilation handles each translation unit. Linking combines required definitions into the executable.

---

## 5. Public and Private Responsibilities

Place only caller-required interfaces in the header. Internal helpers can remain private in the `.c` file:

```c
static double sum_values(const int values[], int length) {
    double sum = 0.0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }
    return sum;
}
```

This reduces external dependency and allows implementation replacement. If this helper is used, the public function must still validate `values`, `length`, and `result` before calling it.

---

## 6. Error Cases

### Invalid Interface Input

Calling `calculate_average(values, 0, &average)` must fail instead of dividing by zero. Calling it with a null input or output pointer must also fail without dereferencing the pointer.

Test these cases before trusting the module:

```c
calculate_average(values, 0, &average);   /* failure */
calculate_average(NULL, 3, &average);     /* failure */
calculate_average(values, 3, NULL);       /* failure */
```

### Function Definitions in a Header

Unless deliberately designed as suitable `static inline` code, definitions included by several `.c` files may cause duplicate-definition errors.

### Declaration and Definition Disagree

```c
/* header */
int calculate_average(const int values[], int length, double *result);

/* source: incorrect */
double calculate_average(int values[], int length) { /* ... */ }
```

Interfaces must match. Compiler diagnostics are evidence.

### Missing Object File During Linking

An undefined reference may appear. This is a link-stage failure, not a syntax error.

### Incomplete Header Dependencies

A header should include or declare what it needs instead of relying on the caller to include another file first. The same principle applies to a `.c` file: this example includes `<stddef.h>` directly, so the source of `NULL` is explicit rather than dependent on an indirect include.

---

## 7. Guided Practice

1. Divide `max_of_two` into `math_utils.h`, `math_utils.c`, and `main.c`.
2. Change the `.c` implementation without changing the header and confirm that caller code remains unchanged.
3. Deliberately omit `math_utils.o` and identify the link error.
4. Add an invalid-input test to the module interface.

---

## 8. Independent Practice: Student Data Module

Create:

```text
student.h
student.c
main.c
```

The interface should support initialization, average update, and formatted output. Expose only types and functions needed by callers. Define what each function does for invalid pointers, invalid counts, or results that cannot be represented under the chosen contract.

---

## 9. Requirement Modification

Add a second front end, `batch_report.c`, that reuses the same student module. Check whether the interface is general enough without exposing unnecessary details for one front end. Compile both front ends separately against the same module.

---

## 10. Optional Extension: Use AI to Check Your Explanation

This section can be skipped directly and is not part of the chapter's core completion standard.

First explain in your own words:

> What is the relationship among a module, interface, implementation, separate compilation, and linking? Why must an interface define failure behavior as well as successful behavior?

If you choose to use AI, you may ask it to identify parts your explanation may have missed. No fixed prompt, saved or submitted conversation, or non-use declaration is required. If an AI response conflicts with compile commands, file dependencies, function contracts, or reproducible errors, judge it again using evidence.

---

## 11. Self-Check

- I can distinguish interface and implementation.
- I can create headers and source files.
- I can use include guards.
- I can explain compile and link stages.
- I can define interface preconditions, numeric range, and failure behavior.
- I can diagnose undefined references and duplicate definitions.
- I expose only necessary interfaces.

## 12. Chapter Summary

Modules use clear interfaces to isolate implementation, allowing parts to be understood, compiled, tested, and replaced independently. A reliable interface describes valid input, numeric range, failure behavior, and output responsibility. Separate compilation produces object files, and linking combines definitions into a program. The next Unit builds systematic testing, verification, and debugging evidence.

## Navigation

- [Previous Unit: Files](unit-09-files.en.md)
- [Next Unit: Testing, Verification, and Debugging](unit-11-testing-debugging.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-10-modular-programming.zh-TW.md)
