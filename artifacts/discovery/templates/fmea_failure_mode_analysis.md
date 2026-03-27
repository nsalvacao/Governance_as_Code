---
title: FMEA / Failure Mode Analysis Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: failure mode analysis and mitigation planning
source_basis: Microsoft Learn risk analysis guidance and NIST-informed failure analysis patterns
source_manifests:
  - platform__microsoft_learn.md
  - operations__nist_cisa.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## FMEA - `{{SYSTEM_OR_PROCESS_NAME}}`

| Failure mode | Cause | Effect | Severity | Occurrence | Detectability | RPN | Mitigation |
|---|---|---|---|---|---|---|---|
| `{{FAILURE_MODE_1}}` | `{{CAUSE_1}}` | `{{EFFECT_1}}` | `{{SEVERITY_1}}` | `{{OCCURRENCE_1}}` | `{{DETECTABILITY_1}}` | `{{RPN_1}}` | `{{MITIGATION_1}}` |
| `{{FAILURE_MODE_2}}` | `{{CAUSE_2}}` | `{{EFFECT_2}}` | `{{SEVERITY_2}}` | `{{OCCURRENCE_2}}` | `{{DETECTABILITY_2}}` | `{{RPN_2}}` | `{{MITIGATION_2}}` |

### Review rules

- Recalculate severity when the system changes.
- Escalate high-RPN items into the backlog or decision log.
- Connect each mitigation to an owner and validation check.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__nist_cisa.md`
- Primary source basis: Microsoft risk analysis guidance with NIST-informed failure analysis patterns
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
