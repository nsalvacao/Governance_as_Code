---
title: "{{ADR_TITLE}}"
artifact_type: architectural_decision_record
status: draft
visibility: public
classification: public
owner: "{{OWNER}}"
review_cadence: "{{REVIEW_CADENCE}}"
applies_to: "{{APPLIES_TO}}"
source_basis: AWS Well-Architected ADR process; Microsoft Learn release/incident frameworks
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
adr_id: "ADR-{{ADR_SEQUENCE}}"
decision_date: "{{ADR_DATE}}"
decision_log_link: "{{DECISION_LOG_LINK}}"
supersedes: "{{SUPERSEDES}}"
---

Use this template for every ADR that feeds the canonical decision log. Keep the reasoning explicit, include alternatives, and define the acceptance criteria that anchor downstream automation and compliance checks.

`Architectural Decision Record`

- **Owner**: `{{OWNER}}`
- **Context**: `{{CONTEXT}}`
- **Decision**: `{{DECISION_SUMMARY}}`
- **Alternatives considered**:
  1. `{{ALTERNATIVE_ONE}}`
  2. `{{ALTERNATIVE_TWO}}`
- **Consequences**: `{{CONSEQUENCES}}`
- **Validation**: `{{VALIDATION_APPROACH}}`
- **Review notes**: `{{REVIEW_NOTES}}`
- **Related automation**: `{{AUTOMATION_HOOKS}}`

The template is intentionally metadata-first so AI agents and automation pipelines can evaluate status, owner, and the decision trace without parsing paragraphs. Save the completed ADR in the repository-specific documentation location chosen by the consuming repository (for example, `docs/governance/adr-{{ADR_SEQUENCE}}.md`) and keep it immutable after acceptance.

## Source Attribution

- Source manifests: platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: AWS and Microsoft ADR and release guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
