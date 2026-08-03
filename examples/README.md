# C17 Examples and Defect Cases

Version: 0.2.0  
Status: Classroom verification draft  
Last updated: 2026-08-03  
Major change summary: Added bilingual test plans and incorrect-AI-suggestion review cases for Preparatory Units 1–4.

## Purpose

These files support instructor demonstrations, student tracing, debugging, requirement modification, regression testing, and technical review of AI suggestions.

Compile correct examples with:

```bash
gcc -std=c17 -Wall -Wextra -pedantic <file>.c -o <program>
```

Windows PowerShell runs the result with:

```powershell
.\<program>.exe
```

Linux and macOS run it with:

```bash
./<program>
```

Files under a `defects` directory are intentionally incorrect. Their purpose is prediction, diagnosis, correction, and regression—not copying a final answer.

## Units

- `unit-01`: source, compilation, execution, and stale executable behavior.
- `unit-02`: values, types, state, input/output, and integer division.
- `unit-03`: conditions, loops, boundaries, sentinels, and termination.
- `unit-04`: functions, responsibility decomposition, return values, and regression.

## Test Plans and Incorrect AI Suggestions

- [測試案例與錯誤 AI 建議（繁體中文）](TESTS-AND-AI.zh-TW.md)
- [Test Cases and Incorrect AI Suggestions (English)](TESTS-AND-AI.en.md)

These documents provide expected outputs, normal and boundary cases, intentionally incorrect AI advice, and verification prompts for Units 1–4. Compiler wording may differ between GCC and Clang; students should verify the stage, cause, correction, and regression result rather than memorize one exact diagnostic sentence.

## Assessment Policy

Homework using these examples is not submitted or individually graded. Students keep their own versions, tests, traces, corrections, and AI-verification notes for classroom discussion and final-oral preparation.

## Current Verification Status

- Source files and expected behaviors are documented for Units 1–4.
- Bilingual test plans and incorrect-AI review cases are available.
- Classroom-machine verification with the installed GCC and Clang versions remains to be recorded.

## Navigation

- [Materials Index](../materials/README.en.md)
- [教材索引](../materials/README.zh-TW.md)
