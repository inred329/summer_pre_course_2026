# Formal Unit F-U10: How Can a Program Be Divided into Independently Maintainable Modules?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U10：程式如何分成可獨立維護的模組？](unit-10-modules.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can separate interfaces from implementations, create `.h` and `.c` files, explain separate compilation and linking, and diagnose duplicate definitions, missing declarations, and link errors.

## Core Question

> How can interface and implementation be separated so different program parts can be understood, compiled, and replaced independently?

After completing this chapter, you should be able to:

1. Distinguish module, interface, and implementation.
2. Create headers and source files.
3. Use include guards.
4. Explain separate compilation and linking.
5. Diagnose common compile and link failures.

---

## 1. One File Begins to Carry Too Many Responsibilities

When functions, structures, and tests all live in one file, every change requires understanding the entire program. A module groups related responsibility and exposes a clear interface.

---

## 2. Interface and Implementation

`score.h`:

```c
#ifndef SCORE_H
#define SCORE_H

double calculate_average(const int values[], int length);
int is_passing(double average, double threshold);

#endif
```

`score.c`:

```c
#include "score.h"

double calculate_average(const int values[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }
    return (double)sum / length;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}
```

`main.c` depends only on the interface:

```c
#include "score.h"
```

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
static int sum_values(const int values[], int length) {
    /* internal helper */
}
```

This reduces external dependency and allows implementation replacement.

---

## 6. Error Cases

### Function Definitions in a Header

Unless deliberately designed as suitable `static inline` code, definitions included by several `.c` files may cause duplicate-definition errors.

### Declaration and Definition Disagree

```c
/* header */
double average(const int values[], int length);

/* source */
int average(int values[], int length) { ... }
```

Interfaces must match. Compiler diagnostics are evidence.

### Missing Object File During Linking

An undefined reference may appear. This is a link-stage failure, not a syntax error.

### Incomplete Header Dependencies

A header should include or declare what it needs instead of relying on the caller to include another file first.

---

## 7. Guided Practice

1. Divide `max_of_two` into `math_utils.h`, `math_utils.c`, and `main.c`.
2. Change the `.c` implementation without changing the header and confirm that caller code remains unchanged.
3. Deliberately omit `math_utils.o` and identify the link error.

---

## 8. Independent Practice: Student Data Module

Create:

```text
student.h
student.c
main.c
```

The interface should support initialization, average update, and formatted output. Expose only types and functions needed by callers.

---

## 9. Requirement Modification

Add a second front end, `batch_report.c`, that reuses the same student module. Check whether the interface is general enough without exposing unnecessary details for one front end.

---

## 10. Explain the Concept to AI

Explain:

> What is the relationship among a module, interface, implementation, separate compilation, and linking?

If an AI response conflicts with compile commands, file dependencies, or reproducible errors, judge it again using evidence.

---

## 11. Self-Check

- I can distinguish interface and implementation.
- I can create headers and source files.
- I can use include guards.
- I can explain compile and link stages.
- I can diagnose undefined references and duplicate definitions.
- I expose only necessary interfaces.

## 12. Chapter Summary

Modules use clear interfaces to isolate implementation, allowing parts to be understood, compiled, tested, and replaced independently. Separate compilation produces object files, and linking combines definitions into a program. The next Unit builds systematic testing, verification, and debugging evidence.

## Navigation

- [Previous Unit: Files](unit-09-files.en.md)
- [Next Unit: Testing, Verification, and Debugging](unit-11-testing-debugging.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-10-modules.zh-TW.md)
