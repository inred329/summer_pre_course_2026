# Formal Unit F-U07: How Can One Data Object Contain Different Fields?

Version: 1.0.1  
Status: Official student material  
Last updated: 2026-08-05  
Corresponding Chinese version: [正式單元 F-U07：資料結構如何由多個不同欄位組成？](unit-07-structures.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can use `struct` to represent an entity with several fields, trace member access and structure assignment, and design structure interfaces with explicit initialization, pointer, string-capacity, and validation contracts.

## Core Question

> When one entity contains several different kinds of data, how can they be combined into one meaningful object?

After completing this chapter, you should be able to:

1. Explain structures, fields, and objects.
2. Define and initialize a `struct`.
3. Access members with `.` and `->`.
4. Compare passing structures by value and by pointer.
5. Copy string fields without exceeding capacity.
6. Design arrays of structures and field validation.

---

## 1. One Student Is Not Three Unrelated Variables

```c
char name[20];
int id;
double average;
```

These values describe one student. With several students, separate variables easily lose their relationships.

---

## 2. Structure Model

```c
struct Student {
    char name[20];
    int id;
    double average;
};
```

```text
Student
├── name
├── id
└── average
```

`struct Student` defines a type. A variable creates an object:

```c
struct Student s;
```

This declaration alone does not initialize the fields. Reading `s.id`, `s.average`, or treating `s.name` as a string before initialization is invalid; scalar members have indeterminate values and the character array may lack a terminator.

---

## 3. Initialization and Member Access

```c
struct Student s = {"Amy", 1001, 87.5};

printf("%s\n", s.name);
printf("%d\n", s.id);
printf("%.1f\n", s.average);
```

`.` accesses a member of a structure object.

```c
s.average = 90.0;
```

A zero initializer is useful when an object will be filled later:

```c
struct Student empty = {0};
```

This sets scalar members to zero and the first character of `name` to `\0`, creating an empty string.

---

## 4. `typedef`

```c
typedef struct {
    char name[20];
    int id;
    double average;
} Student;

Student s = {"Amy", 1001, 87.5};
```

`typedef` creates a type alias; it does not create an object.

---

## 5. Structure Interfaces Need Contracts

By value:

```c
void print_student(Student s) {
    printf("%s %d %.1f\n", s.name, s.id, s.average);
}
```

By pointer with validation:

```c
#include <math.h>

int update_average(Student *s, double value) {
    if (s == NULL || !isfinite(value) || value < 0.0 || value > 100.0) {
        return 0;
    }

    s->average = value;
    return 1;
}
```

`p->member` is equivalent to `(*p).member`. Use `const Student *s` when the function should not modify the object, and still define whether `NULL` is allowed.

---

## 6. Safely Set a Fixed-Capacity Name

```c
#include <stdio.h>

int set_name(Student *s, const char *name) {
    if (s == NULL || name == NULL) {
        return 0;
    }

    int written = snprintf(s->name, sizeof s->name, "%s", name);
    if (written < 0 || (size_t)written >= sizeof s->name) {
        s->name[0] = '\0';
        return 0;
    }

    return 1;
}
```

The function reports truncation instead of silently storing a partial name. Its contract states that failure leaves `name` as an empty string. Other policies are possible, but they must be explicit and tested.

---

## 7. Structure Assignment

```c
Student a = {"Amy", 1001, 87.5};
Student b = a;
```

Structure assignment copies field values, including every element of an array member. Changing `b.average` or `b.name[0]` afterward does not change `a`.

If a field is itself a pointer, only the pointer value is copied; ownership questions are deepened in the dynamic-memory Unit.

C does not provide `a == b` for structures. Compare the required fields individually, and use `strcmp` for string contents.

---

## 8. Arrays of Structures

```c
Student students[3] = {
    {"Amy", 1001, 87.5},
    {"Ben", 1002, 91.0},
    {"Cara", 1003, 78.0}
};
```

```c
for (int i = 0; i < 3; i++) {
    printf("%s %.1f\n", students[i].name, students[i].average);
}
```

The same array boundary rules still apply. Functions should receive the array and its length, and empty-collection behavior must be defined.

---

## 9. Error Cases and Classification

### Reading an Uninitialized Structure

```c
Student s;
printf("%d\n", s.id);
```

Reading the indeterminate scalar member is undefined behavior.

### Using `.` on a Pointer

```c
Student *p = &s;
printf("%d\n", p.id);
```

This is a compile-time type error. Use `p->id` or `(*p).id`.

### Dereferencing a Null Structure Pointer

```c
Student *p = NULL;
printf("%d\n", p->id);
```

This compiles, but evaluating `p->id` dereferences a null pointer and is undefined behavior.

### Ignoring String Capacity

```c
strcpy(s.name, source);
```

If `source` is too long, this writes beyond the array and causes undefined behavior. Use a checked interface with a clear truncation policy.

### Comparing Structures with `==`

```c
if (a == b) { /* ... */ }
```

For structure operands, this is a compile-time constraint violation. Compare selected members explicitly.

---

## 10. Guided Practice

1. Define `Point` with `x` and `y`, including a zero initializer.
2. Write a function to calculate the distance between two points and define null-pointer behavior.
3. Define `Book` with title, page count, and price, then write checked setter functions.
4. Create an array of books and find the highest price, including empty-array behavior.

---

## 11. Independent Practice: Student Data Analysis

Create an array of up to ten students. Display the student with the highest average, the class average, and the record matching a requested ID.

Define and test:

- a missing ID
- an empty collection
- tied highest averages
- an overlong name
- invalid or non-finite averages
- null output pointers if helper functions use them

---

## 12. Requirement Modification

Add field `char grade`, calculated from the average. Identify all initializers, validation functions, interfaces, output, structure comparisons, and tests that must change.

---

## 13. Explain the Concept to AI

Explain:

> How does a structure combine several fields into one data object? Why do initialization, string capacity, nullability, and field validation remain separate contracts?

If an AI response conflicts with a member trace, function interface, compiler diagnostic, or reproducible result, judge it again using evidence.

---

## 14. Self-Check

- I can define and fully initialize a structure.
- I can distinguish a type from an object.
- I can use `.` and `->` with valid objects and pointers.
- I can explain structure assignment, including array and pointer members.
- I can safely set a fixed-capacity string field.
- I can validate structure fields and empty collections.

## 15. Chapter Summary

Structures combine fields that describe one entity into a type, making relationships, interfaces, and traversal clearer. Reliable structure use still requires complete initialization, valid pointers, bounded string operations, field validation, and explicit comparison rules. The next Unit allocates storage during execution and manages ownership and lifetime.

## Navigation

- [Previous Unit: Pointers](unit-06-pointers.en.md)
- [Next Unit: Dynamic Memory](unit-08-dynamic-memory.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-07-structures.zh-TW.md)
