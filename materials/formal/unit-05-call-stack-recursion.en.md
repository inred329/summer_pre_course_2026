# Formal Unit F-U05: How Does a Function Call Create a New Execution Environment?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U05：函數呼叫如何建立新的執行環境？](unit-05-call-stack-recursion.zh-TW.md)

The previous Units have already called many functions: `sum_array`, `max_array`, `strlen`, `strcmp`, and others.

So far, we have mostly treated a function as “give it data, let it do its work, then receive a result.” Now move the camera inside the call:

> When `main` calls another function, where does the caller's unfinished work go? How are the callee's parameters and local variables kept separate? What happens when that function calls another function—or even itself?

This Unit uses **call frame** and **call stack** as reasoning models. Many implementations really do use a runtime stack to manage function-call state, but the C language standard does not require one fixed physical stack layout. The diagrams here are therefore a model for tracing execution, not a promise about one machine's exact memory arrangement.

---

## 1. One Function Call Needs State That Belongs to That Call

Start with a familiar function:

```c
int square(int x) {
    int result = x * x;
    return result;
}
```

Suppose `main` executes:

```c
int a = square(5);
```

To complete this call, we must at least be able to track:

- this call's parameter `x` is 5;
- this call's local `result` becomes 25;
- when `square` finishes, execution must return to the place in `main` that is waiting for the value.

Think of this set of state that belongs to one particular call as a **call frame**.

If the program later executes:

```c
int b = square(8);
```

that is a new call with its own `x` and `result`. The previous call's local state is not reused as the new call's local state.

---

## 2. When One Function Calls Another, Unfinished Work Forms Layers

Consider:

```c
int double_value(int x) {
    return x * 2;
}

int add_one_then_double(int x) {
    return double_value(x + 1);
}
```

Calling:

```c
add_one_then_double(4)
```

can be traced as:

```text
main
└─ add_one_then_double(4)
   └─ double_value(5)
```

The innermost `double_value(5)` finishes first and returns 10. Only then can `add_one_then_double` finish and return to `main`.

Using a call-stack model:

```text
top/current: double_value frame
             add_one_then_double frame
             main frame
```

When a function returns, the most recent active call completes first and control returns to the call that was waiting for it.

That “last called, first completed” order is the key preparation for recursion.

---

## 3. Scope and Lifetime Answer Different Questions

Consider:

```c
int function(void) {
    int local = 10;
    return local;
}
```

There are two different questions about `local`.

### Where may the name be written in the source code?

That is a question of **scope**. The name `local` can be used directly only within its block scope.

### How long does the object exist while the program runs?

That is a question of **lifetime**. A normal automatic local object exists during that execution of the block; when that call ends, that call's `local` object also reaches the end of its lifetime.

This distinction becomes directly important for pointer safety. Even if a program once knew where an object was, it cannot keep treating that location as a live object after the object's lifetime has ended.

F-U06 handles that formally. For now, keep “where the name is visible” separate from “when the object exists.”

---

## 4. Recursion Is a Function Calling Itself, but Every Call Is Still a Separate Call

Start with a small countdown:

```c
void countdown(int n) {
    if (n == 0) {
        printf("Go!\n");
        return;
    }

    printf("%d\n", n);
    countdown(n - 1);
}
```

Calling:

```c
countdown(3);
```

can be traced as:

```text
countdown(3)
└─ countdown(2)
   └─ countdown(1)
      └─ countdown(0)
         └─ print Go! and return
```

Each level has its own parameter `n`: 3, 2, 1, and 0.

Two roles appear:

- `n == 0`: the **base case**, which finishes without calling itself again;
- `countdown(n - 1)`: the **recursive case**, which turns the problem into a smaller one and calls again.

Merely writing a base case is not enough. The recursive case must actually move the state toward it.

---

## 5. “A Base Case Exists” and “The Program Will Reach It” Are Different Claims

For example:

```c
void broken(int n) {
    if (n == 0) {
        return;
    }

    broken(n + 1);
}
```

The base case `n == 0` exists, but a call that starts at `broken(3)` moves through 4, 5, 6, and farther away.

So when judging recursion, do not ask only:

> Where is the base case?

Also ask:

> Does every recursive step actually move the state toward that base case?

If calls continue without bound, the implementation must keep preserving more active-call state and can eventually exhaust available execution resources. On common systems this appears as stack exhaustion or stack overflow. The key idea is not one fixed stack size; it is that **an unbounded call chain requires unbounded resources, while real programs have finite resources.**

---

## 6. Factorial Shows Both the Downward Calls and the Work Waiting on the Way Back

Mathematically:

```text
4! = 4 × 3 × 2 × 1
```

Start with a direct recursive version:

```c
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }

    return (unsigned long long)n * factorial(n - 1);
}
```

For `factorial(4)`, the calls go downward first:

```text
factorial(4)
└─ factorial(3)
   └─ factorial(2)
      └─ factorial(1)
```

Only after the base case returns do the waiting operations complete:

```text
factorial(1) = 1
factorial(2) = 2 × 1 = 2
factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
```

Each level therefore preserves not only its own `n`, but also the unfinished idea “after the next level returns, multiply by my `n`.”

---

## 7. Termination Does Not Mean the Result Fits the Type

The direct `factorial` still has two problems:

1. negative values are not valid inputs for the factorial interface defined here;
2. even when recursion terminates correctly, the mathematical result may exceed `unsigned long long`.

We can reuse the sentinel idea from F-U02 and keep the example free of output pointers:

> Every valid factorial result is greater than 0, so reserve the return value 0 to mean “failure.”

```c
#include <limits.h>

unsigned long long factorial_checked(int n) {
    if (n < 0) {
        return 0;
    }

    if (n == 0 || n == 1) {
        return 1;
    }

    unsigned long long smaller = factorial_checked(n - 1);
    if (smaller == 0) {
        return 0;
    }

    if (smaller > ULLONG_MAX / (unsigned long long)n) {
        return 0;
    }

    return (unsigned long long)n * smaller;
}
```

This separates three questions:

- **termination**: does `n` move toward 0 or 1?
- **input validity**: is `n < 0` rejected?
- **representation range**: is the multiplication checked before producing a value that does not fit `unsigned long long`?

A return value of 0 tells the caller that this interface could not produce a valid factorial result.

This sentinel design works because a mathematically valid factorial result is never 0. If a problem can legitimately return 0, then 0 cannot be borrowed casually as a failure marker.

---

## 8. Do Not Call Every Recursion Failure “Stack Overflow”

Several failures can look related but have different causes.

### No base case

```c
int countdown(int n) {
    return countdown(n - 1);
}
```

There is no terminating branch, so the active call chain keeps growing and may eventually exhaust execution resources.

### A base case exists, but the direction is wrong

```c
return factorial_checked(n + 1);
```

The termination condition exists, but the state moves away from it. This is a logic/termination defect.

### Negative input is accepted incorrectly

If the code says:

```c
if (n <= 1) {
    return 1;
}
```

then `factorial(-5)` also returns 1 immediately. It terminates, but violates the input requirement.

### The result exceeds the selected type

The recursive path can be completely correct and still produce a factorial too large for the representation. That is a range problem, not a base-case problem.

So when recursion fails, classify the problem first: **no termination, wrong direction, invalid input, or insufficient result range?**

---

## 9. Use Strings for One More Recursive Example Without Introducing Pointer Arithmetic Early

F-U04 established that a C string ends at `\0`.

We can write a recursive length function using an index:

```c
#include <stddef.h>

size_t recursive_length_at(const char text[], size_t index) {
    if (text[index] == '\0') {
        return 0;
    }

    return 1 + recursive_length_at(text, index + 1);
}
```

Call it with:

```c
size_t length = recursive_length_at("cat", 0);
```

Trace:

```text
index 0: 'c' → 1 + recursive_length_at(text, 1)
index 1: 'a' → 1 + recursive_length_at(text, 2)
index 2: 't' → 1 + recursive_length_at(text, 3)
index 3: '\0' → 0
return values: 1 → 2 → 3
```

This example still assumes `text` is a valid terminated C string. The complete relationship between string parameters and pointers is the subject of the next Unit.

---

## 10. Iteration and Recursion Preserve Progress in Different Places

String length can also be written iteratively:

```c
size_t length = 0;
while (text[length] != '\0') {
    length++;
}
```

Both versions need to preserve “where are we now?”

- The iterative version stores progress explicitly in `length`.
- The recursive version lets each function call preserve its own `index` while waiting for the next call to return.

Recursion is not simply a “more advanced loop.” The choice between iteration and recursion depends on the problem structure, readability, resource cost, and how easily the behavior can be verified.

---

## 11. Independent Practice: `sum_to_n`

Create a recursive function for:

```text
1 + 2 + ... + n
```

Before writing code, define:

- which values of `n` are valid;
- the base case;
- why the recursive case moves toward the base case;
- the result type;
- how the maximum accepted input avoids exceeding that type.

If you choose 0 as a failure sentinel, prove first that every legal result is nonzero. Otherwise, choose another interface design.

Test at least the smallest legal input, a small normal value, the maximum value you permit, an out-of-range value, and a negative input.

---

## 12. Change the Requirement: Limit Recursion Depth and Accepted Input

Suppose the original contract accepted every `n` whose result could be represented. Now add another rule:

> To control recursive resource use, accept values only up to an explicit `MAX_N`.

This separates two limits:

- **mathematical/type limit**: can the result be represented?
- **resource/specification limit**: even if it can, do we intentionally restrict call depth?

Update the input checks and tests without disturbing the base-case logic.

---

## 13. Optional: Let AI Challenge Your Recursion Trace

You may skip this section completely.

Without any tool first, answer:

> Why does “a base case exists” not guarantee termination? Why does “the recursion terminates” still not guarantee valid input or a representable result?

If you want another check, give your explanation to an AI tool and ask it for one example that terminates but returns a wrong result, and one example that has a base case but moves away from it. No fixed prompt is required, and you do not need to save or submit the conversation.

If the AI response conflicts with a call trace, a type limit, or a reproducible result, return to that evidence and judge again.

---

## 14. Before Leaving This Unit, Make Sure You Can Tell Which Call You Are Looking At

Return to the code in this chapter and answer directly:

- Why do two calls to `square(...)` each have their own parameters and local state?
- What different questions do scope and lifetime answer?
- Why are call stack and call frame used here as reasoning models rather than as one fixed physical layout guaranteed by the C standard?
- What is the value of `n` in every level of `countdown(3)`?
- Why can recursion still fail to terminate when a base case exists but the recursive step moves in the wrong direction?
- Why can `factorial_checked` reserve 0 as a failure sentinel?
- Why must the overflow check happen before multiplication?
- Where does the iterative string-length version preserve its current position, and where does the recursive version preserve it?

If an answer has become only a memorized term, draw every active call with its parameter, unfinished work, and return order.

---

## 15. Chapter Wrap-Up

This Unit opened the function “black box” a little. Every call has parameters, local state, and unfinished work that belong to that call. Nested calls create a waiting relationship, and recursion allows many distinct active calls of the same function to exist at once.

Reliable recursion separates at least three questions: **Can execution reach the base case? Is the input valid for the interface? Can the result be represented by the selected type?** Resource limits form another layer.

The next Unit finally answers a question we have deliberately postponed several times. When an array is given to a function, when `scanf` is given a place to store input, or when one function needs to modify data owned by its caller, how does C represent that “place”? That is the model of addresses and pointers.

## Navigation

- [Previous Unit: Strings](unit-04-strings.en.md)
- [Next Unit: Pointers](unit-06-pointers.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-05-call-stack-recursion.zh-TW.md)
