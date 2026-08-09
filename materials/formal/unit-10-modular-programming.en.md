# Formal Unit F-U10: How Can a Program Be Divided into Independently Maintainable Modules?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U10：程式如何分成可獨立維護的模組？](unit-10-modular-programming.zh-TW.md)

By F-U09, our program can contain student records, growable arrays, file I/O, analysis functions, and failure handling.

If all of that continues to live in one `main.c`, the program may still run, but every change becomes expensive to reason about:

> Why do I need to reread the file parser just to change the average calculation? Why should a second front end copy the same student functions?

Modular programming is not mainly about making files shorter. It is about **letting different responsibilities cooperate through stable interfaces without requiring every caller to know every implementation detail.**

---

## 1. Separate “What Must the Caller Know?” from “How Is It Done?”

Suppose average calculation is exposed as:

```c
int calculate_average(const int values[],
                      int length,
                      double *result);
```

The caller needs to know:

- what inputs to provide;
- which inputs are valid;
- what success produces;
- what remains unchanged on failure.

It does not need to know whether the implementation uses `for` or `while`, or whether a private helper exists.

Those caller-visible promises form the **interface**.

The code that fulfills them is the **implementation**.

---

## 2. Put the Public Interface in a Header and the Implementation in a Source File

`score.h`:

```c
#ifndef SCORE_H
#define SCORE_H

int calculate_average(const int values[],
                      int length,
                      double *result);
int is_passing(double average, double threshold);

#endif
```

`score.c`:

```c
#include <stddef.h>
#include "score.h"

int calculate_average(const int values[],
                      int length,
                      double *result) {
    if (values == NULL || result == NULL || length <= 0) {
        return 0;
    }

    double sum = 0.0;
    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    *result = sum / (double)length;
    return 1;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}
```

`main.c`:

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
    printf("%s\n",
           is_passing(average, 60.0) ? "Pass" : "Try again");
    return 0;
}
```

The caller includes `score.h` and depends on the interface contract.

It is also important that `score.c` includes its own public header. If the implementation's function type drifts away from the declaration, the compiler can diagnose that mismatch rather than allowing two descriptions of the same interface to evolve independently.

---

## 3. A Good Interface Describes Failure as Well as Success

A first contract for `calculate_average` might be:

```text
values identifies at least length readable int elements
length > 0
result != NULL
success: return 1 and write *result
failure: return 0 and do not modify *result
```

Those rules matter more than the function's name alone.

They let the caller reason safely:

```c
if (!calculate_average(values, length, &average)) {
    /* do not treat average as a new result */
}
```

The implementation may later change algorithms as long as it preserves the same public behavior.

This example accumulates in `double` so that many integer inputs are not first summed in `int` and exposed to signed overflow. That does not provide unlimited precision for arbitrary data sizes; acceptable range and precision still belong to the application requirement.

---

## 4. Include Guards Handle Headers Reached Through Multiple Include Paths

```c
#ifndef SCORE_H
#define SCORE_H

/* declarations and type definitions */

#endif
```

A larger program can easily form a dependency shape such as:

```text
main.c
├── includes a.h
│   └── includes score.h
└── includes b.h
    └── includes score.h
```

The include guard lets the header's contents be expanded only once in that translation unit.

This is especially important for type definitions and other declarations that should not be repeatedly introduced through indirect include paths.

A useful rule is:

> A header should include or declare the types its own public interface requires instead of depending on callers to include some unrelated header first.

---

## 5. After `#include` Processing, Each `.c` Becomes Its Own Translation Unit

Compile separately:

```bash
gcc -std=c17 -Wall -Wextra -pedantic -c main.c
gcc -std=c17 -Wall -Wextra -pedantic -c score.c
```

This produces:

```text
main.c  ──compile──► main.o
score.c ─compile──► score.o
```

Then link:

```bash
gcc main.o score.o -o report
```

Conceptually:

```text
main.o + score.o ──link──► report
```

Now two failure classes become easier to distinguish.

### Compile-stage problem

A translation unit has invalid syntax, incompatible types, or lacks a declaration it needs.

### Link-stage problem

`main.c` may know the declaration of `calculate_average` and compile successfully, yet the final command forgets the object file containing the definition:

```text
undefined reference to calculate_average
```

That is not a syntax failure. The required definition was not connected into the final program.

---

## 6. The Less You Expose, the More Freely the Implementation Can Change

Suppose average calculation uses an internal helper:

```c
static double sum_values(const int values[], int length) {
    double sum = 0.0;

    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    return sum;
}
```

If only `score.c` needs it, there is no reason to place it in `score.h`.

Keeping it internal means callers cannot begin depending on that helper. Later the module can rename it, remove it, or replace the algorithm without changing every program that uses the public score interface.

That is the practical value of information hiding: **reduce the set of details that external code must track when the implementation changes.**

---

## 7. Diagnose Three Common Failures by Looking at the Module Boundary

### Declaration and definition disagree

Header:

```c
int calculate_average(const int values[],
                      int length,
                      double *result);
```

Source defines a different function type. Because `score.c` includes `score.h`, the compiler has direct evidence of the conflict.

### An ordinary external function definition is placed in a header

If several `.c` files include that header, multiple external definitions can be produced and conflict at link time.

Do not turn this into the oversimplified rule “headers can never contain a function body.” Deliberate `static inline` designs follow different rules. The current goal is simpler: **do not accidentally create the same external definition in every translation unit.**

### An object file is omitted from the link

Every `.c` can compile successfully, but the final program still fails because a required definition is absent.

So when a build fails, first ask:

> Is one translation unit invalid by itself, or did the failure happen only when object files were combined?

---

## 8. Independent Practice: Turn Student Data into a Reusable Module

Create:

```text
student.h
student.c
main.c
```

The `student` module should at least handle:

- the caller-visible `Student` type or an equivalent interface;
- initialization;
- average updates;
- data needed for formatted output.

Do not expose every helper automatically.

Draw the boundary from two questions:

```text
What must a caller know?
What does only student.c need to know?
```

Then write at least one normal and one failure test for every public operation.

---

## 9. Change the Requirement: Add a Second Front End Without Copying the Module

Create:

```text
batch_report.c
```

Now two front ends use the same student module:

```text
main.c
batch_report.c
```

Compile/link them separately:

```text
main.o + student.o         → interactive_app
batch_report.o + student.o → batch_report
```

If supporting the second front end requires copying implementation details out of `student.c`, the public interface may be missing something useful.

If every imaginable helper is already public “just in case,” the interface may be too large.

The goal is a boundary that is **general enough for real callers without exposing unnecessary implementation details.**

---

## 10. Optional: Let AI Challenge Your Module Boundary

You may skip this section completely.

Without any tool first, explain:

> What responsibilities belong in `score.h` and what belong in `score.c`? If the averaging algorithm changes without changing the interface contract, why should `main.c` normally remain unchanged?

If you want another check, ask an AI tool for one example of an implementation detail that should not have been made public, or one caller requirement the interface fails to express. No fixed prompt is required, and you do not need to save or submit the conversation.

If the response conflicts with actual include dependencies, compile/link behavior, or the function contract, return to that evidence.

---

## 11. Before Leaving This Unit, Make Sure You Can Locate the Layer Where a Failure Occurs

Answer directly:

- What is the difference between the interface promise and implementation detail?
- Why should `score.c` include `score.h` too?
- What multiple-include problem does an include guard address?
- What does compiling a `.c` file produce, and what does the linker do afterward?
- Why can an undefined reference appear after every `.c` file compiled successfully?
- Why does an internal helper not automatically belong in the header?
- Why is “do not modify output on failure” part of the public interface?
- How does a second front end test whether the module boundary is actually reusable?

If the answer is only “`.h` versus `.c`,” draw the two translation units and the final linking step.

---

## 12. Chapter Wrap-Up

F-U09 let data outlive one execution. F-U10 helps the program itself keep understandable boundaries as it grows.

Modularity is not “split the file every few hundred lines.” Its core is: **publish a stable contract, keep implementation details behind that boundary, check translation units independently, and let the linker assemble the final program.**

The next Unit turns “I think this module works” into more systematic evidence. We will organize the boundary tests, failure cases, regression tests, and debugging methods used throughout the course into one testing, verification, and debugging workflow.

## Navigation

- [Previous Unit: Files](unit-09-files.en.md)
- [Next Unit: Testing, Verification, and Debugging](unit-11-testing-debugging.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-10-modular-programming.zh-TW.md)
