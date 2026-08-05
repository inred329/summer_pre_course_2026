# Constitution Maturity Review

Version: 0.1.0  
Status: Review draft  
Review baseline: `CONSTITUTION.en.md` 1.3.0  
Primary audience: Course designers and maintainers  
Normative force: None; this document proposes review conclusions and does not replace the official Constitution

## 1. Purpose of This Review

This review is not merely an attempt to add new articles. It uses the experience gained from completing sixteen bilingual Units, instructor resources, assessment documents, and technical validation to reconsider the current Constitution:

1. Which principles should remain as constitutional rules.
2. Which articles should be rewritten to become more stable and objectively reviewable.
3. Which details should move to templates, writing standards, or operating procedures.
4. Which requirements now conflict with current course policy.
5. Which new long-term governance principles are required.

The highest review standard remains student learning. In particular, student materials should let students read fluently, form mental models, and continue building understanding instead of forcing them to read internal specifications.

## 2. Overall Conclusion

The core values of the current Constitution remain valid:

- Student capability growth comes first.
- Technical correctness is non-negotiable.
- Concepts precede syntax.
- Prediction, testing, debugging, modification, and verification are official learning activities.
- The Chinese-taught and English-taught classes have equivalent core outcomes.
- AI must not replace student thinking.
- Official documents must be bilingual, traceable, and discoverable.

The primary problem is not a lack of principles. It is that several levels of rules are mixed in one highest-level document:

- Highest values and governance principles.
- Detailed student-material section templates.
- Instructor and activity procedures.
- Maintainer commit and version steps.
- Outdated AI logging and assessment requirements.

The recommendation is therefore to refactor Constitution 1.3.0 into a shorter and more stable principle-based 2.0.0, while creating a separate bilingual Document Types and Writing Standards document for detailed rules.

## 3. Highest-Priority Revisions

### 3.1 Formally Define Document Types and Primary Audiences

Every official document should have exactly one primary audience and should prioritize that audience. At minimum, the repository should distinguish:

1. Governance and design documents: answer “What are the rules?” and “Why was the course designed this way?”
2. Instructor execution documents: answer “How should the instructor teach, sequence, and adapt?”
3. Student learning documents: answer “How should the student understand, practise, and verify?”
4. Review and validation documents: answer “Does the current work satisfy the rules and evidence?”

Assessment documents should belong to the student or instructor path according to their true primary audience instead of becoming an ambiguous mixed category.

### 3.2 Make Student Reading Quality an Explicit Highest-Level Principle

Student materials should prioritize:

- Natural and fluent sentences.
- Clear transitions between paragraphs and sections.
- Context and prerequisites for new concepts.
- Continuous readable prose rather than only lists and specification fields.
- Information density that does not obstruct understanding.

When readability and information density conflict, authors should choose the more understandable expression without sacrificing technical correctness, necessary constraints, or important boundaries.

Student materials should be treated as long-term learning texts, not course specifications, instructor flowcharts, or acceptance checklists.

### 3.3 Require Three Reading Paths from the Root README

The root README should function as a routing entry point rather than a complete index. It should provide at least:

- A student reading path.
- An instructor execution path.
- A course design and maintenance path.

Each path-specific README should prioritize only documents needed by that reader. Students should not first encounter review reports, instructor observation forms, or internal Concept IDs.

### 3.4 Remove AI Rules That Conflict with the Current AI Role

The current AI part includes several overly heavy requirements:

- Students must preserve a large set of pre-AI artifacts before important activities.
- Every activity must separately specify what may be asked, prohibited, disclosed, and preserved.
- AI verification is listed as a fixed assessment dimension.
- Important histories must preserve before-and-after AI differences.

These rules conflict with the current role of AI as a low-weight, optional concept-conversation tool and create unnecessary obligations for students who do not use AI.

Recommended replacement:

- Students must not be disadvantaged for not using AI.
- When AI is used, its response is not authoritative evidence.
- Activity-specific restrictions are required only when AI use materially affects the learning objective or assessment fairness.
- Fixed prompts, conversation logs, use declarations, and before/after AI comparisons must not be universal course requirements.
- Authors using AI remain fully responsible for review and correctness.

### 3.5 Strengthen the Single Authoritative Source Principle

Every official policy should be fully defined in one authoritative source. Other documents should summarize and link according to reader needs instead of redefining the rule independently.

For example:

- The Constitution defines highest principles.
- The official assessment policy defines grading rules.
- The student entry point provides only the concise explanation students need.
- Instructor documents explain execution without changing policy.
- Review reports do not create new rules.

## 4. Recommended Treatment by Current Part

### Part I — General Provisions

Decision: Retain and simplify.

- Articles 1 through 3 should remain, with a clearer reference to student understanding and reading quality in the priority order.
- Article 4 should be rewritten so that temporary working notes do not automatically expand into official documents; official status should depend on publication, reference, or use in decision-making.
- Add principles that every document has one primary audience and that student learning documents receive priority.

### Part II — Writing and Documentation Standards

Decision: Major restructuring.

Retain in the Constitution:

- Bilingual completion and substantive equivalence.
- Synchronized changes within one unit of work.
- A single authoritative source.
- Clear purpose, primary audience, and discoverability.
- Independently readable student materials.
- Terminology consistency.
- Technical consistency between code and explanation.

Rewrite:

- Article 10 currently requires every official document to state prerequisites, tools, input/output, common errors, and AI use; this over-applies the student-material format. It should require the information necessary for that document type.
- Article 12’s “what must be submitted or demonstrated” does not fit unsubmitted student practice or governance documents. It should become “what observable result the reader should produce or achieve.”
- Article 15 should explicitly apply to student materials rather than all teaching materials.
- Article 17 should not require all official documents to provide visualizations; the requirement should focus on student learning materials and instructor resources where visualization materially improves understanding.

Move out of the Constitution:

- Article 14’s thirteen-section material template.
- Eight detailed visual-production rules.
- Specific editorial techniques such as short paragraphs and small examples.
- The complete five-level information-label list.

These belong in the Document Types and Writing Standards document and student-material template.

### Part III — Course and Material Design Principles

Decision: Retain the core and merge overlapping articles.

- Competency orientation, concepts before syntax, knowledge dependencies, complete learning cycles, prediction, error cases, minimal examples, and multiple reasonable solutions should remain.
- Articles 20 and 23 overlap and may be reorganized into “capability evidence” and “learning cycle.”
- Article 24 should not require written prediction in every situation; it should preserve the principle of forming a comparable expectation when pedagogically useful.
- Competency maturity may remain as a principle, while detailed L1–L5 definitions belong in the Concept Registry or competency framework.

### Part IV — Bilingual Equivalence

Decision: Retain.

- Equivalent core outcomes, different delivery pacing, and preventing language difficulty from replacing technical assessment all remain valid.
- “The English-taught class must not be a literal translation” should remain, but the Constitution should distinguish document equivalence from instructional adaptation: official content remains substantively equivalent while pacing and language scaffolding may differ.

### Part V — AI Use

Decision: Rewrite completely.

Retain:

- AI must not replace student thinking.
- AI claims require evidence-based verification.
- Authors remain fully responsible for AI-generated content.

Delete or rewrite:

- Mandatory preservation of pre-AI artifacts.
- Six fixed AI fields for every activity.
- Universal AI-use disclosure requirements.
- AI verification as a fixed assessment item for all students.

Add:

- AI use is optional unless an activity explicitly targets AI judgment as a learning objective.
- Not using AI must not be treated as missing evidence.
- AI appears only when it supports the current Concept or verification capability and must not become the material’s main narrative.

### Part VI — Implementation, Testing, and Debugging

Decision: Retain and simplify.

- Observable success conditions, testing as part of design, evidence-based debugging, requirement modification, and traceable versions should remain.
- “Every implementation activity must include normal, boundary, error, and regression tests” is too absolute; the rule should require enough evidence according to the activity’s risk and learning objective.
- Mandatory preservation of before-and-after AI differences should be deleted.

### Part VII — Assignments and Assessment

Decision: Retain capability principles and remove fixed fields that conflict with current policy.

- Assessment alignment, the insufficiency of a single output, public criteria, and multiple forms of evidence should remain.
- “AI verification” should not be a universal fixed rubric category.
- Assignment rules should recognize the current policy that independent homework is not submitted or individually graded, while avoiding locking permanent percentages and procedures into the Constitution.
- The relationship between remediation and the current single final oral examination should be clarified. The Constitution may require further learning opportunities for capability gaps without mandating a formal retest system.

### Part VIII — Maintenance, Review, and Evolution

Decision: Retain principles and move steps out of the Constitution.

- Traceable changes, constitutional review for major changes, periodic cleanup, and reasoned bilingual constitutional amendments should remain.
- Fixed fields such as version, date, and change summary belong in a document maintenance standard.
- The six-step amendment checklist should become a higher-level procedural principle, with detailed steps moved to a contribution guide.

### Part IX — Final Provisions

Decision: Reorganize.

The minimum non-negotiable conditions should become truly long-term principles:

- Student safety, dignity, and fairness.
- Student understanding and capability growth first.
- Student materials that are readable and technically correct.
- Substantive equivalence of core Chinese and English content.
- Concepts before syntax.
- Important claims verified through reproducible evidence.
- AI does not replace student thinking.
- Assessment uses sufficient and diverse evidence to support capability judgments.

Specific activity formats or AI verification procedures should not become permanent constitutional conditions.

## 5. Recommended Structure for Constitution 2.0.0

1. Preamble and highest educational purpose.
2. Governance, applicability, and order of authority.
3. Document types, primary audiences, and single authoritative sources.
4. Student learning materials and reading quality.
5. Course and capability design principles.
6. Bilingual substantive equivalence.
7. AI and external tool positioning.
8. Implementation, testing, debugging, and technical correctness.
9. Assignment, participation, and assessment principles.
10. Maintenance, review, and amendment.
11. Minimum non-negotiable conditions.

## 6. Supporting Standards That Should Be Created Separately

Constitution 2.0.0 should not carry every detail. The repository should also establish:

- `design/document-types-and-writing-standards.zh-TW.md`
- `design/document-types-and-writing-standards.en.md`
- A student-material template.
- An instructor execution document template.
- A review document template.
- A three-path README standard.
- Document metadata and maintenance procedures.

## 7. Current Review Decision

This review recommends:

> Do not merely add isolated articles directly to `main`. Draft a bilingual Constitution 2.0.0 that preserves the core educational values, removes outdated mandatory AI obligations, moves detailed templates out of the Constitution, and formally establishes student-first document types and writing principles.
