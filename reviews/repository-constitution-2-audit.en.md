# Repository-Wide Constitution 2.0 Compliance Audit

Version: 2.0.0  
Status: Completed audit record for PR #10 review snapshot  
Last updated: 2026-08-07  
Authoritative basis: `CONSTITUTION.en.md` 2.0.0  
Primary audience: Course designers, instructors, and maintainers  
Normative force: This document records findings and verification results only; it does not create new rules

## 1. Purpose and Ratings

This audit records the completed Constitution 2.0 review of governance level, primary audience, authoritative role, bilingual equivalence, student readability, technical verifiability, and consistency of AI and assessment rules for the repository snapshot proposed by PR #10.

Ratings: A compliant, B minor correction, C structural correction, D noncompliant, H historicalized.  
Priorities: P0 immediate, P1 high, P2 medium, P3 general improvement.

“Complete” means the identified finding was corrected and rechecked. It does not mean the file can never receive future editorial or pedagogical improvements.

## 2. Completed Audit Matrix

| Path | Governance Level | Primary Audience | Rating | Priority | Findings | Action | Status |
|---|---|---|---|---|---|---|---|
| `README.md` | Guide / routing entry | Students, instructors, maintainers | C → A | P0 | Duplicated assessment policy, progress reporting, and obsolete AI requirements | Rewritten as a three-role entry | Complete |
| `classes/zh/README.md`, `classes/en/README.md` | Material entry | Students | D → A | P0 | Early TBD drafts did not match current delivery | Rewritten for current 4×3-hour and 5×2-hour tracks | Complete |
| `design/13-learning-assessment-policy.*` | Official Policy | Students and instructors | D → A | P0 | Mandatory pre-AI artifacts, summaries, logs, and universal AI oral capability | AI made optional; non-use is not a deficit | Complete |
| `design/12-constitution-compliance-review.*` | Historical Record | Maintainers | D → H | P0 | Treated Constitution 1.2.0 as current | Historicalized with an obsolete warning | Complete |
| `materials/preparatory/ASSESSMENT-NOTE.*` | Migration Note | Maintainers | C → A | P0 | Claimed precedence and duplicated assessment policy | Removed normative force; retained only migration guidance | Complete |
| `materials/preparatory/unit-01*` through `unit-04*` | Student Material | Students | B → A | P1 | AI appeared in the core path and implied mandatory use | Converted to directly skippable optional extensions | Complete |
| `materials/assignments/*` | Student resources / assessment implementation | Students, instructors | B → A | P1 | Indexing and rubric wording could imply AI was required | Homework remains unsubmitted and ungraded; AI notes optional; rubrics consider AI only when actually used | Complete |
| `materials/README.*`, `materials/TEMPLATE.*` | Role-based index / authoring guide | Students, instructors, maintainers | C → A | P1 | Mixed audiences, copied policy, fixed AI chapter, and premature completion claims | Rewritten as role-based navigation and purpose-driven authoring guidance | Complete |
| `materials/instructor/session-guides.*` | Instructor Guide | Instructors, TAs | A | P1 | Needed executable pacing, misconceptions, fallbacks, fairness supports, and concise records without becoming policy | Retained as implementation guidance; `design/13` remains authoritative | Reviewed |
| `materials/formal/README.*`, `materials/formal/unit-01*` through `unit-12*` | Student Material | Students | B → A | P1 | AI in core paths and multiple technical-contract gaps | AI made directly skippable; value, input, lifetime, allocation, stream, dependency, overflow, and failure contracts strengthened | Complete |
| `design/README.*` | Governance index / guide | All roles | C → A | P2 | Listed all design files as equally official, duplicated policy text, and contained obsolete next steps | Rewritten with authority order, governance roles, maintenance workflow, and current navigation | Complete |
| `design/01-product-vision.*` | Revisable planning model | Designers and maintainers | C → A | P1 | Claimed governing authority and made AI use universal success evidence | Reclassified as planning context; higher-authority precedence explicit; external-assistance verification conditional; AI non-use neutral | Complete |
| `design/02-requirements-map.*` | Revisable planning and traceability model | Designers and maintainers | C → A | P1 | Claimed controlling-baseline authority; universal AI literacy/records; stale sequential navigation | Reclassified as non-governing model; higher-authority precedence stated; AI requirements conditional; stale navigation removed | Complete |
| `design/03-programming-domain-model.*` | Revisable planning model | Designers and maintainers | C → A | P1 | AI embedded as a core domain; universal disclosure; metadata drift; physical build pipeline overclaimed | External assistance optional; disclosure contextual; bilingual metadata synchronized; implementation-neutral toolchain and pointer/storage wording added | Complete |
| `design/04-programming-language-knowledge-graph.*` | Revisable planning and traceability model | Designers and maintainers | C → A | P1 | AI judgment treated as universal dependency; universal record path; stale draft navigation; build stages over-specified | Conditional dependency added; external-assistance branch optional; records contextual; metadata/navigation/toolchain caveats corrected | Complete |
| `design/05-competency-map.*` | Design standard | Designers and maintainers | B → A | P1 | Needed explicit policy boundary and conditional external-assistance evidence | Governance boundary clarified; EV-AI/PC-A apply only when assistance is actually used; no core competency requires AI | Complete |
| `design/06-scope-boundary.*` | Design standard | Designers and maintainers | B → A | P1 | Scope needed an explicit optional state so tool use could not become a hidden minimum-delivery gate | Added/used SB-X Conditional/Optional; minimum delivery excludes AI use; scope and maturity remain independent of tool use | Complete |
| `design/07-acceptance-model.*` | Revisable planning and traceability model | Designers, instructors | B → A | P1 | Candidate evidence could be mistaken for assessment policy or universal tool evidence | Policy authority boundary explicit; external-assistance evidence conditional; no AI/non-use declaration required | Complete |
| `design/08-delivery-map.*` | Revisable planning model | Designers, instructors | B → A | P1 | Delivery placement could make optional tool activity functionally mandatory | Optional-tool activities directly skippable; shared baseline excludes tool use; policy details delegated to `design/13` | Complete |
| `design/09-risk-register.*` | Revisable planning and traceability model | Designers, instructors, maintainers | B → A | P2 | Tool-misuse controls could become mandatory surveillance/logging | Risks emphasize capability evidence and verification while preserving optionality, dignity, and policy authority | Complete |
| `design/10-traceability-matrix.*` | Revisable planning and traceability model | Designers and maintainers | B → A | P2 | AI traceability could become a universal dependency path | External-assistance traceability conditional; core chain complete without AI; authority precedence stated | Complete |
| `design/11-terminology-glossary.*` | Design standard | Authors, translators, maintainers | B → A | P2 | Terms needed governance roles and precise C/toolchain boundaries | Standardized governance, null-pointer, storage-duration, stream, verification, and optional-assistance terminology | Complete |
| `design/14-programming-concept-tree.*` | Design standard | Designers and maintainers | B → A | P2 | Concept inventory needed to separate stable concepts from tool choice and implementation folklore | External assistance outside prerequisite core; toolchain/runtime implementation caveats and concept boundaries clarified | Complete |
| `design/15-programming-concept-registry.*` | Design standard | Designers and maintainers | C → A | P1 | Draft metadata, local maturity redefinition, AI-assisted programming marked core, terminology and toolchain assumptions conflicted with current standards | Activated as design standard; delegated maturity/scope definitions; external-assistance concepts X conditional; C terminology/runtime boundaries corrected | Complete |
| `design/16-unit-map.*` | Design standard | Designers and maintainers | C → A | P1 | Every Unit previously required a post-Unit AI explanation and contained overly physical compiler/call-stack wording | Core evidence independent of external tools; AI conversations/logs/prompts/non-use declarations removed from completion; toolchain and activation models implementation-neutral | Complete |
| `design/17-student-material-outlines.*` | Revisable planning and traceability model | Material authors and maintainers | C → A | P1 | Every outline previously made AI the post-Unit conversational audience; stale technical models could reintroduce mandatory AI and implementation folklore | Rewritten with tool-independent core reflection/evidence, directly skippable optional external-assistance pattern, and explicit technical contracts | Complete |
| Repository navigation / bilingual structure | Mechanical validation | Maintainers | B → A | P2 | Pair, link, orphan, and obsolete-reference coverage needed repository-wide verification | Automated checks added and run across 114 Markdown files; no orphan/unreferenced Markdown candidates found | Complete |
| `examples/` and C validation fixtures | Technical verification | Instructors, maintainers | B → A | P2 | Correct examples and intentional defects needed explicit, reproducible classification | Compile manifest, runtime/defect verification, GCC and Clang validation added | Complete |
| `.github/workflows/*validation*` | CI verification | Maintainers | B → A | P2 | Validation results needed repeatable repository checks | Documentation/governance, technical validation, and example verification workflows enabled and passing on the reviewed PR snapshot | Complete |

## 3. Governing Decisions

### 3.1 AI Must Not Become Implicitly Mandatory

AI may be offered as an extension, but it must not become mandatory through placement in a core sequence, completion checklist, fixed template, requirements baseline, domain model, dependency graph, competency field, scope state, Unit skeleton, material outline, or assessment field. AI non-use does not affect completion, participation, or assessment. Verification responsibilities apply conditionally when optional external assistance is actually adopted.

### 3.2 Assessment Has One Authoritative Source

`design/13-learning-assessment-policy.*` is the sole authoritative assessment policy. READMEs, task packs, rubrics, templates, instructor guides, design standards, and planning models may provide navigation, traceability, definitions, or implementation guidance only.

### 3.3 Design Documents Do Not Share Equal Authority

The authority order is Constitution → official learning/assessment policy → approved design standards → planning and traceability models → implementation guides and materials → historical records. Lower-level files may not override higher-level sources.

### 3.4 Student Materials Must State Technical Contracts

Materials must state relevant value ranges, input states, termination conditions, lifetimes, dereference preconditions, allocation sizes, ownership/release responsibility, failure preservation, stream states, module dependencies, compile/link distinctions, and undefined-behavior boundaries when those matters are relevant. Successful compilation or one correct output cannot replace those contracts.

### 3.5 Conceptual Models Must Not Be Mistaken for Implementation Guarantees

The C standard does not require one physical pipeline of standalone preprocessor, compiler, assembler, linker, object files, executable files, or one physical call-stack/heap representation. Concrete materials identify and verify the target implementation when commands, artifacts, layout, or runtime behavior matter.

### 3.6 Earlier Audits Are Historical

Earlier reviews record decisions under a particular date and constitutional version. Current decisions follow Constitution 2.0 and the current authoritative sources.

## 4. Human Review Coverage

The Constitution 2.0 document-by-document pass covered:

- preparatory student Units P-U01 through P-U04 in Chinese and English;
- formal student Units F-U01 through F-U12 in Chinese and English;
- assignment/rubric resources, material indexes/templates, and instructor session guidance;
- all bilingual `design/01–17` pairs;
- repository/governance entry points and historical-review boundaries.

The review checked authority boundaries, assessment and AI rules, student readability, instructor-document boundaries, substantive bilingual equivalence, and technical claims. P3 wording or pacing refinements may still arise from classroom use; those do not reopen this completed P0/P1 audit unless they reveal a substantive conflict.

## 5. Automated and Technical Verification Record

For the PR #10 snapshot immediately preceding this 2.0.0 matrix update:

- `scripts/validate_repository.py --skip-c` passed across 114 Markdown files.
- Repository validation with GCC passed across 114 Markdown files and 8 ordinary C translation units.
- Repository validation with Clang passed across 114 Markdown files and 8 ordinary C translation units.
- `validation/check_materials.py` checked 114 Markdown files, reported no orphan/unreferenced Markdown candidates, and passed navigation/bilingual/former-Constitution checks.
- `validation/run_validation.py` passed with GCC and Clang.
- `examples/verify.sh` passed with GCC 13.3.0 and Clang 18.1.3, including the documented diagnostic-only `missing-return.c` case.
- The GitHub Actions workflows `Technical Validation`, `Repository validation`, and `Verify C17 examples` all completed successfully for that reviewed snapshot.

These automated checks verify structure and executable contracts; they do not replace the human review described above.

## 6. Current Conclusion

The repository-wide Constitution 2.0 audit for the current PR #10 review scope is complete. All P0/P1 findings identified in the review have been corrected. The bilingual audit matrix records the reviewed repository areas, the student-material and design-document passes are complete, and repository navigation/technical validation has been executed successfully.

PR #10 is therefore eligible for formal review rather than draft-only audit work. Future reviewer or CI findings should be recorded as new findings against the affected traceability path; P2/P3 editorial or classroom refinements may continue without contradicting this completed review snapshot.
