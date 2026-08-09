# Formal Unit F-U06: How Can Data Be Manipulated Indirectly Through Addresses?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U06：如何透過位址間接操作資料？](unit-06-pointers.zh-TW.md)

Since the preparatory course, we have repeatedly written code such as:

```c
scanf("%d", &score);
```

At first, it was enough to read `&score` as “tell `scanf` where to write the input.”

F-U03 and F-U04 deliberately postponed another question: why can a function that receives an array access the caller's original elements?

Now put those clues together:

> A C program can work not only with the current value of an object, but also with the object's location. It can store that location and later use it to reach the original object again.

That is the model of addresses and pointers.

---

## 1. Separate Object, Value, and Address

Start with:

```c
int score = 80;
```

`score` names an `int` object whose current value is 80.

Besides reading the value:

```c
printf("%d\n", score);
```

we can obtain the object's address:

```c
&score
```

Now declare a variable that can store the address of an `int` object:

```c
int *p = &score;
```

Conceptually:

```text
p ──────► score
          value: 80
```

Keep four things separate:

- `score`: the object name;
- `80`: its current value;
- `&score`: the address of the object;
- `p`: a pointer object that stores that address.

A pointer is itself an object with a value; its value is used to identify another object's location.

---

## 2. `&` Obtains a Location; `*` Uses the Location to Reach the Object

Given:

```c
int score = 80;
int *p = &score;
```

then:

```c
printf("%d\n", *p);
```

uses the address stored in `p` to access the `int` object at that location, so it reads 80.

Dereferencing can also appear on the left side of assignment:

```c
*p = 90;
```

This does not replace the pointer value with 90. It follows `p` to `score` and changes `score` to 90.

Trace it:

```text
p stores &score
→ *p denotes the score object
→ *p = 90
→ score now contains 90
```

This is **indirect access**: the program reaches an object through another value rather than naming the object directly.

---

## 3. Now Revisit `scanf(..., &score)`

```c
int score;
scanf("%d", &score);
```

`scanf` must modify the caller's `score`. Receiving only the current integer value would not tell it which object should receive the converted result.

`&score` provides that location.

That is why:

```c
scanf("%d", score);
```

is not merely “missing one symbol.” For `%d`, the corresponding argument must provide a writable location for an `int`; the integer value stored in `score` does not satisfy that interface contract.

---

## 4. Pointer Parameters Let a Function Modify a Caller-Owned Object

For example:

```c
#include <limits.h>
#include <stddef.h>

int add_bonus(int *score, int bonus) {
    if (score == NULL) {
        return 0;
    }

    if ((bonus > 0 && *score > INT_MAX - bonus) ||
        (bonus < 0 && *score < INT_MIN - bonus)) {
        return 0;
    }

    *score += bonus;
    return 1;
}
```

Call it with:

```c
int value = 80;

if (add_bonus(&value, 5)) {
    printf("%d\n", value);
}
```

The flow is:

```text
main owns value
→ pass &value
→ parameter score stores value's address
→ *score denotes the caller's value
→ *score += 5
→ main's value becomes 85
```

This is the output/modification-parameter model that earlier Units deliberately postponed until the pointer model was ready.

F-U01 still applies: because the function performs integer addition, it checks representability before the operation. Pointers do not make overflow rules disappear.

---

## 5. `NULL` Means “There Is No Object to Dereference Through This Pointer”

You can write:

```c
int *p = NULL;
```

Now `p` is a null pointer.

It may be tested:

```c
if (p != NULL) {
    printf("%d\n", *p);
}
```

but it must not simply be dereferenced:

```c
printf("%d\n", *p);
```

When `p == NULL`, there is no `int` object that this pointer may legally access. Dereferencing a null pointer is undefined behavior.

So any pointer-parameter interface should answer:

> May this parameter be null? If it is null, what does that mean? If null is forbidden, who guarantees that precondition?

`add_bonus` chooses one design: null is accepted as input but causes failure before any dereference. That is an interface choice, not the only possible design for every function.

---

## 6. A Pointer Can Be Invalid Even When It Is Not `NULL`

Consider:

```c
int *bad_pointer(void) {
    int local = 10;
    return &local;
}
```

While `local` is alive, `&local` really is its address.

But F-U05 established that an ordinary automatic local object's lifetime ends when that execution of the function ends.

After the function returns, the old address cannot be used as though the same `local` object still existed there. Such a pointer is commonly called a **dangling pointer**.

The important lesson is:

> The numeric-looking address may appear unchanged, but that does not mean the original object is still within its lifetime.

Pointer validity therefore requires more than “not null.” The pointed-to object must still exist and the requested access must be permitted.

---

## 7. Two Different Pointers Can Reach the Same Object

```c
int value = 10;
int *a = &value;
int *b = &value;
```

Conceptually:

```text
a ──┐
    ├──► value
b ──┘
```

`a` and `b` are **aliases** for the same object.

If:

```c
*a = 20;
```

then `*b` also reads 20 because there are not two copies of the integer—there are two routes to the same object.

This matters for function interfaces.

For example:

```c
#include <stddef.h>

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

Calling:

```c
swap(&value, &value);
```

passes the same object through both parameters. This implementation remains valid; the final value simply stays unchanged, making the operation a no-op.

Another interface might forbid aliasing. The important point is not that aliasing is always wrong, but that the function should know whether its behavior remains meaningful when two parameters identify the same object.

---

## 8. Now Answer the Deferred Array Question

Given:

```c
int values[3] = {10, 20, 30};
```

in most expressions, the array expression `values` is converted to a pointer to its first element, effectively corresponding to:

```c
&values[0]
```

So:

```c
int *p = values;
```

makes `p` point to the first element.

```text
p
│
v
+----+----+----+
| 10 | 20 | 30 |
+----+----+----+
  0    1    2
```

Therefore:

```c
*p        /* 10 */
*(p + 1)  /* 20 */
*(p + 2)  /* 30 */
```

`p + 1` does not mean “add one byte to the numeric address.” It advances to the next `int` element position.

---

## 9. A One-Past Pointer May Be Formed but Not Dereferenced

For the length-3 array:

```c
int *begin = values;
int *end = values + 3;
```

`end` is a pointer one position past the final element.

That **one-past pointer** can serve as a traversal boundary:

```c
for (int *p = begin; p != end; p++) {
    printf("%d\n", *p);
}
```

Every pointer actually dereferenced still identifies one of the three elements. When `p == end`, the loop stops before `*p` occurs.

So these are different:

```c
int *end = values + 3;   /* may be formed */
```

and:

```c
printf("%d\n", *end);  /* must not be dereferenced */
```

Pointer arithmetic is not arbitrary integer-address arithmetic. Its valid relationships are tied to the relevant array object and its one-past boundary.

---

## 10. Reduce Pointer Defects to Four Questions

Before evaluating `*p`, ask:

1. **Was `p` initialized to a usable pointer value?**
2. **Is it null?** If so, what does the interface say?
3. **Is the target object still alive?**
4. **Is the position within the legal element range rather than one-past or beyond?**

For example:

```c
int *p;
*p = 10;
```

`p` has not been given a valid target.

```c
int *p = NULL;
*p = 10;
```

there is explicitly no object to dereference.

```c
int *p = bad_pointer();
*p = 10;
```

the object that once occupied the location has ended its lifetime.

```c
int values[3] = {10, 20, 30};
int *p = values + 3;
printf("%d\n", *p);
```

the one-past pointer can exist but does not identify an element that may be dereferenced.

These four questions are more useful than memorizing a disconnected vocabulary list of “wild,” “null,” or “dangling” pointer defects.

---

## 11. Independent Practice: Return Minimum and Maximum Through Two Outputs

Now that pointers have been established formally, revisit an interface that earlier Units deliberately postponed:

```c
int find_min_max(const int values[], int length,
                 int *min_out, int *max_out);
```

Define the first contract before implementing it:

- `values` must identify at least `length` readable `int` elements;
- `length <= 0` means failure;
- in version 1, neither output pointer may be `NULL`;
- no output object is modified on failure;
- on success, both results are written;
- version 1 allows `min_out == max_out`.

The last rule deserves attention.

If both outputs may alias, first compute into local variables:

```c
int local_min = values[0];
int local_max = values[0];
```

After traversal, write outputs in the interface's defined order:

```c
*min_out = local_min;
*max_out = local_max;
```

If the pointers are the same, the second write becomes the final observable value. That shows why merely saying “aliasing is allowed” is not enough; the contract should explain what aliasing means for the result.

If that behavior is not useful, another reasonable design is to reject `min_out == max_out`. A good interface is not the one that accepts the most cases; it is the one whose rules are clear and testable.

---

## 12. Change the Requirement: Allow One Output to Be Omitted

New rule:

> Either `min_out` or `max_out` may be `NULL` to mean “that result is not requested,” but they may not both be `NULL`.

Update the contract before changing the code.

When results are written, test each optional output separately:

```c
if (min_out != NULL) {
    *min_out = local_min;
}

if (max_out != NULL) {
    *max_out = local_max;
}
```

Do not dereference an optional pointer and only then check whether it was omitted.

Test at least: both outputs requested, minimum only, maximum only, both omitted, empty input, and whatever aliasing rule your interface defines.

---

## 13. Optional: Let AI Challenge Your Pointer Diagram

You may skip this section completely.

Without any tool first, draw and explain:

> In `int value = 10; int *p = &value;`, what are the object, value, address, pointer, and `*p`? Besides “not `NULL`,” what must be true before a pointer can be dereferenced safely?

If you want another check, give the diagram and explanation to an AI tool and ask for an example of a non-null pointer that still must not be dereferenced. No fixed prompt is required, and you do not need to save or submit the conversation.

If the response conflicts with object lifetime, array bounds, or a reproducible program, return to that evidence and judge again.

---

## 14. Before Leaving This Unit, Make Sure You Can Trace “What Does This Point To?”

Answer directly:

- What do `score`, `&score`, `p`, and `*p` each represent?
- Why does `*p = 90` change the target object rather than replacing the pointer with 90?
- Why does `scanf` need `&score`?
- Can `NULL` be compared? Can it be dereferenced?
- Why can a non-null pointer still become invalid when an object's lifetime ends?
- When two pointers identify the same object, why is a modification through one visible through the other?
- How does an array expression connect to the address of its first element in most expressions?
- Why may `values + length` be used as a one-past end position but not dereferenced?

If an answer is only a memorized sentence, draw objects as boxes and pointers as arrows, then trace one read or write.

---

## 15. Chapter Wrap-Up

Earlier Units repeatedly used the idea of a “location” without forcing the entire model at once. `scanf` needed a place to write, array parameters let functions reach elements, string functions moved through character positions, and F-U05 reminded us that objects have lifetimes.

F-U06 brings those clues together: **a pointer stores a location; dereferencing uses that location to access an object; safe use depends on initialization, nullability, lifetime, array boundaries, and aliasing.**

The next Unit shifts from “how do we reach one object?” to “how can one object contain several fields of different kinds?” A student record may have an ID, a name, and a score at the same time. That is the data-organization problem structures solve.

## Navigation

- [Previous Unit: Call Stack and Recursion](unit-05-call-stack-recursion.en.md)
- [Next Unit: Structures](unit-07-structures.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-06-pointers.zh-TW.md)
