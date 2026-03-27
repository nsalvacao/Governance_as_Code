---
title: "{{DECISION_TITLE}}"
artifact_type: decision_log_entry
status: draft
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
updated: 2026-03-27
decision_log_id: "DL-{{DECISION_SEQUENCE}}"
decision_date: "{{DECISION_DATE}}"
linked_adr: "{{ADR_REFERENCE}}"
---

Use this template to add a `DL-` entry to the shared decision log. Keep the context short, capture the accepted outcome, and trace the governing source(s).

- **Owner**: `{{OWNER}}`
- **Context**: `{{BRIEF_CONTEXT}}`
- **Decision**: `{{DECISION_SUMMARY}}`
- **Consequences**: `{{CONSEQUENCES}}`
- **Supersedes**: `{{SUPERSEDES}}` (leave blank if none)
- **Review trigger**: `{{NEXT_REVIEW}}`
- **Linked ADR**: `{{ADR_REFERENCE}}`

Downstream automation (AI or scripts) should parse these fields, apply the schema, and update `decision_log.md` using the ordering rules defined in `decision_log_standard.md`.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: GitHub governance docs plus AWS/Microsoft guidance on decision records and reviews
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
