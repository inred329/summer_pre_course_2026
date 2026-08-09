# Preparatory Unit P-U01: Once a Program Starts Running, How Do Statements Become Results?

Version: 1.2.0  
Status: Student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [前導單元 P-U01：程式開始執行後，敘述怎麼變成結果？](unit-01-execution.zh-TW.md)

P-U00 separated the tool layer: source files, Build, the compiler, executables, Run, and the IDE all have different roles.

This Unit starts with the next question:

> **Assume the Build succeeded and the newest executable is the one being run. Once the program actually starts, how do the statements inside it become the result we observe?**

We will still use a very small program, but we will not relearn the compiler or Build. The focus now is execution order, prediction, observation, and explanation.

---

## 1. Predict the result from the program text before you run it

Consider:

```c
#include <stdio.h>

int main(void) {
    printf("First\n");
    printf("Second\n");
    return 0;
}
```

Before running it, answer three questions:

1. Which line of text will appear first?
2. Can `Second` appear before `First` in this program?
3. After `return 0;` executes, are there more statements in this `main` that still need to run?

Write down your prediction, then Build and Run.

You should see:

```text
First
Second
```

The important part is not merely that two lines appeared. It is whether you could explain the execution order from the program before running it.

---

## 2. `main` is our starting point for tracing execution

For the small programs we are using now, you can initially read:

```c
int main(void) {
    ...
}
```

as the place where the program's main work begins after the program starts running.

We will study functions more fully in P-U04. For now, the important idea is that once this program is started, we can trace forward from the first statement that executes inside `main`.

For example:

```c
int main(void) {
    printf("A\n");
    printf("B\n");
    printf("C\n");
    return 0;
}
```

At this stage, read it in the most direct way:

```text
enter main
→ execute the first printf
→ execute the second printf
→ execute the third printf
→ execute return 0
→ main ends
```

After we add conditions and loops, execution will no longer always move straight downward. First we need a clear model of simple sequential execution so that later changes have something to build on.

---

## 3. `printf` gives us an observable action

This statement:

```c
printf("Hello, C!\n");
```

asks the program to send text to standard output.

Inside the string:

```text
\n
```

means a newline.

So:

```c
printf("Hello, ");
printf("C!\n");
```

normally produces:

```text
Hello, C!
```

while:

```c
printf("Hello,\n");
printf("C!\n");
```

produces:

```text
Hello,
C!
```

Predict both results before running them, then compare with what you observe. This becomes a repeated habit throughout the course:

```text
read the program
→ form an expectation
→ run it
→ compare the actual result
```

---

## 4. Turn execution into a trace

For this program:

```c
#include <stdio.h>

int main(void) {
    printf("One\n");
    printf("Two\n");
    return 0;
}
```

we can write a simple trace:

| Order | Statement about to execute | What becomes observable afterward? |
|---:|---|---|
| 1 | `printf("One\n");` | `One` appears |
| 2 | `printf("Two\n");` | `Two` appears next |
| 3 | `return 0;` | `main` ends |

A trace is not meant to copy the source code. Its purpose is to make clear which step happens first and what changes after that step.

Once P-U02 introduces variables, tracing becomes even more useful because we will follow not only output but also data and program state.

---

## 5. For now, read `return 0;` as “this main ends here”

When you see:

```c
return 0;
```

we do not yet need the full rules of function return values.

In these small programs, read it as:

> `main` ends here, and this execution completes normally.

Therefore:

```c
int main(void) {
    printf("Before\n");
    return 0;
    printf("After\n");
}
```

Do not simply count two `printf` statements and assume both outputs appear. Follow the execution: after `return 0;` executes, `main` has ended, so the later `printf` is not part of this normal execution path.

The point is not to encourage unreachable code. It is to begin separating “text exists in the source file” from “this execution actually reaches that statement.”

---

## 6. Keep compile errors separate from execution behavior

P-U00 already separated Build from Run. Now use that distinction to read an error.

Suppose a semicolon is missing:

```c
#include <stdio.h>

int main(void) {
    printf("Hello\n")
    return 0;
}
```

Ask first:

> Did this new version actually begin executing `main`?

If the Build fails because of a syntax problem, the new version never enters its normal execution flow.

That gives us a useful first classification:

```text
Did the problem happen during Build?
or
did the program Run, but its behavior differ from the expectation?
```

When a compiler points to one line, treat the location as a diagnostic clue rather than an automatic guarantee that the true cause is exactly on that character. A missing symbol on the previous line may only become obvious when the tool reads the next line.

---

## 7. A program can run and still fail the requirement

Suppose the requirement is:

```text
Print Hello, C!
```

but the program is:

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye, C!\n");
    return 0;
}
```

The program may Build. It may Run. Its execution path may be perfectly clear.

It still does not satisfy the requirement.

So when someone says “the program runs,” keep at least these questions separate:

```text
Did the tools successfully build it?
↓
Which statements did this execution actually reach?
↓
Does the observed result satisfy the requirement?
```

P-U00 established the first tool-level distinction. This Unit connects that to execution tracing and requirement comparison.

---

## 8. Make a change: predict first, then edit

Start with:

```c
#include <stdio.h>

int main(void) {
    printf("Hello, C!\n");
    return 0;
}
```

Change it so the output is:

```text
Hello, <your English name>!
Welcome to C.
```

Do not start by typing immediately. Instead:

1. Write the complete expected output first.
2. Decide how many `printf` statements you need.
3. Decide where each `\n` belongs.
4. Edit the program.
5. Build and Run.
6. Compare the prediction with the actual result.

If the result differs, do not rewrite the entire program first. Follow the execution order through `main` and find the earliest place where the actual behavior stops matching your expectation.

---

## 9. Run one experiment that changes only the order

First consider:

```c
printf("A\n");
printf("B\n");
printf("C\n");
```

Predict the output.

Then swap only the first and third statements:

```c
printf("C\n");
printf("B\n");
printf("A\n");
```

Predict again.

This is a tiny experiment, but it establishes an idea we will keep using:

> A program's result depends not only on which statements exist, but also on the order in which this execution reaches them.

When P-U03 adds conditions and loops, this question becomes much more interesting.

---

## 10. Optional: let AI challenge your execution trace

This section may be skipped completely.

First, without any tool, explain:

```c
printf("A\n");
printf("B\n");
return 0;
```

Why do we see `A`, then `B`, and then the program ends?

If you want one more check, give your trace to an AI and ask it to point out a step that is unclear. You do not need a fixed prompt, and you do not need to save or submit the conversation.

If the AI's explanation conflicts with behavior you can reproduce by running the program, return to the program and the trace as evidence.

---

## 11. Before leaving this Unit, make sure you can really trace

Choose one program from this Unit and answer from the program rather than from memorized wording:

- Once the program starts, where do we begin tracing?
- In these simple programs, in what order do consecutive `printf` statements execute?
- What does `\n` change?
- What happens to this `main` after `return 0;` executes?
- Why should a failed Build be separated from “the program Ran but the result was wrong”?
- Why does “the program runs” still not prove that the requirement is satisfied?
- Can you write the expected output before Run and then verify it with the actual result?

If an answer is uncertain, take two or three `printf` statements, change their order or add/remove `\n`, and repeat prediction → Run → compare.

---

## 12. Wrap-up: next, let the program remember something

P-U00 showed how source becomes a program that is actually executed. P-U01 moved the focus to what happens after execution begins: enter `main`, follow statements in order, produce output, and use prediction and tracing to explain the result.

So far, these programs mostly “do one thing, then the next thing.”

The next Unit adds a new problem:

> **If a program needs to remember a value and use or change it later, where does that value go?**

That leads us into data, types, variables, and program state.

## Navigation

- [Previous Unit P-U00: How Does the C Code You Write Actually Start Running?](unit-00-compiler-ide.en.md)
- [Next Unit P-U02: How Does a Program Remember Data and Change State?](unit-02-data-state.en.md)
- [Preparatory Student Materials Index](../README.en.md)
- [繁體中文版](unit-01-execution.zh-TW.md)
