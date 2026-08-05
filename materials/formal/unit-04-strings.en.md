# Formal Unit F-U04: How Is Text Represented and Processed as Data?

Version: 1.0.1  
Status: Official student material  
Last updated: 2026-08-05  
Corresponding Chinese version: [正式單元 F-U04：文字資料如何被表示與處理？](unit-04-strings.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can explain how C strings use character arrays and a null terminator, read and traverse strings safely, and diagnose terminator, buffer, truncation, and formatting errors.

## Core Question

> How does a computer store text as data, and how does it know where the text ends?

After completing this chapter, you should be able to:

1. Distinguish a character, character array, and C string.
2. Explain the role of `\0`.
3. Use `fgets` to read a line safely.
4. Distinguish a complete line from a truncated line.
5. Traverse and measure a string.
6. Diagnose missing terminators, insufficient buffers, retained newlines, and leftover input.

---

## 1. A String Is a Sequence of Characters

```c
char word[] = "cat";
```

Conceptual layout:

```text
Index:    0    1    2    3
Content: 'c'  'a'  't' '\0'
```

C does not have a separate built-in string type. A C string is usually a `char` array ending with a null character.

---

## 2. The Terminator Marks the End

```c
char letters[3] = {'c', 'a', 't'};
```

This is a character array, but not a reliable C string because it has no null terminator.

```c
char word[4] = {'c', 'a', 't', '\0'};
```

String functions read from the first element until `\0`.

---

## 3. String Length and Array Capacity Differ

```c
char name[20] = "Amy";
```

- array capacity: 20 `char` elements
- string length: 3
- required contents: `'A'`, `'m'`, `'y'`, `'\0'`

Capacity must include space for the text and terminator.

---

## 4. Read a Line with `fgets`

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

`fgets` reads at most capacity minus one characters and always adds `\0` when it succeeds. If the input line fits, the newline is usually stored too. If the line is too long, the buffer contains only the first part and the remaining characters stay in the input stream.

---

## 5. Remove a Newline and Detect Truncation

```c
#include <stdio.h>
#include <string.h>

int read_line(char text[], size_t capacity) {
    if (text == NULL || capacity == 0) {
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
        /* discard the remainder of the overlong line */
    }

    return 0;
}
```

Return rule:

- `1`: one complete line was read and the newline was removed
- `0`: input failed, the arguments were invalid, or the line exceeded the buffer

Discarding the remainder prevents the next input operation from reading leftover characters from the same line.

Test:

- empty line
- a short line
- exactly `capacity - 2` visible characters plus newline
- a line longer than the buffer
- end-of-file before any character is read

---

## 6. Traverse a String Manually

```c
int length = 0;
while (name[length] != '\0') {
    length++;
}
```

Trace for `"Amy"`:

| Index | Character | End? |
|---:|---|---|
| 0 | `A` | no |
| 1 | `m` | no |
| 2 | `y` | no |
| 3 | `\0` | yes |

---

## 7. Common String Functions

```c
strlen(text)
strcmp(a, b)
strcpy(destination, source)
```

Before using them, confirm that inputs are terminated, destination capacity is sufficient, and the return value of `strcmp` is understood.

Equality test:

```c
if (strcmp(a, b) == 0) {
    /* equal */
}
```

---

## 8. Error Cases

### Comparing Strings with `==`

```c
if (a == b)
```

This compares addresses or converted pointer values, not string contents. Use `strcmp`.

### Buffer Too Small

```c
char word[3] = "cat";
```

There is no room for `\0`. At least 4 elements are needed. A compiler should diagnose this initializer.

### Assuming `fgets` Always Reads the Whole Line

A successful `fgets` call guarantees a terminated buffer, not a complete logical line. When no newline is present and the buffer filled, inspect whether the input was truncated and discard the remainder before reading again.

---

## 9. Guided Practice

1. Read a name and remove the newline.
2. Detect and report an overlong line.
3. Calculate string length manually.
4. Count vowels.
5. Convert lowercase English letters to uppercase.

Draw characters and indexes first.

---

## 10. Independent Practice: Text Analyzer

Read one complete line and display string length, space count, digit-character count, and the first and last characters when the string is nonempty.

Test an empty line, short text, text that exactly fits, an overlong line, and text containing spaces. Do not silently analyze only the first part of a truncated line.

---

## 11. Requirement Modification

New rule: ignore newlines and punctuation and count only English letters. Update test data first, then modify classification conditions and run regression tests.

---

## 12. Explain the Concept to AI

Explain:

> What is the relationship among a C string, character array, capacity, length, and the null terminator? How can `fgets` succeed while still reading only part of a line?

If an AI response conflicts with an index diagram, function specification, or reproducible result, judge it again using evidence.

---

## 13. Self-Check

- I can draw a string and its terminator.
- I can distinguish capacity from length.
- I can read a line with `fgets`.
- I can distinguish a complete line from a truncated line.
- I can remove a retained newline and discard leftover input deliberately.
- I can compare contents with `strcmp`.
- I can diagnose missing terminators and insufficient capacity.

## 14. Chapter Summary

A C string is a character array ending with a null character. Safe text processing requires attention to capacity, length, terminators, complete-line detection, and leftover input. The next Unit examines function-call environments and recursion.

## Navigation

- [Previous Unit: Arrays](unit-03-arrays.en.md)
- [Next Unit: Call Stack and Recursion](unit-05-call-stack-recursion.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-04-strings.zh-TW.md)
