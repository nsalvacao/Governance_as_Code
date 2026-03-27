---
title: Rollback / Backout Plan Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: delivery@org
review_cadence: quarterly
applies_to: rollback planning and recovery
source_basis: Google SRE rollback guidance and Microsoft Learn deployment recovery guidance
source_manifests:
  - operations__google_sre.md
  - platform__microsoft_learn.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Rollback Plan - `{{RELEASE_NAME}}`

- **Rollback trigger:** `{{ROLLBACK_TRIGGER}}`
- **Decision owner:** `{{DECISION_OWNER}}`
- **Data impact:** `{{DATA_IMPACT}}`
- **Service impact:** `{{SERVICE_IMPACT}}`
- **Validation steps:** `{{VALIDATION_STEPS}}`

### Steps

1. Stop the rollout.
2. Restore the prior known-good state.
3. Validate service health.
4. Communicate the outcome.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__microsoft_learn.md`
- Primary source basis: Google SRE rollback and Microsoft recovery guidance
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
