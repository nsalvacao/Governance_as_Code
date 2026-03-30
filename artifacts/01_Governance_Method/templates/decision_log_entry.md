---
title: "{{DECISION_TITLE}}"
artifact_type: decision_log_entry
status: public
visibility: public
classification: public
owner: "{{OWNER}}"
review_cadence: "{{REVIEW_CADENCE}}"
applies_to: "{{APPLIES_TO}}"
source_basis: GitHub Docs community governance guidance; AWS Well-Architected ADR process; Microsoft Learn incident and readiness reviews
source_manifests:
  - governance__github_docs.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
decision_log_id: "DL-{{DECISION_SEQUENCE}}"
decision_date: "{{DECISION_DATE}}"
linked_adr: "{{ADR_REFERENCE}}"
---

## Entry Header

<!-- Populate these fields before submitting the entry for review. The ID must be the next sequential DL- number in the log. -->

| Field | Value |
|---|---|
| ID | `{{DL_ID}}` |
| Date | `{{DATE}}` |
| Status | `{{STATUS}}` <!-- proposed \| accepted \| superseded \| revoked --> |
| Owner | `{{OWNER}}` |

## Context

{{CONTEXT}}

<!-- Describe the situation that forced the decision. What changed in the environment, requirements, or constraints that made this decision necessary? Keep this to 2–4 sentences. -->

## Concern

{{CONCERN}}

<!-- State the quality attribute or constraint at stake. What would break or degrade without a clear decision here? Examples: security posture, deployment frequency, maintainability, cost control. -->

## Decision

{{DECISION}}

<!-- State the chosen option clearly and unambiguously. Write in plain language so it can be read without additional context. -->

## Rationale

{{RATIONALE}}

<!-- Explain why this option was chosen over the alternatives. Reference the linked ADR for full options analysis. Keep this focused on the decisive factors. -->

## Consequences

{{CONSEQUENCES}}

<!-- List the trade-offs accepted and any follow-up actions required as a result of this decision. Include known risks and mitigation steps. -->

## Y-Statement Summary

<!-- The Y-Statement provides a one-sentence structured summary of the decision and its trade-off. Complete all five slots. -->

> In the context of `{{SITUATION}}`, facing `{{CONCERN}}`, we decided `{{OPTION}}`, to achieve `{{QUALITY}}`, accepting `{{DOWNSIDE}}`.

## Related ADRs

<!-- List all ADRs that provide the full context and options analysis for this decision. -->

* `{{RELATED_ADR_1}}` — {{BRIEF_RELATION_DESCRIPTION}}
* `{{RELATED_ADR_2}}` — {{BRIEF_RELATION_DESCRIPTION}}

## Review Date

Next review: `{{REVIEW_DATE}}`

<!-- Set this to the date when this decision should be re-evaluated. Use the review_cadence from the frontmatter as the default interval. -->

## Source Attribution

- Source manifests: governance__github_docs.md, platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: GitHub governance docs plus AWS/Microsoft guidance on decision records and reviews
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
