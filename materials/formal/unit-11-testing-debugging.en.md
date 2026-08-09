# Formal Unit F-U11: How Can Programs Be Tested, Diagnosed, and Improved Systematically?

Version: 1.1.0  
Status: Official student material  
Last updated: 2026-08-09  
Corresponding Chinese version: [正式單元 F-U11：如何系統化地測試、診斷與改善程式？](unit-11-testing-debugging.zh-TW.md)

We have actually been testing programs throughout the course:

- P-U03 used 99, 100, and 101 to examine condition boundaries.
- F-U03 used the final legal index to expose out-of-bounds access.
- F-U08 tested allocation failure and ownership behavior.
- F-U09 used malformed records, EOF, and overlong lines to test file flow.

Now gather those habits into one larger question:

> After a program produces the correct output for one input, what additional evidence gives us reason to trust that it satisfies the requirement?

This Unit does not introduce a button that can “prove the whole program correct.” It builds a repeatable evidence workflow.

---

## 1. One Successful Case Proves Only That One Case

Requirement:

> A score must be between 0 and 100. Scores 60 and above produce `Pass`; other valid scores produce `Try again`.

Testing only:

```text
80 → Pass
```

says nothing about:

```text
59?
60?
0?
100?
-1 or 101?
```

The first testing step is therefore not “pick a few random numbers.” It is to derive behavior classes from the requirement.

---

## 2. Derive Test Cases Directly from the Requirement

| Type | Input | Expected result |
|---|---:|---|
| ordinary pass | 80 | Pass |
| below pass boundary | 59 | Try again |
| pass boundary | 60 | Pass |
| minimum valid | 0 | Try again |
| maximum valid | 100 | Pass |
| invalid low | -1 | Invalid |
| invalid high | 101 | Invalid |

For every row, you should be able to answer:

> Which requirement or boundary is this case checking?

That is the core of **testing**: execute a program or component and compare the actual result with an expected result defined in advance.

If the expected result is rewritten only after seeing what the program printed, much of the test's value is lost.

---

## 3. A Failed Test Shows a Mismatch, Not Yet Its Cause

Suppose the code is:

```c
int is_valid_score(int score) {
    return score > 0 && score < 100;
}
```

Tests reveal:

```text
0   → false, but the requirement says valid
100 → false, but the requirement says valid
```

We now know that implementation and requirement disagree, but diagnosis is not finished.

**Debugging** looks for the cause of the mismatch.

A useful hypothesis is:

> The condition uses `>` and `<`, so it excludes the inclusive boundaries 0 and 100.

That is more useful than “the program is weird” because it can be checked, disproved, and connected to a specific change.

---

## 4. A Repeatable Debugging Cycle

Use this pattern:

```text
reproduce
→ find the first mismatch
→ form a cause hypothesis
→ design an experiment that distinguishes hypotheses
→ observe evidence
→ make the smallest necessary correction
→ rerun relevant tests
```

If a large application's final average is wrong, do not begin by rewriting every module.

Narrow the path:

```text
Were Student records parsed correctly?
Is the StudentList state correct?
Is count correct?
Does the average function work by itself?
```

The goal is to find the **first place where actual state begins to diverge from expected state**.

---

## 5. A Bug Report Should Let Another Person Reproduce the Problem

“The program is broken” is not useful evidence.

Record at least:

- version or commit;
- build/run steps;
- input or interaction steps;
- expected result;
- actual result;
- whether it reproduces consistently;
- relevant warnings, error messages, or a minimal reproducer.

The more reliably a problem can be reproduced, the easier it is to eliminate unrelated explanations.

---

## 6. Fixing the Failing Case Is Not the End

Suppose:

```c
score > 0 && score < 100
```

becomes:

```c
score >= 0 && score <= 100
```

Of course, retest 0 and 100.

But also rerun:

```text
80
59
60
-1
101
```

This is **regression testing**: after a change, confirm that behavior which should remain unchanged still works.

Every fix should therefore ask:

> Which cases are intentionally changing, and which previously correct cases could my change accidentally disturb?

---

## 7. Verification and Validation Ask Questions at Different Levels

Suppose the program perfectly implements this specification:

```text
0–100 valid
60 and above Pass
```

### Verification

asks:

> Does the implementation conform to the defined specification?

Tests, code review, interface checks, and compiler diagnostics can all contribute verification evidence.

### Validation

asks one level higher:

> Does this specification actually solve the user's real problem?

If the school rule is really “70 is passing,” then a perfect implementation of a 60-point threshold is still the wrong product.

So:

```text
Verification: did we build according to the specification?
Validation: is this the right specification for the intended need?
```

Both matter, but one cannot replace the other.

---

## 8. The Test Itself Can Be Wrong

Suppose someone calculates an expected average incorrectly and places that wrong number in the test table.

A correct program may then appear to fail.

Keep three layers separate:

```text
requirement
→ expected result
→ actual program result
```

Any layer can contain a mistake.

When actual and expected differ, do not automatically assume the code is wrong. First make sure the expectation really follows from the correct requirement.

---

## 9. Refactoring Uses Existing Tests to Protect External Behavior

Original code:

```c
if (score >= 0) {
    if (score <= 100) {
        return 1;
    }
}
return 0;
```

Refactored:

```c
return score >= 0 && score <= 100;
```

If the goal is only to improve structure while required observable behavior remains the same, this is **refactoring**.

“Looks equivalent” should not be the only evidence.

The tests that were trusted before refactoring should run again afterward. They now protect behavior that is *not supposed to change*.

---

## 10. Code Review Should Make Claims That Can Be Checked

Compare:

```text
This code is ugly.
```

with:

```text
This loop uses i <= length, so when length is 5 it reaches values[5].
The final legal index is 4. Change the condition to i < length and add
boundary tests for lengths 0, 1, and 5.
```

The second review is useful because it contains:

```text
location
→ risk
→ reason
→ verifiable change
```

Code review can reuse every model built earlier: initialization, bounds, lifetime, ownership, failure contracts, complete input, and module dependencies.

---

## 11. Independent Practice: Produce a Reproducible Debugging Record

Choose one defect from an earlier Unit and create:

1. one clear requirement statement;
2. a minimal reproducer or input;
3. expected and actual results;
4. at least two possible cause hypotheses;
5. an experiment that distinguishes the hypotheses;
6. the root cause;
7. the smallest correction;
8. a regression-test table;
9. one sentence explaining why the corrected version deserves more trust than before.

Then identify which evidence contributes to verification and whether additional validation is needed to know that the requirement itself is appropriate.

---

## 12. Change the Requirement: Raise the Passing Threshold from 60 to 70

Do not change the code first.

First identify which expectations change:

```text
60: Pass → Try again
69: Try again
70: Pass
100: still Pass
0: still Try again
-1 and 101: still Invalid
```

Then modify the implementation.

Finally run both:

- cases whose expected result intentionally changed;
- regression cases whose expected result should remain unchanged.

This order prevents the anti-pattern “change the code first, then edit the tests to match whatever it now prints.”

---

## 13. Optional: Let AI Challenge Your Evidence Chain

You may skip this section completely.

Without any tool first, explain:

> What is the difference between a failed test and a bug's root cause? What different questions do verification and validation answer?

If you want another check, give an AI tool your debugging hypothesis and ask for another possible cause that could explain the same observation, then design an experiment to distinguish the two. No fixed prompt is required, and you do not need to save or submit the conversation.

The AI suggestion is still only a hypothesis; reproducible evidence decides whether it survives.

---

## 14. Before Leaving This Unit, Make Sure You Can Trace from Requirement to Evidence

Answer directly:

- Why can one successful output not establish the whole requirement?
- Where should a test's expected result come from?
- How is a test failure different from the root cause found during debugging?
- What makes a debugging hypothesis easy to test or disprove?
- Why are regression tests needed after the failing case is fixed?
- What two things are compared during verification, and what two things are compared during validation?
- Why must expected test results themselves be reviewed?
- Why does refactoring need an already trustworthy test set?

If the answers are only definitions, choose a real defect and draw the entire evidence chain beginning with the requirement.

---

## 15. Chapter Wrap-Up

The first ten formal Units established many programming rules. F-U11 organizes the question “how do we know we actually followed them?” into a method.

Trust does not come from one success. It comes from a chain where **requirements, expected results, tests, reproducible failures, testable hypotheses, minimal corrections, and regression evidence all connect.**

The final Unit does not introduce another isolated C syntax topic. It places the earlier data model, pointers, dynamic memory, files, modules, and testing into one small application. The challenge is to keep responsibilities and evidence understandable even when several concepts operate at the same time.

## Navigation

- [Previous Unit: Modular Programming](unit-10-modular-programming.en.md)
- [Next Unit: Integrated Application](unit-12-integrated-application.en.md)
- [Formal-Course Index](README.en.md)
- [繁體中文版](unit-11-testing-debugging.zh-TW.md)
