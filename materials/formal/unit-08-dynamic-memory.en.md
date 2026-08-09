# Formal Unit F-U08: How Does a Program Obtain and Release Space During Execution?

Version: 1.2.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U08：程式如何在執行期間取得與釋放空間？](unit-08-dynamic-memory.zh-TW.md)

F-U07 could store student records like this:

```c
Student students[10];
```

The design is clear, but it also fixes one decision in the source code: at most ten records.

Now change the requirement:

> The number of records is known only after the program starts, and the required capacity may grow later.

What changes is not merely that we need a “more advanced function.” The important change is that **the program now takes responsibility for the size and lifetime of the storage it uses**.

It must answer: How much space is needed? Can that size be calculated safely? What happens when allocation fails? Who eventually releases the storage? If the allocation moves while growing, are old pointers still valid?

Those questions form the main path through dynamic allocation and ownership.

---

## 1. A Fixed Array First Shows When Dynamic Allocation Is Not Needed

If the real requirement is simply “at most 100 integers,” then:

```c
int values[100];
```

may be the simplest design.

Dynamic allocation is useful when the required size is known only during execution. Once an element count `count` is available, storage can be requested with:

```c
int *values = malloc(count * sizeof *values);
```

Draw it first:

```text
values ─────► dynamically allocated block
              space for count int elements
```

The first detail to keep visible is that `malloc` receives a **byte count**, not an element count.

So:

```c
count * sizeof *values
```

means:

```text
number of elements × bytes per element
```

If `count` has not been validated yet, that multiplication should not happen yet either.

---

## 2. Validate the Element Count, Then Validate the Byte Count

Suppose the count comes from input:

```c
int n;

if (scanf("%d", &n) != 1 || n <= 0) {
    fprintf(stderr, "Invalid size\n");
    return 1;
}

size_t count = (size_t)n;
```

Now `count` is positive, but a second question remains:

> Can `count * sizeof *values` be represented by `size_t`?

Check before multiplying:

```c
#include <stdint.h>

if (count > SIZE_MAX / sizeof *values) {
    fprintf(stderr, "Requested size is too large\n");
    return 1;
}
```

This is the same boundary principle used in F-U01: **prove that an operation is representable before performing it.**

If the byte count wraps first, a later non-`NULL` result from `malloc` may still describe a block much smaller than the program assumes.

So “the element count is valid” and “the allocation size can be calculated safely” are two separate checks.

---

## 3. Trace One Complete Lifetime: Allocate, Use, Release

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

Do not memorize the function names first. Read the lifetime instead:

```text
obtain element count
→ validate the requirement
→ validate byte size
→ allocate
→ check allocation success
→ use within capacity
→ release
→ stop using the released object
```

There are at least three different failures here: invalid input, unsafe size calculation, and a valid allocation request that cannot be satisfied. They should not all be collapsed into “malloc failed.”

---

## 4. `free` Ends the Allocated Object's Lifetime; It Does Not Repair Every Pointer

After a successful allocation:

```text
values ─────► [ allocation ]
```

After:

```c
free(values);
```

the allocated object's lifetime has ended, so this is no longer valid:

```c
printf("%d\n", values[0]);
```

Changing the owner variable to:

```c
values = NULL;
```

can help prevent accidental reuse through `values` itself.

But suppose another alias was saved earlier:

```c
int *first = values;
```

Setting `values = NULL` does not magically set `first` to `NULL` too.

The real rule is therefore:

> Once an allocation is released, every route that used to identify it must stop treating it as a live object.

This is the dynamic-allocation version of the lifetime and dangling-pointer ideas from F-U05 and F-U06.

---

## 5. Ownership Answers “Who Must Eventually Call `free`?”

Suppose a function has this interface:

```c
int *create_values(size_t count);
```

If it allocates a new block and returns the pointer, the interface should say:

> Does the caller now own that allocation and therefore become responsible for the eventual `free`?

**Ownership is not a C keyword.** It is a design rule that avoids two opposite mistakes:

```text
A expects B to free
B expects A to free
→ memory leak
```

and:

```text
A believes it must free
B also believes it must free
→ double free
```

So when a dynamically allocated pointer crosses an interface, ask not only “what does it point to?” but also:

> Who is responsible for ending this lifetime correctly?

---

## 6. `calloc` Is Another Way to Create an Allocation

```c
int *values = calloc(count, sizeof *values);
```

Unlike `malloc`, `calloc` receives the element count and element size separately. On success, it also zeroes the bytes in the allocated block.

For the `int` arrays used in this Unit, the initial integer values are therefore zero.

Do not generalize that into “`calloc` performs the correct semantic default initialization for every C type.” Its direct guarantee is allocated storage whose bytes are zeroed.

Whether you use `malloc` or `calloc`, three responsibilities remain:

- input and size must satisfy the requirement;
- the returned pointer must be checked;
- ownership and eventual release must be clear.

---

## 7. When Capacity Grows, Preserve the Old Owner Until Success Is Known

Suppose the program currently has:

```c
int *values;
size_t capacity;
```

and now needs `new_capacity` elements.

Validate the requested size first:

```c
if (new_capacity == 0 ||
    new_capacity > SIZE_MAX / sizeof *values) {
    return 0;
}
```

Then use `realloc` through a temporary pointer:

```c
int *temporary = realloc(values,
                         new_capacity * sizeof *values);

if (temporary == NULL) {
    return 0;
}

values = temporary;
capacity = new_capacity;
```

Why not write this directly?

```c
values = realloc(values,
                 new_capacity * sizeof *values);
```

For a nonzero requested size, failed `realloc` leaves the old allocation alive. If the only owner pointer is overwritten directly, `values` becomes `NULL` while the old allocation still exists, and the program may lose its final route to that object.

So the purpose of `temporary` is simple:

> Do not destroy the old owner before the new allocation is known to be usable.

---

## 8. Successful `realloc` Can Still Invalidate Old Aliases

A successful `realloc` may resize in place or move the allocation to another location.

After success, the returned pointer is the current allocation pointer.

Suppose the state before growth is:

```text
values ───► [ old allocation ]
first  ───► [ first element of old allocation ]
```

If `realloc` moves the allocation:

```text
values ───► [ new allocation ]
first  ───► [ old location; cannot be assumed valid ]
```

A growable container therefore has one more question than a fixed array:

> Which pointer owns the allocation, and which pointers are only temporary aliases that may be invalidated by growth?

This course treats capacity zero as an explicit “clear” operation: call `free` and update the owner state rather than depending on special `realloc(pointer, 0)` behavior.

---

## 9. Common Defects Reduce to Three Questions

### Memory leak

The allocation is still alive, but the final route responsible for releasing it has been lost.

### Use after free

The allocation's lifetime has ended, but code still accesses it through an old pointer.

### Double free

The same allocation is passed to `free` again after its lifetime has already ended.

### Allocation too small

The program believes it owns space for `count` elements, but the actual byte allocation is smaller because the size formula was wrong or multiplication wrapped first.

Instead of memorizing four disconnected labels, keep returning to:

```text
Is this allocation still alive?
Who owns it?
Does the real capacity support the next access?
```

---

## 10. First Build a Growable Integer List

Requirements:

- start with `capacity = 4`;
- keep reading integers;
- `-1` means stop;
- when `size == capacity`, double the capacity.

Maintain:

```text
size <= capacity
```

Before growth, check:

```c
if (capacity > SIZE_MAX / 2) {
    /* capacity * 2 cannot be represented safely */
}

size_t new_capacity = capacity * 2;

if (new_capacity > SIZE_MAX / sizeof *values) {
    /* byte size cannot be represented safely */
}
```

Only then attempt `realloc` through a temporary pointer.

Update `values` and `capacity` only after growth succeeds. If growth fails, the old data, `size`, and `capacity` should remain usable.

That “old state remains intact on failure” goal becomes the core function contract in the next section.

---

## 11. Why Does `append_value` Need `int **values`?

Now wrap append behind a function:

```c
int append_value(int **values,
                 size_t *size,
                 size_t *capacity,
                 int value);
```

The first `int **` can look like a new layer of punctuation. Do not memorize it first. Return to the F-U06 rule:

> If a function must modify an object owned by its caller, give the function the location of that object.

This time, the caller-owned object that may change is itself an **owner pointer**:

```c
int *values;
```

That pointer object has an address too:

```c
&values
```

and the type of `&values` is `int **`.

Draw it:

```text
append_value parameter values
          │
          v
caller's owner pointer ─────► dynamic allocation
        int *
```

Inside `append_value`:

- `values` points to the caller's owner-pointer object;
- `*values` is the caller's current `int *` owner value;
- if `realloc` returns a new location, assigning to `*values` updates the owner's pointer in the caller.

`size_t *size` and `size_t *capacity` follow the same idea: the function may update those metadata objects after success.

So `**` is not a separate kind of magic. It appears because **the caller-owned object we need to modify happens to be a pointer itself**.

---

## 12. The Important Append Rule Is “Do Not Damage the Old State on Failure”

Define the contract before the implementation:

> If `append_value` reports failure, the caller's original `*values`, `*size`, `*capacity`, and all existing elements remain valid and unchanged.

That contract suggests this operation order:

```text
validate parameters and size <= capacity
→ space remains: write directly
→ growth needed: calculate new capacity and byte size safely
→ temporary = realloc(...)
→ failure: leave old state untouched
→ success: commit new owner/capacity
→ write the new value
→ increment size last
```

A concrete implementation is:

```c
#include <stdint.h>
#include <stdlib.h>

int append_value(int **values,
                 size_t *size,
                 size_t *capacity,
                 int value) {
    if (values == NULL || size == NULL || capacity == NULL) {
        return 0;
    }

    if (*size > *capacity) {
        return 0;
    }

    if (*capacity > 0 && *values == NULL) {
        return 0;
    }

    if (*size == *capacity) {
        size_t new_capacity;

        if (*capacity == 0) {
            new_capacity = 4;
        } else {
            if (*capacity > SIZE_MAX / 2) {
                return 0;
            }
            new_capacity = *capacity * 2;
        }

        if (new_capacity > SIZE_MAX / sizeof **values) {
            return 0;
        }

        int *temporary = realloc(*values,
                                 new_capacity * sizeof **values);
        if (temporary == NULL) {
            return 0;
        }

        *values = temporary;
        *capacity = new_capacity;
    }

    (*values)[*size] = value;
    (*size)++;
    return 1;
}
```

When reading this code, do not begin by counting stars. Keep asking:

> Which operation may fail? Which old state must remain intact until that failure is no longer possible? Which values can be committed together after success?

That reasoning is more reusable than memorizing one `realloc` pattern.

---

## 13. Optional: Let AI Challenge Your Ownership Diagram

You may skip this section completely.

First draw four moments:

```text
before allocation
after allocation
after realloc succeeds by moving
after free
```

Mark the owner, aliases, and the allocation that is still alive in each diagram.

If you want another check, ask an AI tool which transition is most likely to create a leak, dangling alias, or double free and why. No fixed prompt is required, and you do not need to save or submit the conversation.

If the explanation conflicts with the `malloc`/`realloc`/`free` contracts, your allocation diagram, or a memory-checking tool, return to the verifiable evidence.

---

## 14. Before Leaving This Unit, Make Sure You Can Trace the Whole Lifetime

Answer directly:

- Why does a valid element count still require a separate byte-multiplication check?
- Why are `malloc` returning `NULL` and allocation-size overflow different failures?
- After `free(values)`, why does `values = NULL` not automatically make other aliases safe?
- Which two opposite failures is ownership mainly trying to prevent?
- Why is `realloc` usually stored in a temporary pointer first?
- What risk do old aliases face if successful `realloc` moves the allocation?
- Why does modifying the caller's `int *values` require passing `&values` to an `int **` parameter?
- Why does an “unchanged on failure” contract make `append_value` easier for its caller to reason about?

If an answer has collapsed into a function name or a number of `*` symbols, redraw the owner pointer, the address of that pointer object, and the allocation itself.

---

## 15. Chapter Wrap-Up

F-U07 let us organize one record as a `Student`. F-U08 removes the assumption that the number of records must be fixed when the program is written.

The cost is additional responsibility: **calculate size safely before allocation, know who owns the result, preserve the old state while growth can still fail, and stop every route from using the object after release.**

The `int **` in `append_value` is a natural extra layer in that same story: when the caller-owned object that a function must modify is itself a pointer, the function receives the address of that pointer object.

The next Unit addresses a different kind of lifetime beyond the current execution. Dynamic memory exists only while the program runs. If data must still exist after the program exits, it must be written to a file, bringing new questions about opening, reading, writing, formats, failures, and partial updates.

## Navigation

- [Previous Unit: Structures](unit-07-structures.en.md)
- [Next Unit: Files](unit-09-files.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-08-dynamic-memory.zh-TW.md)