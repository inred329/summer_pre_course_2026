# Formal Unit F-U03: How Does Data Form an Ordered Collection?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U03：資料如何形成有順序的集合？](unit-03-arrays.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can use arrays to store same-type values, trace indexes and traversal, prevent out-of-bounds access, and pass arrays to functions for testing and modification.

## Core Question

> When multiple values of the same kind must be stored and processed together, how does a program organize, locate, and traverse them?

After completing this chapter, you should be able to:

1. Explain arrays, elements, indexes, and length.
2. Trace one-dimensional traversal.
3. Distinguish legal indexes from out-of-bounds access.
4. Pass an array and its length to a function.
5. Test boundaries and empty-collection assumptions.

---

## 1. Why Not Use Many Separate Variables?

```c
int score1, score2, score3, score4, score5;
```

As the number of values grows, separate names and repeated processing become difficult and error-prone. An array organizes same-type elements through consecutive indexes.

---

## 2. Array Model

```c
int scores[5] = {80, 90, 75, 88, 92};
```

```text
Index:   0   1   2   3   4
Value:  80  90  75  88  92
```

The length is 5. Legal indexes are 0 through 4. The final index is `length - 1`.

---

## 3. Access and Update

```c
printf("%d\n", scores[2]);
scores[2] = 78;
```

The index is evaluated first, then the element is located and read or written. The index is not the element value.

---

## 4. Traverse an Array

```c
int sum = 0;

for (int i = 0; i < 5; i++) {
    sum += scores[i];
}
```

Trace:

| `i` | `scores[i]` | `sum` after update |
|---:|---:|---:|
| 0 | 80 | 80 |
| 1 | 90 | 170 |
| 2 | 75 | 245 |
| 3 | 88 | 333 |
| 4 | 92 | 425 |

Use `i < 5`, not `i <= 5`.

---

## 5. Pass the Length with the Array

```c
int sum_array(const int values[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }
    return sum;
}
```

A function usually cannot determine the number of elements from `values[]` alone, so the interface includes the length.

---

## 6. Find the Maximum

```c
int max_array(const int values[], int length) {
    int max = values[0];

    for (int i = 1; i < length; i++) {
        if (values[i] > max) {
            max = values[i];
        }
    }

    return max;
}
```

This function assumes `length > 0`. Preconditions must be stated and tested.

---

## 7. Error Cases

### Out-of-Bounds Access

```c
int values[5];
printf("%d\n", values[5]);
```

The last legal index is 4. Out-of-bounds access is undefined behavior; one apparently normal run does not make it safe.

### Uninitialized Elements

```c
int values[5];
printf("%d\n", values[0]);
```

A local array does not automatically contain reliable zeros.

### Reading the First Element of an Empty Collection

`max_array(values, 0)` still tries to access `values[0]`. The interface must reject or represent the absence of a result.

---

## 8. Guided Practice

1. Store five temperatures and display total and average.
2. Replace every negative value with zero.
3. Count elements greater than or equal to 60.

Draw indexes and values before writing each loop.

---

## 9. Independent Practice: Score Analysis

Read a fixed set of ten scores and display average, maximum, minimum, and passing count.

Test all-equal, increasing, decreasing, and boundary values 59/60.

---

## 10. Requirement Modification

New requirement: calculate the average after removing one lowest score. You do not need to physically modify the array. Define what “remove” means for total and count, then update tests.

---

## 11. Explain the Concept to AI

Explain:

> What is the relationship among an array, index, length, and boundary? Why does a function usually need both an array and its length?

If an AI response conflicts with an index diagram, loop trace, or reproducible test, judge it again using evidence.

---

## 12. Self-Check

- I can identify the legal index range.
- I can trace array traversal.
- I can explain that out-of-bounds access is undefined behavior.
- I can pass an array and length to a function.
- I can handle the precondition `length > 0`.
- I can design ordered and boundary-focused test data.

## 13. Chapter Summary

Arrays organize same-type data into a collection located by index. Reliable operations require an explicit length, legal boundaries, and traceable traversal. The next Unit shows how strings represent text with character arrays and a terminator.

## Navigation

- [Previous Unit: Advanced Control Flow](unit-02-advanced-control.en.md)
- [Next Unit: Strings](unit-04-strings.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-03-arrays.zh-TW.md)
