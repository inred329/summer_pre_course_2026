# Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?

Version: 1.0.1  
Status: Official student material  
Last updated: 2026-08-05  
Corresponding Chinese version: [正式單元 F-U08：程式如何在執行期間取得與釋放空間？](unit-08-dynamic-memory.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can use `malloc`, `calloc`, `realloc`, and `free`, explain ownership and lifetime, and diagnose memory leaks, dangling pointers, and double free.

## Core Question

> When data size or lifetime cannot be fixed in advance, how does a program manage storage?

After completing this chapter, you should be able to:

1. Distinguish automatic storage from dynamic allocation.
2. Allocate, check, use, and release storage.
3. Explain ownership and release responsibility.
4. Use `realloc` safely.
5. Diagnose common lifetime errors.

---

## 1. Why Dynamic Allocation?

```c
int values[100];
```

A fixed array chooses capacity before runtime work. If the user determines the number of values, or an object must outlive the current function call, dynamic storage may be needed.

---

## 2. Allocation Model

```c
int *values = malloc(n * sizeof *values);
```

```text
values ─────► dynamically allocated block
              n int elements
```

`malloc` returns the starting address; on failure it returns `NULL`.

```c
if (values == NULL) {
    return 1;
}
```

---

## 3. Complete Lifetime

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;

    if (scanf("%d", &n) != 1) {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }

    if (n <= 0) {
        fprintf(stderr, "Size must be positive\n");
        return 1;
    }

    int *values = malloc((size_t)n * sizeof *values);
    if (values == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        values[i] = i * 10;
    }

    free(values);
    values = NULL;
    return 0;
}
```

```text
Read and validate size
→ allocate
→ check
→ initialize/use
→ release
→ stop using
```

The input check is part of the program contract. Without it, a failed `scanf` leaves `n` without a valid value for later decisions.

---

## 4. `calloc`

```c
int *values = calloc(n, sizeof *values);
```

`calloc` allocates elements and clears their bits to zero. Understand this as zero-initialized storage rather than a universal semantic initialization guarantee for every possible type.

---

## 5. Ownership

Ownership answers: who is responsible for releasing this block?

```c
int *create_values(int n);
```

If a function returns newly allocated storage, its interface should state that the caller receives ownership and must call `free`.

Avoid both sides assuming the other will release it, or both releasing the same block.

---

## 6. `realloc`

```c
int *temporary = realloc(values, new_size * sizeof *values);
if (temporary != NULL) {
    values = temporary;
}
```

Avoid assigning directly to `values`. If reallocation fails, overwriting the original pointer can lose the only address of the old block and cause a leak.

---

## 7. Error Cases

### Memory Leak

The final address of an allocated block is lost, or no responsible owner releases it.

### Dangling Pointer

```c
free(values);
printf("%d\n", values[0]);
```

The object's lifetime ended at `free`; it must not be dereferenced afterward.

### Double Free

```c
free(values);
free(values);
```

A block must not be released twice. Setting the pointer to `NULL` can reduce some risks but does not replace ownership design.

### Wrong Allocation Size

```c
malloc(n * sizeof(int *))
```

When allocating `int` elements, use `sizeof *values` so the expression remains aligned with the pointer's target type.

---

## 8. Guided Practice

1. Allocate `n` integers dynamically and calculate their sum.
2. Draw the pointer before allocation, after allocation, and after release.
3. Convert a fixed-capacity program into one whose size comes from input.

---

## 9. Independent Practice: Growable Integer List

Begin with capacity 4 and read integers. Double the capacity when full. Stop on `-1`.

Track `size`, `capacity`, the address before and after growth, `realloc` failure handling, and the final `free`.

---

## 10. Requirement Modification

Add:

```c
int append_value(int **values, int *size, int *capacity, int value);
```

Define ownership, success/failure return rules, which parameters may change, and whether original data remains valid on failure.

---

## 11. Explain the Concept to AI

Explain:

> What is the relationship among dynamic allocation, ownership, lifetime, and `free`? Why is a temporary pointer often used with `realloc`?

If an AI response conflicts with an allocation diagram, function contract, or memory-checking result, judge it again using evidence.

---

## 12. Self-Check

- I can check input and allocation failure.
- I can pair every successful allocation with a release responsibility.
- I can explain ownership.
- I do not use objects after `free`.
- I can diagnose leaks, dangling pointers, and double free.
- I can preserve the original block when `realloc` fails.

## 13. Chapter Summary

Dynamic memory lets a program choose size and lifetime during execution, but it also gives ownership and release responsibility to the programmer. Reliable management requires explicit contracts, input and allocation checks, correct release, and no use afterward. The next Unit stores data in files so it can persist after program termination.

## Navigation

- [Previous Unit: Structures](unit-07-structures.en.md)
- [Next Unit: Files](unit-09-files.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-08-dynamic-memory.zh-TW.md)
