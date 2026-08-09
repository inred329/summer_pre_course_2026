# Formal Unit F-U01: Why Do Representation, Type, and Operations Affect Results?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U01：表示、型別與運算為什麼會影響結果？](unit-01-representation-types.zh-TW.md)

In the preparatory course, we already used `int`, `double`, arithmetic, and input many times. At that stage, the most important goal was to make data flow, control flow, and function responsibilities clear.

Now look at a very ordinary-looking program:

```c
int a = 5;
int b = 2;
double result = a / b;

printf("%.1f\n", result);
```

If you expect `2.5`, the actual result may make you stop:

```text
2.0
```

The problem is not `double result`. What determines the division rule is the type of the operands at the moment the operation happens. Both `a` and `b` are `int`, so `a / b` performs integer division first and produces `2`. That result is converted to `double` afterward, and the discarded fraction cannot be restored.

This example opens the first theme of the formal course: **a value in a program is not only about “what number it is.” How it is represented, what type interprets it, and when an operation happens can all change the result.**

This Unit follows that question downward.

---

## 1. A Bit Pattern Does Not Tell the Whole Story by Itself

Start with these eight bits:

```text
10110010
```

If this is all you see, you cannot completely answer “what does it mean?” It could be interpreted by some program as part of an unsigned integer, a signed-integer representation, part of character data, or a field in another format.

It helps to separate three ideas that are easy to mix together:

- **Value**: the abstract result we want to discuss, such as decimal 45.
- **Representation**: how that value is stored as bits under some rule.
- **Type**: the rules the program uses to interpret the data and determine what operations are available.

For example, decimal 45 can be written as an unsigned binary integer:

```text
00101101
```

The bits do not carry a built-in label saying “I am 45.” We get that interpretation only after choosing the rule “treat this as an unsigned binary integer.”

So when you see a bit pattern, do not rush to ask only:

> What number is it?

A better question is:

> What representation rule and type am I using to interpret it?

---

## 2. Read Weights from the LSB to the Left

For a fixed-width unsigned binary integer, begin at the right:

```text
0 0 1 0 1 1 0 1
^             ^
MSB           LSB
```

- **LSB (Least Significant Bit)** is the rightmost, lowest-weight bit.
- **MSB (Most Significant Bit)** is the leftmost, highest-weight bit.

For an unsigned binary integer, the weights from the LSB are:

```text
128 64 32 16 8 4 2 1
 0  0  1  0 1 1 0 1
```

Therefore:

```text
00101101
= 32 + 8 + 4 + 1
= 45
```

One detail is worth remembering now: **MSB is a positional name. It does not mean “the sign bit in every representation.”** Different representations can give the highest bit different roles. In this Unit, unsigned integers are enough to build the idea of position and weight; you do not need to memorize every signed-integer representation first.

---

## 3. Type Is More Than a Keyword Before a Variable

Look at these declarations:

```c
unsigned int count = 10;
int change = -3;
double ratio = 0.5;
char letter = 'A';
```

At first they may look like the same kind of variable with different labels in front, but type affects many things:

- which values can be represented;
- which rules an operation uses;
- how mixed types are converted;
- which formats `printf` and `scanf` require;
- whether behavior is still defined beyond certain boundaries.

Also, do not think of `int` as “always exactly this many bits with exactly this maximum.” C specifies minimum capabilities and relationships for many integer types; the actual range comes from the implementation and standard headers.

For example:

```c
#include <limits.h>
#include <stdio.h>

int main(void) {
    printf("INT_MIN = %d\n", INT_MIN);
    printf("INT_MAX = %d\n", INT_MAX);
    return 0;
}
```

That is much more reliable than hard-coding an `int` maximum from memory.

---

## 4. Return to the Opening: The Operation Happens Before the Storage

Now return to the opening example:

```c
int a = 5;
int b = 2;

double x = a / b;
double y = (double)a / b;
```

Before running it, predict:

```text
x = ?
y = ?
```

The result is:

```text
x = 2.0
y = 2.5
```

The difference happens before the assignment.

In the first line:

```c
a / b
```

both operands are `int`, so integer division happens first and produces `2`. Only then is `2` converted to `double` and stored in `x`.

In the second line:

```c
(double)a / b
```

`a` is converted to `double` before the division. This time the division follows floating-point rules and produces `2.5`.

You can read them as two different data flows:

```text
5(int) / 2(int) → 2(int) → 2.0(double)
```

and:

```text
5(int) → 5.0(double)
5.0(double) / 2(int) → 2.5(double)
```

When a result surprises you, asking “what types did the operands have when the operation happened?” is often more useful than looking only at the destination variable on the left.

---

## 5. A Format String Is Also a Type Contract

Type affects more than arithmetic. It also affects input and output.

For example:

```c
int n = 42;
double x = 3.14;

printf("%d\n", n);
printf("%f\n", x);
```

`%d` tells `printf`: “retrieve the corresponding argument according to the rules for `int`.”

`%f` in `printf` requires the corresponding argument to be a `double`.

If you write:

```c
printf("%d\n", 3.14);
```

this is not just “bad-looking output.” `%d` requires an `int`, but the actual argument is a `double`. The type contract does not match. For a variable-argument function such as `printf`, this causes **undefined behavior**.

That is why format warnings are not cosmetic. With warnings such as:

```text
-Wall -Wextra -Wformat=2 -pedantic
```

a compiler can often identify this mismatch before you run the program.

This is also a good example of why “it compiled” and “the program has well-defined behavior” are not the same statement.

---

## 6. The Same `char` Can Be Presented in Different Ways

Here is a more visual example:

```c
char c = 'A';

printf("%c\n", c);
printf("%d\n", c);
```

The first line asks for a character presentation. The second presents the converted value as an integer.

This reminds us that **stored data and presentation are not the same thing.** The format string tells `printf` how to interpret and present the corresponding argument.

But do not turn this into the rule:

> `'A'` is always 65.

That is true in common ASCII environments, but C itself does not require the execution character set to be ASCII. Unless the environment or problem statement says so, a particular character code is not a language guarantee.

---

## 7. Why Is `0.1 + 0.2` Worth Looking At?

Integer problems often appear at boundaries or in operation rules. Floating-point values add another issue: **many familiar decimal fractions cannot be represented exactly using a finite binary floating-point representation.**

Try:

```c
#include <stdio.h>

int main(void) {
    double x = 0.1 + 0.2;
    printf("%.17f\n", x);
    return 0;
}
```

You may see a value extremely close to `0.3` but slightly different in the last few digits.

This does not mean the computer “performed addition incorrectly.” Values such as decimal `0.1` and `0.2` are usually stored as nearby representable binary floating-point values, and later operations work on those approximations.

So for a value produced by approximate calculation, writing:

```c
if (x == 0.3) {
    /* ... */
}
```

is often not the comparison you actually want.

One common approach is to use a tolerance:

```c
#include <math.h>

if (fabs(x - 0.3) < 1e-9) {
    printf("close enough\n");
}
```

But `1e-9` is not a magic constant. A reasonable tolerance comes from the requirement, the scale of the values, and the amount of error the application can accept.

Also, do not turn this into “floating-point values can never be compared with `==`.” If the program uses an exact sentinel deliberately—for example, checking whether the user directly entered `0.0` to mean “zero divisor”—an exact comparison may express the requirement correctly. The key question is still: **how was this data produced, and what does the requirement really mean to test?**

---

## 8. Near a Boundary, Intuition Is Most Likely to Fail

Do not guess the maximum `int`. Let the header tell you:

```c
#include <limits.h>
#include <stdio.h>

int main(void) {
    printf("%d\n", INT_MAX);
    return 0;
}
```

Now imagine:

```c
int x = INT_MAX;
int y = x + 1;
```

For signed integers, arithmetic overflow beyond the representable range is **undefined behavior**. If one run happens to appear to “wrap into a negative number,” that observation is not a C language guarantee.

If a requirement allows `x + y` and the inputs may be close to the boundary, check before performing the risky addition. For example, when `y > 0`:

```c
if (x > INT_MAX - y) {
    printf("would overflow\n");
} else {
    int sum = x + y;
    printf("%d\n", sum);
}
```

The important order is: **check first, then operate.** If you produce an already-overflowed signed result and inspect it afterward, the undefined behavior has already happened.

Unsigned integers are different. Unsigned arithmetic follows modular rules, so values beyond the maximum wrap according to those rules. That behavior is defined, but “defined” does not automatically mean “correct for the requirement.” Wraparound is useful only when the problem actually intends modular arithmetic.

---

## 9. Do Not Call Every Strange Result the Same Kind of Error

We have now seen several cases that all look like “the result is wrong,” but they are not the same:

| Situation | Is the C behavior defined? | What should you ask? |
|---|---|---|
| `5 / 2` produces `2` | Yes | Is integer division what the requirement wanted? |
| A calculated floating-point value is compared directly with `==` | Yes | Does the comparison rule fit approximate data? |
| A signed integer exceeds its representable range | No | Can the overflow be prevented before the operation? |
| `printf("%d", 3.14)` | No | Do the format and actual argument type agree? |

This distinction matters.

“Defined but not what the requirement wanted” is usually a logic or requirement problem. Undefined behavior means the language no longer gives you a reliable rule from which to interpret one observed run.

So while debugging, do not ask only:

> Why is the output different from what I wanted?

Go one step earlier:

> Am I seeing a defined rule that does not match the requirement, or have I entered undefined behavior?

---

## 10. Run Three Small Experiments and Turn Rules into Evidence

### Experiment A: Integer Division and Conversion Timing

Predict and run:

```c
printf("%d\n", 7 / 3);
printf("%.6f\n", 7.0 / 3);
printf("%.6f\n", (double)7 / 3);
```

Do not memorize only the outputs. For each line, explain what types the two operands have when division happens.

### Experiment B: Decimal and Hexadecimal Views of the Same Unsigned Value

```c
unsigned int value = 45;
printf("%u %x\n", value, value);
```

The two outputs look different, but they are not two different `value` objects. The same numeric value is simply written using two textual representations.

### Experiment C: Compile a Format Mismatch, but Do Not Run It

Create:

```c
#include <stdio.h>

int main(void) {
    printf("%d\n", 3.14);
    return 0;
}
```

Compile it with:

```text
-Wall -Wextra -Wformat=2 -pedantic
```

and read the warning. The goal is not to “see what undefined behavior prints today.” The goal is to practice finding a broken type contract with static diagnostics before execution.

---

## 11. Independent Practice: Build a Representation and Division Reporter

Write a small program that reads:

```text
one unsigned int value
one double divisor
```

After successful input, display:

1. the integer in decimal;
2. the same integer in hexadecimal;
3. the divisor with fixed precision;
4. `(double)value / divisor` when the divisor is not `0.0`;
5. `Undefined` without performing division when the divisor is `0.0`.

For example:

```text
Input: 45 2
Decimal: 45
Hex: 2d
Divisor: 2.000
Quotient: 22.500
```

Start with tests such as:

| Input | What should you pay attention to? |
|---|---|
| `45 2` | Normal decimal, hexadecimal, and division |
| `7 3` | A floating-point quotient that is not an integer |
| `0 5` | Zero dividend |
| `45 0` | Division by zero must be prevented |
| Non-numeric input | Whether `scanf` reports input failure |
| A value near `UINT_MAX` | Whether the type boundary and formats remain correct |

Write the expected result before running the program. When the result differs, trace the path “input type → operand types → operation → output format.”

If you use `scanf`, make the format agree with the destination types, for example:

```c
unsigned int value;
double divisor;

if (scanf("%u %lf", &value, &divisor) != 2) {
    printf("Invalid input\n");
    return 1;
}
```

You already saw the `&` syntax in the preparatory course. A full pointer model comes later in the formal course. For now, read it as “give `scanf` the location where it may store the input.”

---

## 12. Change One Requirement and See What Really Has to Move

Suppose the first version prints hexadecimal using lowercase letters:

```text
2d
```

Now the requirement changes:

> Hexadecimal letters must always be uppercase.

Do not rewrite the whole program. Find the part that is actually connected to this requirement.

In `printf`, `%x` and `%X` select different hexadecimal text formats. After changing it, rerun the original normal, zero, and boundary cases. Confirm that only the intended presentation changed and the other behavior still works.

This tiny requirement change connects several ideas from the Unit: the value did not change, the type did not change, and the arithmetic did not change. What changed was the **representation used for output**.

---

## 13. Optional: Let AI Challenge Your Explanation

You may skip this section completely.

First, without any tool, explain:

> Why does `double x = 5 / 2;` produce `2.0`, while `double y = (double)5 / 2;` produces `2.5`?

If you want an extra check, you may give your explanation to an AI system and ask it to identify any unclear step. No fixed prompt, saved conversation, or submission is required.

If an AI explanation conflicts with type rules, compiler diagnostics, or an experiment you can reproduce, return to that evidence and judge again.

---

## 14. Before Leaving This Unit, Explain from Programs Instead of Memorizing Definitions

Return to the code fragments above and make sure you can answer these without reciting the wording of the chapter:

- Why does `00101101` represent 45 under the rule “unsigned binary integer”?
- Why are MSB and LSB positional names rather than a guarantee that MSB is always a sign bit?
- In `double result = a / b;`, why does the `double` on the left not make the division on the right preserve a fraction?
- Why is a `printf` format string also a type contract?
- Why should a value such as `0.1 + 0.2` usually be judged with a requirement-driven tolerance?
- What is the fundamental difference between signed overflow and unsigned wraparound?
- When a result looks strange, can you first decide whether it is “defined but wrong for the requirement” or “undefined behavior”?

If one answer feels like a sentence you memorized rather than something you understand, return to the corresponding program, change one value, make a prediction, and observe what happens.

---

## 15. Closing the Unit

The preparatory course taught us to trace what a program is doing. This Unit adds a deeper question: **once a program has a value, what rules does it use to interpret and operate on that value?**

A bit pattern needs a representation rule to gain meaning. Type determines available operations and conversions. The moment when an operation happens can change the result. Floating-point data often requires approximate comparison rules. Formatted I/O requires the format to agree with the actual type. Near integer boundaries, we must first ask whether the language still defines the behavior at all.

The next Unit carries these judgments into more complex control flow. When there is more than one condition, branches become nested, and checks must happen in a particular order, the next reading and debugging question becomes: “which condition is evaluated first, and which states can reach each path?”

## Navigation

- [Previous Stage: Preparatory Unit P-U04 — Functions and Integration](../preparatory/unit-04-functions-integration.en.md)
- [Next Unit: Complex Control Flow](unit-02-complex-control-flow.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-01-representation-types.zh-TW.md)
