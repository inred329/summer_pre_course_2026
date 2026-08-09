# Formal Unit F-U07: How Can One Data Object Contain Different Fields?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U07：資料結構如何由多個不同欄位組成？](unit-07-structures.zh-TW.md)

F-U06 solved the problem “how do we locate one object and, when appropriate, let a function modify it through a pointer?”

Now change the data-organization problem. Suppose one student is described by:

```c
char name[20];
int id;
double average;
```

None of these variables is wrong, but the three values belong to **the same student**. With ten or fifty students, keeping names, IDs, and averages as scattered variables makes it easy to lose which values form one record.

So this Unit asks:

> When one entity contains fields of different types, how can C combine them into one meaningful data object?

That is the role of `struct`.

---

## 1. First Combine One Student into a Type

```c
struct Student {
    char name[20];
    int id;
    double average;
};
```

Think of the shape as:

```text
Student
├── name      char[20]
├── id        int
└── average   double
```

This defines a **type**. It has not yet created an actual student object.

An object appears when we write:

```c
struct Student s;
```

Keep the distinction clear:

- `struct Student`: describes the form of this kind of data;
- `s`: one actual `struct Student` object during execution.

---

## 2. Creating the Structure Object Does Not Make Every Field Valid Automatically

If we only write:

```c
struct Student s;
```

do not immediately assume these are ready:

```c
printf("%d\n", s.id);
printf("%s\n", s.name);
```

Ordinary automatic local fields do not become reliable values merely because they are members of a structure.

In particular:

- `id` and `average` have not been initialized;
- `name` has 20 character positions, but nothing yet guarantees a `\0` that makes it a C string.

The earlier rules therefore still apply: **a legal field location does not imply valid field contents.**

The simplest approach is complete initialization:

```c
struct Student s = {"Amy", 1001, 87.5};
```

Now all three fields have defined contents.

---

## 3. `.` Means “Select This Field from This Structure Object”

Given:

```c
struct Student s = {"Amy", 1001, 87.5};
```

we can write:

```c
printf("%s\n", s.name);
printf("%d\n", s.id);
printf("%.1f\n", s.average);
```

and modify one field:

```c
s.average = 90.0;
```

The left side of `.` is a structure object; the right side names one of its members.

If an object will be filled in gradually, zero initialization can provide a defined starting state:

```c
struct Student empty = {0};
```

The numeric fields begin at zero and `name[0]` is `\0`, so the name begins as an empty C string.

---

## 4. `typedef` Gives the Type a Shorter Name

Repeating `struct Student` can be verbose, so a common form is:

```c
typedef struct {
    char name[20];
    int id;
    double average;
} Student;
```

Then:

```c
Student s = {"Amy", 1001, 87.5};
```

`typedef` creates a type alias. It does not create a student object by itself.

Read it as:

> From here on, use `Student` as a name for this structure type.

---

## 5. Once Structures Meet Pointers, `->` Has a Natural Meaning

F-U06 established that if:

```c
Student s = {"Amy", 1001, 87.5};
Student *p = &s;
```

then `p` points to `s`.

To modify the `average` through the pointer, we could write:

```c
(*p).average = 90.0;
```

because `*p` first denotes the `Student` object and `.` then selects the field.

C provides the usual shorter notation:

```c
p->average = 90.0;
```

So:

```text
p->member
```

is equivalent to:

```text
(*p).member
```

This is why the previous Unit did not need to introduce `->` before structures existed as a concept.

---

## 6. Pass by Value or Pass by Pointer According to the Job

If a function only needs a small structure value for reading and display:

```c
void print_student(Student s) {
    printf("%s %d %.1f\n", s.name, s.id, s.average);
}
```

that is value passing: the function receives a `Student` value.

If the function must modify the caller's object, it needs the object's location:

```c
#include <math.h>
#include <stddef.h>

int update_average(Student *s, double value) {
    if (s == NULL || !isfinite(value) ||
        value < 0.0 || value > 100.0) {
        return 0;
    }

    s->average = value;
    return 1;
}
```

Now the F-U06 questions return naturally:

- may `s` be `NULL`?
- is the pointed-to object still alive?
- is the function allowed to modify it?

If a function should read through a pointer without modifying the `Student`, its parameter can be written as:

```c
const Student *s
```

which prevents modification of the `Student` through that parameter.

---

## 7. A String Field Inside a Structure Still Has a Capacity

The `name` field is still:

```c
char name[20];
```

so all F-U04 string rules still apply. Putting the array inside `Student` does not remove the terminator or capacity requirements.

One setter with an explicit “reject truncation” policy is:

```c
#include <stddef.h>
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

The policy is:

> Succeed only when the complete name fits; otherwise report failure and do not leave a truncated value that looks complete.

Other policies, such as explicit truncation, are possible. The unsafe choice is having no policy while assuming the data always fits.

---

## 8. Structure Assignment Copies the Structure Value

```c
Student a = {"Amy", 1001, 87.5};
Student b = a;
```

This assigns the structure value of `a` to `b`.

Because `name` is an array member inside the structure, its elements become part of the copied structure value as well.

So later:

```c
b.average = 60.0;
b.name[0] = 'E';
```

does not modify `a.average` or `a.name[0]`.

A pointer field is different. If a structure contains a pointer, structure assignment copies the **pointer value**; it does not automatically duplicate the separate object that the pointer identifies.

That distinction becomes central in F-U08 when dynamic storage and ownership enter the course.

---

## 9. Structures Do Not Have a Built-In Whole-Record `==`

This is not valid general structure comparison:

```c
if (a == b) {
    /* ... */
}
```

C does not provide `==` for structure values.

More importantly, the requirement should first define what “the same student” means. It might mean:

- same ID;
- same ID, name, and average;
- equality of only selected fields.

String fields need string-content comparison such as `strcmp`.

So equality should come from the problem's semantics rather than from an assumption that `struct` automatically knows what “same record” means.

---

## 10. An Array of Structures Connects F-U03 to This Unit

Three students can be stored as:

```c
Student students[3] = {
    {"Amy", 1001, 87.5},
    {"Ben", 1002, 91.0},
    {"Cara", 1003, 78.0}
};
```

Traverse them:

```c
for (int i = 0; i < 3; i++) {
    printf("%d %s %.1f\n",
           students[i].id,
           students[i].name,
           students[i].average);
}
```

Read `students[i].average` in two location steps:

```text
i
→ students[i] selects the ith Student
→ .average selects that student's average field
```

The F-U03 array-boundary rules have not changed. Each array element is simply a complete `Student` rather than one `int`.

---

## 11. Independent Practice: A Small Student-Record Analyzer

Create an array containing up to 10 students, with at least:

```text
id
name
average
```

Requirements:

1. find a student with the highest average;
2. calculate the class average;
3. look up a student by ID.

Before implementing, decide:

- may IDs repeat?
- what happens when a name exceeds 19 visible characters?
- must `average` stay in 0 through 100, and are NaN/Infinity rejected?
- if several students tie for the highest average, do you choose the first, return all, or apply another rule?
- when there are no students, how are “highest” and “class average” reported?

These decisions define what a valid `Student` collection means.

Test at least an empty collection, one student, ties, missing ID, overlong name, invalid average, and an ordinary multi-record case.

---

## 12. Change the Requirement: Add `grade`

Add a field:

```c
char grade;
```

computed from `average`, for example:

```text
90–100 → A
80–89  → B
70–79  → C
otherwise → D
```

Do not stop after adding one line to the structure declaration.

Find every place affected by the new relationship:

- initializers;
- what happens to `grade` when `average` changes;
- output formatting;
- comparison or lookup behavior if relevant;
- boundary tests such as 79/80 and 89/90.

The point of the change is to see that once several fields form one object, **the fields may have consistency relationships that must be maintained together.**

---

## 13. Optional: Let AI Challenge Your Data Model

You may skip this section completely.

Without any tool first, explain:

> Why does `Student` express the relationship among name, ID, and average better than three scattered groups of variables? If `average` changes, what other fields or rules might also need to stay consistent?

If you want another check, give your `Student` design to an AI tool and ask for an example where every individual field appears legal but the record as a whole is inconsistent. No fixed prompt is required, and you do not need to save or submit the conversation.

If the suggestion conflicts with string capacity, pointer contracts, field ranges, or reproducible tests, return to that evidence and judge again.

---

## 14. Before Leaving This Unit, Make Sure You Are Not Just Memorizing `struct` Syntax

Answer directly:

- How is the `Student` type different from one `Student s` object?
- Why does `Student s;` not mean every field already contains safe readable data?
- When do you use `s.average`, and when do you use `p->average`?
- Why is `p->member` equivalent to `(*p).member`?
- What happens to an array member during structure assignment? What happens to a pointer member?
- Why do `\0` and capacity still matter when a name is stored inside a structure?
- Why should the requirement define what it means for two students to be “equal”?
- Into which two location steps can `students[i].average` be decomposed?

If the answers reduce to symbol rules, draw one whole student object and its fields again.

---

## 15. Chapter Wrap-Up

F-U06 showed how a program can reach one object through a location. F-U07 lets one object itself contain several fields of different types.

The real value of `struct` is not merely using fewer variable names. It puts **data that belongs to one entity—and the rules that keep those fields meaningful—back into one model.** Initialization, string capacity, field validation, pointer validity, and comparison rules still matter; they now protect a complete record.

The next Unit changes another assumption. So far, most arrays and structure objects have sizes decided when we write the program. What if the required number of records is known only while the program runs, and the amount of storage must grow or shrink? That leads to dynamic memory and ownership.

## Navigation

- [Previous Unit: Pointers](unit-06-pointers.en.md)
- [Next Unit: Dynamic Memory](unit-08-dynamic-memory.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-07-structures.zh-TW.md)
