# Formal Unit F-U09: How Does a Program Interact with Files and Persistent Data?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U09：程式如何與檔案及持久資料互動？](unit-09-files.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can open, read, write, and close text files, check I/O return values and EOF, and diagnose mode, format, and resource-release errors.

## Core Question

> When data must remain after a program ends, how does the program read, write, and detect errors?

After completing this chapter, you should be able to:

1. Explain streams, files, and persistent data.
2. Use `fopen`, `fprintf`, `fscanf`, `fgets`, and `fclose`.
3. Check file-open and read/write results.
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

## 2. Open and Close

```c
FILE *file = fopen("scores.txt", "w");
if (file == NULL) {
    return 1;
}

fprintf(file, "%d\n", 80);
fclose(file);
```

Modes:

- `"r"`: read an existing file
- `"w"`: write and truncate existing contents
- `"a"`: append at the end

The mode is part of the requirement. Choosing the wrong one can destroy data.

---

## 3. Read Text Data

```c
FILE *file = fopen("scores.txt", "r");
if (file == NULL) {
    return 1;
}

int score;
while (fscanf(file, "%d", &score) == 1) {
    printf("%d\n", score);
}

fclose(file);
```

Do not use `while (!feof(file))` as the main reading pattern. Let the read operation itself determine whether data was obtained.

---

## 4. EOF and Errors

Reading may stop because of normal EOF, a format mismatch, or an I/O error.

```c
if (ferror(file)) {
    /* I/O error */
}
```

If `fscanf` stops at non-integer text, that is different from normal EOF.

---

## 5. Read by Line

```c
char line[100];
while (fgets(line, sizeof line, file) != NULL) {
    printf("%s", line);
}
```

Line-based reading is useful when preserving or parsing a format. Consider what happens when a line exceeds the buffer.

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

### Using `"w"` When Append Was Intended

Existing contents are truncated. Test with a copy of the file first.

### `while (!feof(file))`

EOF is set only after a failed read attempt, so the last item may be processed incorrectly. Control the loop with the read result.

### Not Closing the File

Resources may not be released promptly, and buffered output may not be fully written. Every successful open path should have a corresponding close.

---

## 8. Guided Practice

1. Write three integers, then read them back and sum them.
2. Compare `"w"` and `"a"`.
3. Add one malformed line and observe where reading stops.

---

## 9. Independent Practice: Score File Report

Read student ID, name, and score records from a text file. Display count, average, and highest score.

Test a missing file, empty file, normal records, one malformed record, and a final line without a newline.

---

## 10. Requirement Modification

Write the analysis result to `report.txt`. Decide whether to overwrite or append, and define how write failure is reported.

---

## 11. Explain the Concept to AI

Explain:

> What is the relationship among streams, file modes, EOF, formats, and error checking? Why should `feof` not be the only loop condition?

If an AI response conflicts with function return rules or reproducible file tests, judge it again using evidence.

---

## 12. Self-Check

- I can choose the correct file mode.
- I check `fopen`.
- I control loops with read results.
- I can distinguish EOF, format failure, and I/O error.
- I close successfully opened files.
- I can test empty and malformed files.

## 13. Chapter Summary

Files allow data to persist after program termination. Reliable file processing requires a clear format, correct modes, return-value checks, EOF reasoning, and resource closure. The next Unit separates interfaces and implementations into maintainable modules.

## Navigation

- [Previous Unit: Dynamic Memory](unit-08-dynamic-memory.en.md)
- [Next Unit: Modular Programming](unit-10-modules.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-09-files.zh-TW.md)
