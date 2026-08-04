# Formal Unit F-U07: How Can One Data Object Contain Different Fields?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U07：資料結構如何由多個不同欄位組成？](unit-07-structures.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can use `struct` to represent an entity with several fields, trace member access and structure assignment, and design clear data interfaces and tests.

## Core Question

> When one entity contains several different kinds of data, how can they be combined into one meaningful object?

After completing this chapter, you should be able to:

1. Explain structures, fields, and objects.
2. Define and initialize a `struct`.
3. Access members with `.` and `->`.
4. Compare passing structures by value and by pointer.
5. Design arrays of structures and field validation.

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

## 5. Structures as Function Parameters

By value:

```c
void print_student(Student s) {
    printf("%s %d %.1f\n", s.name, s.id, s.average);
}
```

By pointer:

```c
void update_average(Student *s, double value) {
    s->average = value;
}
```

`p->member` is equivalent to `(*p).member`.

Use `const Student *s` when the function should not modify the object.

---

## 6. Structure Assignment

```c
Student a = {"Amy", 1001, 87.5};
Student b = a;
```

Structure assignment copies field values. Changing `b.average` afterward does not change `a.average`.

If a field is itself a pointer, the address is copied; ownership questions are deepened in the dynamic-memory Unit.

---

## 7. Arrays of Structures

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

---

## 8. Error Cases

### Parallel Data Becomes Unsynchronized

Separate arrays for names, IDs, and averages can lose correspondence when only one array is reordered. An array of structures keeps one entity's fields together.

### Using `.` on a Pointer

```c
Student *p = &s;
printf("%d\n", p.id);
```

Use `p->id` or `(*p).id`.

### Ignoring String Capacity

Writing a long name into a fixed array can overflow it. String capacity and termination rules still apply.

---

## 9. Guided Practice

1. Define `Point` with `x` and `y`.
2. Write a function to calculate the distance between two points.
3. Define `Book` with title, page count, and price.
4. Create an array of books and find the highest price.

---

## 10. Independent Practice: Student Data Analysis

Create an array of up to ten students. Display the student with the highest average, the class average, and the record matching a requested ID.

Define behavior for a missing ID, an empty collection, and tied highest averages.

---

## 11. Requirement Modification

Add field `char grade`, calculated from the average. Identify all initializers, interfaces, output, and tests that must change.

---

## 12. Explain the Concept to AI

Explain:

> How does a structure combine several fields into one data object? What are the differences among `.`, `->`, passing by value, and passing by pointer?

If an AI response conflicts with a member trace, function interface, or reproducible result, judge it again using evidence.

---

## 13. Self-Check

- I can define and initialize a structure.
- I can distinguish a type from an object.
- I can use `.` and `->`.
- I can explain structure assignment.
- I can choose value or pointer parameters.
- I can build and traverse an array of structures.

## 14. Chapter Summary

Structures combine fields that describe one entity into a type, making relationships, interfaces, and traversal clearer. The next Unit allocates storage during execution and manages ownership and lifetime.

## Navigation

- [Previous Unit: Pointers](unit-06-pointers.en.md)
- [Next Unit: Dynamic Memory](unit-08-dynamic-memory.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-07-structures.zh-TW.md)
