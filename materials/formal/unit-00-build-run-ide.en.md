# Formal Unit F-U00: What Actually Happens After You Press Run?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U00：按下 Run 之後，到底發生了什麼？](unit-00-build-run-ide.zh-TW.md)

You may already have written programs and may already be used to pressing Run, Build, or Debug in an IDE.

This Unit does not reteach where every button is located. It asks something more important first: when you say “I ran the program,” what different steps actually happened in between?

The formal course will keep using compilers, Build, Run, Debug, tests, and error messages. If all of these words blur into one action in your mind, many later problems will look more mysterious than they really are.

So begin with a familiar action:

> When you press Run, what is the IDE actually doing for you?

---

## 1. Break one button press back into several actions

Suppose you have:

```c
#include <stdio.h>

int main(void) {
    printf("Hello\n");
    return 0;
}
```

You press Run in the IDE and see:

```text
Hello
```

The interface may need only one click, but conceptually we should still separate:

```text
source code
→ Build / compile-related work
→ executable
→ Run
→ running program
→ output
```

Some IDEs automatically check whether a Build is needed before running. Other workflows make Build and Run two explicit actions. The interface can differ, but the roles should not be collapsed into one idea.

---

## 2. Source code is not the thing you finally execute

Your source may live in:

```text
main.c
```

What you actually execute is the executable produced by the Build.

So if you change:

```c
printf("Hello\n");
```

to:

```c
printf("Goodbye\n");
```

but do not update the executable, you may still see the old result.

A useful way to restate that situation is:

> Does the source I am looking at correspond to the same Build as the executable I am running now?

That question is much easier to investigate than simply saying “the IDE is acting strangely.”

---

## 3. Do not treat the compiler and the IDE as the same thing

An IDE provides an integrated development environment.

It may contain:

```text
editor
build controls
terminal
run controls
debugger
project management
```

A compiler handles part of the work needed to turn C source code into a runnable program.

So a better model is:

```text
IDE
  └─ helps invoke and organize the compiler, debugger, and other tools
```

not:

```text
IDE = compiler
```

That distinction becomes important when you change IDEs, move to another machine, inspect CI, or diagnose a build error.

---

## 4. A successful Build answers only part of the question

Suppose the requirement is:

```text
Print Hello
```

but the program is:

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye\n");
    return 0;
}
```

It may still show:

```text
Build succeeded
Run succeeded
```

while failing the requirement.

So every later Unit can use three layers of evidence:

```text
1. Did the tools accept my program?
2. Did the program actually execute to the point I am observing?
3. Does the result match the requirement and my prior reasoning?
```

These layers provide different evidence. Do not let one stand in for the others.

---

## 5. Use one “old executable” experiment to prove that you understand

Do this once:

1. Build a program that prints `Version A`.
2. Run it and confirm that you see `Version A`.
3. Change the source so it prints `Version B`.
4. Save it, but deliberately do not Build again.
5. If your environment allows it, run the previous executable directly.
6. Explain why it may still print `Version A`.
7. Build again and then Run.
8. Confirm that the output changes to `Version B` only after the new Build.

The important part is not the text itself. It is whether you can point out clearly:

```text
Which file changed?
Which file was executed?
Which step made them correspond again?
```

---

## 6. For now, keep one key distinction between Run and Debug

Run lets the program execute normally.

Debug lets you pause during execution and inspect program state.

For example:

```c
int a = 5;
int b = 2;
int result = a / b;
```

If you place a breakpoint around the `result` line, a debugger can let you pause and inspect:

```text
a = 5
b = 2
```

and observe the state of `result` before and after the assignment executes.

You do not need every debugger feature yet. F-U11 will place the debugger inside a more complete testing, diagnosis, and improvement workflow.

For now, remember:

> A debugger is a tool for observing execution evidence, not another magical kind of Run.

---

## 7. Build contains finer-grained steps, but we do not need all of them yet

When a program has only one `.c` file, Build may look simple.

Later, when a program is split into:

```text
main.c
student.c
student.h
```

we will need a fuller model involving compilation, object files, and linking.

F-U10 on modular programming will study those steps properly. For now, keep:

```text
source files
→ Build
→ executable
```

and remember that Build is not always one indivisible action.

---

## 8. Treat the IDE as a replaceable interface, not as the course itself

Whether you use Visual Studio, VS Code, Code::Blocks, CLion, or another development environment, button locations and configuration may differ.

But these questions remain:

- Which source am I editing?
- Which compiler is processing it?
- Did the Build succeed?
- Which executable am I actually running?
- Am I using normal Run or Debug?
- Does the output support my conclusion?

If you can answer those questions, you are less dependent on one specific interface.

---

## 9. Before leaving this Unit, make sure you can explain instead of only operate

Without using IDE button names, answer:

- What is the relationship between a source file and an executable?
- Why are Build and Run different actions?
- How do the roles of an IDE and a compiler differ?
- Why can edited source code still produce old output?
- Why does `Build succeeded` not prove that the program satisfies the requirement?
- What is the most important difference between Run and Debug?
- Why can the full compile/link details wait until later?

If your answer is only “because I press this button,” repeat the old-executable experiment and explain it using files and steps instead.

---

## 10. The next problem: the tools can work correctly and the result can still surprise you

At this point, we have separated the tool layer: source, Build, compiler, executable, Run, and Debug have different roles.

But even when you are certain that:

```text
the Build did not fail
and you are running the newest executable
```

the result can still differ from your intuition.

For example:

```c
int a = 5;
int b = 2;
double result = a / b;
```

Why might `result` become `2.0` rather than `2.5`?

That is no longer an IDE or Build problem.

The next Unit asks: **why can representation, type, and operation rules change the result?**

## Navigation

- [Next Unit F-U01: Why Do Representation, Type, and Operations Affect Results?](unit-01-representation-types.en.md)
- [Formal Course Student Materials](README.en.md)
- [繁體中文版](unit-00-build-run-ide.zh-TW.md)
