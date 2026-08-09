# Preparatory Unit P-U04: How Can a Large Problem Be Divided into Understandable Work?

Version: 1.1.0  
Status: Student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [前導單元 P-U04：如何把一個大問題拆成可理解的工作？](unit-04-functions-integration.zh-TW.md)

## When `main` Starts Doing Too Much

In the previous Unit, the program learned to inspect state, choose a path, and repeat work. That is enough to solve increasingly interesting problems—but it also creates a new difficulty.

Imagine that one `main` function now does all of this:

```text
read three quiz scores
→ reject invalid input
→ calculate the average
→ decide pass or try again
→ print the report
```

The program may still work, but every responsibility is mixed into the same place. If the passing rule changes, where should you look? If the average is wrong, how much of the program must you inspect? If you want to test only the decision rule, should keyboard input be involved at all?

This Unit follows one question:

> How can a growing program be divided into pieces whose jobs are easy to name, understand, test, and change?

The answer is the **function**.

By the end of the Unit, you should be able to read and write small functions, explain parameters and arguments, follow a return value back to the caller, divide one requirement into several responsibilities, and update the affected calls and tests when an interface changes.

The activities do not need to be submitted. An optional AI extension appears near the end; skipping it does not affect the Unit.

---

## 1. Start with One Job That Is Easy to Name

Suppose the program repeatedly needs the larger of two integers.

You could write the same `if` statement every time, but the job already has a clear name:

> receive two integers and give back the larger one.

That can become a function:

```c
int max_of_two(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}
```

Read the first line from left to right:

```c
int max_of_two(int a, int b)
```

- the first `int` says the function gives an integer result back;
- `max_of_two` is the function name;
- `a` and `b` are the values the function receives while it is doing its work.

The body answers only one question: which value is larger?

It does not read from the keyboard. It does not print a report. It does not decide what the rest of the program should do next.

That narrow responsibility is what makes the function useful.

---

## 2. Call the Function and Use Its Result

A function does nothing merely because it has been defined. Another part of the program must **call** it.

```c
#include <stdio.h>

int max_of_two(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}

int main(void) {
    int larger = max_of_two(5, 8);
    printf("%d\n", larger);
    return 0;
}
```

Expected output:

```text
8
```

The call is:

```c
max_of_two(5, 8)
```

Here, `5` and `8` are **arguments**: the values supplied by the caller.

Inside the function, those values are received by the **parameters** `a` and `b`.

For this call, you can picture the relationship as:

```text
caller gives 5 and 8
        ↓
a becomes 5, b becomes 8
        ↓
function compares them
        ↓
return 8
        ↓
caller stores 8 in larger
```

A parameter belongs to the function definition. An argument belongs to a particular call.

---

## 3. Trace One Call Before Adding More Functions

Walk through this line again:

```c
int larger = max_of_two(5, 8);
```

| Step | Location | What happens? |
|---|---|---|
| 1 | `main` | prepares arguments `5` and `8` |
| 2 | `max_of_two` | receives them as `a = 5`, `b = 8` |
| 3 | `max_of_two` | evaluates `a > b`, which is false |
| 4 | `max_of_two` | executes `return b;` and produces `8` |
| 5 | `main` | stores the returned `8` in `larger` |

While the function is running, the caller is waiting for that call to finish. After `return`, execution continues where the call was used.

This is the basic pattern to keep in mind:

```text
arguments go in
→ function performs one responsibility
→ return value comes back
```

---

## 4. A Good Function Name Describes a Responsibility

Consider these two ideas:

```c
int calculate_average_of_three(int a, int b, int c);
int is_passing(double average, double threshold);
```

Their names already tell you what each part of the program is supposed to do.

The first calculates an average. The second answers a decision question.

That means the rest of the program can coordinate the overall flow without also containing every calculation and rule.

A useful test is to finish this sentence:

> This function is responsible for ________.

If the blank requires a long list joined by “and,” the function may be doing too much.

For example:

```text
read input AND calculate an average AND classify it AND print a report
```

is harder to reason about than several smaller responsibilities.

The goal is not to create as many functions as possible. The goal is to make each important responsibility easy to locate and explain.

---

## 5. Give a Function a Clear Interface

A function is easier to use when the caller knows what values are allowed and what result to expect.

Suppose we define:

```c
int add_bonus(int score, int bonus) {
    return score + bonus;
}
```

For this preparatory example, let the requirement say:

```text
score must be from 0 through 100
bonus must be from 0 through 20
```

Because those inputs are deliberately bounded, the largest possible result is 120, so the addition is safely within the range of an ordinary C `int` on conforming implementations.

That requirement is part of the function's **interface contract**:

```text
input: score 0..100, bonus 0..20
result: score + bonus
responsibility: calculate only
```

The function itself does not need to read the keyboard or print anything.

The caller can check the requirement before the call:

```c
if (score < 0 || score > 100 || bonus < 0 || bonus > 20) {
    printf("Invalid input\n");
    return 1;
}

int adjusted = add_bonus(score, bonus);
```

This gives us an important design habit:

> Know what a function promises, and know what the caller must guarantee before using it.

Later formal Units will study more demanding interfaces, including pointer outputs, integer-range checks, and failure-preserving patterns. They are useful topics, but they are not needed to understand the basic function idea here.

---

## 6. Put a Declaration Before `main` When Needed

So far, each function definition appeared before `main`, which means the compiler saw the full function before the call.

You may also place the definition later in the file. In that case, tell the compiler the interface first with a declaration, often called a **function prototype**:

```c
#include <stdio.h>

int max_of_two(int a, int b);

int main(void) {
    printf("%d\n", max_of_two(5, 8));
    return 0;
}

int max_of_two(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}
```

Now three related ideas can be separated:

- **declaration / prototype**: tells the compiler the function interface;
- **definition**: contains the function body and actual work;
- **call**: asks the function to run with particular arguments.

The declaration and definition must agree in return type and parameter types.

---

## 7. Build the Score Reporter from Responsibilities

Return to the growing program from the opening.

Requirement:

> Read three quiz scores from 0 through 100, calculate their average, and print `Pass` when the average is at least a chosen threshold; otherwise print `Try again`.

Instead of placing the calculation and decision directly inside `main`, give them names:

```c
double average_of_three(int a, int b, int c) {
    return (a + b + c) / 3.0;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}
```

Because each quiz score has already been checked to be between 0 and 100, `a + b + c` is at most 300 and does not create an integer-overflow problem in this example.

A complete small program can then read like this:

```c
#include <stdio.h>

double average_of_three(int a, int b, int c) {
    return (a + b + c) / 3.0;
}

int is_passing(double average, double threshold) {
    return average >= threshold;
}

int main(void) {
    int q1;
    int q2;
    int q3;
    const double threshold = 60.0;

    if (scanf("%d %d %d", &q1, &q2, &q3) != 3) {
        printf("Invalid input\n");
        return 1;
    }

    if (q1 < 0 || q1 > 100 ||
        q2 < 0 || q2 > 100 ||
        q3 < 0 || q3 > 100) {
        printf("Invalid input\n");
        return 1;
    }

    double average = average_of_three(q1, q2, q3);

    printf("Average: %.1f\n", average);

    if (is_passing(average, threshold)) {
        printf("Pass\n");
    } else {
        printf("Try again\n");
    }

    return 0;
}
```

The `&` symbols in the `scanf` call are the same input-address syntax you saw earlier. Pointer concepts will be developed in the formal course; for this Unit, the important part is the division of responsibility after input succeeds.

Read `main` now as a story:

```text
read
→ validate
→ calculate average
→ print average
→ decide pass/fail
```

The detailed calculation and decision rules have names, so you can inspect or test them separately.

---

## 8. Test a Function Without Running the Whole Story

Because `average_of_three` does not read input or print output, you can reason about it directly.

| Call | Expected result |
|---|---:|
| `average_of_three(60, 60, 60)` | 60.0 |
| `average_of_three(59, 60, 61)` | 60.0 |
| `average_of_three(100, 100, 100)` | 100.0 |
| `average_of_three(0, 0, 0)` | 0.0 |

The decision function can be checked independently too:

| Call | Expected meaning |
|---|---|
| `is_passing(59.9, 60.0)` | false / 0 |
| `is_passing(60.0, 60.0)` | true / nonzero |
| `is_passing(60.1, 60.0)` | true / nonzero |

This is one of the strongest reasons to separate responsibilities: when a result is wrong, you can narrow the question.

Instead of asking:

> Why is the entire program wrong?

ask:

> Did input fail, did the average calculation fail, or did the passing decision fail?

---

## 9. Three Common Function Mistakes

### 9.1 Forgetting to Use a Returned Result

This call calculates a value and immediately throws it away:

```c
average_of_three(80, 70, 90);
```

If you need the result later, store or use it:

```c
double average = average_of_three(80, 70, 90);
```

### 9.2 Mixing Too Many Responsibilities

A function like this hides several unrelated jobs behind one vague name:

```c
void do_everything(void) {
    /* read, validate, calculate, decide, print */
}
```

When one rule changes, it becomes harder to tell which part should be edited or tested.

### 9.3 Supplying Arguments in the Wrong Order

Suppose the interface is:

```c
int subtract(int left, int right);
```

Then:

```c
subtract(10, 2)
```

and:

```c
subtract(2, 10)
```

are different calls. Parameter order is part of the interface.

Names help, but the caller still has to understand what each position means.

---

## 10. Change the Requirement and Follow the Interface

Suppose the first version of a function used a fixed five-point bonus:

```c
int add_bonus(int score) {
    return score + 5;
}
```

Later, the requirement changes:

> The caller chooses the bonus amount.

A better interface is now:

```c
int add_bonus(int score, int bonus) {
    return score + bonus;
}
```

That change affects more than the function body.

You must also look for:

1. the declaration, if there is one;
2. every call site;
3. the valid range for the new `bonus` argument;
4. tests for different bonus values;
5. old behavior that should still work, such as a bonus of 5.

For example, an old call:

```c
add_bonus(score)
```

must become something like:

```c
add_bonus(score, 5)
```

A function interface is a connection between parts of the program. Changing one side without updating the other side breaks that connection.

---

## 11. Try It: Write and Trace `max_of_two`

Write this function yourself:

```c
int max_of_two(int a, int b);
```

Before implementation, choose four tests:

| `a` | `b` | Expected result |
|---:|---:|---:|
| 5 | 3 | 5 |
| 2 | 7 | 7 |
| 4 | 4 | 4 |
| -2 | -5 | -2 |

Then trace one call from arguments, through the condition, to the returned value.

If your implementation fails one row, find the first decision that differs from the expected trace instead of rewriting the whole function immediately.

---

## 12. Try It Again: Build the Score Reporter

Create a small program that:

1. reads three integer quiz scores;
2. rejects nonnumeric input and scores outside 0 through 100;
3. calculates the average with a function;
4. decides `Pass` or `Try again` with another function;
5. prints the result.

Useful tests include:

```text
59 60 61 → average 60.0 → Pass
60 60 59 → average 59.7 → Try again
100 100 100 → average 100.0 → Pass
0 0 0 → average 0.0 → Try again
101 80 80 → Invalid input
nonnumeric input → Invalid input
```

Do not begin by writing every line at once. First decide the responsibilities and expected results. Then implement one function, test it, and add the next part.

---

## 13. Optional: Use AI to Challenge Your Function Explanation

If you want an extra exercise, first explain in your own words:

> What is the difference between a parameter and an argument, and why does separating a calculation into a function make testing and requirement changes easier?

You may then ask an AI system to challenge or improve the explanation. This is optional. No fixed prompt or saved conversation is required.

If an AI explanation conflicts with a function trace, compiler result, direct test, or the stated interface, use that evidence to judge the claim again.

---

## 14. Before Moving On, Explain These without Memorizing Definitions

Try to answer from one of the programs in this Unit:

- What responsibility does each function have?
- Which values are parameters, and which are arguments?
- Where does a return value go after `return` executes?
- Why is `average_of_three` easier to test when it does not also read input and print output?
- What must change when a function interface gains a new parameter?
- Why are valid input ranges part of understanding an interface?

If an answer feels abstract, choose one concrete call such as:

```c
max_of_two(5, 8)
```

and walk through it value by value.

---

## 15. Chapter Closing

The preparatory course began with a text file becoming a running program. Then the program gained values and state, learned to choose paths and repeat work, and finally learned to divide growing work into named responsibilities.

Functions give a larger program structure. Arguments carry values into a call, parameters receive them, and return values carry results back. Clear responsibilities make it easier to explain what a program is doing, test one part at a time, and update the right places when a requirement changes.

You have now completed the preparatory sequence. The formal course starts by revisiting something that looked simple earlier: values and types. We have used `int`, `double`, arithmetic, and input many times, but each of those hides representation rules and boundary behavior that become important as programs grow.

That is the next question: why can representation, type, and operations change the result even when the source code looks reasonable?

## Navigation

- [Previous Unit: How Does a Program Select and Repeat?](unit-03-control-flow.en.md)
- [Next: Formal Unit F-U01 — Why Do Representation, Type, and Operations Affect Results?](../formal/unit-01-representation-types.en.md)
- [Formal-Course Materials Index](../formal/README.en.md)
- [Materials Index](../README.en.md)
- [繁體中文版](unit-04-functions-integration.zh-TW.md)
