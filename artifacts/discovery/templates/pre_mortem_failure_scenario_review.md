---
title: Pre-mortem / Failure Scenario Review Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: discovery and risk anticipation
source_basis: Google SRE and Microsoft Learn failure-mode anticipation guidance
source_manifests:
  - operations__google_sre.md
  - platform__microsoft_learn.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Pre-mortem - `{{SCENARIO_NAME}}`

- **Scenario:** `{{SCENARIO_DESCRIPTION}}`
- **Likely failure signals:** `{{FAILURE_SIGNALS}}`
- **Blast radius:** `{{BLAST_RADIUS}}`
- **Preventive actions:** `{{PREVENTIVE_ACTIONS}}`
- **Recovery anchors:** `{{RECOVERY_ANCHORS}}`

### Failure modes

| Failure mode | Trigger | Impact | Mitigation |
|---|---|---|---|
| `{{FAILURE_MODE_1}}` | `{{TRIGGER_1}}` | `{{IMPACT_1}}` | `{{MITIGATION_1}}` |
| `{{FAILURE_MODE_2}}` | `{{TRIGGER_2}}` | `{{IMPACT_2}}` | `{{MITIGATION_2}}` |

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__microsoft_learn.md`
- Primary source basis: Google SRE pre-mortem thinking and Microsoft Learn risk analysis guidance
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
