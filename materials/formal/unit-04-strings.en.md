# Formal Unit F-U04: How Is Text Represented and Processed as Data?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U04：文字資料如何被表示與處理？](unit-04-strings.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can explain how C strings use character arrays and a null terminator, read and traverse strings safely, and diagnose terminator, buffer, and formatting errors.

## Core Question

> How does a computer store text as data, and how does it know where the text ends?

After completing this chapter, you should be able to:

1. Distinguish a character, character array, and C string.
2. Explain the role of `\0`.
3. Use `fgets` to read a line safely.
4. Traverse and measure a string.
5. Diagnose missing terminators, insufficient buffers, and retained newlines.

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

    if (fgets(name, sizeof name, stdin) != NULL) {
        printf("Hello, %s", name);
    }

    return 0;
}
```

`fgets` reads at most capacity minus one characters, leaving room for `\0`. If the line fits, the newline is usually stored too.

---

## 5. Remove a Retained Newline

```c
#include <string.h>

name[strcspn(name, "\n")] = '\0';
```

`strcspn` finds the first newline position; if there is none, it returns the string length. The assignment replaces the newline with the terminator.

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

This does not compare string contents. Use `strcmp`.

### Buffer Too Small

```c
char word[3] = "cat";
```

There is no room for `\0`. At least 4 elements are needed.

### Assuming `fgets` Removes the Newline

Output may contain an unexpected extra line. Inspect the stored array and remove the newline deliberately.

---

## 9. Guided Practice

1. Read a name and remove the newline.
2. Calculate string length manually.
3. Count vowels.
4. Convert lowercase English letters to uppercase.

Draw characters and indexes first.

---

## 10. Independent Practice: Text Analyzer

Read one line and display string length, space count, digit-character count, and the first and last characters when the string is nonempty.

Test an empty line, short text, text near capacity, and text containing spaces.

---

## 11. Requirement Modification

New rule: ignore newlines and punctuation and count only English letters. Update test data first, then modify classification conditions and run regression tests.

---

## 12. Explain the Concept to AI

Explain:

> What is the relationship among a C string, character array, capacity, length, and the null terminator?

If an AI response conflicts with an index diagram, function specification, or reproducible result, judge it again using evidence.

---

## 13. Self-Check

- I can draw a string and its terminator.
- I can distinguish capacity from length.
- I can read a line with `fgets`.
- I can handle a retained newline.
- I can compare contents with `strcmp`.
- I can diagnose missing terminators and insufficient capacity.

## 14. Chapter Summary

A C string is a character array ending with a null character. Safe text processing requires attention to capacity, length, terminators, and input behavior. The next Unit examines function-call environments and recursion.

## Navigation

- [Previous Unit: Arrays](unit-03-arrays.en.md)
- [Next Unit: Call Stack and Recursion](unit-05-call-stack-recursion.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-04-strings.zh-TW.md)
