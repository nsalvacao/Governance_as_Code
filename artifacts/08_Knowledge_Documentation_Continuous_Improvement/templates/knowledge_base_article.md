---
title: Knowledge Base Article Template
artifact_type: template
status: public
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: stable operational guidance and reusable references
source_basis: Diataxis, GitHub Docs, and Google SRE knowledge capture guidance
source_manifests:
  - documentation__diataxis.md
  - governance__github_docs.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Purpose

Capture a stable answer, procedure, or reference that can be reused by humans and agents. This template applies the Diataxis how-to and reference patterns to produce knowledge base articles that are scopeable, searchable, and maintainable.

## Article Metadata

Fill in all metadata fields before publishing the article. Metadata drives search, freshness tracking, and ownership routing.

| Field | Value |
|---|---|
| Article ID | `{{ARTICLE_ID}}` |
| Title | `{{ARTICLE_TITLE}}` |
| Article type | `{{ARTICLE_TYPE}}` — one of: `how-to`, `reference`, `explanation` |
| Audience | `{{AUDIENCE}}` (e.g., platform engineers, on-call operators, new contributors) |
| Last updated | `{{LAST_UPDATED}}` |
| Owner | `{{ARTICLE_OWNER}}` |
| Tags | `{{ARTICLE_TAG_1}}`, `{{ARTICLE_TAG_2}}`, `{{ARTICLE_TAG_N}}` |

The article type determines the structure used in the Main Content section. Choose the type that best matches the reader's intent: `how-to` for task completion, `reference` for lookup, `explanation` for background understanding.

## Problem Statement

State the question or problem this article answers. Be specific: a reader scanning the article title and problem statement should immediately know whether this article is relevant to their situation.

`{{PROBLEM_STATEMENT}}`

Example pattern: "This article explains how to `{{GOAL}}` when `{{CONDITION}}`. It applies to `{{SCOPE}}` and assumes `{{BASELINE_KNOWLEDGE}}`."

## Prerequisites

List everything the reader must have in place before starting. Each prerequisite should be independently verifiable.

- `{{PREREQUISITE_1}}`
- `{{PREREQUISITE_2}}`
- `{{PREREQUISITE_N}}`

If no prerequisites apply, write "None." Do not omit this section — its absence signals to the reader that they can begin without preparation.

## Main Content

The content structure depends on the article type selected in Article Metadata.

---

### If article type is `how-to`: Procedure

Provide numbered steps. Each step is one action. State the expected outcome after steps where an intermediate state needs to be verified.

1. `{{STEP_1}}`
   - Expected outcome: `{{EXPECTED_OUTCOME_1}}`
2. `{{STEP_2}}`
   - Expected outcome: `{{EXPECTED_OUTCOME_2}}`
3. `{{STEP_N}}`
   - Expected outcome: `{{EXPECTED_OUTCOME_N}}`

After the final step, state the overall expected outcome: `{{FINAL_EXPECTED_OUTCOME}}`.

---

### If article type is `reference`: Structured entries

Organize reference content in consistent, predictable entries. Each entry covers one concept, parameter, command, or configuration item.

**`{{ENTRY_NAME_1}}`**
- Description: `{{ENTRY_DESCRIPTION_1}}`
- Type / format: `{{ENTRY_TYPE_1}}`
- Default: `{{ENTRY_DEFAULT_1}}`
- Constraints: `{{ENTRY_CONSTRAINTS_1}}`
- Example: `{{ENTRY_EXAMPLE_1}}`

**`{{ENTRY_NAME_N}}`**
- Description: `{{ENTRY_DESCRIPTION_N}}`
- Type / format: `{{ENTRY_TYPE_N}}`
- Default: `{{ENTRY_DEFAULT_N}}`
- Constraints: `{{ENTRY_CONSTRAINTS_N}}`
- Example: `{{ENTRY_EXAMPLE_N}}`

---

### If article type is `explanation`: Concept → Context → Implications

Present background knowledge in three layers. Do not include step-by-step instructions here; link to related how-to articles instead.

**Concept**

`{{CONCEPT_DESCRIPTION}}` — what this thing is and how it works at a fundamental level.

**Context**

`{{CONTEXT_DESCRIPTION}}` — why this concept exists in `{{REPOSITORY_NAME}}`, what problem it solves, and how it relates to other concepts.

**Implications**

`{{IMPLICATIONS_DESCRIPTION}}` — what the reader should take away; trade-offs, constraints, and design decisions that flow from this concept.

---

## Troubleshooting

List known failure modes, their likely causes, and resolutions. Add a row whenever a recurring issue is identified in production or support.

| Symptom | Likely cause | Resolution |
|---|---|---|
| `{{SYMPTOM_1}}` | `{{CAUSE_1}}` | `{{RESOLUTION_1}}` |
| `{{SYMPTOM_2}}` | `{{CAUSE_2}}` | `{{RESOLUTION_2}}` |
| `{{SYMPTOM_N}}` | `{{CAUSE_N}}` | `{{RESOLUTION_N}}` |

If no troubleshooting entries exist yet, write "No known issues." and create a task to populate this section after the article enters production use.

## Related Articles

Link to articles that provide adjacent context, prerequisites, or follow-on tasks.

- `{{RELATED_ARTICLE_1}}`
- `{{RELATED_ARTICLE_2}}`
- `{{RELATED_ARTICLE_N}}`

## Feedback

If this article does not answer your question or contains an error, report it via `{{FEEDBACK_CHANNEL}}`. Include the article ID (`{{ARTICLE_ID}}`) in your feedback so it can be routed to the correct owner.

## Review History

Track each review of this article. A review confirms that the content is still accurate; it does not require changes.

| Reviewed by | Review date | Outcome | Notes |
|---|---|---|---|
| `{{REVIEWER}}` | `{{REVIEW_DATE}}` | `{{REVIEW_OUTCOME}}` | `{{REVIEW_NOTES}}` |

Reviews are required at the cadence set by the owning document type in the Documentation Review and Ownership Matrix.

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md, operations__google_sre.md
- Primary source basis: Diataxis, GitHub Docs, and Google SRE knowledge capture guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
