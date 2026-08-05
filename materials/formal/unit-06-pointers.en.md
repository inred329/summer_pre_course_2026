# Formal Unit F-U06: How Can Data Be Manipulated Indirectly Through Addresses?

Version: 1.0.1  
Status: Official student material  
Last updated: 2026-08-05  
Corresponding Chinese version: [正式單元 F-U06：如何透過位址間接操作資料？](unit-06-pointers.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can explain the relationship among addresses, pointers, and dereferencing, trace indirect modification with memory diagrams, and design pointer interfaces with explicit nullability, lifetime, boundary, and aliasing contracts.

## Core Question

> How can one value refer to another object and use its address to access or modify it?

After completing this chapter, you should be able to:

1. Distinguish object, value, address, and pointer.
2. Use `&` to obtain an address and `*` to dereference.
3. Trace pointer parameters that modify caller data.
4. Explain aliasing, null pointers, and lifetime.
5. Define whether pointer parameters may be null or aliases.
6. Avoid dereferencing invalid addresses.

---

## 1. A Variable Has an Address as Well as a Value

```c
int score = 80;
int *p = &score;
```

```text
p ──────► score
          value: 80
```

`score` is an object, `80` is its current value, `&score` is its address, and `p` stores that address.

---

## 2. `&` and `*`

```c
printf("%d\n", *p);
*p = 90;
```

- `&score`: obtain the address of `score`.
- `*p`: access the object pointed to by `p`.

`*p = 90` changes `score` through the pointer; it does not change the pointer value itself.

---

## 3. Trace Indirect Modification

```c
int score = 80;
int *p = &score;
*p = *p + 5;
```

```text
Read the address stored in p
→ locate score
→ read 80
→ compute 85
→ write 85 back to score
```

The final value of `score` is 85.

---

## 4. Pointer Parameters Need a Contract

```c
int add_bonus(int *score, int bonus) {
    if (score == NULL) {
        return 0;
    }

    *score = *score + bonus;
    return 1;
}

int main(void) {
    int value = 80;

    if (!add_bonus(&value, 5)) {
        return 1;
    }

    printf("%d\n", value);
    return 0;
}
```

The caller passes an address, so the function can modify the caller's object. The interface states that `score` must identify a live `int`; null input is rejected without dereferencing it.

This function still relies on ordinary `int` addition being representable. If extreme bonus values are part of the requirement, the interface must add an overflow check before assignment.

---

## 5. Two Pointers Can Refer to One Object

```c
int value = 10;
int *a = &value;
int *b = &value;
```

`a` and `b` are aliases. A change through `*a` is visible through `*b` because both refer to the same object.

Aliasing behavior belongs in the function contract. For example, this swap is valid even when both parameters refer to the same object:

```c
int swap(int *a, int *b) {
    if (a == NULL || b == NULL) {
        return 0;
    }

    int temporary = *a;
    *a = *b;
    *b = temporary;
    return 1;
}
```

When `a == b`, the object keeps the same value. That is a valid no-op, not an error. A different interface could reject aliases, but it must state and test that rule explicitly.

---

## 6. Null Pointer

```c
int *p = NULL;
```

`NULL` means the pointer currently refers to no valid object.

```c
if (p != NULL) {
    printf("%d\n", *p);
}
```

Do not dereference `NULL`.

---

## 7. Lifetime and Dangling Pointers

```c
int *bad_pointer(void) {
    int local = 10;
    return &local;
}
```

The lifetime of `local` ends when the function returns. The returned pointer is indeterminate for useful access; dereferencing it later is undefined behavior. Do not rely on the numeric address appearing unchanged.

---

## 8. Pointers and Arrays

```c
int values[3] = {10, 20, 30};
int *p = values;
```

In many expressions, an array name converts to the address of its first element.

```c
*p        /* 10 */
*(p + 1)  /* 20 */
```

Pointer arithmetic must remain within the same array object or one position past its end. A one-past pointer may be formed and compared, but it must not be dereferenced.

---

## 9. Error Cases and Classification

### Uninitialized Pointer

```c
int *p;
*p = 10;
```

`p` has an indeterminate value. Dereferencing it is undefined behavior.

### Dereferencing NULL

```c
int *p = NULL;
printf("%d\n", *p);
```

This compiles, but dereferencing a null pointer is undefined behavior.

### Dereferencing One Past the End

```c
int values[3] = {10, 20, 30};
int *end = values + 3;
printf("%d\n", *end);
```

Forming `end` is valid; dereferencing it is out of bounds and undefined behavior.

### Using `.` on a Pointer

```c
/* for a structure pointer p */
p.member
```

This is a compile-time type error. Use `p->member` or `(*p).member`.

---

## 10. Guided Practice

1. Draw the relationship among `value`, `p`, and `*p`.
2. Test `swap` with different objects, the same object, and each null parameter.
3. Compare returning a new value with modifying through a pointer.
4. Explain why a one-past pointer may be compared but not dereferenced.

---

## 11. Independent Practice: Find Minimum and Maximum

Create:

```c
int find_min_max(const int values[], int length, int *min, int *max);
```

Recommended contract:

- failure when `values`, `min`, or `max` is `NULL`
- failure when `length <= 0`
- no output object is modified on failure
- success writes both values
- `min == max` is allowed; the final object receives the maximum after both results are calculated locally

Test an empty array, null parameters, one element, all-equal values, and aliasing output pointers.

---

## 12. Requirement Modification

New rule: allow either output pointer to be `NULL`, meaning that result is not requested. At least one output must be non-null. Update the contract, implementation, and tests without dereferencing omitted outputs.

---

## 13. Explain the Concept to AI

Explain:

> What is the relationship among an address, pointer, and dereference? Why must a pointer interface define nullability, lifetime, boundaries, and aliasing?

If an AI response conflicts with a memory diagram, function contract, or reproducible result, judge it again using evidence.

---

## 14. Self-Check

- I can distinguish object, value, address, and pointer.
- I can use `&` and `*`.
- I can trace pointer-parameter modification.
- I can explain aliasing and define whether it is allowed.
- I do not dereference null, indeterminate, dangling, or one-past pointers.
- I can explain how lifetime determines pointer validity.

## 15. Chapter Summary

A pointer stores an object's address, and dereferencing accesses or modifies that object through the address. Reliable pointer interfaces define valid targets, lifetime, nullability, array boundaries, output behavior, and aliasing. The next Unit combines different fields into structured data objects.

## Navigation

- [Previous Unit: Call Stack and Recursion](unit-05-call-stack-recursion.en.md)
- [Next Unit: Structures](unit-07-structures.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-06-pointers.zh-TW.md)
