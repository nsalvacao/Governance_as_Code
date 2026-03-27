---
title: Release Checklist Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: delivery@org
review_cadence: quarterly
applies_to: release readiness checks
source_basis: GitHub release guidance and Google SRE readiness checks
source_manifests:
  - governance__github_docs.md
  - operations__google_sre.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Release Checklist - `{{RELEASE_NAME}}`

- [ ] Release notes prepared
- [ ] Validation completed
- [ ] Observability confirmed
- [ ] Rollback path tested
- [ ] Communication sent
- [ ] Approvers recorded

### Checklist details

| Check | Owner | Evidence |
|---|---|---|
| `{{CHECK_1}}` | `{{OWNER_1}}` | `{{EVIDENCE_1}}` |
| `{{CHECK_2}}` | `{{OWNER_2}}` | `{{EVIDENCE_2}}` |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `operations__google_sre.md`
- Primary source basis: GitHub release readiness and Google SRE validation practices
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
