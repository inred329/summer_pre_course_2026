# Formal Unit F-U03: How Does Data Form an Ordered Collection?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U03：資料如何形成有順序的集合？](unit-03-arrays.zh-TW.md)

F-U02 ended with a problem where the number of inputs was not known in advance. We could read one value, decide what to do with it, update the current state, and then move on.

Now change the requirement:

> What if all five scores must remain available so that we can revisit one value, find a maximum, modify an item, or analyze the same data again in a different way?

A `sum` and a `count` are no longer enough. We need to keep an entire group of values at the same time, and we need a reliable way to locate each one.

That is the problem arrays solve.

---

## 1. Five Separate Variables Are Possible; Fifty Become a Problem

You could write:

```c
int score1 = 80;
int score2 = 90;
int score3 = 75;
int score4 = 88;
int score5 = 92;
```

But computing an average still requires naming every variable separately. With fifty values, naming, processing, modifying, and testing quickly becomes repetitive and easy to get wrong.

An array lets us place same-kind, same-type values into one ordered collection:

```c
int scores[5] = {80, 90, 75, 88, 92};
```

Draw it first:

```text
Index:   0   1   2   3   4
Value:  80  90  75  88  92
```

Three terms belong together here:

- `scores` is the array.
- Each stored value is an element.
- The position of an element is identified by an index.

The length is 5, but the legal indexes are not 1 through 5. They are **0 through 4**.

That zero-based rule will keep affecting loop conditions and boundaries throughout the course.

---

## 2. An Index Answers “Which Position?”, Not “What Value?”

For example:

```c
printf("%d\n", scores[2]);
```

`scores[2]` means the element at index 2—the third position—which currently contains `75`.

If we write:

```c
scores[2] = 78;
```

the array becomes:

```text
Index:   0   1   2   3   4
Value:  80  90  78  88  92
```

When you read `scores[i]`, use two steps:

1. Determine the value of `i`.
2. Use that value to locate the element.

This avoids a common confusion: the index is the position; the element is the data stored there.

---

## 3. Arrays and Loops Naturally Fit Together

F-U02 already established repeated control flow. Now the loop-control variable also becomes the current array position:

```c
int sum = 0;

for (int i = 0; i < 5; i++) {
    sum += scores[i];
}
```

Trace it:

| `i` | `scores[i]` | `sum` after update |
|---:|---:|---:|
| 0 | 80 | 80 |
| 1 | 90 | 170 |
| 2 | 75 | 245 |
| 3 | 88 | 333 |
| 4 | 92 | 425 |

The correspondence is exact:

```text
legal indexes: 0, 1, 2, 3, 4
loop i values: 0, 1, 2, 3, 4
```

So the loop condition is:

```c
i < 5
```

not:

```c
i <= 5
```

If `i == 5` still enters the loop, `scores[5]` is no longer an element of this array.

---

## 4. Out-of-Bounds Access Is More Than “Getting a Strange Value”

Consider:

```c
int values[5] = {10, 20, 30, 40, 50};
printf("%d\n", values[5]);
```

The legal indexes are 0 through 4, so `values[5]` is out of bounds.

In C, the rule is not “you are guaranteed to get some garbage value.” This is **undefined behavior**. One run that appears normal does not establish that the access is safe.

A useful way to inspect any array loop is to put two questions side by side:

> What is the largest value `i` can have inside the loop? Is that still a legal index?

For example:

```c
for (int i = 0; i <= 5; i++) {
    printf("%d\n", values[i]);
}
```

You can find the defect without running the program. The loop eventually reaches `i == 5`, while the final legal index of a length-5 array is 4.

---

## 5. “There Are Five Elements” Does Not Mean All Five Already Hold Valid Data

Now consider:

```c
int values[5];
```

This creates five `int` elements, but local automatic elements do not become reliable zeros merely because they are in an array.

If the next line is:

```c
printf("%d\n", values[0]);
```

you are reading an element that has not been initialized. That is not behavior a correct program may rely on.

So a legal index is only the first requirement.

Before reading an element, also ask:

> Has this position actually received a valid value through initialization or successful input?

If the data comes from the user, bring back the F-U02 rule: check that `scanf` succeeded and that the value is in the allowed range before storing it in the array.

---

## 6. When an Array Goes to a Function, Its Length Goes Too

Suppose we move the summation responsibility out of `main`:

```c
int sum_array(const int values[], int length) {
    int sum = 0;

    for (int i = 0; i < length; i++) {
        sum += values[i];
    }

    return sum;
}
```

Call it with:

```c
int total = sum_array(scores, 5);
```

Why include `length`?

A function cannot look at a parameter written as `values[]` and automatically recover how many usable elements the caller intends to provide. The interface must state how far traversal may go.

For now, read:

```c
const int values[]
```

as “this function can read a sequence of `int` elements and does not modify them.” The exact relationship between array parameters and pointers in C will be built carefully in F-U06. Here, keep the focus on the **element, index, length, and traversal contract**.

This minimal function also has an explicit assumption: the complete sum must be representable as `int`. F-U01 established that signed integer overflow is undefined behavior, so a larger possible data range requires a wider suitable type or a pre-addition boundary check.

---

## 7. Before Finding a Maximum, Deal with the Case Where There Is No First Element

A common maximum function starts with the first element:

```c
int max_array(const int values[], int length) {
    int max = values[0];

    for (int i = 1; i < length; i++) {
        if (values[i] > max) {
            max = values[i];
        }
    }

    return max;
}
```

This function has an important precondition:

> `length` must be greater than 0.

The reason is direct. If `length == 0`, there is no first element, so `values[0]` is not a valid access.

The caller handles that case before the call:

```c
if (length > 0) {
    int maximum = max_array(values, length);
    printf("Max: %d\n", maximum);
} else {
    printf("No data\n");
}
```

This version deliberately uses only the direct return-value model already established earlier in the course. It does not introduce output pointers or `NULL` before the pointer model exists. Once F-U06 builds that model, returning status separately from output data will make much more sense.

---

## 8. Use One Array for Three Different Traversals

Start with:

```c
int values[5] = {3, -2, 7, -1, 4};
```

### Task A: add every element

```c
int sum = 0;
for (int i = 0; i < 5; i++) {
    sum += values[i];
}
```

### Task B: replace negative values with zero

```c
for (int i = 0; i < 5; i++) {
    if (values[i] < 0) {
        values[i] = 0;
    }
}
```

### Task C: count values greater than or equal to 4

```c
int count = 0;
for (int i = 0; i < 5; i++) {
    if (values[i] >= 4) {
        count++;
    }
}
```

All three loops travel through exactly the same index path. The only difference is the work performed at each element.

That is the power of arrays: when the amount of data grows, we do not invent a new variable name for every value. We place one reliable element operation inside one reliable traversal.

---

## 9. Independent Practice: Build a Ten-Score Analyzer

Read exactly 10 valid scores, then display:

- average
- maximum
- minimum
- passing count

First define the valid score range, such as 0 through 100.

Do not store data first and try to clean it later. Each input should follow this path:

```text
read succeeded? → value in range? → only then write the next array element
```

Then create at least these test sets:

| Test data | What should it reveal? |
|---|---|
| all equal | maximum, minimum, and average agree |
| increasing | updates remain correct as traversal advances |
| decreasing | logic does not depend on input order |
| includes 59 and 60 | passing boundary |
| includes 0 and 100 | valid-range boundaries |
| invalid text | must not be stored |
| out-of-range value | must not become analysis data |

If `int` is used to add ten scores from 0 through 100, the largest possible total is 1000, so the accumulation range is easy to prove safe in this exercise.

That is a useful habit: do not wait for overflow to become a problem before thinking about types. Derive the worst case from the requirement first.

---

## 10. Change the Requirement: Drop One Lowest Score Before Averaging

Now change the requirement:

> From the ten valid scores, remove one lowest score and compute the average of the remaining nine.

“Remove” does not necessarily mean physically shifting elements in the array.

If you already know:

- total `sum`
- minimum `min`
- number of elements `count`

then the new average follows conceptually from:

```text
(sum - min) / (count - 1)
```

The interesting question is not the formula itself. Ask:

> Did the requirement actually change the stored data, or only the way we analyze that data?

In the fixed-ten-valid-scores version, `count - 1` is always 9, so division by zero cannot occur.

If a future reusable function accepts arbitrary lengths, the specification must be revisited: does “drop one lowest score and average the rest” make sense for an empty array or for only one element?

---

## 11. Optional: Let AI Challenge Your Index Explanation

You may skip this section completely.

Without using any tool first, explain:

> If the length is 5, why are the legal indexes 0 through 4? Why does a function usually need both an array and its length?

If you want another check, give your explanation to an AI tool and ask for a counterexample that could cause either an out-of-bounds access or a missed element. No fixed prompt is required, and you do not need to save or submit the conversation.

If the AI response conflicts with an index diagram, a loop trace, a C language rule, or a reproducible test, return to that evidence and judge again.

---

## 12. Before Leaving This Unit, Make Sure You Can Separate “Position” from “Data”

Return to the code in this chapter and answer directly:

- For an array of length `n`, why is the final legal index `n - 1`?
- In `scores[2]`, how is the `2` different from the element value?
- Why is `i < length` usually easier to maintain than hard-coding the final index in a traversal?
- Why does a legal index still not guarantee that the element has been initialized?
- Why can one apparently normal run not prove that an out-of-bounds access is safe?
- Why does a function usually need a length when it receives an array?
- Why does `max_array` require `length > 0`?
- When the requirement changes from “analyze ten scores” to “drop the lowest score and analyze the rest,” what data must actually change and what can simply be recomputed?

If one answer is only a sentence you memorized, draw a small array with indexes and values and trace the operation yourself.

---

## 13. Chapter Wrap-Up

F-U02 solved the problem “when one value arrives, decide reliably how to process that value.” F-U03 lets us keep many same-type values at the same time and revisit them by position.

Arrays organize elements into an ordered collection. Reliable array code is not mainly about memorizing `[]` syntax. It is about preserving three facts: **how many elements are currently valid, where the legal index range ends, and whether each element you read actually contains valid data.**

The next Unit introduces an extremely common array that already looks familiar: text.

In C, a string is not a separate magical primitive type. Text is stored in an array of characters, with one additional rule: the program must know where the text ends. That will push today's ideas about length and boundaries one step further.

## Navigation

- [Previous Unit: Complex Control Flow](unit-02-complex-control-flow.en.md)
- [Next Unit: Strings](unit-04-strings.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-03-arrays.zh-TW.md)
