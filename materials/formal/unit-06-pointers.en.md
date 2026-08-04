# Formal Unit F-U06: How Can Data Be Manipulated Indirectly Through Addresses?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U06：如何透過位址間接操作資料？](unit-06-pointers.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can explain the relationship among addresses, pointers, and dereferencing, trace indirect modification with memory diagrams, and diagnose null pointers, dangling pointers, and aliasing problems.

## Core Question

> How can one value refer to another object and use its address to access or modify it?

After completing this chapter, you should be able to:

1. Distinguish object, value, address, and pointer.
2. Use `&` to obtain an address and `*` to dereference.
3. Trace pointer parameters that modify caller data.
4. Explain aliasing, null pointers, and lifetime.
5. Avoid dereferencing invalid addresses.

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

## 4. Pointer Parameters

```c
void add_bonus(int *score, int bonus) {
    *score = *score + bonus;
}

int main(void) {
    int value = 80;
    add_bonus(&value, 5);
    printf("%d\n", value);
}
```

The caller passes an address, so the function can modify the caller's object. The interface should state that modification clearly.

---

## 5. Two Pointers Can Refer to One Object

```c
int value = 10;
int *a = &value;
int *b = &value;
```

`a` and `b` are aliases. A change through `*a` is visible through `*b` because both refer to the same object.

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

The lifetime of `local` ends when the function returns. The returned address becomes dangling: the numeric address may still exist, but it no longer identifies a valid object for use.

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

Pointer arithmetic must remain within the same array or one position past its end.

---

## 9. Error Cases

### Uninitialized Pointer

```c
int *p;
*p = 10;
```

`p` has no reliable target. Dereferencing it is undefined behavior.

### Dereferencing NULL

```c
int *p = NULL;
printf("%d\n", *p);
```

Check validity first.

### Confusing the Two Roles of `*`

```c
int *p;   /* declare a pointer */
*p = 5;   /* dereference */
```

Use a memory diagram to distinguish the roles.

---

## 10. Guided Practice

1. Draw the relationship among `value`, `p`, and `*p`.
2. Build `swap(int *a, int *b)` after tracing both addresses and values.
3. Compare returning a new value with modifying through a pointer.

---

## 11. Independent Practice: Find Minimum and Maximum

Create:

```c
int find_min_max(const int values[], int length, int *min, int *max);
```

On success, write the minimum and maximum through pointers. Return failure for an invalid length. Define behavior for null output pointers and an empty array.

---

## 12. Requirement Modification

New rule: if either `min` or `max` is `NULL`, do not write through it. Update preconditions, return rules, and tests.

---

## 13. Explain the Concept to AI

Explain:

> What is the relationship among an address, pointer, and dereference? Why does lifetime determine whether an address remains usable?

If an AI response conflicts with a memory diagram, function interface, or reproducible result, judge it again using evidence.

---

## 14. Self-Check

- I can distinguish object, value, address, and pointer.
- I can use `&` and `*`.
- I can trace pointer-parameter modification.
- I can explain aliasing.
- I do not dereference null or uninitialized pointers.
- I can explain dangling pointers and lifetime.

## 15. Chapter Summary

A pointer stores an object's address, and dereferencing accesses or modifies that object through the address. Reliable pointer use requires a valid target, valid lifetime, null checks, and boundaries. The next Unit combines different fields into structured data objects.

## Navigation

- [Previous Unit: Call Stack and Recursion](unit-05-call-stack-recursion.en.md)
- [Next Unit: Structures](unit-07-structures.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-06-pointers.zh-TW.md)
