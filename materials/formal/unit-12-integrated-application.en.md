# Formal Unit F-U12: How Can the Whole Course Be Integrated into One Maintainable Program?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U12：如何把整門課整合成一個可維護的程式？](unit-12-integrated-application.zh-TW.md)

The first eleven formal Units deliberately separated problems. We first studied values and types, then control flow, arrays, strings, function calls, pointers, structures, dynamic memory, files, modules, and testing.

Real programs do not present those concepts one chapter at a time.

Even a small “score-record manager” can require all of these at once:

```text
Student structure
StudentList growable array
pointers and ownership
file format
module interfaces
failure handling
boundary and regression tests
```

The final Unit is not about adding the largest possible number of features. It asks a different question:

> When many Concepts operate at the same time, can we still explain where the data lives, who may modify it, which states are valid, where each operation may fail, and what evidence tells us that a change did not break the program?

---

## 1. Before Writing a Menu, Write the Behavior the User Can Actually Observe

We will build a small score-record manager.

Version 1 requirements:

1. Add a student record containing an ID, name, and score.
2. Display all current records.
3. Find a record by ID.
4. Calculate the average score.
5. Save records to a text file.
6. Load records from a text file.
7. Accept scores only from 0 through 100.
8. Distinguish invalid input, allocation failure, and file-format failure.

Before writing functions, connect several requirements to observable evidence:

| Requirement | What can we observe? |
|---|---|
| Add a valid record | `count` increases and the record really appears in the list |
| Reject an invalid score | the list stays unchanged and the caller receives failure |
| Average | result matches a hand-calculated example |
| Empty-list average | report “no result” without dividing by zero |
| Save | file contents follow the format and writing/close succeed |
| Load | rebuild data according to an explicit policy; on failure the old state is predictable |

The existence of a function does not prove that a requirement is complete. Required behavior must be observable and testable.

---

## 2. Decide What the Data Looks Like Before Designing the Operations

Reuse the F-U07 record model:

```c
#include <stddef.h>

#define NAME_SIZE 50

typedef struct {
    int id;
    char name[NAME_SIZE];
    int score;
} Student;
```

Now place records in a growable collection:

```c
typedef struct {
    Student *items;
    size_t count;
    size_t capacity;
} StudentList;
```

Draw it:

```text
StudentList
├── items ─────► dynamically allocated Student array
├── count       number of currently valid records
└── capacity    number of Student elements the allocation can hold
```

These three fields cannot change independently without rules.

State the invariant first:

```text
count <= capacity
when capacity == 0, items == NULL
when capacity > 0, items identifies storage for at least capacity Student elements
items[0] ... items[count - 1] are valid initialized records
```

From this point on, every operation should ask:

> Does the invariant still hold after success? What about after failure?

---

## 3. First Milestone: Only an Empty List and Destruction

```c
#include <stdlib.h>

int list_init(StudentList *list) {
    if (list == NULL) {
        return 0;
    }

    list->items = NULL;
    list->count = 0;
    list->capacity = 0;
    return 1;
}

void list_destroy(StudentList *list) {
    if (list == NULL) {
        return;
    }

    free(list->items);
    list->items = NULL;
    list->count = 0;
    list->capacity = 0;
}
```

Do not rush to add records yet.

First verify:

```text
Does init establish the empty invariant?
Does destroy restore the empty invariant?
Is destroying an empty list safe?
Is the policy for a NULL list explicit?
```

If the smallest lifetime is already unclear, adding more features only makes ownership harder to trace.

---

## 4. Second Milestone: Add One Record Without Damaging the Old State on Failure

```c
#include <stdint.h>
#include <stdlib.h>

int list_add(StudentList *list, const Student *student) {
    if (list == NULL || student == NULL) {
        return 0;
    }

    if (student->score < 0 || student->score > 100) {
        return 0;
    }

    if (list->count > list->capacity) {
        return 0;  /* invariant was already broken on entry */
    }

    if (list->count == list->capacity) {
        size_t new_capacity;

        if (list->capacity == 0) {
            new_capacity = 4;
        } else {
            if (list->capacity > SIZE_MAX / 2) {
                return 0;
            }
            new_capacity = list->capacity * 2;
        }

        if (new_capacity > SIZE_MAX / sizeof *list->items) {
            return 0;
        }

        Student *new_items = realloc(
            list->items,
            new_capacity * sizeof *list->items
        );

        if (new_items == NULL) {
            return 0;
        }

        list->items = new_items;
        list->capacity = new_capacity;
    }

    list->items[list->count] = *student;
    list->count++;
    return 1;
}
```

This code mixes ideas from several Units, but it can still be read in order:

```text
pointer parameters valid?             F-U06
Student contents valid?               F-U07
count/capacity invariant?             F-U03 + F-U08
capacity arithmetic safe?             F-U01 + F-U08
realloc preserves the old owner?      F-U08
structure-value copy?                 F-U07
increment count only after success?   F-U02 + invariant reasoning
```

The most important contract is:

> If the incoming list satisfies the invariant and `list_add` reports failure, the old list contents, `items`, `count`, and `capacity` remain usable and unchanged.

Potentially failing growth work happens before the new metadata and element are committed.

---

## 5. Third Milestone: Use Fixed Test Data for Search and Average First

Do not add keyboard input and files immediately.

Create two already validated records directly in the test program and exercise:

```text
list_add
list_find_by_id
list_average
```

An average interface can be:

```c
int list_average(const StudentList *list, double *average) {
    if (list == NULL || average == NULL || list->count == 0) {
        return 0;
    }

    double sum = 0.0;
    for (size_t i = 0; i < list->count; i++) {
        sum += (double)list->items[i].score;
    }

    *average = sum / (double)list->count;
    return 1;
}
```

The empty-collection contract is explicit:

```text
count == 0
→ there is no average result
→ report failure
→ do not modify *average
```

Do not divide by zero first and then inspect what the platform happened to produce.

Scores are constrained to 0–100, and accumulation uses `double` so that many scores are not first summed in `int` and exposed to signed-integer overflow. A real product that permits extremely large collections should still define an acceptable record-count range and floating-point error policy.

---

## 6. Trace One Growth Operation and Make Sure Ownership Never Disappears

Initial state:

```text
items = NULL
count = 0
capacity = 0
```

When storage is first needed:

```text
items ─────► [ Student ][ Student ][ Student ][ Student ]
count = 0
capacity = 4
```

After adding one record:

```text
items ─────► [ valid ][ unused ][ unused ][ unused ]
count = 1
capacity = 4
```

Later, growth to 8 may cause `realloc` to move the allocation:

```text
old location X
new location Y ──► [ storage for 8 Student elements ]
```

`StudentList.items` is therefore the owner. `main` should not keep a long-lived pointer to one element and then assume it remains valid after the list grows.

This is what makes cross-Concept integration difficult. “Find one student” is simple in isolation, but once the collection may move, F-U06 alias lifetime and F-U08 `realloc` rules affect the design together.

---

## 7. Fourth Milestone: Draw the Module Boundaries

One reasonable first version is:

```text
student.h / student.c
    create and validate Student records
    bounded name handling

student_list.h / student_list.c
    list ownership
    add / find / average / destroy

storage.h / storage.c
    file protocol
    save / transactional load

main.c
    user input
    call modules
    display results
```

`main.c` should not reach into the list and write:

```c
list.capacity *= 2;
list.items = realloc(...);
```

because that bypasses the `student_list` module that owns the invariant.

A module boundary answers:

> Who is allowed to modify which state, and which module is responsible for preserving each rule?

---

## 8. Fifth Milestone: Define the File Protocol Before Implementing Save/Load

A first format might be:

```text
1001,Alice,80
1002,Bob,95
```

Answer before implementing the parser:

- May a name contain commas?
- Are blank lines accepted?
- May IDs repeat?
- Is a final line without a newline accepted?
- What happens to the whole load when a score or field is malformed?

This Unit uses **transactional replace**:

```text
create an empty temporary list
→ parse, validate, and add every file record to temporary
→ any failure: destroy temporary; leave the original list completely unchanged
→ complete success: destroy the old list and transfer temporary ownership to the real list
```

That makes the failure contract for `list_load_replace` easy to state:

> If it reports failure, the caller's original data still exists unchanged.

After ownership is transferred, the temporary object must be reset to an empty state so that it does not later destroy the same allocation again.

Save success must likewise mean that required writes succeeded and the final `fclose` did not report failure.

---

## 9. Sixth Milestone: Add Interactive Input Only Now

At this point, core data operations can already be verified independently with fixed test data.

`main` can now handle:

```text
read command
→ check that reading succeeded
→ read Student fields
→ validate them
→ call list / storage APIs
→ display a message based on the returned result
```

Do not place parsing, validation, `realloc`, file-format rules, and UI logic into one enormous `switch`.

Every `scanf` or `fgets` follows the same earlier rule: **confirm that the read succeeded and that complete required input was obtained before using its output.**

A simple text menu is enough. This Unit does not need a decorative UI to demonstrate integration.

---

## 10. Layer the Integrated Tests by Responsibility

### Student layer

- 0 and 100 are valid scores.
- -1 and 101 fail.
- name-capacity boundary.
- overlong or unterminated input rejected according to the setter contract.

### StudentList layer

- empty list.
- first insertion.
- earlier records remain correct after growth beyond initial capacity.
- existing and missing ID.
- duplicate-ID policy.
- empty average fails without modifying the output.
- simulated/reasoned capacity-limit failure leaves state unchanged.

### Storage layer

- normal round trip.
- missing file.
- malformed format.
- overlong record.
- final line without newline.
- failure in the middle of load leaves the official list unchanged.
- write/close failure policy during save.

### Integration/regression layer

- one complete scenario from add → save → reload → search.
- rerun all cases after module refactoring.
- after a requirement change, run both new cases and old cases whose behavior should not change.

Write the expected result before executing each test.

---

## 11. Integrated Bugs: Identify Which Rule Each One Breaks

### Overwriting the `realloc` owner directly

```c
list->items = realloc(list->items, new_size);
```

Failure may lose the old allocation's owner. This is an ownership/failure-state defect.

### Incrementing `count` before success

If allocation or copying later fails, `count` already claims that a nonexistent record is valid. This is an invariant defect.

### Modifying the real list while a load is only half complete

If line six is malformed after five records were already replaced, a transactional-replace contract has been broken. This is a transaction defect.

### Putting the storage parser in `main`

The program may still work, but another front end that needs loading must duplicate the same rules. This is a module-boundary defect.

### Testing only the new feature

The new requirement appears to work, but old round-trip, empty-list, or capacity-boundary behavior may have been damaged. This is an evidence gap.

These defects come from different earlier Units, but the integrated application lets us locate all of them on one system model.

---

## 12. Independent Integration Practice: Complete Version 1 of the Manager

Work in small commits or milestones:

```text
1. Student validation
2. empty StudentList lifecycle
3. add fixed records
4. find / average
5. growth boundary
6. module split
7. save
8. transactional load
9. interactive input
10. integrated regression tests
```

Keep the program in a state that can compile, be tested, and be explained after every step.

If one step fails, do not add two more features at the same time. Use the F-U11 workflow to find the first mismatch first.

---

## 13. Final Requirement Change: Each Student Has Multiple Scores

New requirement:

> Each student may have zero or more scores and can display an individual average.

Do not simply add `int scores[100]` to `Student` and declare the problem solved.

First analyze the consequences.

### Data model

Is the number of scores fixed? Is a dynamic array required?

### Nested ownership

If every `Student` owns its own dynamically allocated score array:

```text
StudentList owns Student array
each Student owns score array
```

then copying `Student` can no longer rely blindly on structure assignment. That would copy only the pointer value and could create shared ownership and double-free risk.

### Empty scores

The average of zero scores should report “no result,” not divide by zero.

### File format

The old one-score-per-record format is no longer sufficient. How are multiple scores represented, and how will old files be migrated?

### Module interface

Which new operations must become public? What are the ownership-transfer rules?

### Tests

Add at least: zero scores, one score, multiple scores, growth failure, deep copy/release, old-file migration, and transactional load.

This modification deliberately has no single supplied answer. The real test is whether you can see, **before changing code**, how a data-model change propagates through ownership, file protocol, API design, and the test plan.

---

## 14. Optional: Let AI Challenge Your Integration Diagram

You may skip this section completely.

First, without any tool, draw:

```text
user
→ main
→ Student / StudentList
→ dynamic storage
→ storage module
→ file
```

Mark ownership, failure points, and which tests can observe each result.

If you want another check, ask an AI tool to find one failure path or ownership transfer missing from your diagram. No fixed prompt is required, and you do not need to save or submit the conversation.

If its suggestion conflicts with the actual function contracts, type ranges, file protocol, memory lifetime, or reproducible tests, return to the engineering evidence.

---

## 15. Before Leaving the Formal-Course Materials, Explain Why This Program Deserves Trust

Do not merely show that the program runs.

Explain:

- How do user requirements become observable acceptance behavior?
- What is the `StudentList` invariant, and which functions preserve it?
- Who owns each dynamic allocation? When is ownership transferred? When is it freed?
- Why does `realloc` failure not damage the old list?
- How is the empty-list average defined?
- Why does load use a temporary list, and what is the official state after failure?
- Which details remain inside modules, and which rules are public contracts?
- What boundary, invalid-input, transaction, and regression evidence do you have?
- When “one Student has several scores” is introduced, which old assumptions stop being true?

If one answer is only “because the program works now,” return to the corresponding Unit model and add evidence.

---

## 16. Formal-Course Wrap-Up

This course used C not to build the longest possible syntax list, but to practice a reasoning process that transfers to other programs and tools:

```text
state the requirement clearly
→ build a data/state model
→ define interfaces and failure behavior
→ check boundaries and preconditions before operations
→ trace ownership / lifetime / invariants
→ divide a large problem into independently verifiable responsibilities
→ support conclusions with tests, reproducible failures, and regression evidence
→ when requirements change, revisit the assumptions they affect
```

If you can take an unfamiliar C program, identify its data, control flow, lifetimes, interface assumptions, and failure paths, then design experiments that test your own reasoning, you have moved beyond memorizing function names.

That is the capability this material is meant to leave with you.

## Navigation

- [Previous Unit: Testing, Diagnosis, and Improvement](unit-11-testing-debugging.en.md)
- [Formal-Course Index](README.en.md)
- [Materials Index](../README.en.md)
- [繁體中文版](unit-12-integrated-application.zh-TW.md)