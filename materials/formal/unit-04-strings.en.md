# Formal Unit F-U04: How Is Text Represented and Processed as Data?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U04：文字資料如何被表示與處理？](unit-04-strings.zh-TW.md)

F-U03 let us place many same-type values in an array and traverse them by index.

Now change the element type from `int` to `char`:

```c
char letters[4] = {'c', 'a', 't', '?'};
```

This is already a character array. But if we want it to represent the text `cat`, a new problem appears:

> An array has a capacity, but it does not automatically tell a string function where the text ends. How does a C program know when to stop reading the characters?

The core C-string rule is to place an explicit terminator in the array data itself.

---

## 1. `"cat"` Actually Needs One More Element

When you write:

```c
char word[] = "cat";
```

first draw it:

```text
Index:    0    1    2    3
Content: 'c'  'a'  't' '\0'
```

The first three elements are visible text. The final element is the **null character** `\0`.

So a C string is not a separate built-in primitive type. The common model is:

> **a sequence of `char` elements followed by `\0` at the end of the text.**

That immediately brings back two F-U03 questions: Is the position legal? Does it contain valid data? Strings add one more question: Is the terminator present in the right place?

---

## 2. A Character Array Is Not Automatically a C String

This array:

```c
char letters[3] = {'c', 'a', 't'};
```

contains three legal, initialized character elements, but no `\0`.

It is therefore a character array, but not a C string that ordinary string functions can safely process.

By contrast:

```c
char word[4] = {'c', 'a', 't', '\0'};
```

has a complete string-termination rule.

Interfaces such as `printf("%s", word)`, `strlen(word)`, and `strcmp(...)` read according to the string convention until they find `\0`. They do not automatically stop merely because the original array happened to have three elements.

---

## 3. Capacity, String Length, and Required Storage Are Different Quantities

Consider:

```c
char name[20] = "Amy";
```

Here:

- the array capacity is 20 `char` elements;
- the current string length is 3;
- storing `"Amy"` requires at least 4 elements because `\0` also needs space.

Draw it:

```text
Index:    0    1    2    3    4 ... 19
Content: 'A'  'm'  'y' '\0'  ...
```

Whenever you see a string buffer, ask:

> How many visible characters may be stored, and is one element still reserved for `\0`?

A capacity-20 array can therefore hold at most 19 visible characters plus the terminator.

---

## 4. `fgets` Makes Capacity Part of the Input Rule

To read a line, start with:

```c
#include <stdio.h>

int main(void) {
    char name[20];

    if (fgets(name, sizeof name, stdin) == NULL) {
        fprintf(stderr, "Input failed.\n");
        return 1;
    }

    printf("Hello, %s", name);
    return 0;
}
```

Here, `sizeof name` is the capacity of the whole array: 20.

For this call, `fgets` stores at most `capacity - 1` characters and preserves space for a terminating `\0` when it succeeds.

But “success” does not automatically mean “the entire logical input line fit in this call.”

Suppose the capacity is only 8 and the user enters:

```text
Alexander\n
```

The buffer cannot hold the whole line. `fgets` can successfully store an initial part and terminate it with `\0`, while the remaining characters stay in the input stream for a later read.

So the next question is:

> Did we receive one complete line, or only the first part of it?

---

## 5. The Newline Can Help Distinguish a Complete Interactive Line

If the user presses Enter and that newline also fits in the array, the stored data commonly looks like:

```text
'A' 'm' 'y' '\n' '\0'
```

Many programs want to keep only `"Amy"`, so they locate `\n` and replace it with `\0`.

Using `strcspn` from `<string.h>`:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char text[20];

    if (fgets(text, sizeof text, stdin) == NULL) {
        fprintf(stderr, "Input failed.\n");
        return 1;
    }

    size_t newline = strcspn(text, "\n");

    if (text[newline] == '\n') {
        text[newline] = '\0';
        printf("Complete line: %s\n", text);
    } else {
        printf("No newline was stored.\n");
    }

    return 0;
}
```

Notice that the final message says only that this buffer contains no newline. It does not by itself prove why.

Possible reasons include:

- the logical line was too long and was truncated by the available capacity;
- the input source ended with a final line that had no newline before EOF.

If the program specification requires “one complete newline-terminated interactive line,” those cases must be defined and handled explicitly.

---

## 6. If a Line Is Too Long, Deal with the Remaining Input Before the Next Read

Here is a simplified helper for interactive text input. It treats “a newline was actually read” as success. If the current buffer contains no newline, it consumes the rest of that logical line so the next `fgets` does not accidentally continue reading the same input line.

```c
#include <stdio.h>
#include <string.h>

int read_line(char text[], size_t capacity) {
    if (capacity == 0) {
        return 0;
    }

    if (fgets(text, capacity, stdin) == NULL) {
        return 0;
    }

    size_t newline = strcspn(text, "\n");
    if (text[newline] == '\n') {
        text[newline] = '\0';
        return 1;
    }

    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF) {
        /* discard the remainder of the current logical line */
    }

    return 0;
}
```

For now, read `text[]` as “the character array supplied by the caller” and `capacity` as “how many elements may be used safely.” The lower-level relationship between array parameters and pointers remains for F-U06.

The return contract is deliberately simple:

- return `1`: a newline was actually obtained and removed;
- return `0`: capacity was invalid, reading failed, or a complete newline-terminated line was not obtained in this call.

Tests should distinguish at least an empty line, short text, a line that exactly fits, an overlong line, and EOF before any character is read.

---

## 7. Manual String Traversal Is Array Traversal with a Special Stop Element

Remember the F-U03 traversal loop? A string loop is similar, except that it stops at `\0` instead of at a separately supplied fixed length:

```c
int length = 0;
while (name[length] != '\0') {
    length++;
}
```

For `"Amy"`:

| Index | Character | End? |
|---:|---|---|
| 0 | `A` | no |
| 1 | `m` | no |
| 2 | `y` | no |
| 3 | `\0` | yes |

The string length is therefore 3. The terminator itself is not included.

This also explains why a missing `\0` is dangerous: the traversal rule loses its valid stopping point.

---

## 8. Common String Functions Share One Assumption: Their Inputs Must Really Be Strings

`<string.h>` provides functions such as:

```c
strlen(text)
strcmp(a, b)
strcpy(destination, source)
```

Their purposes differ, but they share a reading assumption: anything processed as a C string must contain a reachable `\0` within a valid readable region.

### `strlen`

Returns the number of characters before the terminator. `\0` is not counted in the length.

### `strcmp`

Compares string contents. Equal strings produce 0, so write:

```c
if (strcmp(a, b) == 0) {
    printf("equal\n");
}
```

Do not memorize it as “returns true when equal.”

### `strcpy`

Copies the source string, including its terminator, into the destination array. It does not prove for you that the destination capacity is large enough.

The point of this Unit is not to memorize every string function. Keep one fixed check in mind instead: **Where is the terminator, and is the destination capacity sufficient?**

---

## 9. Three Cases That Are Easy to Confuse

### Case A: `char word[3] = "cat";`

In C, this declaration can initialize three elements:

```text
'c' 'a' 't'
```

The capacity is exactly enough for the three visible characters, so there is no room for `\0`.

It can therefore be a validly initialized character array, **but it is not a terminated C string**. That is different from claiming that the compiler must reject the declaration.

If you then pass it to an interface that requires a C string, that interface keeps looking for `\0` and may read beyond the array, producing undefined behavior.

### Case B: using `==` to compare two text contents

```c
if (a == b) {
    /* ... */
}
```

This does not compare the two C strings character by character. The operation involves pointer values after array-expression conversion; the full model comes in F-U06.

For now, keep one rule: **string-content equality uses a content comparison such as `strcmp(a, b) == 0`.**

### Case C: assuming successful `fgets` means the whole logical line was read

A successful `fgets` call means it obtained input and produced a terminated string. It does not mean the user's entire logical line necessarily fit into this buffer.

If the specification requires a complete line, inspect newline, capacity, and leftover input instead of checking only whether the call failed.

---

## 10. Three Small Experiments: Draw Capacity and Termination Explicitly

### Experiment A: calculate length manually

Use:

```c
char text[] = "hello";
```

Draw six elements first: five visible characters plus `\0`, then write the traversal loop and verify that the length is five.

### Experiment B: count vowels

Traverse one element at a time until `\0`. Start with lowercase input so the exercise does not also introduce case conversion at the same time.

### Experiment C: deliberately use a small input array

For example:

```c
char text[6];
```

Try short input, input that exactly fits together with its newline, and input that exceeds capacity. Each time, draw which characters actually entered the array and whether the newline was stored.

---

## 11. Independent Practice: Text Analyzer

Read one input line that your program defines as requiring a complete line. If reading fails or the input is truncated according to that contract, report it explicitly instead of silently analyzing only the first part.

After a complete line is obtained, display:

- string length;
- number of spaces;
- number of digit characters;
- first and last characters, only when the string is nonempty.

Test at least:

| Situation | What should be verified? |
|---|---|
| empty line | length 0; no nonexistent first/last element may be read |
| ordinary short text | basic traversal |
| contains spaces | spaces must not terminate input early |
| exactly fits | boundary still preserves termination and newline handling |
| overlong input | must not silently analyze only the first part |

The exercise keeps repeating the same model:

```text
capacity → complete input? → terminator → legal traversal → character classification
```

---

## 12. Change the Requirement: Count Only English Letters

Now change the text analyzer:

> Ignore spaces, digits, and punctuation; count only English letters.

Do not change the program first. Add tests such as:

```text
abc
A1b2!
hello, world!
12345
```

Then decide how characters will be classified.

If you use `isalpha` from `<ctype.h>`, remember that these classification functions have an input contract. When processing arbitrary `char` values, a common safe pattern is to convert to `unsigned char` before passing the value. This detail will reappear later when interface and representation rules are discussed more deeply.

After the modification, rerun the original empty-line, long-line, and boundary cases. Changing the classification rule must not break complete-line handling or safe traversal.

---

## 13. Optional: Let AI Challenge Your String Model

You may skip this section completely.

Without any tool first, explain:

> What is the relationship among a C string, character array, capacity, length, and `\0`? Why can `fgets` succeed even when the complete logical line has not been obtained?

If you want another check, give your explanation to an AI tool and ask for one counterexample where “the index is legal but the data is still not a reliable C string,” or where “the string is terminated but the whole logical line was still not read.” No fixed prompt is required, and you do not need to save or submit the conversation.

If the AI response conflicts with an index diagram, a function contract, or a reproducible result, return to that evidence and judge again.

---

## 14. Before Leaving This Unit, Make Sure You Are Not Merely Memorizing String Functions

Return to the examples and answer directly:

- Why does `"cat"` normally require four `char` elements rather than three?
- When does a character array satisfy the C-string model?
- What do capacity 20 and string length 3 describe differently?
- Why does successful `fgets` not prove that the entire logical input line was read?
- If an array contains no `\0`, what guarantee is lost for manual traversal and `strlen`?
- Why can `char word[3] = "cat";` be a character array but not a reliable C string?
- Why does `strcmp(a, b) == 0` express equality of string contents?
- Why must you still know destination capacity when using a copying function?

If one answer has become only a memorized sentence, draw every index, character, and terminator position and derive it again.

---

## 15. Chapter Wrap-Up

F-U03 established that an array has a fixed legal position range. F-U04 adds a text-specific convention: **even when unused array capacity remains, the current string ends at the first `\0`.**

Safe text handling therefore tracks two boundaries at once. Array capacity determines which positions may be accessed; the terminator determines where the current string content ends. Input handling adds one more question: did the complete logical input actually enter this buffer?

The next Unit shifts attention from “where is the data stored?” to “where is execution now?” We have already called `sum_array`, `max_array`, `strlen`, and `strcmp` many times. Next we ask what happens to parameters and local variables on each call—and how those execution states remain separate when one function calls another or even calls itself.

## Navigation

- [Previous Unit: Arrays](unit-03-arrays.en.md)
- [Next Unit: Call Stack and Recursion](unit-05-call-stack-recursion.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-04-strings.zh-TW.md)
