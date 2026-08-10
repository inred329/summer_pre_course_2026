# Preparatory Unit P-U00: How Does the C Code You Write Actually Start Running?

Version: 1.2.0  
Status: Student material  
Last updated: 2026-08-10  
Corresponding Chinese version: [前導單元 P-U00：寫好的 C 程式，怎麼真的跑起來？](unit-00-compiler-ide.zh-TW.md)

You may already have seen someone press a green triangle in an IDE and immediately get program output. Or perhaps the first time you opened a development environment, you saw an editor, terminal, Build, Run, and Debug controls all at once and were not sure which parts were actually doing different jobs.

Before learning C syntax, let us make that process clear.

This Unit is not about memorizing tool names or button locations. The important thing is to build a path you will keep using later:

```text
C source code you write
→ compilation and build tools process the source
→ a runnable program is produced
→ the operating system starts it
→ the program runs and produces observable results
```

An IDE makes these steps easier to operate, but the IDE itself is not another name for the entire process.

### You can enter the same idea from three different directions

Different learners first make sense of development tools in different ways. This chapter connects three common entry points to the same model:

- **If the IDE is already familiar to you**: begin with “what work is the IDE doing when I press Run?”
- **If you prefer visible files and commands**: begin with `hello.c`, a Build command, and the executable that appears afterward.
- **If tools make the most sense when something goes wrong**: keep the later “I changed the source, but I still see the old result” experiment in mind, then trace which step failed to update.

All three paths return to the same idea: **source, Build, executable, and Run have different roles; an IDE integrates them without turning them into the same thing.**

If one explanation does not click yet, follow another one for a while. The examples below revisit the same process from several directions.

---

## 1. Start with an ordinary text file

Create a file named:

```text
hello.c
```

Put this inside:

```c
#include <stdio.h>

int main(void) {
    printf("Hello, C!\n");
    return 0;
}
```

If your usual habit is to press Run immediately after typing, pause for a moment this time and look only at what exists right now.

At this moment, `hello.c` is a **source file**. The text inside is **source code**.

You can open it, read it, and edit it, but saving the text does not mean the computer has started executing the C program.

This is the first distinction to keep clear:

```text
I wrote code into a file
```

and

```text
the computer is running my program
```

are not the same event.

---

## 2. What does a compiler do?

C source code is human-readable text written according to C language rules. Before it can run as a program, compilation and build tools must process it.

If your environment uses GCC, you may build from a terminal with:

```text
gcc hello.c -o hello
```

Different operating systems, compilers, or classroom environments may use a different command. If your instructor provides another command, use that one. The important point here is not memorizing `gcc`; it is understanding the role of this step.

In this tiny one-file example, that command performs the work needed to produce a runnable result. After it succeeds, you may see `hello`, `hello.exe`, or a file placed by the development environment inside a build directory.

For now, picture the important relationship like this:

```text
hello.c
  │
  │ compiler / build tools
  ▼
executable
```

If the source code does not satisfy the C rules the tools require, for example because a semicolon is missing, this Build may fail and no corresponding new executable is produced.

When programs later contain multiple source files, Build will contain more detailed stages. You do not need all of them yet.

---

## 3. Compile/Build and Run are different actions

Now run the program that was produced.

In some terminal environments, that may look like:

```text
./hello
```

On Windows, you may instead run:

```text
hello.exe
```

You should see:

```text
Hello, C!
```

Two different kinds of work happened:

```text
Build
hello.c → executable

Run
executable → running program → output
```

So:

- Build or compile-related work turns the current source into the latest runnable result.
- Run starts an executable that already exists.

Later, when you see Build, Run, and Debug controls, try asking: **which stage is happening now?** That question is usually more transferable than memorizing one IDE's buttons.

---

## 4. An important experiment: edit the source, but do not Build again yet

Change the source code to:

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye, C!\n");
    return 0;
}
```

Save `hello.c`.

Now do not Build again. Run the executable from the previous Build.

Before you do it, predict whether you will see:

```text
Hello, C!
```

or:

```text
Goodbye, C!
```

If you are still running the executable produced by the earlier Build, you will see the old result:

```text
Hello, C!
```

The reason is not that the computer “did not notice that you saved the file.” The reason is:

```text
you changed hello.c
but you ran the executable produced earlier
```

They are not the same file.

Build again and then run again. Now you should see:

```text
Goodbye, C!
```

This experiment will stay useful later. Whenever you think “I changed the code, so why did the result not change?”, one of your first questions should be:

> Did I really rebuild? Am I running the newest executable?

If the earlier flow diagram felt abstract, this experiment gives you another way into it: **editing changes the source text; Build turns the new text into a new executable; Run starts that executable.**

---

## 5. So what is an IDE?

IDE stands for **Integrated Development Environment**.

An IDE usually places several development tools and actions in one interface, for example:

```text
IDE
├─ editor: edit source code
├─ build integration: invoke the compiler and related tools
├─ run: start the program
├─ terminal: enter commands directly
└─ debugger: pause and inspect execution
```

Different IDEs may arrange these features differently. Their roles matter more than where the buttons happen to be.

If you previously pictured the IDE and compiler as one thing, split that model slightly:

```text
IDE ≠ compiler
```

A better model is:

> The IDE integrates editing, building, running, debugging, and other development work. The C source is still processed by a compiler and related build tools.

That is also why an editor may be able to open a `.c` file even when the computer does not yet have a usable C development toolchain installed.

Another way to think about it is: **the IDE is an operating interface; the compiler, debugger, and related tools are some of the tools it organizes or invokes.** The interface may change completely when you switch IDEs, while these underlying roles still exist.

---

## 6. Why can Build mean more than Compile?

With a tiny one-file program such as `hello.c`, you can initially think of Build as “do the work needed to turn the current source into the latest runnable result.”

For a very small program, the most visible work is compilation-related processing.

Later, when a program grows and is split across multiple files, one Build may involve more than a single compilation action. A later formal-course Unit on modular programming will separate compilation and linking more carefully.

For now, this model is enough:

```text
Edit source
→ Build
→ obtain the latest runnable result
→ Run
```

The finer build details will be more meaningful when we actually need multiple source files.

---

## 7. Run and Debug are not the same thing either

Run normally aims to let the program execute directly.

Debug mode gives you a way to stop during execution and inspect what is happening.

We do not need variables yet. Consider only two output statements:

```c
printf("First\n");
printf("Second\n");
```

If you place a **breakpoint** on the second line, a debugger can pause before that line executes. At that moment you can observe that the first line has already produced output while the second one has not.

That is enough to see the difference between Debug and an ordinary Run:

```text
Run: let the program execute directly
Debug: pause during execution, move step by step, and observe what is happening
```

You do not need every debugger feature now. After we learn data and program state, inspecting variables will become much more meaningful. The formal course will later place the debugger inside a complete testing and debugging process.

If a playback analogy helps, you can think of Run as letting a video play through, while Debug lets you pause and move forward step by step to see where execution is. The analogy is only about controlling the pace of observation; a debugger is not literally replaying a prerecorded program.

---

## 8. A successful Build and a correct program answer different questions

Consider this program:

```c
#include <stdio.h>

int main(void) {
    printf("Goodbye, C!\n");
    return 0;
}
```

It may Build successfully and Run successfully.

But suppose the requirement is:

```text
Print Hello, C!
```

Then the program is still wrong.

Throughout the course, we will keep separating these questions:

```text
Did the tools accept and successfully build the program?
↓
Was the program actually started and executed?
↓
Does the observed result satisfy the requirement?
```

None of these questions can replace the others.

From another angle, Build answers something like “can this source form a runnable result?”, while a requirement test asks “is that result actually the one we wanted?” Both matter, but they answer different questions.

---

## 9. Walk through the full process

Create:

```text
intro.c
```

Make it print two lines:

```text
My name is <your English name>.
I am learning C.
```

Besides getting the program to run, try to name what is happening at each step:

1. Which source file am I editing?
2. When did I save it?
3. When did I Build?
4. What was produced or updated after the Build succeeded?
5. Which program am I actually Running?
6. Does the output match what I predicted?

If you are using an IDE, locate the editor, terminal, Build, Run, and Debug features. If you are using a terminal, map the commands you type back onto the same process. The two workflows expose the same underlying model in different ways.

---

## 10. Check your understanding through the actual experiment

Try answering from the `hello.c` experiment without repeating the chapter's exact wording:

- Are `hello.c` and the executable the same file?
- Why does editing `hello.c` not automatically change an old executable?
- What do Build and Run each do?
- Why are an IDE and a compiler not the same thing?
- Why does a successful Build not prove that the result satisfies the requirement?
- What is the difference between Run and Debug?
- If you edit the source but still see old output, what should you check first?

Some learners make sense of this most easily from a flow diagram; others need to run the stale executable once before the distinction feels real. Either route is fine if you can finally map your own actions back to source → Build → executable → Run.

---

## 11. Next: start reading a program that is actually running

We now know that a C program is not simply “text plus a magic Run button.”

You have a source file; Build uses a compiler and related tools to create the latest runnable result; Run actually starts the program; and an IDE integrates these actions into one environment.

The next Unit moves the focus away from the tools themselves and asks: **once the program really starts running, how do the statements in `main` become the result we observe?**

## Navigation

- [Next Unit P-U01: Once a Program Starts Running, How Do Statements Become Results?](unit-01-execution.en.md)
- [Preparatory Student Materials Index](../README.en.md)
- [繁體中文版](unit-00-compiler-ide.zh-TW.md)