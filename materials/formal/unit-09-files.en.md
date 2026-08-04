# Formal Unit F-U09: How Does a Program Interact with Files and Persistent Data?

Version: 1.0.1  
Status: Official student material  
Last updated: 2026-08-05  
Corresponding Chinese version: [正式單元 F-U09：程式如何與檔案及持久資料互動？](unit-09-files.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can open, read, write, and close text files, check I/O return values and EOF, and diagnose mode, format, write, close, and resource-release errors.

## Core Question

> When data must remain after a program ends, how does the program read, write, and detect errors?

After completing this chapter, you should be able to:

1. Explain streams, files, and persistent data.
2. Use `fopen`, `fprintf`, `fscanf`, `fgets`, and `fclose`.
3. Check file-open, read, write, and close results.
4. Distinguish EOF, format failure, and I/O error.
5. Design reproducible file tests.

---

## 1. Files Outlive Program Variables

Variables usually disappear when the program ends. Files let the operating system preserve data for later runs.

```mermaid
flowchart LR
    P[Program] -->|write| F[File]
    F -->|read| P
```

---

## 2. Open, Write, and Close

```c
#include <stdio.h>

int main(void) {
    FILE *file = fopen("scores.txt", "w");
    if (file == NULL) {
        perror("scores.txt");
        return 1;
    }

    if (fprintf(file, "%d\n", 80) < 0) {
        fprintf(stderr, "Write failed\n");
        fclose(file);
        return 1;
    }

    if (fclose(file) == EOF) {
        fprintf(stderr, "Close failed\n");
        return 1;
    }

    return 0;
}
```

Modes:

- `"r"`: read an existing file
- `"w"`: write and truncate existing contents
- `"a"`: append at the end

The mode is part of the requirement. Choosing the wrong one can destroy data. A successful `fopen` does not prove that later writing or closing succeeded.

---

## 3. Read Text Data and Classify Why Reading Stopped

```c
#include <stdio.h>

int main(void) {
    FILE *file = fopen("scores.txt", "r");
    if (file == NULL) {
        perror("scores.txt");
        return 1;
    }

    int score;
    int result;

    while ((result = fscanf(file, "%d", &score)) == 1) {
        printf("%d\n", score);
    }

    if (result == EOF) {
        if (ferror(file)) {
            fprintf(stderr, "Read error\n");
            fclose(file);
            return 1;
        }
        /* normal end of file */
    } else {
        fprintf(stderr, "Invalid score format\n");
        fclose(file);
        return 1;
    }

    if (fclose(file) == EOF) {
        fprintf(stderr, "Close failed\n");
        return 1;
    }

    return 0;
}
```

Do not use `while (!feof(file))` as the main reading pattern. Let the read operation itself determine whether data was obtained, then inspect why it stopped.

---

## 4. EOF, Format Failure, and I/O Error

For `fscanf(file, "%d", &score)`:

- return value `1`: one integer was read successfully
- return value `EOF`: no conversion occurred because EOF or an input error was encountered before a value
- return value `0`: input exists, but it does not match the requested integer format

When the result is `EOF`, use `ferror(file)` to distinguish an I/O error from normal EOF.

---

## 5. Read by Line

```c
char line[100];
while (fgets(line, sizeof line, file) != NULL) {
    printf("%s", line);
}

if (ferror(file)) {
    fprintf(stderr, "Read error\n");
}
```

Line-based reading is useful when preserving or parsing a format. Consider what happens when a line exceeds the buffer: one physical line may arrive in several `fgets` calls.

---

## 6. Structured Text Is a Protocol

Example:

```text
1001 Amy 87.5
1002 Ben 91.0
```

Writer and reader must agree on field order, separators, types, and error handling. If names may contain spaces, a whitespace-separated format is no longer sufficient and must be redesigned.

---

## 7. Error Cases

### Not Checking `fopen`

Using a null `FILE *` is invalid.

### Ignoring `fprintf` or `fclose`

Opening a file successfully does not guarantee that buffered data reaches storage. Check write operations and the final close result.

### Using `"w"` When Append Was Intended

Existing contents are truncated. Test with a copy of the file first.

### `while (!feof(file))`

EOF is set only after a failed read attempt, so the last item may be processed incorrectly. Control the loop with the read result.

### Treating Format Failure as EOF

A malformed token can stop `fscanf` with return value `0`. The invalid bytes remain unread, so retrying the same conversion without consuming or reporting them can cause an infinite loop.

### Not Closing the File

Resources may not be released promptly, and buffered output may not be fully written. Every successful open path should have a corresponding checked close.

---

## 8. Guided Practice

1. Write three integers, checking each write and the final close.
2. Read them back, sum them, and classify why reading stops.
3. Compare `"w"` and `"a"`.
4. Add one malformed line and confirm that it is reported as a format failure rather than normal EOF.

---

## 9. Independent Practice: Score File Report

Read student ID, name, and score records from a text file. Display count, average, and highest score.

Test a missing file, empty file, normal records, one malformed record, a line longer than the buffer, and a final line without a newline. Define whether malformed input stops the program, skips a record, or reports an error; do not leave the behavior implicit.

---

## 10. Requirement Modification

Write the analysis result to `report.txt`. Decide whether to overwrite or append, and define how open, write, and close failures are reported.

---

## 11. Explain the Concept to AI

Explain:

> What is the relationship among streams, file modes, EOF, formats, and error checking? Why should `feof` not be the only loop condition?

If an AI response conflicts with function return rules or reproducible file tests, judge it again using evidence.

---

## 12. Self-Check

- I can choose the correct file mode.
- I check `fopen`, write results, and `fclose`.
- I control loops with read results.
- I can distinguish EOF, format failure, and I/O error.
- I close every successfully opened file on every exit path.
- I can test empty, malformed, and overlong input.

## 13. Chapter Summary

Files allow data to persist after program termination. Reliable file processing requires a clear format, correct modes, checked open/read/write/close operations, EOF reasoning, and resource closure. The next Unit separates interfaces and implementations into maintainable modules.

## Navigation

- [Previous Unit: Dynamic Memory](unit-08-dynamic-memory.en.md)
- [Next Unit: Modular Programming](unit-10-modular-programming.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-09-files.zh-TW.md)
