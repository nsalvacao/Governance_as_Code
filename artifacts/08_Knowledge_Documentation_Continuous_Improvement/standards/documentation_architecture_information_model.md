---
title: Documentation Architecture and Information Model
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: semiannual
applies_to: documentation corpora and reusable governance libraries
source_basis: Diataxis framework (Daniele Procida, diataxis.fr)
source_manifests:
  - documentation__diataxis.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define how the document corpus is organized, related, and navigated so that future documents remain consistent and discoverable. This standard applies the Diataxis framework as the primary information model for all documentation produced in or consumed from `{{REPOSITORY_NAME}}`.

## The Four Documentation Types

The Diataxis framework identifies four distinct documentation types. Each type serves a different reader need and must be kept structurally separate. Mixing types degrades both usability and maintainability.

### Tutorial

- **Orientation**: learning-oriented
- **Written for**: learning
- **Primary goal**: help a newcomer succeed at a meaningful task, building confidence through action
- **Characteristic style**: series of steps with expected outcomes; explanation is subordinate to action
- **What it is NOT**: a complete explanation of how the system works; a reference of all options
- **Applies to `{{REPOSITORY_NAME}}`**: `{{TUTORIAL_APPLICABILITY}}`

### How-to Guide

- **Orientation**: task-oriented
- **Written for**: work
- **Primary goal**: direct a competent practitioner toward a specific goal, assuming existing knowledge
- **Characteristic style**: direct imperative steps; no hand-holding; focused on achieving the goal
- **What it is NOT**: a tutorial for beginners; an explanation of why things work
- **Applies to `{{REPOSITORY_NAME}}`**: `{{HOWTO_APPLICABILITY}}`

### Reference

- **Orientation**: information-oriented
- **Written for**: consultation
- **Primary goal**: describe the machinery accurately and completely so the reader can look up facts
- **Characteristic style**: consistent structure, neutral tone, no narrative; organized like a map
- **What it is NOT**: a tutorial; a guide to achieving goals; an explanation of design decisions
- **Applies to `{{REPOSITORY_NAME}}`**: `{{REFERENCE_APPLICABILITY}}`

### Explanation

- **Orientation**: understanding-oriented
- **Written for**: understanding
- **Primary goal**: deepen background knowledge and illuminate design rationale, with no specific task goal
- **Characteristic style**: discursive prose; considers alternatives, history, and trade-offs
- **What it is NOT**: a set of instructions; a reference to look things up
- **Applies to `{{REPOSITORY_NAME}}`**: `{{EXPLANATION_APPLICABILITY}}`

## Information Model per Type

For each documentation type, the following properties must be defined when instantiating this model:

| Property | Tutorial | How-to Guide | Reference | Explanation |
|---|---|---|---|---|
| Purpose | `{{TUTORIAL_PURPOSE}}` | `{{HOWTO_PURPOSE}}` | `{{REFERENCE_PURPOSE}}` | `{{EXPLANATION_PURPOSE}}` |
| Target reader | Newcomer / learner | Competent practitioner | Any — lookup context | Curious reader seeking understanding |
| Writing approach | `{{WRITING_APPROACH_TUTORIAL}}` | `{{WRITING_APPROACH_HOWTO}}` | `{{WRITING_APPROACH_REFERENCE}}` | `{{WRITING_APPROACH_EXPLANATION}}` |
| Placement in navigation | Getting started / onboarding | Task-based or how-to section | API / CLI / schema reference | Concepts / background / architecture |
| Quality criteria | Beginner succeeds on first attempt | Goal is achieved without ambiguity | Accurate, complete, consistent | Illuminates "why", no gaps in rationale |

## Navigation Model

The navigation structure of `{{REPOSITORY_NAME}}` must reflect the four types as distinct sections. Readers arrive with different intents:

- **Tutorials** lead into **how-to guides** once the reader has basic competence.
- **How-to guides** link to **reference** material for option details.
- **Reference** material links back to **explanation** for conceptual background.
- **Explanation** does not link prescriptively to tasks — it broadens understanding.

Implement this navigation in `{{NAVIGATION_FILE_OR_SYSTEM}}`.

## Anti-Pattern Warnings

The following patterns violate Diataxis principles and must be actively avoided:

1. **Mixed types in one document**: a document that is simultaneously a tutorial and a reference confuses readers and is hard to maintain. Split into separate documents.
2. **Tutorial with full reference content**: embedding all options and flags in a tutorial overwhelms beginners. Link to reference instead.
3. **How-to guide that teaches concepts**: explaining background in a how-to interrupts the practitioner's goal. Move background to explanation.
4. **Reference that gives instructions**: reference material should describe, not prescribe. Procedural content belongs in how-to guides.
5. **Explanation that gives steps**: if prose turns into numbered steps, it has drifted into how-to territory.

## Document Map

All documents in `{{REPOSITORY_NAME}}` are classified below. This map is updated whenever a document is added, retired, or reclassified.

| Document | Diataxis Type | Location |
|---|---|---|
| `{{DOC_NAME_1}}` | `{{TYPE_1}}` | `{{LOCATION_1}}` |
| `{{DOC_NAME_2}}` | `{{TYPE_2}}` | `{{LOCATION_2}}` |
| `{{DOC_NAME_N}}` | `{{TYPE_N}}` | `{{LOCATION_N}}` |

Add one row per document. Valid types: `tutorial`, `how-to`, `reference`, `explanation`. Documents that do not fit cleanly should be split; if they cannot be split, classify by dominant intent and note the secondary type.

## Governance of this Model

- The document map is owned by `{{INFORMATION_ARCHITECTURE_OWNER}}`.
- Reclassification decisions must be recorded in the decision log with rationale.
- This model is reviewed `{{REVIEW_CADENCE}}` or when the corpus grows by more than `{{GROWTH_THRESHOLD}}` documents.

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md
- Primary source basis: Diataxis framework (Daniele Procida, diataxis.fr)
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
