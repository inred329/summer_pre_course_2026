# Constitution of the 2026 Summer Preparatory Course

Version: 2.0.0-draft  
Status: Amendment draft; does not yet replace the official 1.3.0 baseline  
Primary audience: Course designers, instructors, and maintainers  
Scope: All official course designs, student materials, instructor documents, assessment documents, code examples, review documents, and publication processes in this repository

---

## Preamble

Every course design decision, teaching material, assignment, assessment, and use of tools shall serve one highest purpose: the growth of students’ capabilities.

Any practice that increases product completion, document output, or teaching convenience while weakening students’ understanding, reasoning, implementation, debugging, verification, or communication shall not be adopted.

This Constitution does not protect a particular tool, document format, or instructor habit. It protects these non-negotiable values:

- Students’ genuine opportunities to learn
- Student safety, dignity, and fairness
- Readable and technically correct student materials
- Substantive equality between the Chinese-taught and English-taught classes
- The right of teachers and students to understand course requirements clearly
- The long-term maintainability, transferability, and evolution of the course
- The role of AI as a learning aid rather than a substitute for thinking

# Part I — Highest Principles and Governance

## Article 1 — Highest Educational Purpose

The course shall not treat submitting an answer, passing tests, or completing a product as the sole definition of completion.

A learning outcome is achieved only when students can understand, explain, modify, test, debug, verify, and extend their own work.

## Article 2 — Applicability

This Constitution applies to:

1. Both the Chinese-taught and English-taught classes.
2. All instructors, teaching assistants, authors, translators, and maintainers.
3. All official content created, modified, or translated by humans or AI.
4. All documents published, referenced, or used by this repository to make official course decisions.

Temporary notes and working drafts may lack official force, but they must be clearly marked and must not replace official policies or published content.

## Article 3 — Order of Priority

When a document or teaching design conflicts with this Constitution, this Constitution prevails.

When principles compete, the following order applies:

1. Student safety, dignity, and fairness.
2. Student understanding, capability growth, and reading quality.
3. Knowledge and technical correctness.
4. Substantive equivalence between the Chinese-taught and English-taught classes.
5. Documentation clarity, traceability, and maintainability.
6. Teaching convenience, document output, and product completion.

## Article 4 — Single Authoritative Source

Each official policy or rule shall have one authoritative source.

Other documents may summarize, explain, or link to that rule for their primary audience, but they must not redefine it independently and create conflicting versions.

Review reports may judge whether current work follows existing rules, but they must not create new official policies by themselves.

# Part II — Document Types and Reading Paths

## Article 5 — Every Document Has One Primary Audience

Every official document must identify one primary audience and prioritize that audience.

A document may have secondary readers, but it must not mix conflicting writing purposes merely to serve everyone at once.

## Article 6 — Official Document Types

Official documents shall include at least these four types:

1. Governance and design documents: define rules, scope, dependencies, rationale, and long-term decisions.
2. Instructor execution documents: help instructors sequence, guide, observe, adapt, and deliver teaching.
3. Student learning documents: help students understand, practise, verify, and rebuild concepts.
4. Review and validation documents: use explicit criteria and evidence to judge whether current work meets requirements.

Assessment documents shall belong to the student or instructor reading path according to their true primary audience, while the official assessment policy remains the authoritative source.

Detailed formats, metadata, and templates for each type shall be defined in a separate bilingual writing standard rather than fully embedded in this Constitution.

## Article 7 — Three Primary Reading Paths

The repository root README shall function as a routing entry point and provide at least:

1. A student reading path.
2. An instructor execution path.
3. A course design and maintenance path.

Each path shall begin with documents needed by that reader. Students must not be required to pass through internal design, review, or instructor documents before reaching their learning materials.

No official document may become an orphan that cannot be reached through the appropriate reading path.

## Article 8 — Document Purpose and Boundaries

Every official document must answer:

1. Who is the primary audience?
2. What should that reader know, understand, or be able to do after reading it?
3. What core question is this document responsible for answering?
4. Which content belongs in another authoritative document?

A document must provide the information necessary for its purpose, must not rely on oral background known only to the original author, and must not include information irrelevant to its primary audience merely for the sake of completeness.

## Article 9 — Bilingual Completion and Substantive Equivalence

Every official document must be available in both Traditional Chinese and English.

The two versions must have the same official purpose, core content, requirements, code, test data, assessment conditions, and version status.

Translation may adapt sentence structure, paragraph rhythm, and explanation style to the target language, but must not add, remove, weaken, or alter substantive requirements.

When one official document is modified, its counterpart should be modified within the same unit of work.

## Article 10 — Terminology and Technical Consistency

The same concept shall use consistent Chinese and English terminology throughout the course.

Code, diagrams, tests, input/output, and explanatory text must be mutually consistent. Complete programs, fragments, pseudocode, and intentionally incorrect examples must be clearly distinguished.

Technical content shall be verified against the specified environment, language standard, and reproducible evidence.

# Part III — Student Learning Documents and Reading Quality

## Article 11 — Student Learning Documents Take Priority

Students are the most important audience in this course’s document system.

When student reading quality conflicts with maintenance convenience, information density, document shortening, or teaching convenience, the course shall protect students’ ability to understand and continue reading, without sacrificing technical correctness, necessary constraints, or important boundaries.

## Article 12 — Student Materials Must Read as Fluent Prose

Student materials shall use natural, clear, and coherent language.

They shall:

1. Use complete and readable sentences.
2. Provide clear transitions between paragraphs and sections.
3. Give new concepts a motivating problem, phenomenon, or need before moving to definitions and syntax.
4. Use lists, tables, and specification fields only when they genuinely improve understanding and not as a substitute for necessary explanation and reasoning.
5. Support continuous reading, review, and rebuilding of understanding rather than functioning only as instructor slide notes or maintainer lookup tables.
6. Avoid placing internal Concept IDs, maintenance procedures, instructor notes, review conclusions, or design disputes directly in the student reading flow.

## Article 13 — Concepts Before Syntax

Before introducing new syntax, student materials shall first answer:

1. Why is this concept needed?
2. What problem does it solve?
3. How does it affect program state, data, control flow, or structure?
4. How can students verify their understanding through diagrams, tracing, programs, tests, or other evidence?

Syntax shall be presented as a tool for expressing and solving problems, not as an isolated memorization target.

## Article 14 — Learning Sequence for Student Materials

Where appropriate, student materials should follow this sequence:

> Problem or need → expectation or prediction → visual or state model → core concept → syntax and code → execution observation → error diagnosis → verification and modification → summary

When the full sequence does not fit the topic, the material may adapt it but must retain a motivating problem, concept formation, implementation or observation, and student-executable verification.

## Article 15 — Cognitive Load and Information Priority

Student materials shall not require beginners to process too many unestablished concepts at once.

New content shall increase in complexity gradually and clearly distinguish core requirements, recommended practice, and extension content.

Visual attractiveness, reduced length, and a single class period shall not take precedence over readability and understanding.

## Article 16 — Errors and Verification Are Official Learning Content

Every important concept should include enough correct cases, representative errors, and verification methods to support understanding.

Materials must not merely reveal the correct answer. They should show how to form expectations, detect mismatches, propose causes, correct them, and verify again.

Intentionally incorrect examples must not require students to execute code known to risk danger, data loss, or uncontrolled behavior. Compiler diagnostics, models, isolated environments, or safe alternatives should be used where necessary.

# Part IV — Instructor and Course Design Documents

## Article 17 — Instructor Documents Serve Teaching Execution

Instructor execution documents shall explain teaching intent, classroom sequence, questioning approaches, expected student responses, common misconceptions, timing adjustments, and fallback plans.

Instructor documents should not rewrite student materials or expose instructor observations and prompts in the student reading flow before they are pedagogically appropriate.

Instructors may adjust pacing and activity form for class needs but may not alter official learning goals, core content, or assessment standards.

## Article 18 — Governance and Design Documents Must Be Precise and Traceable

Governance and design documents shall emphasize authoritative sources, choices and rationale, Concept and capability dependencies, scope and exclusions, change impact, and long-term maintenance.

They may use IDs, matrices, status fields, and decision records, but must not be treated directly as student learning materials.

## Article 19 — Review Documents Do Not Replace Official Documents

Review and validation documents must identify their criteria, distinguish facts, evidence, inference, and recommendation, state whether they have normative force, and write necessary corrections back into the authoritative source.

Completing a review report does not automatically correct the reviewed material.

# Part V — Course and Capability Design

## Article 20 — Competency Orientation

Course content and assessment must correspond to observable capabilities rather than only chapter names, syntax lists, or completion counts.

Capability evidence may include explanation, prediction, implementation, testing, diagnosis, modification, comparison, and verification, but no single form should carry the full judgment by itself.

## Article 21 — Knowledge Dependencies Must Be Explicit

A new concept must not depend on required knowledge that has not been established, explained, or explicitly identified as prerequisite knowledge.

Formal course design shall maintain Concepts, prerequisite dependencies, target maturity, and Unit relationships. Student materials shall translate those dependencies into natural and readable prerequisite explanations and transitions.

## Article 22 — Complete Learning Cycle

Where appropriate, major learning activities should include:

> Understand the problem → form an expectation → design an approach → implement or reason → test → debug → modify → run regression verification → explain

Activity forms may vary, but students must not be asked only to produce a first correct output without understanding, testing, or modification.

## Article 23 — Multiple Reasonable Solutions Are Allowed

Unless a learning objective explicitly requires a specific technique, one implementation must not be treated as the only correct solution.

Materials, instructor documents, and assessments shall distinguish required constraints, recommended practices, style preferences, and acceptable alternatives.

# Part VI — Equivalence Between Chinese-Taught and English-Taught Classes

## Article 24 — Shared Core Outcomes

The Chinese-taught and English-taught classes must achieve the same core capability outcomes and technical depth.

Instructional hours, pacing, number of examples, oral activities, and language support may differ, but core content, capability expectations, and assessment standards must not be reduced because of the teaching language.

## Article 25 — Language Support and Technical Assessment Must Be Separated

Language fluency must not replace programming competence in assessment.

Without lowering technical requirements, the course may provide terminology lists, sentence frames, bilingual keywords, diagrams, written explanation time, and longer reading time.

Official Chinese and English documents must be substantively equivalent. Actual teaching may adapt pacing and scaffolding to the language environment without literal sentence-by-sentence translation.

# Part VII — AI and External Tools

## Article 26 — AI Must Not Replace Student Thinking

AI may support learning, but it must not replace students in requirement understanding, initial reasoning, testing judgment, debugging decisions, result verification, or oral explanation.

## Article 27 — AI Use Is Optional by Default

Unless an activity explicitly targets AI judgment, AI verification, or AI collaboration as a learning objective, students must not be disadvantaged for not using AI and must not be required to declare that they did not use it.

Fixed prompts, conversation logs, before-and-after AI comparisons, and use disclosures must not become universal course completion requirements.

Activity-specific restrictions are required only when AI use materially affects the learning objective, academic integrity, or assessment fairness.

## Article 28 — AI Responses Are Not Authoritative Evidence

When students, instructors, or authors use AI, its explanations, programs, translations, tests, and suggestions shall be treated as claims requiring verification.

Adoption shall be judged through program execution, tests, compiler diagnostics, reliable sources, or other reproducible evidence.

## Article 29 — Author Responsibility Does Not Transfer to AI

When AI is used to create or modify official content, authors and maintainers remain responsible for correctness, bilingual equivalence, age appropriateness, licensing, executability, and avoiding unestablished concepts.

“Generated by AI” is not a justification for unreviewed or incorrect content.

# Part VIII — Implementation, Testing, and Technical Correctness

## Article 30 — Important Claims Must Be Verifiable

Program behavior, input/output, boundaries, error classifications, and technical conclusions shall be supported by sufficient reproducible evidence.

The number and form of tests should depend on the learning objective, risk, and nature of the program. Not every small activity requires the same checklist, but one successful run is never complete evidence.

## Article 31 — Debugging Is Evidence-Based

Debugging should include reproducing the problem, comparing expected and actual results, forming a testable hypothesis, narrowing the scope, modifying a cause, and rerunning the original and regression tests.

Random modification until the program passes must not be taught as a standard method.

## Article 32 — Requirement Modification Is Important Capability Evidence

Where appropriate, major programming activities should include a requirement change so students can identify design impact, code changes, existing tests, and new tests.

Formal requirement modification need not be applied mechanically to every minimal demonstration.

## Article 33 — Technical Validation and Continuous Integration

Official code examples and important technical claims shall be validated against the specified standard and target environment.

Where practical, automatically verifiable content should be maintained through tests, link checks, compiler warnings, or continuous integration. Automated validation does not replace human review of pedagogy and readability.

# Part IX — Assignments, Participation, and Assessment

## Article 34 — Assessment Must Correspond to Capability

Formal assessment must correspond to explicit capabilities and use enough evidence to support a judgment.

Successful compilation, correct output, passing an Online Judge, submitting a complete program, AI approval, or reciting a definition cannot individually prove full capability.

## Article 35 — Assessment Rules Must Be Clearly Published

Before formal assessment, students shall know the purpose, form, primary capabilities and criteria, permitted and prohibited resources, and how reasonable technical or language needs are handled.

Detailed percentages, procedures, and current-term policies shall be defined in the official bilingual assessment policy rather than permanently embedded in this Constitution.

## Article 36 — Independent Homework Serves Learning

Independent homework shall provide room for attempts, errors, modification, testing, and discussion. It must not be reduced to syntax copying or a single submitted answer merely for grading convenience.

The course may use a policy in which independent homework is not submitted or individually graded. Submission and grading rules shall be defined in the official assessment policy rather than scattered across materials.

## Article 37 — Capability Gaps Require Further Learning Opportunities

When students demonstrate a capability gap, the course should provide further learning, explanation, modification, or practice directed at that capability.

This article does not mandate a particular retest system. Formal remediation and assessment procedures are defined by the current assessment policy.

# Part X — Maintenance, Review, and Amendment

## Article 38 — Changes Must Be Traceable

Major changes to official documents must remain traceable in their rationale, impact, bilingual synchronization, and review outcome.

Fixed metadata, version fields, and contribution procedures shall be defined by a separate maintenance standard.

## Article 39 — Major Changes Require Constitutional Review

The following changes require review against this Constitution:

- Changes to the highest educational purpose, core capabilities, or document governance.
- Changes to the official assessment system.
- Changes to the role of AI in the course.
- Changes to equivalence between the Chinese-taught and English-taught classes.
- Major restructuring of student materials or reading paths.
- Introduction of tools or platforms that materially change how students learn.

## Article 40 — The Course Must Be Cleaned Regularly

Maintenance shall periodically check for duplicate rules, broken links, outdated content, bilingual drift, orphan documents, unused resources, and activities that cannot be verified.

## Article 41 — Constitutional Amendment Procedure

A constitutional amendment must explain its reasons and expected impact, provide synchronized Chinese and English drafts, remain reviewable before taking effect, identify existing official documents that may require follow-up changes, and preserve a traceable change record.

# Part XI — Minimum Non-Negotiable Conditions

## Article 42 — Minimum Conditions

The following conditions must not be omitted because of time pressure, tool limits, document output, or teaching convenience:

1. Student safety, dignity, and fairness.
2. Student understanding and capability growth first.
3. Student materials that are fluent, continuously readable, and technically correct.
4. Substantive equivalence of core Chinese and English content.
5. Concepts and mental models before syntax memorization.
6. Important technical claims supported by reproducible evidence.
7. AI does not replace student thinking, and not using AI is not a deficiency.
8. Assessment uses sufficient and diverse evidence to judge capability.
9. Official rules have clear authoritative sources and reading paths.

## Article 43 — Draft Effect

This version is a 2.0.0 amendment draft.

It shall replace version 1.3.0 as the official baseline only after bilingual review, confirmation of impact on existing official documents, and formal merge.
