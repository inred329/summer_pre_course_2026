# P-U02 Optional Appendix: How Is Data Represented at the Bit Level?

Version: 1.0.0  
Status: Optional student appendix  
Last updated: 2026-08-11  
Corresponding Chinese version: [P-U02 選讀附錄：資料在位元層級是怎麼表示的？](appendix-bit-level-data-representation.zh-TW.md)

The main P-U02 path focuses on values, types, variables, and state:

```text
score currently stores 80
→ an assignment executes
→ score becomes 85
```

But if we ask one level deeper:

> What do `80`, `-5`, `5.75`, or `'A'` actually look like when stored in memory?

we reach **bit-level data representation**.

This appendix is optional. You do not need it before continuing to P-U03. Its purpose is to build a lower-level intuition: **a computer ultimately stores bit patterns, while types determine how those patterns are interpreted and operated on.**

---

## 1. Separate a value from its bit pattern

A bit has two possible states:

```text
0
1
```

Several bits together can form many patterns.

Eight bits can form:

```text
00000000
00000001
00000010
...
11111111
```

for a total of:

```text
2^8 = 256
```

different patterns.

The pattern itself does not automatically say “I am an integer,” “I am negative,” or “I am a character.”

For example:

```text
01000001
```

interpreted as an unsigned binary integer is decimal 65. In a common ASCII environment, that same numeric code also corresponds to the character `A`.

So the important question is not only:

> What are these bits?

but also:

> Which type and representation rule am I using to interpret them?

That is the lower-level version of P-U02's idea that type affects representation and operation rules.

---

## 2. A C byte is not defined as “always exactly 8 bits”

In C:

```c
sizeof(char) == 1
```

is always true.

The number of bits in one C byte is given by:

```c
CHAR_BIT
```

from:

```c
#include <limits.h>
```

On common machines:

```text
CHAR_BIT = 8
```

which is why everyday explanations often say “1 byte = 8 bits.” Strictly, C guarantees `CHAR_BIT >= 8`; it does not require every implementation to use exactly 8.

For clear diagrams, the rest of this appendix frequently uses an **8-bit teaching model**. Do not infer from those diagrams that C `int` is always 8 bits—or always 32 bits.

---

## 3. Unsigned integers: each bit position has a weight

Start with an unsigned binary integer.

For 8 bits:

```text
position: 7   6   5   4   3   2   1   0
weight: 128  64  32  16   8   4   2   1
```

For example:

```text
00001101
```

means:

```text
8 + 4 + 1 = 13
```

so:

```text
00001101₂ = 13₁₀
```

An 8-bit unsigned integer model represents:

```text
00000000 = 0
...
11111111 = 255
```

or:

```text
0 through 2^8 - 1
```

More generally, if `N` bits are all used for an unsigned value, the range is:

```text
0 through 2^N - 1
```

---

## 4. How can negative integers fit into bits?

Unsigned interpretation has already used every pattern for zero or positive values.

To represent negative values, we need another rule.

The dominant modern representation is **two's complement**.

Using an 8-bit model:

```text
00000101 = +5
```

A common way to calculate the two's-complement representation of `-5` is:

### Step 1: write +5

```text
00000101
```

### Step 2: invert every bit

```text
11111010
```

### Step 3: add 1

```text
11111010
+       1
----------
11111011
```

So in an 8-bit two's-complement model:

```text
+5 = 00000101
-5 = 11111011
```

---

## 5. Why is two's complement convenient for addition?

Consider:

```text
  00000101   (+5)
+ 11111011   (-5)
-----------
1 00000000
```

If the model keeps only eight positions, the carry beyond the left edge is outside those eight bits, leaving:

```text
00000000
```

which is zero.

This property allows the same binary addition machinery to handle many positive and negative integer operations naturally.

---

## 6. Another way to read two's complement: give the top bit a negative weight

An 8-bit two's-complement value can also be read with these weights:

```text
bit:      7    6   5   4   3   2   1   0
weight: -128  64  32  16   8   4   2   1
```

For:

```text
11111011
```

we get:

```text
-128 + 64 + 32 + 16 + 8 + 2 + 1
= -5
```

For direct reading, this can be easier than “invert and add one” every time.

---

## 7. Why is the 8-bit two's-complement range -128 through 127?

Eight bits provide 256 patterns.

Under two's complement:

```text
00000000 through 01111111
```

represent:

```text
0 through 127
```

while:

```text
10000000 through 11111111
```

represent:

```text
-128 through -1
```

So the range is:

```text
-128 through 127
```

Notice the asymmetry:

```text
largest positive = 127
smallest negative = -128
```

There is no `+128` in the same 8-bit signed range.

---

## 8. C17 and two's complement: do not confuse “common” with “the only language guarantee”

The course examples use C17 as the language baseline.

In C17, **you should not treat every signed integer implementation as guaranteed by the language to use two's complement**. Historically, C permitted other signed representations as well.

This appendix uses two's complement because:

- it is the dominant model on modern general-purpose processors;
- it gives a useful explanation of signed binary arithmetic;
- it appears constantly when you later study machine-level data and assembly language.

But portable C code should not assume that one observed signed bit pattern has the same language-guaranteed meaning on every C17 implementation.

Also avoid memorizing:

```text
int = 32 bits
```

The actual C `int` size and range are implementation-dependent. You can inspect:

```c
#include <limits.h>
```

for:

```text
INT_MIN
INT_MAX
CHAR_BIT
```

and use:

```c
sizeof(int)
```

for the current environment.

---

## 9. Floating-point is not just “an integer with some bits after a decimal point”

Now consider:

```c
double temperature = 5.75;
```

Floating-point representation does not normally reserve a fixed number of bits permanently to the left and right of a binary point.

It is closer to scientific notation.

Decimal scientific notation might use:

```text
6.02 × 10^23
```

Binary floating-point can use a form like:

```text
1.xxxxx × 2^e
```

A common IEEE 754 binary floating-point format divides bits into three roles:

```text
sign | exponent | fraction
```

---

## 10. Use IEEE 754 binary32 to examine `5.75`

This section uses the common IEEE 754 **binary32** model, which corresponds to 32-bit `float` on many systems.

Its fields are:

```text
1 bit   sign
8 bits  exponent
23 bits fraction
```

Convert decimal `5.75` to binary:

```text
5    = 101₂
0.75 = 0.11₂
```

therefore:

```text
5.75 = 101.11₂
```

Normalize it:

```text
1.0111 × 2^2
```

So:

```text
sign = 0
```

The exponent `2` is stored in binary32 using bias 127:

```text
2 + 127 = 129
```

129 in binary is:

```text
10000001
```

The fraction field stores the bits after the normalized leading `1`:

```text
01110000000000000000000
```

Thus the binary32 pattern for `5.75` is:

```text
0 | 10000001 | 01110000000000000000000
```

---

## 11. How is a negative floating-point value represented?

In this IEEE 754 example, `-5.75` does not come from taking the entire positive bit pattern and applying two's complement.

The main difference is the sign bit:

```text
+5.75
0 | 10000001 | 01110000000000000000000

-5.75
1 | 10000001 | 01110000000000000000000
```

This contrast matters:

> **Two's complement is a common signed-integer representation. IEEE 754 negative floating-point values do not use two's complement over the entire floating-point bit pattern.**

Do not transfer the signed-integer rule directly to floating-point.

---

## 12. Why can decimal `0.1` fail to be exact?

Decimal:

```text
0.5
```

has the binary form:

```text
0.1₂
```

so it is easy to represent exactly.

Decimal `0.1`, however, has an infinitely repeating binary expansion.

A finite fraction field cannot store infinitely many digits, so the representation uses a nearby representable value.

That is why a floating-point calculation such as:

```c
0.1 + 0.2
```

may not produce a bit-level result that is exactly the mathematical decimal value `0.3`.

The computer is not randomly doing addition incorrectly. The **representation itself has finite precision**.

Formal Unit F-U01 revisits this from the perspective of representation, type, and operation rules.

---

## 13. IEEE 754 also reserves special bit patterns

For binary32, special exponent patterns are used for values such as:

```text
+0 / -0
subnormal numbers
+infinity / -infinity
NaN
```

This appendix does not require you to memorize every pattern.

For now, keep the main idea:

```text
floating-point is not ordinary binary integer storage
its bits are divided among sign, scale, and precision roles
```

C17 itself also does not require every `float` and `double` implementation to be exactly IEEE 754 binary32 or binary64. IEEE 754 is a major and common implementation model, not the only language-level possibility.

---

## 14. `char` is also an integer type in C

P-U02 uses code such as:

```c
char grade = 'A';
```

At the programming level, we think of `grade` as a character.

At the C type-system level, `char` belongs to the integer types.

Memory still contains a bit pattern. A character-encoding rule tells us which character a numeric code represents.

In a common ASCII environment:

```text
'A' → 65 → 01000001
```

So for:

```c
char c = 'A';
```

the same stored information can be viewed differently:

```text
%c  → displayed as A
%d  → after integer promotion, displayed as numeric code 65
```

But remember:

> **C does not require the execution character set to be ASCII.**

So “`'A'` is always 65” is not a universal C-language guarantee.

---

## 15. UTF-8 adds another layer: one human-visible character may use multiple `char` units

ASCII letters can create the impression:

```text
1 char = 1 human-visible character
```

That does not generalize to UTF-8.

A Unicode character may be encoded using multiple bytes in UTF-8.

So in a typical UTF-8 environment:

```text
'A'
```

usually uses one byte, while many Chinese characters use multiple bytes.

A safer way to think about:

```c
char text[]
```

is:

> It stores a sequence of `char` units; a character-encoding rule is still needed to interpret those units as human-readable text.

Formal Unit F-U04 later studies C strings, `\0`, and buffer capacity.

---

## 16. Bit representation and byte order in memory are separate questions

Suppose a value occupies multiple bytes.

Besides asking “what binary pattern represents the value?”, another question appears:

> When those bytes occupy consecutive memory addresses, which byte goes at the lower address?

That is **endianness**.

For a 32-bit value such as:

```text
0x12345678
```

big-endian and little-endian machines can arrange the bytes differently in memory.

This appendix does not go deeply into endianness because it is a different layer from two's-complement signed representation.

Keep them separate:

```text
representation: which bits encode the value?
endianness: how are multiple bytes ordered by address?
```

---

## 17. Return to P-U02: a type selects interpretation rules

Now revisit:

```c
int count = 5;
double temperature = 23.5;
char grade = 'A';
```

At first these look like three variables with different type names.

One level lower:

```text
int
→ integer representation and integer operation rules

double
→ floating-point representation and operation rules

char
→ an integer type used to store a character-encoding unit and present it according to character rules
```

That is why type is not decorative syntax before a variable name.

It affects:

- which values can be represented;
- how a bit pattern is interpreted;
- which operation rules apply;
- where the boundaries lie;
- input/output format contracts.

---

## 18. Check your understanding with a few questions

You do not need to memorize the appendix. Try answering:

1. Why can the same bit pattern not be assigned one universal meaning without a type or representation rule?
2. In an 8-bit two's-complement model, how do `00000101` and `11111011` represent `+5` and `-5`?
3. Why should the two's-complement rule for signed integers not be applied directly to an IEEE 754 negative floating-point value?
4. Why may a decimal fraction such as `0.1` be representable only approximately?
5. Why does a `char` bit pattern still need a character-encoding rule before it becomes human-readable text?
6. Why should `int = 32 bits`, ASCII, and IEEE 754 not all be treated as universal C17 guarantees?

If you can explain these in your own words, you have the model this appendix is trying to build.

---

## Navigation

- [Back to P-U02: How Does a Program Remember Data and Change State?](unit-02-data-state.en.md)
- [Next Unit P-U03: How Does a Program Select and Repeat?](unit-03-control-flow.en.md)
- [繁體中文版](appendix-bit-level-data-representation.zh-TW.md)
