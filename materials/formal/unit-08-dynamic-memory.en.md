# Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?

Version: 1.0.2  
Status: Official student material  
Last updated: 2026-08-06  
Corresponding Chinese version: [正式單元 F-U08：程式如何在執行期間取得與釋放空間？](unit-08-dynamic-memory.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can use `malloc`, `calloc`, `realloc`, and `free`, explain ownership and lifetime, prevent size-calculation overflow, and diagnose memory leaks, dangling pointers, and double free.

AI use is not part of the completion standard. The optional AI extension near the end may be skipped without affecting completion, participation, or assessment.

## Core Question

> When data size or lifetime cannot be fixed in advance, how does a program manage storage?

After completing this chapter, you should be able to:

1. Distinguish automatic storage from dynamic allocation.
2. Validate an element count before calculating allocation size.
3. Allocate, check, use, and release storage.
4. Explain ownership and release responsibility.
5. Use `realloc` without losing the original block on failure.
6. Diagnose common lifetime errors.

---

## 1. Why Dynamic Allocation?

```c
int values[100];
```

A fixed array chooses capacity before runtime work. If the user determines the number of values, or an object must outlive the current function call, dynamic storage may be needed.

Dynamic allocation is not automatically better than a fixed array. It adds failure handling, ownership, lifetime, and release responsibilities. Use it when the requirement actually needs runtime-controlled size or lifetime.

---

## 2. Allocation Model

```c
int *values = malloc(count * sizeof *values);
```

```text
values ─────► dynamically allocated block
              count int elements
```

`malloc` receives a size in bytes. It returns the starting address of suitably aligned storage, or `NULL` when the request cannot be satisfied.

Two questions must be answered before allocation:

1. Is the element count valid for the program requirement?
2. Can `count * sizeof *values` be represented by `size_t`?

```c
if (count > SIZE_MAX / sizeof *values) {
    fprintf(stderr, "Requested size is too large\n");
    return 1;
}
```

The multiplication must be checked before it is performed. A wrapped byte count could allocate a block smaller than the program later assumes.

---

## 3. Complete Lifetime

```c
#include <stdint.h>
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

    size_t count = (size_t)n;
    if (count > SIZE_MAX / sizeof(int)) {
        fprintf(stderr, "Requested size is too large\n");
        return 1;
    }

    int *values = malloc(count * sizeof *values);
    if (values == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }

    for (size_t i = 0; i < count; i++) {
        values[i] = (int)i;
    }

    free(values);
    values = NULL;
    return 0;
}
```

```text
Read and validate count
→ verify byte-size calculation
→ allocate
→ check allocation result
→ initialize/use within bounds
→ release exactly once
→ stop using every pointer to the released object
```

The input check is part of the program contract. Without it, a failed `scanf` leaves `n` without a valid value for later decisions.

The size check protects the allocation contract. Allocation failure and size-calculation overflow are different failures and should not be confused.

---

## 4. `calloc`

```c
int *values = calloc(count, sizeof *values);
```

`calloc` accepts an element count and an element size. It either allocates enough space for their product or fails; it also clears the allocated bytes to zero.

Understand this as zeroed storage, not a universal semantic initialization guarantee for every possible C type. For integer arrays it produces all-bits-zero representations, which represent integer zero in the C implementations targeted by this course.

Even with `calloc`, the program must validate that `count` is meaningful for the requirement and must check the returned pointer.

---

## 5. Ownership

Ownership answers: who is responsible for releasing this block?

```c
int *create_values(size_t count);
```

If a function returns newly allocated storage, its interface should state:

- whether the caller receives ownership
- which function must eventually call `free`
- whether `NULL` indicates failure
- whether any aliases remain elsewhere

Avoid both sides assuming the other will release the block, or both releasing the same block.

Setting one pointer to `NULL` after `free` does not update other aliases. Every pointer that referred to the released object becomes unusable for dereference, comparison as an object address, or another `free`.

---

## 6. `realloc`

A successful `realloc` may return the same address or move the object to a new address. On success, the old pointer value must no longer be used. On failure for a nonzero requested size, the original allocation remains valid and unchanged.

First validate the new element count and byte-size calculation:

```c
if (new_count == 0 || new_count > SIZE_MAX / sizeof *values) {
    /* handle an invalid or unsupported requested capacity */
}
```

Then preserve the original pointer until success is known:

```c
int *temporary = realloc(values, new_count * sizeof *values);
if (temporary == NULL) {
    /* values still owns the original block */
    return 0;
}

values = temporary;
```

Avoid assigning directly to `values`:

```c
values = realloc(values, new_count * sizeof *values); /* unsafe pattern */
```

If reallocation fails, direct assignment can overwrite the only pointer to the original block and cause a leak.

This course treats a zero-capacity request as a separate operation: call `free(values)` explicitly and set the owner pointer to `NULL`. Do not rely on implementation-sensitive `realloc(pointer, 0)` behavior.

---

## 7. Error Cases

### Memory Leak

The final address of an allocated block is lost, or no responsible owner releases it after it is no longer needed.

### Use After Free and Dangling Pointers

```c
free(values);
printf("%d\n", values[0]);
```

The object's lifetime ended at `free`; it must not be dereferenced afterward. Any aliases to the same object are dangling too.

### Double Free

```c
free(values);
free(values);
```

A block must not be released twice. Setting the owning pointer to `NULL` immediately after release can reduce some risks because `free(NULL)` is permitted, but it does not repair other dangling aliases or replace ownership design.

### Wrong Allocation Size

```c
malloc(count * sizeof(int *))
```

When allocating `int` elements, use `sizeof *values` so the expression remains aligned with the pointer's target type.

### Allocation-Size Overflow

```c
malloc(count * sizeof *values)
```

This expression is only safe after verifying:

```c
count <= SIZE_MAX / sizeof *values
```

A non-`NULL` result does not prove that an unchecked multiplication represented the intended size.

---

## 8. Guided Practice

1. Allocate `n` integers dynamically and calculate their sum without overflowing the allocation-size calculation.
2. Draw the owner pointer and any aliases before allocation, after allocation, and after release.
3. Convert a fixed-capacity program into one whose size comes from validated input.
4. Explain which statements execute when allocation fails and why no element access may occur afterward.

---

## 9. Independent Practice: Growable Integer List

Begin with capacity 4 and read integers. Double the capacity when full. Stop on `-1`.

Track:

- `size` and `capacity`
- the invariant `size <= capacity`
- whether doubling `capacity` and converting it to bytes are representable
- the address before and after successful growth
- the fact that the original block remains valid on `realloc` failure
- the one owner responsible for the final `free`

Do not update `capacity` until reallocation succeeds.

---

## 10. Requirement Modification

Add:

```c
int append_value(int **values, size_t *size, size_t *capacity, int value);
```

Define:

- ownership before and after the call
- success and failure return rules
- which output parameters may change
- the invariant connecting `size` and `capacity`
- overflow handling when capacity grows
- whether the original data remains valid on failure

A useful failure contract is: when the function reports failure, the original pointer, size, capacity, and existing elements remain valid and unchanged.

---

## 11. Optional Extension — Evaluate an AI Explanation

This section may be skipped. AI use is not required, and no prompt, conversation, note, submission, or non-use declaration is required.

When you choose to use an AI system, first explain in your own words:

> What is the relationship among dynamic allocation, ownership, lifetime, allocation-size calculation, and `free`? Why is a temporary pointer used with `realloc`?

Then evaluate the response against the allocation diagrams, C library contracts, compiler diagnostics, tests, and a memory-checking tool when one is available. Do not accept a claim merely because the explanation sounds confident.

---

## 12. Self-Check

- I can validate input and reject unsupported element counts.
- I can check allocation-size multiplication before performing it.
- I can check allocation failure before accessing elements.
- I can pair every successful allocation with one release responsibility.
- I can explain ownership and the effect of aliases.
- I do not use an object through any pointer after `free`.
- I can diagnose leaks, use after free, dangling pointers, and double free.
- I can preserve the original block and metadata when `realloc` fails.
- I can explain why zero-capacity handling is kept separate from ordinary growth.

## 13. Chapter Summary

Dynamic memory lets a program choose size and lifetime during execution, but it also gives the programmer explicit size, ownership, and release responsibilities. Reliable management requires validating element counts, preventing byte-size overflow, checking allocation results, defining ownership, releasing exactly once, and stopping all use afterward. Safe growth preserves the original object until `realloc` succeeds. The next Unit stores data in files so it can persist after program termination.

## Navigation

- [Previous Unit: Structures](unit-07-structures.en.md)
- [Next Unit: Files](unit-09-files.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-08-dynamic-memory.zh-TW.md)