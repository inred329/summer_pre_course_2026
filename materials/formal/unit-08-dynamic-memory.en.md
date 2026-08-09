# Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U08：程式如何在執行期間取得與釋放空間？](unit-08-dynamic-memory.zh-TW.md)

F-U07's `Student students[10]` makes one assumption explicit: at most ten records will be stored.

Now change the requirement:

> What if the user tells us how many records are needed only after the program starts, and the required capacity may grow later?

A fixed array may no longer fit the problem. The program needs to obtain an appropriately sized block of storage **during execution**, use it, and explicitly release it when the object is no longer needed.

That is dynamic allocation.

Dynamic memory is not “better because it is more advanced.” It transfers responsibilities to the program: size calculation, allocation failure, ownership, release timing, and making sure no path keeps using an object after release.

---

## 1. Start with a Runtime-Selected Element Count

A fixed version is simple:

```c
int values[100];
```

If 100 is really part of the requirement, this may be exactly the right design.

If the count is known only during execution, storage can be requested later:

```c
int *values = malloc(count * sizeof *values);
```

Conceptually:

```text
values ─────► dynamically allocated block
              space for count int elements
```

`malloc` receives a number of **bytes**, not a number of elements.

So:

```text
count * sizeof *values
```

means:

```text
number of elements × bytes per element
```

---

## 2. Before Allocation, Validate Both the Count and the Byte Calculation

Suppose the count comes from input:

```c
int n;

if (scanf("%d", &n) != 1) {
    fprintf(stderr, "Invalid input\n");
    return 1;
}

if (n <= 0) {
    fprintf(stderr, "Size must be positive\n");
    return 1;
}
```

Only then convert to `size_t`:

```c
size_t count = (size_t)n;
```

Do not assume that:

```c
count * sizeof(int)
```

is always representable as `size_t`.

Check before multiplying:

```c
#include <stdint.h>

if (count > SIZE_MAX / sizeof(int)) {
    fprintf(stderr, "Requested size is too large\n");
    return 1;
}
```

This is the same boundary principle as F-U01: **prove the operation is representable before performing it.**

If the unsigned byte count wraps first, even a later non-`NULL` result from `malloc` may describe a block far smaller than the program assumes.

---

## 3. Trace One Complete Allocate → Use → Release Lifetime

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;

    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "Invalid size\n");
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

Read the path as:

```text
obtain element count
→ validate the requirement
→ validate byte size
→ malloc
→ check the result
→ use within bounds
→ free
→ stop using the released object
```

Three failures are different:

1. the input count is invalid;
2. the required byte count cannot be computed safely;
3. the requested size is valid but the allocation still cannot be satisfied.

---

## 4. `free` Ends the Lifetime of the Allocated Object

After successful allocation, `values` points to a dynamically allocated object.

When:

```c
free(values);
```

executes, that allocated object's lifetime ends.

So this must not follow:

```c
printf("%d\n", values[0]);
```

That is use after free.

Setting the owner variable to:

```c
values = NULL;
```

can help prevent accidental reuse through that variable, but other aliases do **not** automatically become null.

The real rule is:

> Once the allocated object is released, every route that used to identify it must stop treating it as a live object.

---

## 5. Ownership Answers “Who Must Eventually Call `free`?”

Suppose a function has this interface:

```c
int *create_values(size_t count);
```

If it allocates a new block and returns a pointer, the interface should answer:

> Does the caller now own this allocation and therefore become responsible for the eventual `free`?

**Ownership** is not a C keyword. It is a design rule used to avoid two opposite failures:

```text
A expects B to free
B expects A to free
→ leak
```

or:

```text
A believes it must free
B also believes it must free
→ double free
```

Whenever a dynamically allocated pointer crosses an interface, ask not only “what does it point to?” but also:

> Who is responsible for the final release?

---

## 6. `calloc` Allocates and Zeroes the Storage Bytes

```c
int *values = calloc(count, sizeof *values);
```

`calloc` receives an element count and element size. On success it provides the requested storage and initializes its bytes to zero.

For the integer arrays used here, that gives initial integer values of zero.

Do not generalize this into:

> `calloc` performs the correct semantic default initialization for every possible C type.

Its direct guarantee is allocated storage with zeroed bytes. You still must:

- validate that `count` makes sense for the requirement;
- check the returned pointer;
- define ownership and eventual release.

---

## 7. When Capacity Grows, Do Not Overwrite the Only Owner with `realloc`

Suppose the program currently has:

```c
int *values;
size_t capacity;
```

and needs `new_count` elements.

Validate the new capacity first:

```c
if (new_count == 0 ||
    new_count > SIZE_MAX / sizeof *values) {
    /* unsupported capacity */
}
```

Then preserve the original pointer until success is known:

```c
int *temporary = realloc(values,
                         new_count * sizeof *values);

if (temporary == NULL) {
    /* values still owns the original allocation */
    return 0;
}

values = temporary;
```

Why use `temporary`?

For a nonzero requested size, failed `realloc` leaves the original allocation intact. We do not want to overwrite the only pointer that still owns it.

This pattern is dangerous:

```c
values = realloc(values,
                 new_count * sizeof *values);
```

If reallocation fails, `values` becomes `NULL` while the old allocation still exists, potentially losing the final owner pointer and creating a leak.

---

## 8. Successful `realloc` May Move the Object

A successful reallocation may:

- resize the allocation in place; or
- move the object and return a different address.

After success, use the returned pointer as the current allocation.

Any other alias that still identifies a location in the old allocation cannot be assumed to remain valid after a move.

That gives growable arrays another design question:

> Which pointer is the owner during growth, and which external aliases might be invalidated if the allocation moves?

This course also treats zero capacity as a separate operation: explicitly `free(values)` and update owner state rather than relying on special `realloc(pointer, 0)` behavior.

---

## 9. Four Common Defects All Break Lifetime, Ownership, or Capacity

### Memory leak

The allocation is still alive, but the program has lost the final responsible route that could release it.

### Use after free

The object's lifetime has ended, but code still accesses it through an old pointer.

### Double free

The same allocation is passed to `free` again after its lifetime already ended.

### Allocation too small

The element-size calculation is wrong, or `count * sizeof *values` wraps before being checked. Later traversal then assumes more elements than the real block can hold.

Instead of memorizing four isolated labels, keep three questions visible:

```text
Is this allocation still alive?
Who owns it?
Does the actual capacity support the access about to occur?
```

---

## 10. Independent Practice: Build a Growable Integer List

Requirements:

- begin with `capacity = 4`;
- keep reading integers;
- `-1` means stop;
- when `size == capacity`, double the capacity.

Maintain the invariant:

```text
size <= capacity
```

Before each growth, prove:

1. `capacity * 2` itself is representable;
2. the new element capacity can be converted to a representable byte count;
3. the original owner and metadata are not destroyed before `realloc` succeeds.

Update:

```c
capacity = new_capacity;
```

only after successful reallocation.

If growth fails, the old data, `size`, and `capacity` should remain usable so the caller can choose whether to stop, retry, or preserve the partial result.

---

## 11. Change the Requirement: Put Append Behind a Function Interface

Now introduce:

```c
int append_value(int **values,
                 size_t *size,
                 size_t *capacity,
                 int value);
```

This interface is more complex because the function may need to change not only an element but also the owner's pointer itself after `realloc`.

Define failure before writing the implementation:

> If `append_value` reports failure, the caller's original `*values`, `*size`, `*capacity`, and all existing elements remain valid and unchanged.

That contract suggests the operation order:

```text
validate parameters and invariant
→ if space remains, write directly
→ if growth is needed, calculate new capacity and bytes safely
→ realloc through a temporary pointer
→ only after success commit new pointer/capacity
→ write value
→ increment size last
```

This is an important design pattern: **perform work that may fail first, then commit the new state only after success is known.**

---

## 12. Optional: Let AI Challenge Your Ownership Diagram

You may skip this section completely.

First draw owner and alias relationships at four moments:

```text
before allocation
after allocation
after realloc succeeds by moving
after free
```

If you want another check, ask an AI tool which transition is most likely to create a leak, dangling alias, or double free and why. No fixed prompt is required, and you do not need to save or submit the conversation.

If the explanation conflicts with the `malloc`/`realloc`/`free` contracts, your allocation diagram, or a memory-checking tool, return to that evidence.

---

## 13. Before Leaving This Unit, Make Sure You Can Trace the Entire Lifetime

Answer directly:

- Why does a valid element count still require a separate byte-multiplication check?
- Why are `malloc` returning `NULL` and allocation-size overflow different failures?
- After `free(values)`, why does `values = NULL` not automatically make other aliases safe?
- Which two opposite failures is ownership mainly trying to prevent?
- Why is `realloc` commonly assigned to a temporary pointer first?
- What risk do old aliases face when successful `realloc` moves the allocation?
- Why can a growable list update `capacity` only after growth succeeds?
- Why does an “unchanged on failure” contract make `append_value` easier for its caller to reason about?

If an answer has collapsed into a function name, redraw the owner arrow and the allocated object's lifetime.

---

## 14. Chapter Wrap-Up

F-U07 let us organize one record as a `Student`. F-U08 removes the assumption that the number of records must be fixed when the program is written.

The cost is additional responsibility: **calculate size safely before allocation, know who owns the result, preserve the old state while growth can still fail, and stop every route from using the object after release.**

The next Unit addresses a different kind of “lifetime beyond the current execution.” Dynamic memory exists only while the program runs. If data must still exist after the program exits, it has to be written to a file, bringing new questions about opening, reading, writing, formats, failures, and partial updates.

## Navigation

- [Previous Unit: Structures](unit-07-structures.en.md)
- [Next Unit: Files](unit-09-files.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-08-dynamic-memory.zh-TW.md)
