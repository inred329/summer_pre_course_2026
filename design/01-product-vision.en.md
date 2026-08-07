# Instructional Product Vision

Version: 0.1.1  
Status: Revisable planning model  
Corresponding Chinese version: `01-product-vision.zh-TW.md`

## Document Purpose

This document defines the educational problem, target audience, core value, and definition of success shared by the 2026 Summer C Programming Preparatory Course and the subsequent 16-week formal course.

It provides planning context for the requirements map, competency map, scope boundaries, delivery plan, and teaching-material design. It must remain consistent with the Constitution, the official learning and assessment policy, and approved design standards.

## 1. Educational Problem to Solve

When beginners enter a formal programming course, they often face several sources of cognitive load at the same time:

- They are unfamiliar with the compilation and execution model of programs.
- They are unfamiliar with the development environment, input/output, and error messages.
- They have not yet developed the habit of decomposing problems into executable steps.
- They may treat programming as syntax memorization or answer assembly.
- They may form disconnected understandings of variables, control flow, and functions.
- They lack experience reading, tracing, testing, modifying, and debugging programs.
- When they use AI or other external assistance, they may bypass understanding, reasoning, and verification.
- Different instructional languages and contact hours may create learning gaps between the Chinese-taught and English-taught classes.

The course system must therefore solve more than “students do not know C.” It must address the fact that students do not yet possess a stable mental model for learning programming.

## 2. Product Vision Statement

For beginners who are about to begin university-level programming study, provide a continuous learning system that uses C as the implementation medium and organizes programming around data and variables, control flow, and functions and problem decomposition, while integrating the execution model, input/output, testing, debugging, and responsible verification of any adopted external assistance.

The preparatory course delivers the minimum viable capabilities needed to begin formal study. The 16-week formal course then develops programming capability that students can understand, implement, test, modify, explain, and transfer.

## 3. Target Audience

Primary audience:

- Students who are about to take an introductory university programming course.
- Beginners who may have no prior programming experience.
- Students who need the same core content delivered in either Chinese or English.

Secondary audience:

- Instructors.
- Teaching assistants.
- Future maintainers or instructors who take over the materials.

## 4. Core Capability Model

The course initially organizes programming knowledge around three core pillars:

### 4.1 Data and Variables

Students understand how programs represent, store, receive, transform, and output data.

### 4.2 Control Flow

Students understand how programs choose their next action through sequence, selection, and repetition.

### 4.3 Functions and Problem Decomposition

Students understand how to decompose larger problems into reusable units with clear responsibilities, inputs, and outputs.

The following cross-cut all three pillars:

- Program execution model.
- Input and output.
- Expressions and state tracing.
- Program reading and explanation.
- Testing and verification.
- Debugging and modification.
- Responsible understanding and verification when external assistance is adopted.

## 5. Role of the Preparatory Course

The preparatory course is not a compressed version of the first several weeks of the formal course, nor is it intended to cover a large amount of C syntax in advance.

It acts as the Minimum Viable Preparation and should:

- Reduce tool and environment barriers at the start of the formal course.
- Establish a basic mental model of sequential execution and changing program state.
- Introduce the three core pillars and their relationships.
- Establish basic workflows for reading, predicting, modifying, testing, and debugging programs.
- Establish habits that prevent students from replacing learning with unverified externally generated answers.
- Allow instructors to identify major learning risks before the formal course begins.

## 6. Role of the Formal Course

The 16-week formal course should fully develop students’ ability to solve basic problems with C and enable them to:

- Analyze problems and define input, processing, and output.
- Select suitable ways to represent data.
- Express algorithms with control flow.
- Decompose and organize programs with functions.
- Read, trace, test, debug, and modify programs.
- Explain design choices and the basis for verification.
- When choosing to adopt AI or another external suggestion, understand it, verify it, and remain responsible for the result.
- Build a foundation for later study in data structures, object-oriented programming, algorithms, and other computing courses.

AI use is optional. Non-use does not reduce Unit completion, classroom participation, or assessment outcomes.

## 7. Definition of Success

Success is not determined solely by how much syntax is covered or how many artifacts are completed.

Evidence of success must include at least the following:

1. Students can explain in their own words how a program executes.
2. Students can trace changes in data and variables during execution.
3. Students can select basic control-flow structures for a problem.
4. Students can decompose a problem into reasonable functions.
5. Students can read and modify existing programs rather than only starting from a blank file.
6. Students can design tests and explain why results should be trusted.
7. Students can use error messages and observed behavior to locate problems.
8. When students adopt AI or another external suggestion, they can identify the adopted assistance and explain how they verified it; non-use does not affect success.
9. The Chinese-taught and English-taught classes meet the same standards for shared core capabilities.
10. Other instructors or teaching assistants can understand, deliver, and maintain the materials.

## 8. Non-Goals

The course system does not prioritize:

- Covering the full C language in the preparatory course.
- Replacing core capability practice with large or visually impressive projects.
- Having students memorize syntax details without being able to explain execution results.
- Allowing AI, model answers, or frameworks to complete core work students do not understand.
- Creating different core capability standards because the Chinese-taught class has two additional hours.
- Omitting testing, debugging, modification, or explanation activities in order to move faster.

## 9. Key Constraints

- English preparatory class: five 2-hour sessions, totaling 10 hours.
- Chinese preparatory class: four 3-hour sessions, totaling 12 hours.
- Formal course: sixteen 3-hour weeks, totaling 48 hours.
- The preparatory and formal courses must connect without unnecessary duplication.
- Chinese and English documents must remain synchronized and substantively equivalent.
- Every capability requirement must ultimately map to observable acceptance evidence.

## 10. Product Decisions Still to Be Confirmed

The following remain for later requirements and scope decisions:

- Whether the formal course covers arrays, strings, pointers, structures, files, and recursion, and at what depth.
- Whether each preparatory-course pillar should reach awareness, guided implementation, or independent implementation.
- The standardized development environment, compiler, and submission method.
- Whether the preparatory course uses formal assessment or primarily diagnostic evidence.
- How the additional two hours in the Chinese-taught class should be divided among reinforcement, practice, diagnosis, and extension.
