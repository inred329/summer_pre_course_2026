# Formal Unit F-U02: How Can Reliable Multi-Branch and Repetitive Flows Be Built?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U02：如何建立可靠的多分支與重複流程？](unit-02-complex-control-flow.zh-TW.md)

F-U01 showed that the same program can behave differently when types, representations, or the timing of operations change.

Now take one more step. Once a program does more than compute one result and begins choosing different paths from its data, a new question appears:

> When conditions multiply, branches become nested, and the amount of input is not known in advance, how can we know that every important path is reliable?

This Unit is not just about adding more `if` statements and loop syntax. We will keep returning to three questions: **What paths are possible? Under what conditions does each path happen? What evidence would show that we did not miss an important case?**

---

## 1. Start with a Grade Rule That Looks Simple

Consider this program:

```c
int score = 85;

if (score >= 90) {
    printf("A\n");
} else if (score >= 80) {
    printf("B\n");
} else if (score >= 70) {
    printf("C\n");
} else {
    printf("D\n");
}
```

Do not run it yet. Trace from the first condition downward:

1. `85 >= 90` is false, so evaluation continues.
2. `85 >= 80` is true, so the program prints `B`.
3. Once one branch is selected, the remaining `else if` conditions are not tested.

The important idea is not merely that you can write `else if`. It is that **the order of the branches is part of the rule itself.**

For example:

```c
if (score >= 70) {
    printf("C or above\n");
} else if (score >= 90) {
    printf("A\n");
}
```

For `95`, the first condition is already true, so the `score >= 90` branch can never be reached.

The program can compile and every condition is legal C, yet the rule has still been arranged incorrectly.

---

## 2. Boundary Values Expose Branch Rules Quickly

Suppose the grading rule is:

- 90 and above: A
- 80 through 89: B
- 70 through 79: C
- otherwise: D

Testing only `85` is far from enough.

At minimum, look at values like these:

| `score` | Expected result | Why it matters |
|---:|---|---|
| 69 | D | just below C |
| 70 | C | start of C |
| 79 | C | just before B |
| 80 | B | start of B |
| 89 | B | just before A |
| 90 | A | start of A |

These numbers are not arbitrary. They sit next to the points where the rule changes, so they quickly reveal mistakes such as `>` versus `>=`, incorrect branch order, or a missing range.

When you meet a multi-branch rule, ask:

> At which values does the rule change, and where do the value just before the boundary, the boundary itself, and the value just after it go?

---

## 3. `switch` Is Another Way to Choose a Path, but for a Different Kind of Problem

Now suppose the program is not classifying a numeric range. It is handling a menu:

```text
1 = Add
2 = Delete
anything else = Unknown
```

For this kind of discrete choice from one value, you can use:

```c
switch (command) {
    case 1:
        printf("Add\n");
        break;
    case 2:
        printf("Delete\n");
        break;
    default:
        printf("Unknown\n");
}
```

`switch` fits discrete choices from an integer-like or enumeration value. Range conditions such as `score >= 90` still fit `if` better.

There is another piece of control flow here that is easy to overlook: `break`.

If you write:

```c
case 1:
    printf("One\n");
case 2:
    printf("Two\n");
```

then when `command == 1`, execution continues from `case 1` into `case 2`. This is called **fall-through**.

Fall-through is not automatically a syntax error. Sometimes it is intentional. But if the requirement says one command should perform only one action, forgetting `break` is a logic error. When fall-through is intentional, the reason should also be obvious to the reader.

---

## 4. Nested Conditions Mean More Path Combinations, Not Merely More `if` Statements

Consider a member-discount rule:

```c
if (is_member) {
    if (amount >= 1000) {
        discount = 0.15;
    } else {
        discount = 0.10;
    }
} else {
    discount = 0.0;
}
```

Instead of reading only the indentation, translate it into paths:

| `is_member` | `amount` | Expected discount |
|---|---:|---:|
| false | 1500 | 0.00 |
| true | 999 | 0.10 |
| true | 1000 | 0.15 |

The first row reveals something useful: when `is_member` is false, `amount >= 1000` does not need to be checked to determine the discount at all.

So when conditions are nested, a path table often works better than staring at braces. It shows which combinations can actually reach a result.

This matters for testing too: **the goal is to test reachable paths, not simply to make every individual `if` true once.**

---

## 5. When the Same Decision Must Repeat, the Problem Moves from Branches into Loops

So far, every example has processed one item.

Now suppose you want to keep reading integers and add them, but you do not know how many values will arrive. Repeating `scanf` five times is clearly not a real solution; the process itself must repeat.

First define a protocol:

> The user enters `-1` to mean “the data is finished.”

A special value used this way is called a **sentinel**.

Here is a complete example:

```c
#include <stdio.h>

int main(void) {
    int value;
    int sum = 0;

    while (scanf("%d", &value) == 1) {
        if (value == -1) {
            printf("Sum: %d\n", sum);
            return 0;
        }

        sum += value;
    }

    if (feof(stdin)) {
        fprintf(stderr, "Input ended before sentinel\n");
    } else {
        fprintf(stderr, "Invalid input\n");
    }

    return 1;
}
```

Trace three different situations.

### Case A: the sentinel is reached normally

```text
5 8 2 -1
```

`5`, `8`, and `2` are added to `sum`. `-1` means “stop” and is not part of the sum.

### Case B: EOF arrives first

If the input source ends before `-1` appears, `scanf` cannot successfully read another integer. That is not the sentinel; it means there is no more input available from the source.

### Case C: invalid text appears

```text
5 8 hello
```

`hello` cannot be converted according to `%d`, so the conversion fails. That is not a sentinel and it is not EOF either.

Therefore:

> **A sentinel is valid data with a special meaning; EOF means the input source has ended; invalid text means the requested conversion failed. They are three different states.**

---

## 6. Why Should the Loop Condition Check the Result of `scanf` Directly?

You may have seen code like this:

```c
scanf("%d", &value);
while (value != -1) {
    sum += value;
    scanf("%d", &value);
}
```

It looks shorter, but it throws away an important piece of information: **Did this read actually succeed?**

If the first conversion fails, `value` does not receive a valid integer from that input. If a later conversion fails, the previous value may remain in the variable and can be processed again by mistake.

A reliable input loop therefore often makes “the read succeeded” part of the condition that permits the value to be used:

```c
while (scanf("%d", &value) == 1) {
    /* value is used only after a successful read */
}
```

This is the same principle established in the preparatory course: **check that input succeeded before using the value.**

---

## 7. Loop Invariant: Find One Fact That Every Iteration Must Preserve

A loop is harder to verify than one `if` partly because the same code may run many times.

Instead of trying to reason about all iterations at once, identify one fact that should remain true at the same point in every iteration.

For the sum program, after a value has been read successfully and before the current value is processed, we can state:

> `sum` equals the total of all previously accepted, non-sentinel inputs.

This kind of statement is called a **loop invariant**.

Do not rush to memorize the definition. Use the invariant to answer three questions:

1. **Is it true before the work begins?** With no accepted values yet, `sum == 0`.
2. **Does one normal iteration preserve it?** After the current value is added, it becomes part of the previously accepted data seen by the next iteration.
3. **Does it give the required result when the sentinel appears?** The sentinel is not added, so the current `sum` is exactly the total of all valid data.

If you can explain those three steps, you are no longer saying only that “the loop seems to work.” You are explaining why its state stays correct as repetition continues.

---

## 8. Put Each Error Back into the Rule It Breaks

Now several common errors no longer need to become another list to memorize.

### The sentinel is included in the sum

If the program performs:

```c
sum += value;
```

before checking `value == -1`, then the sentinel has already contaminated `sum`. That breaks the invariant that `sum` contains only non-sentinel values.

### `break` is missing

If the menu requirement permits one action per command, fall-through lets one path accidentally continue into another path.

### Only the easiest nested path is tested

Testing only `true/true` does not establish that the false path or the 999/1000 boundary is correct. This is not a compiler defect; the evidence is simply incomplete.

### A stale value is used after an input failure

That breaks the assumption that the `value` processed in each iteration came from a successful read. The root problem is not the `while` statement itself; the data was never validated before entering the processing path.

Debugging becomes much easier when you can name the rule that has been broken instead of merely naming an error category.

---

## 9. Two Small Exercises: Make the Paths Visible First

### Exercise A: a discrete menu

Build this menu:

```text
1 = Query
2 = Modify
0 = Exit
anything else = Invalid
```

Before writing the `switch`, list the four classes of possible paths. Check that `scanf` succeeded before using `command`.

After it works, deliberately remove one `break`, predict which input will perform one extra action, and then verify the prediction.

### Exercise B: member discount

Reuse the member-discount rule from earlier, but do not add more code yet.

First answer:

- Does a non-member need the `amount >= 1000` test to determine the discount?
- Where does `amount == 999` go?
- Where does `amount == 1000` go?

Once you can answer all three from the path table, implement the program.

---

## 10. Independent Practice: How Do You Average an Unknown Number of Scores?

Now turn the sentinel sum into a fuller problem.

Keep reading scores from `0` through `100`. Use `-1` to mean that input is finished. At the end, display:

- the number of valid scores
- the average of the valid scores

Before writing the entire program, define:

> What do `count` and `sum` mean at the start of each iteration?

Then trace at least these cases:

| Input situation | Risk to observe |
|---|---|
| one value then `-1` | basic counting and averaging |
| several values then `-1` | repeated updates stay consistent |
| immediate `-1` | `count == 0`, so division by zero must be avoided |
| `0` and `100` | valid range boundaries |
| invalid text | must not be mistaken for the sentinel |
| EOF before sentinel | must be distinguished from normal termination |
| out-of-range number | requirement not yet defined; a decision is needed |

The last row deliberately leaves a specification question open. If the program reads `120`, should it reject the value, ignore it, or terminate?

The program should not silently invent a requirement that was never stated.

---

## 11. Change the Requirement: Ignore Out-of-Range Values

Now complete the missing rule:

> Ignore ordinary numeric values below 0 or above 100, but keep `-1` as the sentinel. Invalid text and EOF still follow their original handling.

Notice that `-1` is also below 0, so the order of checks now matters.

If you write this first:

```c
if (value < 0 || value > 100) {
    continue;
}
```

then `-1` is classified as “ignore” before it can be recognized as the termination signal. The program will never receive the intended stop command.

So the sentinel must be recognized before the ordinary range check.

After the change, answer again:

- Has the invariant for `sum` changed?
- Exactly when does `count` increase?
- Which paths do `-1`, `120`, `hello`, and EOF follow?
- Do all of the previously correct cases still pass?

This is a small regression test: adding a new rule must not accidentally break behavior that was already correct.

---

## 12. Optional: Let AI Challenge Your Path Explanation

You may skip this section completely.

Without using any tool first, explain:

> Why can branch order change the result? What do `-1`, EOF, invalid text, and a loop invariant each mean?

If you want one more check, give your explanation to an AI tool and ask it to identify places where you may have confused data, input status, or loop guarantees. No fixed prompt is required, and you do not need to save or submit the conversation.

If the AI response conflicts with a path table, `scanf` return rules, an actual trace, or a reproducible result, return to that evidence and judge again.

---

## 13. Before Leaving This Unit, Make Sure You Can Actually Trace the Paths

Return to the programs in this chapter and answer directly from the code rather than from memorized definitions:

- Why can changing the order of an `if`/`else if` chain change program behavior?
- Why do 79, 80, 89, and 90 verify the grade rule better than testing only 85?
- When does `switch` fit the problem, and when does `if` still fit better?
- Why should nested conditions be understood through reachable combinations rather than by simply counting `if` statements?
- Why are a sentinel, EOF, and invalid input three different things?
- Why should `scanf` success be checked before `value` is used?
- Can you state the sum loop invariant in your own words and explain how it is initialized, preserved, and used to establish the result?
- When the requirement changes to ignore out-of-range values, why does the position of the `-1` check become important?

If one answer is only a sentence you memorized, return to the corresponding example, change an input, predict the path, and trace it again.

---

## 14. Chapter Wrap-Up

F-U01 asked how one value is represented, interpreted, and operated on. This Unit moved the question forward: **Which path does that value make the program take, and is that path reliable?**

Reliable multi-branch flow comes from correct condition order and boundary tests. Nested logic must be understood through paths that can actually be reached. Repetitive input needs both a termination rule and a preserved record of whether reading succeeded. A loop invariant gives us a way to explain how state remains correct across iteration after iteration.

The next Unit changes the scale of the data itself. We can now process one value after another reliably, but if five, fifty, or five hundred values must all be kept at the same time, naming them `score1`, `score2`, `score3`, and so on quickly becomes unmanageable. That is the problem arrays are designed to solve.

## Navigation

- [Previous Unit: Representation, Types, and Operations](unit-01-representation-types.en.md)
- [Next Unit: Arrays](unit-03-arrays.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-02-complex-control-flow.zh-TW.md)
