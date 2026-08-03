# Constitution of the 2026 Summer Preparatory Course

Version: 1.3.0  
Status: Official baseline document  
Scope: All course plans, teaching materials, handouts, slides, code examples, exercises, assignments, assessments, teacher documents, student documents, and maintenance documents in this repository

---

## Preamble

Every course design decision, teaching material, assignment, assessment, and use of AI in this course shall serve one highest purpose: the growth of students’ capabilities.

Any practice that increases product completion, document output, or teaching convenience while weakening students’ understanding, reasoning, implementation, debugging, verification, or communication shall not be adopted.

This Constitution does not protect a particular tool, document format, or instructor’s personal habits. It protects the following non-negotiable values:

- Students’ genuine opportunities to learn
- Substantive equality between the Chinese-taught and English-taught classes
- Accuracy and consistency of course materials
- The right of teachers and students to understand course requirements clearly
- The long-term maintainability, transferability, and evolution of the course
- The role of AI as a learning aid rather than a substitute for thinking

---

# Part I — General Provisions

## Article 1 — Highest Educational Purpose

The course shall not treat submitting an answer, passing tests, or completing a product as the sole definition of completion.

A learning outcome is achieved only when students can understand, explain, modify, test, debug, verify, and extend their own work.

## Article 2 — Applicability

This Constitution applies to:

1. Both the Chinese-taught and English-taught classes.
2. All instructors, teaching assistants, authors, translators, and maintainers.
3. All official content created, modified, or translated by humans or AI.
4. All official course documents stored in or published from this repository.

## Article 3 — Order of Priority

When a document or teaching design conflicts with this Constitution, this Constitution prevails.

When principles compete, the following order applies:

1. Student safety, dignity, and fairness.
2. Learning quality and genuine understanding.
3. Accuracy of knowledge.
4. Consistency between the Chinese-taught and English-taught classes.
5. Clarity and maintainability of documentation.
6. Teaching convenience and product completion.

## Article 4 — Definition of an Official Document

Any document used by teachers, teaching assistants, or students to understand the course, carry out activities, submit work, assess performance, maintain materials, or make decisions is an official document.

Internal drafts may temporarily exist in only one language, but they must be clearly marked as drafts and must not be used as official published versions.

---

# Part II — Writing and Documentation Standards

## Article 5 — Bilingual Documentation Is a Completion Requirement

Every official document must be available in both Traditional Chinese and English.

A single-language version is an incomplete draft unless it is explicitly identified as an unpublished temporary document. Only one language version may not be formally released by itself.

This requirement applies to, but is not limited to:

- READMEs and course navigation documents
- Course descriptions and syllabi
- Handouts and slides
- Classroom activities and exercises
- Assignments and project specifications
- Assessments, rubrics, and checklists
- Explanatory text for code examples
- FAQs, setup guides, and operating manuals
- Teacher, teaching-assistant, and maintainer documentation
- GitHub Issues, templates, and official process documents

## Article 6 — Substantive Equivalence Between Language Versions

The Chinese and English versions must contain the same:

- Learning objectives
- Core content
- Section structure
- Code and test data
- Assignment requirements
- Submission items
- Grading criteria
- Completion and deadline conditions
- Notes and warnings
- Version status

Translation may adapt sentence structure to the target language, but it must not add, remove, weaken, or alter substantive requirements.

## Article 7 — Synchronized Bilingual Maintenance

When an official document is modified, its counterpart in the other language must be updated within the same unit of work.

When synchronization is temporarily impossible, both versions must clearly state:

- Which version is currently authoritative
- What content is not synchronized
- The last synchronization date
- The responsible person or follow-up task

Unsynchronized status must not become permanent.

## Article 8 — Single Source of Truth

The course shall maintain a Single Source of Truth.

The Chinese and English versions are two language representations of the same course content. They must not be maintained indefinitely as independent materials that evolve separately.

Numbers, dates, grading percentages, input/output formats, code, test data, and submission requirements should be maintained through shared data or automatically verifiable mechanisms whenever practical.

## Article 9 — Every Document Must Have a Clear Purpose

Every official document must answer:

1. Who is the intended reader?
2. What should the reader know or be able to do after reading it?
3. Is the document explanatory, instructional, operational, practice-oriented, assessment-oriented, or maintenance-oriented?
4. What defines successful use or completion?

Scattered notes without a defined purpose or use case shall not replace formal documentation.

## Article 10 — Documents Must Be Independently Understandable

Official documents must provide the information needed to complete their intended task and must not rely on oral context known only to the original author.

Where appropriate, documents must state:

- Prerequisite knowledge
- Required tools
- Procedures
- Inputs and outputs
- Completion criteria
- Common errors
- Permitted and prohibited resources
- Rules for AI use

## Article 11 — Document Discoverability and Navigation Integrity

Every official document must be reachable from the repository root `README.md` through either a direct link or a semantically clear indirect navigation path.

Navigation must satisfy the following requirements:

1. The root README must provide the primary document categories and first-level entry points.
2. A subdirectory containing multiple official documents must provide a README or equivalent index that explains the directory’s purpose and links to its official documents.
3. Every level of an indirect navigation path must have a clear name and purpose; readers must not be expected to guess file paths.
4. Adding, moving, renaming, or deleting an official document requires updating the relevant READMEs, indexes, and cross-links within the same unit of work.
5. An official document must not become an orphan that cannot be discovered through the navigation system.
6. Chinese and English navigation must be substantively equivalent and must allow readers to switch between corresponding language versions.
7. Navigation depth must remain reasonable; if too many levels are required to reach a document, the information architecture must be reorganized.

Presence in version control does not by itself mean that a document has been formally incorporated into the course. A document becomes officially usable only after bilingual completion, review, and inclusion in the navigation structure.

## Article 12 — Clear and Actionable Language

Instructions must be concrete, observable, and executable.

Avoid vague directions such as “research this yourself,” “think about it,” “complete the program,” or “become familiar with the concept” when no completion state can be determined.

Activity instructions should state at least:

- What to do
- Why it is being done
- What must be submitted or demonstrated
- Which resources may be used
- What counts as completion

## Article 13 — Terminology Consistency

The course shall establish and maintain a Chinese–English terminology glossary.

The same concept shall use the same term throughout the course. Important terms should include both their Chinese and English names when first introduced, where appropriate.

Literal translations that conflict with professional conventions, create ambiguity, or cause inconsistency shall not be used.

## Article 14 — Consistent Document Structure

Documents of the same type shall use a consistent template.

Teaching materials should ordinarily include:

1. Document purpose
2. Learning objectives
3. Prerequisites
4. Core concepts
5. Appropriate visual representation
6. Minimal executable example
7. Execution-flow or reasoning explanation
8. Common errors
9. Guided practice
10. Independent practice
11. Self-check
12. AI rules or guidance
13. Unit summary

Different document types may adapt this structure to their purpose, but equivalent documents shall not change their basic organization arbitrarily.

## Article 15 — Pedagogical Writing Sequence and Student-Reading Principle

Teaching materials are not merely handouts for one class meeting. They must function as long-term learning resources that students can read independently, review, consult, and use to rebuild understanding.

Where appropriate, teaching materials should follow this instructional sequence:

> Problem or need → student prediction → visual model → core concept → syntax and code → execution trace → error diagnosis → verification and modification → summary

Pedagogical writing must follow these principles:

1. Begin with a problem, need, or observable phenomenon rather than using a syntax label or definition list as the sole entry point.
2. Establish the concept and mental model before introducing syntax; syntax must be presented as a tool for solving a problem, not isolated knowledge to memorize.
3. Where appropriate, require students to predict a path, state, output, or error before revealing execution results.
4. Every important concept must include at least one correct case, one representative incorrect case, and a verification process that can be reproduced, diagnosed, corrected, and checked again.
5. Do not provide only the correct answer; explain how to judge, how to detect a mismatch, and what evidence supports a correction.
6. AI-generated explanations, programs, or suggestions must be treated as claims requiring verification. Materials must guide students to question, test, modify, or reject them rather than treat AI output as authoritative.
7. New concepts must connect to previously learned knowledge and explain their necessity and position in the larger programming knowledge map.
8. Examples must increase in complexity gradually and must not introduce several unestablished concepts in one example without clear separation.
9. Material length must be determined by what understanding requires. Necessary explanation must not be removed merely to reduce page count, fit slides, or match one class period.
10. Materials must preserve space for student thinking; questions, predictions, and exercises must not immediately disclose complete answers in a form that cannot reasonably be skipped.

When a topic cannot use the full sequence, authors may adapt it, but must preserve four core elements: a motivating problem, concept formation, practical observation, and student verification.

## Article 16 — Code and Explanatory Text Must Correspond

Code in official documents must:

- Run in the specified environment
- Match the surrounding explanation
- Avoid unnecessary techniques that have not yet been introduced
- Clearly distinguish complete programs, fragments, pseudocode, and intentionally incorrect examples
- State expected input and output

The Chinese and English versions should ordinarily use identical code, data, and test cases. Only explanatory text, interface text, or comments may be translated where needed.

## Article 17 — Visual-First Teaching Principle

To help students form accurate mental models, official documents must provide an appropriate visual representation whenever diagrams, flowcharts, structural diagrams, memory diagrams, sequence diagrams, relationship diagrams, concept maps, state diagrams, or other visual forms would materially improve understanding. Such content must not be presented only in prose.

Visualizations must satisfy the following requirements:

1. Every visual must address a clear learning objective or question and must not serve merely as decoration.
2. The visual, explanatory text, code, inputs and outputs, and observed execution results must be mutually consistent.
3. The visual must emphasize the current core concept and avoid introducing elements that are irrelevant or have not yet been taught.
4. The visual must label the necessary nodes, relationships, directions, states, scopes, time order, or memory locations so that readers can interpret it correctly.
5. The Chinese and English versions must use the same visual structure, data, and meaning; necessary text labels may be translated.
6. A visual must not replace necessary explanation, and prose must not redundantly restate every visual element without reason; the two should complement one another.
7. When a visual alone cannot establish correctness, it must be paired with program execution, tracing, testing, or student manipulation for verification.
8. When an author judges that a topic is unsuitable for visualization, the reason must be defensible; obvious learning-supporting visuals may not be omitted merely because they are inconvenient to create.

Where appropriate, teaching materials should follow this comprehension path:

> Visual model → verbal concept → code implementation → execution observation → student verification

## Article 18 — Cognitive Load Must Be Controlled

Documents shall not require beginners to process too many new concepts at once.

They should use:

- Short paragraphs
- Clear hierarchy
- Small examples
- Staged explanations
- Data that can be checked manually
- Explicit labels for core and extension content

Visual attractiveness shall not take precedence over readability and understanding.

## Article 19 — Information Priority Levels

Documents must clearly distinguish:

- Must understand
- Must complete
- Recommended practice
- Extension exploration
- May be deferred

Not all information should appear equally important.

---

# Part III — Course and Material Design Principles

## Article 20 — Competency Orientation

Course content must correspond to observable capabilities rather than only to chapter titles or syntax lists.

Every major unit should enable students to:

- Explain a concept
- Predict behavior
- Implement functionality
- Test results
- Diagnose problems
- Modify requirements
- Compare approaches
- Explain verification methods

## Article 21 — Concepts Before Syntax

Teaching materials must first answer:

1. Why is this concept needed?
2. What problem does it solve?
3. How does it affect program state or control flow?
4. How can students verify that their understanding is correct?

Only after this understanding is established should syntax be introduced.

## Article 22 — Knowledge Dependencies Must Be Explicit

A new concept must not depend on knowledge that has not been taught, explained, or explicitly identified as prerequisite knowledge.

Every unit should identify:

- Prerequisite concepts
- New concepts introduced in the unit
- Content that may be deferred
- Its relationship to later units

## Article 23 — Learning Activities Must Include a Complete Cycle

Major learning activities should ordinarily include:

> Understand the requirement → establish expectations → design an approach → implement → test → debug → modify → run regression verification → explain and reflect

Students must not be asked only to complete a first program version without verification or modification.

## Article 24 — Prediction Before Execution

Where appropriate, students should record expected results before running code, viewing an answer, or using AI.

Predictions may include:

- Output
- Variable state
- Control flow
- Function-call order
- Error category
- Test results

A prediction need not be correct initially. Its value is in allowing students to compare expectation with observed behavior.

## Article 25 — Errors Are Official Teaching Content

Every important concept should include controlled, reproducible, and diagnosable error cases.

An error case should explain at least:

- The observed symptom
- Possible causes
- Diagnostic steps
- Correction
- Regression testing after correction

Materials must not provide only correct answers and final versions.

## Article 26 — Example Size Must Be Minimized

Examples designed to teach a new concept should use the smallest reasonable scale that demonstrates that concept.

When an example contains several unrelated concepts, it should be split into smaller cases or clearly identify which parts students are not yet expected to understand.

## Article 27 — Multiple Reasonable Solutions Are Allowed

Unless a learning objective requires a specific technique, a single implementation must not be treated as the only correct solution.

Materials and assessments must distinguish:

- Required constraints
- Recommended practices
- Style preferences
- Acceptable alternatives

## Article 28 — Competency Maturity

The course shall describe capabilities using maturity levels rather than only “taught” or “not taught.”

Maturity levels shall include at least:

- L1: recognize
- L2: complete with guidance
- L3: independently complete familiar tasks
- L4: complete under modified requirements or in a new context
- L5: compare, explain, and evaluate multiple approaches

The preparatory course does not require every capability to reach the same maturity level.

---

# Part IV — Equivalence Between Chinese-Taught and English-Taught Classes

## Article 29 — Shared Core Outcomes

The Chinese-taught and English-taught classes must achieve the same core capability outcomes.

Instructional hours, pacing, and language support may differ, but the English-taught class must not reduce technical depth, remove core activities, or simplify assessment standards merely because instruction occurs in English.

## Article 30 — Delivery Pace May Differ

The two classes may use different:

- Unit segmentation
- Time allocation
- Language support
- Number of examples
- Proportion of oral activities

However, a traceability matrix must demonstrate that both classes ultimately cover the same core capabilities.

## Article 31 — Language Difficulty Must Not Be Misclassified as Technical Weakness

English fluency must not replace programming competence in assessment.

Without reducing technical expectations, the course may provide:

- Terminology lists
- Sentence frames
- Bilingual keywords
- Diagrams
- Written explanation time
- Longer reading time

## Article 32 — The English-Taught Class Must Not Be a Literal Translation of the Chinese Class

The English-taught class should be designed for English-medium instruction through:

- Terminology scaffolding
- Adjusted explanation pacing
- Appropriate classroom interaction
- Visual support
- Written and oral communication support

These adaptations must not alter the core content or capability standards.

---

# Part V — Principles for AI Use

## Article 33 — AI Must Not Replace Student Thinking

AI may support learning, but it must not replace students in:

- Understanding requirements
- Initial design
- Output prediction
- Test creation
- Debugging judgment
- Result verification
- Oral explanation

## Article 34 — Students Must Retain Pre-AI Work

Before using AI in important activities, students should preserve their own:

- Understanding
- Predictions
- Initial design
- First program version
- Test cases
- Error hypotheses

AI-assisted results must not erase all evidence of prior thinking.

## Article 35 — AI Suggestions Must Be Verified

Before adopting an AI suggestion, students must:

1. Explain the suggestion.
2. Create tests capable of determining whether it is correct.
3. Verify it through execution or reasoning.
4. Compare the situation before and after use.
5. Explain why the suggestion was accepted, modified, or rejected.

“AI says it is correct” is not evidence.

## Article 36 — AI Rules Must Vary by Activity

The course must not rely on a single course-wide rule that merely says “AI allowed” or “AI prohibited.”

Each activity should specify according to its learning objective:

- When AI may be used
- What may be asked
- What may not be asked
- What must be retained
- How verification must occur
- How use must be disclosed

## Article 37 — Author Responsibility for AI-Generated Content

When AI is used to generate teaching materials, code, translations, tests, diagrams, or assessment content, the author or maintainer remains responsible for:

- Accuracy
- Consistency
- Age and level appropriateness
- Bilingual equivalence
- Executability
- Copyright and licensing
- Avoiding untaught concepts

“Generated by AI” is not a justification for unreviewed content.

---

# Part VI — Implementation, Testing, and Debugging

## Article 38 — Implementations Must Be Verifiable

Every implementation activity must have observable success conditions.

At minimum, it should provide:

- Expected input
- Expected output or state
- Normal cases
- Boundary cases
- Error or exceptional cases
- Regression tests

## Article 39 — Testing Is Part of Design

Students should create tests before or during implementation rather than entering arbitrary values only after the program is complete.

A test case should explain its purpose rather than merely provide numbers.

## Article 40 — Debugging Must Be Evidence-Based

The debugging process should include:

1. Reproduce the problem.
2. Record expected and actual results.
3. Propose a testable hypothesis.
4. Narrow the problem scope.
5. Modify one suspected cause.
6. Re-run the original tests and regression tests.

Random modification until the program passes is not an acceptable standard method.

## Article 41 — Requirement Modification Is Necessary

Major programming activities should include at least one requirement change.

Students must be able to identify:

- Which designs are affected
- Which code must change
- Which original tests should continue to pass
- Which new tests must be added

## Article 42 — Versions and History Must Be Traceable

Important activities should preserve:

- Initial version
- Defective version
- Corrected version
- Requirement-change version
- Differences before and after AI suggestions

Version control, file copies, change logs, or other reasonable methods may be used.

---

# Part VII — Assignments and Assessment

## Article 43 — Assessment Must Correspond to Competencies

Every assessment must correspond explicitly to at least one competency and maturity level.

The course must not assess only memorization, syntax transcription, or a single output merely because such evidence is easy to grade.

## Article 44 — A Single Piece of Evidence Cannot Establish Full Competence

The following outcomes cannot independently prove competence:

- Successful compilation
- Correct output
- Passing an Online Judge
- Positive AI evaluation
- Submission of a complete program
- Memorization of a definition

They should be combined with explanation, modification, testing, debugging, tracing, or oral verification.

## Article 45 — Assignments Must Permit Learning to Occur

Assignments must not serve only to rank students. They must also provide:

- Space for attempts
- Error feedback
- Opportunities to revise
- Reflection requirements
- Defined resource boundaries

## Article 46 — Grading Criteria Must Be Published in Advance

Formal assessments must provide a rubric or equivalent explanation.

Criteria should distinguish:

- Understanding
- Design
- Implementation
- Testing
- Debugging
- Modification
- Explanation
- AI verification

## Article 47 — Assessment Methods Should Be Diverse

The course may use:

- Programming implementation
- Oral explanation
- Program tracing
- Error diagnosis
- Test design
- Requirement modification
- Code review
- Reflection records

A single question type must not carry all competency judgments.

## Article 48 — Remediation Must Target Capability Gaps

When a student has not reached the standard, remediation should target the missing capability rather than merely require resubmission of the same answer.

Remediation may include:

- Tracing with new input
- Modifying a new requirement
- Explaining an error cause
- Creating additional tests
- Comparing two approaches
- Verifying an AI suggestion

---

# Part VIII — Maintenance, Review, and Evolution

## Article 49 — Changes Must Be Traceable

Changes to official documents should record:

- Version
- Date
- Change summary
- Impacted scope
- Bilingual synchronization status

## Article 50 — Major Changes Require Constitutional Review

The following changes require review for constitutional compliance:

- Adding or removing core content
- Changing learning objectives
- Changing assessment methods
- Changing AI-use rules
- Changing equivalence between classes
- Changing official document structure
- Introducing a teaching tool or platform

## Article 51 — The Course Must Be Cleaned Regularly

Course maintenance should regularly review:

- Duplicate documents
- Broken links
- Outdated content
- Bilingual divergence
- Unused materials
- Activities that cannot be verified
- Content outside the current scope

## Article 52 — Constitutional Amendment Procedure

Amending this Constitution requires:

1. Explaining the reason for the amendment.
2. Identifying affected articles.
3. Updating both language versions synchronously.
4. Updating the version number.
5. Reviewing whether existing official documents require adjustment.
6. Preserving a change record.

---

# Part IX — Final Provisions

## Article 53 — Minimum Non-Negotiable Conditions

The following conditions must not be omitted because of time limits, tool limitations, or teaching convenience:

1. Official documents are complete in both languages.
2. Core capabilities are equivalent between the Chinese-taught and English-taught classes.
3. Major concepts establish understanding before syntax is introduced.
4. Major activities include prediction, testing, and verification.
5. AI suggestions are verified by students.
6. Code and explanatory content are accurate and consistent.
7. Assessment corresponds to capability rather than only answers.
8. Students can explain and modify their own work.

## Article 54 — Effect

This Constitution takes effect upon formal publication and applies to all content created or modified afterward.

All authors, instructors, teaching assistants, and maintainers must check constitutional compliance before submitting official content.

---

## Version History

### 1.3.0

- Added the pedagogical writing sequence and student-reading principle.
- Required materials to begin from problems and needs, establish concepts and mental models before syntax, and support long-term independent reading.
- Added requirements for prediction, error cases, AI-suggestion verification, knowledge connections, and protected thinking space.
- Renumbered subsequent articles.

### 1.2.0

- Added the official-document discoverability and navigation-integrity article.
- Required every official document to be reachable from the root README through a clear navigation chain.
- Required indexes and cross-links to be updated when official documents are added, moved, renamed, or deleted.
- Renumbered subsequent articles.

### 1.1.0

- Added the Visual-First Teaching Principle.
- Required appropriate visual representation whenever visualization would materially improve understanding.
- Defined consistency requirements among diagrams, code, data, tests, and bilingual versions.
- Added the comprehension path: “Visual model → verbal concept → code implementation → execution observation → student verification.”

### 1.0.0

- Established the first official Course Constitution.
- Defined requirements for bilingual documentation, course equivalence, material structure, competency orientation, AI use, testing and debugging, assessment, and maintenance.
