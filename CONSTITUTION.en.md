# Constitution of the 2026 Summer Preparatory Course

Version: 1.2.0  
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

## Article 15 — Code and Explanatory Text Must Correspond

Code in official documents must:

- Run in the specified environment
- Match the surrounding explanation
- Avoid unnecessary techniques that have not yet been introduced
- Clearly distinguish complete programs, fragments, pseudocode, and intentionally incorrect examples
- State expected input and output

The Chinese and English versions should ordinarily use identical code, data, and test cases. Only explanatory text, interface text, or comments may be translated where needed.

## Article 16 — Visual-First Teaching Principle

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

## Article 17 — Cognitive Load Must Be Controlled

Documents shall not require beginners to process too many new concepts at once.

They should use:

- Short paragraphs
- Clear hierarchy
- Small examples
- Staged explanations
- Data that can be checked manually
- Explicit labels for core and extension content

Visual attractiveness shall not take precedence over readability and understanding.

## Article 18 — Information Priority Levels

Documents must clearly distinguish:

- Must understand
- Must complete
- Recommended
- Extension exploration
- May be skipped for now

Not all information shall be presented as equally important.

## Article 19 — Accuracy and Source Responsibility

Technical facts, tool instructions, version information, and rules in official documents must be verified.

Content likely to change over time must state its version, date, or applicable environment. External material must be traceable to an adequate source.

AI-generated content shall not be presumed correct merely because it is fluent.

## Article 20 — Version and Change Traceability

Important documents shall preserve:

- Version number or status
- Last updated date
- Summary of major changes
- The corresponding version in the other language

Major changes should retain their decision history through Git commits, Issues, or Pull Requests.

---

# Part III — Curriculum Content and Teaching Standards

## Article 21 — Understanding Before Completion

Successful execution, passing automated tests, or producing a polished artifact does not by itself demonstrate understanding.

The course must enable students to explain:

- What problem is being solved
- What the data means
- How the solution is decomposed
- How the program executes
- Why the result is reasonable
- How an error is located
- How the solution changes when requirements change

## Article 22 — Students Retain Responsibility for Thinking

Teachers, classmates, search engines, and AI may assist, but they shall not replace students’ understanding of and responsibility for their own work.

Code that a student cannot explain, modify, test, or verify shall not be treated as a completed learning outcome.

## Article 23 — Think First, Implement Second, Verify Last

Programming activities should ordinarily follow this sequence:

1. Understand the problem.
2. Identify input and output.
3. Decompose the problem.
4. Express the solution in natural language, a table, a flowchart, or pseudocode.
5. Build the smallest executable version.
6. Create test data.
7. Compare expected and actual results.
8. Correct errors.
9. Improve program structure.
10. Explain and reflect.

“Obtain a complete answer first and infer the reasoning afterward” shall not be designed as the main learning process.

## Article 24 — Progressive Learning

New concepts must build on abilities that can reasonably be confirmed.

Teaching shall:

- Introduce a limited number of new concepts at a time
- Begin with minimal examples
- Teach individual concepts before integration
- Ask students to predict before execution
- Begin with modification before full construction from scratch
- Address normal cases before boundaries and exceptions
- Establish correctness before quality improvement

Frameworks, abstraction layers, or libraries that students cannot yet understand shall not be introduced merely to increase project scale.

## Article 25 — Examples Must Serve Concepts

Every example must have a clear instructional purpose and identify:

- The concept to observe
- What is newly introduced
- Common misunderstandings
- Modifications that can verify understanding
- How it can be extended into practice

Entertainment or visual effects shall not obscure the core concept.

## Article 26 — Reading, Modification, and Debugging Are Equal Skills

The course shall not train students only to write programs from a blank file.

It must provide sufficient opportunities to:

- Read existing programs
- Predict output
- Trace variables
- Complete missing code
- Locate errors
- Modify requirements
- Compare solutions
- Design tests
- Explain trade-offs

## Article 27 — Errors Are Official Teaching Materials

Syntax errors, type errors, runtime errors, logic errors, boundary errors, and incorrect AI responses may all be used as formal teaching materials.

Students must learn to:

1. Read error messages.
2. Reproduce a problem.
3. Narrow its scope.
4. Form a hypothesis about its cause.
5. Test the hypothesis.
6. Explain the reason for the correction.

## Article 28 — Testing and Verification Are Core Skills

Students shall not accept an answer merely because it came from a teacher, textbook, website, or AI system.

The course must require students to:

- Calculate simple cases manually
- Create normal cases
- Create boundary cases
- Create exceptional cases where appropriate
- Compare expected and actual results
- Check assumptions about input
- Explain why the current result should be trusted

## Article 29 — Multiple Reasonable Solutions Are Permitted

Students may use solutions different from the example when those solutions satisfy the specification, current learning scope, safety requirements, and readability expectations.

Marks shall not be deducted solely because program structure, variable naming, or step order differs from a model answer.

Assessment should focus on:

- Correctness
- Understanding
- Readability
- Testability
- Ability to modify
- Ability to explain

## Article 30 — Products Serve Learning

Projects and artifacts are vehicles for integrating abilities; they are not the ultimate purpose of the course.

Teachers, frameworks, libraries, or AI shall not complete core parts that students do not understand merely so that a large project can be finished.

Every project should be decomposable into units that students can understand, implement, test, modify, and explain.

## Article 31 — The Curriculum Must Be Continuous

Every unit should state:

- Which existing abilities it uses
- Which new abilities it adds
- How those abilities will be used later
- Which advanced topics are intentionally deferred

The curriculum shall not become a collection of disconnected activities without cumulative development.

## Article 32 — Preserve Flexibility Without Sacrificing the Core

Teachers may adapt the following according to student readiness, available time, and classroom response:

- Example contexts
- Number of exercises
- Supporting explanations
- Activity order
- Extension content
- Tools used

They may not arbitrarily lower common learning objectives, understanding requirements, bilingual consistency, or assessment fairness.

---

# Part IV — AI Use Standards

## Article 33 — Role of AI

AI is an aid for teaching, learning, feedback, debugging, and content maintenance. It is not a replacement for student thinking, teacher judgment, or content review.

## Article 34 — Appropriate Uses of AI

AI may be used to:

- Explain concepts
- Provide staged hints
- Help interpret error messages
- Generate or review test cases
- Compare alternative solutions
- Question student reasoning
- Assist with translation and expression
- Help teachers draft materials

All results must still be understood and verified by the user.

## Article 35 — Learning Behaviors AI Must Not Replace

AI shall not replace:

- Initial comprehension of the task
- Problem decomposition
- Design of the core solution
- Basic implementation
- Tracing of execution
- Diagnosis of error causes
- Verification of test results
- Explanation of learning outcomes

Teachers may impose stricter limits according to the objective of a unit.

## Article 36 — Transparency of AI Use

When AI is permitted in an assignment, assessment, or activity, the document must state:

- Permitted scope
- Prohibited uses
- Whether prompts or conversation records must be retained
- How students must explain whether they accepted or rejected AI suggestions
- How violations are determined

A vague statement such as “AI may be used appropriately” is not sufficient by itself.

## Article 37 — AI-Generated Content Must Be Reviewed

Official material generated or translated by AI must be reviewed by a human for:

- Technical correctness
- Instructional suitability
- Substantive equivalence between Chinese and English
- Natural language quality
- Difficulty and prerequisites
- Accidental disclosure of assignment solutions
- Unfairness or misleading content

Unreviewed AI-generated content shall not be published as official course material.

---

# Part V — Assessment and Fairness Standards

## Article 38 — Assessment Measures Ability, Not Output Alone

Assessment shall not use final output or automated-test results as the sole measure of learning.

Major assessments must include at least one form of understanding check, such as:

- Program explanation
- Execution tracing
- Error location
- Requirement modification
- Test design
- Solution comparison
- Oral explanation
- Reflection record
- Explanation of AI use

## Article 39 — Substantive Equality Between the Two Classes

The Chinese-taught and English-taught classes must have the same:

- Learning objectives
- Core content
- Workload
- Difficulty
- Assessment methods
- Rubrics
- Access to resources
- AI rules

Differences in instructional language shall not result in lower expectations, fewer resources, or a disadvantage in assessment for either class.

## Article 40 — Assessment Rules Must Be Public

Before an assessment begins, students must know:

- Its objectives
- Permitted resources
- AI restrictions
- Required submissions
- Grading components
- Completion criteria
- Late and resubmission policies
- Academic-integrity requirements

Hidden criteria announced only after submission shall not affect grades.

## Article 41 — Accessibility and Respect

Documents and activities should avoid preventing students from demonstrating genuine learning because of language, cultural background, equipment differences, or unnecessary technical barriers.

Humiliation, public comparison, or punishment of normal mistakes shall not be used as teaching methods.

Students’ questions, mistakes, and learning records shall be treated respectfully and protected with appropriate privacy where necessary.

---

# Part VI — Maintenance, Governance, and Amendment

## Article 42 — Materials Must Be Transferable to Other Teachers and Maintainers

Official materials shall not depend on implicit knowledge held only by the original author.

Important units should preserve:

- Instructional purpose
- Prerequisite abilities
- Suggested pacing
- Rationale for activity design
- Common student difficulties
- Elements that may be adapted and elements that must not be sacrificed

## Article 43 — Review Before Major Changes

Before adding or substantially revising a document, check at least:

1. Does it map to a clear learning objective?
2. Does it fit students’ current level?
3. Does it introduce too many new concepts?
4. Does it preserve student responsibility for thinking?
5. Can it check genuine understanding?
6. Can students bypass learning by copying an answer?
7. Are the AI rules explicit?
8. Does it include testing, modification, reading, or debugging?
9. Are the Chinese and English versions synchronized and substantively equivalent?
10. Does it distinguish core and extension content?
11. Does it define completion clearly?
12. Can another teacher use and maintain it independently?
13. Has visual content been provided where appropriate, or is there a defensible reason not to provide it?
14. Are visuals consistent with the prose, code, data, and actual execution?
15. Is the document linked from the root README through a direct or indirect navigation path?
16. After adding or moving the document, have the relevant READMEs, indexes, and cross-links been updated?

## Article 44 — Amendment Principles

This Constitution may evolve, but its protected values shall not be weakened for short-term convenience.

Every amendment must:

- Update both language versions together
- Explain the reason for the change
- Preserve a change record
- Check the impact on existing materials
- Create a migration or correction plan where necessary

## Article 45 — Resolving Unspecified Conflicts

When this Constitution does not explicitly resolve a situation, ask in order:

1. Which decision better protects genuine student learning?
2. Which decision is fairer and avoids language-based disadvantage?
3. Which decision is more accurate, transparent, and verifiable?
4. Which decision is easier for future teachers and students to understand?
5. Which decision prevents AI, tools, or products from replacing core abilities?

## Article 46 — Supreme Test

Every course decision shall ultimately be tested against this question:

> Does this design make students more capable of understanding, explaining, implementing, modifying, debugging, testing, verifying, and extending what they have learned?

When the answer is no, the design shall not be adopted, even when it is faster, more visually impressive, or easier to complete.