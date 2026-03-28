---
title: Documentation Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: documentation corpus and publication rules
source_basis: Diataxis framework (Daniele Procida) and GitHub Docs documentation guidance
source_manifests:
  - governance__github_docs.md
  - documentation__diataxis.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Policy Statement

Document only what improves understanding, reuse, traceability, or operational safety, and keep the document type aligned with the reader need. Every document serves exactly one of the four Diataxis quadrants; mixing quadrants in a single document degrades navigability and maintenance quality.

## The Four Documentation Types

The Diataxis framework (Daniele Procida) defines four distinct documentation types organized by two axes: practical/theoretical and acquisition/application. Each type serves a different reader need and must not be conflated with the others.

### Tutorial (Learning-oriented)

**Purpose:** Help the reader learn by doing. Tutorials are lessons that take the reader through a meaningful task from start to finish. They are not about explaining or covering all cases — they are about building confidence through successful practice.

- Reader need: learning, acquiring skills, first-time experience.
- Author obligation: guarantee success; every step must work exactly as described.
- Structural pattern: numbered steps with concrete actions, explicit expected outcomes, minimal explanation of why.
- Quality signal: a reader with no prior context can complete the tutorial and has something working at the end.

### How-to Guide (Task-oriented)

**Purpose:** Help the reader achieve a specific real-world goal. How-to guides are recipes for practitioners who already know the fundamentals and need to accomplish a concrete task.

- Reader need: achieving a goal, solving a problem they already understand.
- Author obligation: be direct and practical; assume the reader knows what they are doing and why.
- Structural pattern: numbered or bulleted steps, focused on one goal, no introductory background unless essential.
- Quality signal: a practitioner can follow the guide to completion without needing to consult other documents for the core task.

### Reference (Information-oriented)

**Purpose:** Provide accurate, complete, and consistent technical information for lookup. Reference documentation describes the machinery — APIs, schemas, CLI flags, configuration options — without prescribing how to use it.

- Reader need: accurate information, exhaustive coverage, reliable lookup.
- Author obligation: be precise and complete; omissions are defects.
- Structural pattern: structured entries (alphabetical, hierarchical, or by concept), neutral tone, consistent format across all entries.
- Quality signal: every public interface, field, and behavior is described; nothing is left to inference.

### Explanation (Understanding-oriented)

**Purpose:** Illuminate context, background, and reasoning. Explanations help the reader understand why things are the way they are, explore concepts, and appreciate trade-offs. They do not instruct or direct.

- Reader need: understanding, context, conceptual clarity.
- Author obligation: illuminate; explore alternatives and the reasoning behind choices.
- Structural pattern: discursive prose, may include comparisons, historical context, and acknowledged trade-offs.
- Quality signal: after reading, the reader has a mental model they did not have before, without needing to take any specific action.

## When to Write Each Type

Use the following triggers as guidance. When multiple types seem applicable, write separate documents.

| Situation | Write this type |
|---|---|
| A new user needs to get started with zero prior knowledge | Tutorial |
| A practitioner needs to accomplish a specific task | How-to guide |
| A developer needs to look up a parameter, field, or behavior | Reference |
| A team needs to understand an architectural decision or design trade-off | Explanation |
| An operator needs to respond to an incident | How-to guide (runbook) |
| A stakeholder needs to understand why a technology was chosen | Explanation |

## Mixing Prohibition

Each document serves exactly one Diataxis quadrant. Do not mix types in a single document. Common anti-patterns:

- A "Getting Started" guide that is half tutorial and half reference (split into two documents).
- A runbook that explains the architecture before giving steps (move the explanation to a separate explanation document).
- A reference page that includes a tutorial walkthrough (link to the tutorial instead).

When reviewing documentation, flag mixed-type documents and track their split as a maintenance task.

## Navigation Principles

Good documentation navigation guides readers through the four types in a progression that matches their growing familiarity:

1. **Tutorials** — entry point for new users; should be prominently linked from onboarding flows.
2. **How-to guides** — the primary destination for practitioners; organized by task, not by feature.
3. **Reference** — lookup destination; always accessible, never the starting point.
4. **Explanation** — contextual depth; linked from tutorials and how-to guides where "why" questions arise.

Navigation structures must not mix these types in the same navigation level. A sidebar that lists tutorials and reference entries side-by-side makes both harder to find.

## Quality Criteria per Type

| Type | Key quality criteria |
|---|---|
| Tutorial | Every step works; reader succeeds on first attempt; no prerequisites not stated upfront |
| How-to guide | Single goal; no unnecessary preamble; steps are executable |
| Reference | Complete, accurate, consistent format; no instructional content |
| Explanation | Illuminates rather than instructs; acknowledges trade-offs; does not embed steps |

## Review Triggers

Documentation reviews are triggered by:
- **Time-based:** `{{REVIEW_CADENCE}}` review cycle for all published documents.
- **Code change:** Any change to a system, API, or process described by a reference or how-to guide triggers an immediate review of that document.
- **User report:** A documented report of inaccuracy, confusion, or incompleteness triggers a targeted review within `{{REVIEW_RESPONSE_SLA}}`.
- **Tutorial failure:** A confirmed report that a tutorial cannot be completed as written triggers an urgent fix before the next publish cycle.

## Source Attribution

- Source manifests: governance__github_docs.md, documentation__diataxis.md
- Primary source basis: Diataxis framework (Daniele Procida) and GitHub Docs documentation guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
