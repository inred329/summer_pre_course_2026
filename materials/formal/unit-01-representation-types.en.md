# Formal Unit F-U01: Why Do Representation, Type, and Operations Affect Results?

Version: 1.0.0  
Status: Official student material  
Last updated: 2026-08-04  
Corresponding Chinese version: [正式單元 F-U01：表示、型別與運算為什麼會影響結果？](unit-01-representation-types.zh-TW.md)

## Purpose and Completion Standard

This chapter is for independent reading, practice, and review. Completing it means you can explain how the same bits may have different meanings under different types and interpretation rules, predict conversions and operations, and diagnose overflow, integer division, and floating-point error with tests.

## Core Question

> Why can the same value or operation produce different outcomes because of representation and type?

After completing this chapter, you should be able to:

1. Distinguish value, representation, and type.
2. Explain the positional meaning of bits, MSB, and LSB.
3. Predict integer division, conversion, and formatted output.
4. Explain that floating-point values are not exact representations of all real numbers.
5. Test results with boundary cases and tolerances.

---

## 1. Begin with a Bit Pattern

```text
10110010
```

Without additional information, it could represent an unsigned integer, signed integer, part of a character encoding, or another format. Bits alone are only 0 and 1; types and rules give them meaning.

---

## 2. MSB and LSB

For a fixed-width bit sequence:

```text
1 0 1 1 0 0 1 0
^             ^
MSB           LSB
```

- MSB: Most Significant Bit, the highest-weight leftmost bit.
- LSB: Least Significant Bit, the lowest-weight rightmost bit.

In an unsigned binary integer, the LSB has weight 1 and each position to the left doubles. MSB is a positional name; different representations may give it different roles.

---

## 3. Type Determines Interpretation and Operations

```c
unsigned int count = 10;
int change = -3;
double ratio = 0.5;
char letter = 'A';
```

Type affects range, storage, operations, formatted I/O, and conversions. It is more than a keyword before a variable; it is a set of interpretation and operation rules.

---

## 4. Integer Division and Conversion

```c
int a = 5;
int b = 2;
double x = a / b;
double y = (double)a / b;
```

Prediction:

```text
x = 2.0
y = 2.5
```

`a / b` uses integer division first. Storing the result in `double` cannot restore the discarded fraction. Converting before the operation changes the operation's type.

---

## 5. Floating-Point Representation and Error

```c
#include <stdio.h>

int main(void) {
    double x = 0.1 + 0.2;
    printf("%.17f\n", x);
    return 0;
}
```

The result may be close to but not exactly `0.3`. Many decimal fractions cannot be represented exactly with a finite number of binary digits.

Use a tolerance:

```c
#include <math.h>

if (fabs(x - 0.3) < 1e-9) {
    printf("close enough\n");
}
```

---

## 6. Integer Range and Overflow

```c
#include <limits.h>

printf("%d\n", INT_MAX);
```

Do not guess fixed ranges. Signed integer overflow may cause undefined behavior, so one observed result is not a guarantee. Test values near the boundary and define a prevention strategy before performing risky operations.

---

## 7. Characters Are Data Representations Too

```c
char c = 'A';
printf("%c %d\n", c, c);
```

The same `char` can be presented as a character or an integer code. It is one stored value shown through different formats.

---

## 8. Error Cases

### Storage Type Does Not Change an Earlier Operation

```c
double average = total / count;
```

Inspect operand types, not only the left side.

### Direct Floating-Point Equality

Compare calculated values using an appropriate tolerance.

### Format Mismatch

```c
printf("%d\n", 3.14);
```

Use compiler warnings and a type table to diagnose.

---

## 9. Guided Practice

1. Mark the weights from LSB to MSB for `00101101` and compute its unsigned value.
2. Predict `7 / 3`, `7.0 / 3`, and `(double)7 / 3`.
3. Compare `0.1 + 0.2` with `0.3` using a tolerance.

---

## 10. Independent Practice: Data Representation Reporter

Read an integer and a floating-point value. Display the integer in decimal and hexadecimal, the floating value with fixed precision, and the floating-point quotient. Test normal values, zero, and values near relevant limits.

---

## 11. Requirement Modification

New rule: when the divisor is zero, do not divide; print `Undefined`. Update the test table first, then modify the control flow and run regression tests.

---

## 12. Explain the Concept to AI

Explain:

> What are MSB and LSB, and how does type affect the interpretation of the same bits and the same operation?

If an AI response conflicts with type rules, compiler warnings, or reproducible results, judge it again using evidence.

---

## 13. Self-Check

- I can distinguish value, representation, and type.
- I can identify MSB and LSB.
- I can predict integer division and conversion.
- I can explain floating-point error.
- I know signed overflow cannot be inferred safely from one result.
- I can design boundary tests from type and requirement.

## 14. Chapter Summary

A bit representation gains meaning only through types and interpretation rules. Operation results depend on operand types, conversion timing changes outcomes, and floating-point work requires approximation and tolerance. The next Unit applies these judgments to more complex control flow.

## Navigation

- [Formal-Course Index](README.en.md)
- [Next Unit: Advanced Control Flow](unit-02-advanced-control.en.md)
- [繁體中文版](unit-01-representation-types.zh-TW.md)
