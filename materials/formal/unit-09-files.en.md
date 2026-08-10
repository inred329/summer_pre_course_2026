# Formal Unit F-U09: How Does a Program Interact with Files and Persistent Data?

Version: 1.2.0  
Status: Official student material  
Last updated: 2026-08-10  
Corresponding Chinese version: [正式單元 F-U09：程式如何與檔案及持久資料互動？](unit-09-files.zh-TW.md)

F-U08 let data obtain storage for as long as the running program needs it, but an object created by `malloc` still belongs to that execution of the program.

If today's student records must still be available when the program starts again tomorrow, the data has to move into persistent storage outside the program's own runtime objects.

The simplest example is a file.

File I/O is more than “move a variable to disk.” The program first needs a connection through which it can read or write the file. In C standard I/O, that connection together with its current read/write state is treated as a **stream**. For now, think of a stream as “the channel and state the program is currently using to exchange data with some input or output source.” The next section shows how `FILE *` represents that stream.

The program also needs an explicit open mode, an agreed format, and success/failure checks at every important step.

This Unit follows one score record through that complete path.

---

## 1. Write One Number All the Way to a File

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

Read the path as:

```text
fopen
→ obtain a FILE * that represents the open stream
→ fprintf writes through the stream
→ fclose finishes and closes the stream
```

`FILE *` is the standard-library type through which we operate on a stream. It lets the library preserve state for this open connection, such as the current position and error state; you do not need to know the internal layout of `FILE`.

Keep these two things separate:

```text
scores.txt        the file itself, which can remain after the program ends
FILE *file        the object used during this execution to operate on that file stream
```

Every successful `fopen` therefore needs a corresponding use-and-close path.

---

## 2. The Open Mode Is Part of the Data Policy

Common text modes include:

```text
"r"  read an existing file
"w"  write; truncate old contents if the file already exists
"a"  append at the end; preserve existing contents
```

If the requirement says “add today's records” but the program opens with `"w"`, yesterday's data may disappear before record processing even begins.

So the mode is not merely a detail of how a library function is called. It answers a requirement question:

> Is this run reading, replacing, or appending?

Also, successful `fopen` does not prove that later `fprintf` operations or the final `fclose` succeed.

---

## 3. Let the Read Operation Control the Loop

Now read the integer back:

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

    /* classify why reading stopped below */

    fclose(file);
    return 0;
}
```

This is the same rule used earlier with `scanf`:

> **Use a value only after the read function reports that the conversion actually succeeded.**

Do not make this the primary pattern:

```c
while (!feof(file)) {
    fscanf(file, "%d", &score);
    /* use score */
}
```

The EOF indicator is observed after a read attempt encounters the end. Checking `feof` first tries to predict whether the *next* read will succeed and can lead to processing a stale value one extra time.

---

## 4. After Reading Stops, Classify Why It Stopped

For:

```c
fscanf(file, "%d", &score)
```

important results are:

- `1`: one `%d` conversion succeeded;
- `0`: input remains, but the next data does not match `%d`;
- `EOF`: no conversion completed because end-of-file or an input error was encountered first.

So after the loop:

```c
if (result == EOF) {
    if (ferror(file)) {
        fprintf(stderr, "Read error\n");
        /* I/O error */
    } else {
        /* normal EOF */
    }
} else {
    fprintf(stderr, "Invalid score format\n");
}
```

These are different outcomes:

```text
normal end
format mismatch
actual I/O error
```

When the result is `0`, the offending input normally remains in the stream. Retrying the same `%d` conversion without consuming or reporting the bad data can leave the program stuck at the same place forever.

---

## 5. If One Record Is a Whole Line, Make Sure You Actually Have the Whole Line

F-U04 already established the capacity issue with `fgets`; file streams follow the same rule.

```c
char line[100];

while (fgets(line, sizeof line, file) != NULL) {
    printf("%s", line);
}
```

One successful `fgets` call guarantees a terminated string fragment, not necessarily one complete logical record.

If the buffer fills before a newline arrives, the rest of the same physical line remains for a later call.

A useful check is:

```c
#include <string.h>

if (strchr(line, '\n') == NULL && !feof(file)) {
    fprintf(stderr, "Line exceeds buffer\n");
}
```

This detects the common case where no newline has arrived and the stream is not yet at EOF.

A final line that legitimately ends at EOF without a newline is a different case. The code responsible for turning input text into valid records—a **parser**—must define its own policy:

- accept a final non-newline-terminated line?
- discard an overlong record?
- combine fragments?
- reject the record entirely?

It must not silently treat the first fragment as one complete record.

---

## 6. A File Format Is a Protocol

Suppose the file contains:

```text
1001 Amy 87.5
1002 Ben 91.0
```

The reader assumes:

```text
field 1 = id
field 2 = name
field 3 = average
```

That is a simple **protocol**: the writer and reader agree on what each field means and how the data is arranged.

If a name may contain spaces:

```text
1003 Mary Jane 88.0
```

the old whitespace-separated format is no longer sufficient.

A file does not understand the fields of a `struct` automatically. The writer and reader must agree on a serialization format, and changing that format is a real change to their shared contract.

---

## 7. Avoid Letting a Failed Load Half-Modify the Official State

Suppose a program loads many student records.

A difficult failure mode is:

```text
records 1–5 modify the real array
record 6 is malformed
loader returns failure
```

The caller now hears “load failed,” but half of the official state has already changed.

A more predictable policy is:

```text
read into temporary state
→ validate every record
→ all succeed
→ commit the completed result
```

This is the same pattern used in F-U08's `realloc` and `append_value`: **perform failure-prone work in temporary state and commit only after success.**

A different policy—such as keeping all valid records before the first malformed one—is possible, but it should be an explicit requirement rather than an accidental side effect.

---

## 8. Writing Has a Complete Failure Path Too

Opening the output successfully is not the same as saving successfully.

At minimum consider:

```text
fopen failure
fprintf / fwrite failure
final fclose failure
```

For example:

```c
if (fprintf(file, "%d\n", score) < 0) {
    fprintf(stderr, "Write failed\n");
    /* the successfully opened stream still needs closure */
}
```

and finally:

```c
if (fclose(file) == EOF) {
    fprintf(stderr, "Close failed\n");
}
```

Standard I/O can buffer output, so some failures may only become visible during flushing or close.

“Opened successfully” is therefore the beginning of the operation, not proof that persistence succeeded.

---

## 9. Put Common File Defects Back into the Flow

### Wrong mode

Appending was intended, but `"w"` truncates data before record processing begins.

### Unchecked `fopen`

Later code treats a null `FILE *` as a valid stream.

### `while (!feof(file))`

The program predicts the next read from the previous stream state and can reuse stale data.

### Format failure treated as normal EOF

A bad token remains unread while the program pretends the file simply ended.

### `fgets` fragment treated as a full record

One long physical line becomes two false logical records.

### Write or close result ignored

The program says “Saved” without verifying the persistence path.

All of these can be located on one path:

```text
open → obtain complete record → parse/validate → process → write → close
```

---

## 10. Independent Practice: Score-File Report

Define a text format for multiple records containing:

```text
student ID  name  score
```

The program displays:

- number of valid records;
- average score;
- highest score.

Define the format limitations first. If names cannot contain spaces, state that. If spaces must be supported, choose a format you can parse reliably.

Test at least:

| Situation | What should be verified? |
|---|---|
| missing file | `fopen` failure path |
| empty file | meaning of zero records |
| normal records | ordinary flow |
| one malformed record | not mistaken for EOF |
| overlong line | fragment not accepted as a full record |
| final line without newline | accepted or rejected according to your rule |
| failure partway through | official result follows the chosen commit policy |

---

## 11. Change the Requirement: Write the Analysis to `report.txt`

Now the program must persist the report as well as read the source data.

First decide:

> Does each run replace the previous report, or append another result?

That directly determines `"w"` versus `"a"`.

Then define:

- what happens if the output file cannot be opened;
- what happens when one `fprintf` fails;
- whether a failed `fclose` can still produce a success status;
- what overall exit status is used when input succeeds but report output fails.

Do not use the mere existence of `report.txt` as proof of success.

---

## 12. Optional: Let AI Challenge Your File-State Model

You may skip this section completely.

Without any tool first, explain:

> Why should an `fscanf` loop be controlled by the function's return value? After reading stops, how do you distinguish normal EOF, format mismatch, and I/O error?

If you want another check, ask an AI tool to create one input record that looks plausible but violates an assumption in your file format. No fixed prompt is required, and you do not need to save or submit the conversation.

If its claim conflicts with function return rules, an actual test file, or a reproducible result, return to the evidence.

---

## 13. Before Leaving This Unit, Make Sure You Can Trace One Record's Entire Journey

Answer directly:

- How is a stream different from the file itself, and what role does `FILE *` play between them?
- Why are `"w"` and `"a"` requirement decisions rather than mere syntax choices?
- Why does successful `fopen` not prove final output success?
- What do return values `1`, `0`, and `EOF` mean for `fscanf(..., "%d", ...)`?
- Why should `feof` not be used to predict whether the next read will succeed?
- Why can successful `fgets` still return only a fragment of one physical line?
- Why can a file format be viewed as a protocol between writer and reader?
- Why is “load into temporary state, then commit” easier to reason about than half-modifying official state before failure?
- Why is the result of `fclose` worth checking?

If the answers collapse into function names, draw the full path from open to close and mark the stream together with every possible failure point.

---

## 14. Chapter Wrap-Up

F-U08 managed object lifetime during one execution. F-U09 extends data lifetime beyond program termination.

Reliable file processing is not merely knowing `fopen` and `fclose`. It preserves the entire path: **establish and manage the stream, choose the right mode, obtain complete records, let read results determine state, obey a format protocol, define partial-failure/commit policy, and check writes and closure.**

The next Unit addresses the program's own growth. When file I/O, student records, growable arrays, and analysis logic all live in one `.c` file, changing one feature begins to disturb the whole program. We need to separate public interfaces from private implementation and move into modular programming.

## Navigation

- [Previous Unit: Dynamic Memory](unit-08-dynamic-memory.en.md)
- [Next Unit: Modular Programming](unit-10-modular-programming.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-09-files.zh-TW.md)
