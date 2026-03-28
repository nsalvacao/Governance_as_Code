---
title: Release Checklist Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{DELIVERY_OWNER}}"
review_cadence: quarterly
applies_to: release readiness checks
source_basis: Standard pre/during/post deployment gates aligned with SRE and DORA practices
source_manifests:
  - governance__github_docs.md
  - operations__google_sre.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Release Checklist - `{{RELEASE_ID}}`

Complete every gate before progressing to the next phase. Mark each item as done, pending, or N-A with justification. The release manager must sign off before deployment begins. Any unresolved blocking item halts the release.

---

### 1. Release Metadata

| Field | Value |
|---|---|
| Release ID | `{{RELEASE_ID}}` |
| Version | `{{VERSION}}` |
| Release date | `{{RELEASE_DATE}}` |
| Release manager | `{{RELEASE_MANAGER}}` |
| Target environment | `{{TARGET_ENVIRONMENT}}` |
| Change record | `{{CHANGE_RECORD_ID}}` |
| Rollback plan reference | `{{ROLLBACK_PLAN_REFERENCE}}` |

---

### 2. Pre-Deployment Checklist

Complete all items before opening the deployment window. Items marked N-A require a written justification in the notes column.

| Item | Owner | Status | Notes |
|---|---|---|---|
| Code review complete and approved | `{{OWNER_CODE_REVIEW}}` | [pending / done / N-A] | |
| All automated tests passing | `{{OWNER_TESTS}}` | [pending / done / N-A] | |
| Security scan clean (SAST/DAST/SCA) | `{{OWNER_SECURITY}}` | [pending / done / N-A] | |
| Dependencies reviewed for vulnerabilities | `{{OWNER_DEPS}}` | [pending / done / N-A] | |
| Documentation updated (API, runbook, user docs) | `{{OWNER_DOCS}}` | [pending / done / N-A] | |
| Stakeholders notified of upcoming release | `{{OWNER_COMMS}}` | [pending / done / N-A] | |
| Rollback plan reviewed and tested | `{{OWNER_ROLLBACK}}` | [pending / done / N-A] | |
| Monitoring and alerting configured | `{{OWNER_MONITORING}}` | [pending / done / N-A] | |
| Feature flags configured correctly | `{{OWNER_FLAGS}}` | [pending / done / N-A] | |
| Database migrations reviewed and reversible | `{{OWNER_DB}}` | [pending / done / N-A] | |
| On-call notified and available | `{{ON_CALL_CONTACT}}` | [pending / done / N-A] | |
| Deployment pipeline validated in staging | `{{OWNER_PIPELINE}}` | [pending / done / N-A] | |

Release manager sign-off (pre-deployment): `{{RELEASE_MANAGER}}` — `{{PRE_DEPLOY_SIGN_OFF_DATE}}`

---

### 3. Deployment Checklist

Track each step during the deployment itself. Record the actual time and result for each step.

| Step | Description | Expected result | Actual result | Time | Status |
|---|---|---|---|---|---|
| `{{DEPLOY_STEP_1}}` | `{{DEPLOY_STEP_1_DESC}}` | `{{DEPLOY_EXPECTED_1}}` | `{{DEPLOY_ACTUAL_1}}` | `{{DEPLOY_TIME_1}}` | [pending / done / failed] |
| `{{DEPLOY_STEP_2}}` | `{{DEPLOY_STEP_2_DESC}}` | `{{DEPLOY_EXPECTED_2}}` | `{{DEPLOY_ACTUAL_2}}` | `{{DEPLOY_TIME_2}}` | [pending / done / failed] |
| `{{DEPLOY_STEP_N}}` | `{{DEPLOY_STEP_N_DESC}}` | `{{DEPLOY_EXPECTED_N}}` | `{{DEPLOY_ACTUAL_N}}` | `{{DEPLOY_TIME_N}}` | [pending / done / failed] |

If any step fails, invoke the rollback trigger defined in the release plan. Record the failure in the change record before initiating rollback.

---

### 4. Post-Deployment Checklist

Complete all items after deployment and before closing the change record.

#### Smoke tests

| Smoke test | Expected result | Actual result | Verified by |
|---|---|---|---|
| `{{SMOKE_TEST_1}}` | `{{SMOKE_EXPECTED_1}}` | `{{SMOKE_ACTUAL_1}}` | `{{SMOKE_VERIFIER_1}}` |
| `{{SMOKE_TEST_2}}` | `{{SMOKE_EXPECTED_2}}` | `{{SMOKE_ACTUAL_2}}` | `{{SMOKE_VERIFIER_2}}` |
| `{{SMOKE_TEST_N}}` | `{{SMOKE_EXPECTED_N}}` | `{{SMOKE_ACTUAL_N}}` | `{{SMOKE_VERIFIER_N}}` |

Smoke tests must cover the critical user journeys for the affected service. A failing smoke test is a rollback trigger unless explicitly scoped as non-critical with documented justification.

#### Monitoring review

| Item | Owner | Status | Notes |
|---|---|---|---|
| Monitoring dashboards reviewed — no anomalies | `{{OWNER_MONITORING_POST}}` | [pending / done / N-A] | |
| Error rate within acceptable threshold | `{{OWNER_ERRORS}}` | [pending / done / N-A] | |
| Latency within acceptable threshold | `{{OWNER_LATENCY}}` | [pending / done / N-A] | |
| No unexpected alerts firing | `{{OWNER_ALERTS}}` | [pending / done / N-A] | |

#### Stakeholder notification

| Stakeholder | Channel | Notified at | Owner |
|---|---|---|---|
| `{{STAKEHOLDER_1}}` | `{{CHANNEL_1}}` | `{{NOTIFIED_AT_1}}` | `{{NOTIF_OWNER_1}}` |
| `{{STAKEHOLDER_2}}` | `{{CHANNEL_2}}` | `{{NOTIFIED_AT_2}}` | `{{NOTIF_OWNER_2}}` |

---

### 5. Sign-Off

The release manager must confirm all blocking items are resolved before the change record is closed. Any open items must be tracked as follow-up actions.

| Role | Name | Sign-off date | Outcome |
|---|---|---|---|
| Release manager | `{{RELEASE_MANAGER}}` | `{{SIGN_OFF_DATE}}` | [success / partial success / rolled back] |
| Technical lead | `{{TECHNICAL_LEAD}}` | `{{TECH_SIGN_OFF_DATE}}` | [confirmed / exceptions noted] |

**Open items / follow-up actions:**
- `{{FOLLOW_UP_ITEM_1}}` — owner: `{{FOLLOW_UP_OWNER_1}}`
- `{{FOLLOW_UP_ITEM_2}}` — owner: `{{FOLLOW_UP_OWNER_2}}`

**Change record closure reference:** `{{CHANGE_RECORD_ID}}`
**PIR required:** [yes / no] — if yes, PIR reference: `{{PIR_REFERENCE}}`

---

## Source Attribution

- Source manifests: `governance__github_docs.md`, `operations__google_sre.md`
- Primary source basis: Standard pre/during/post deployment gates aligned with SRE and DORA practices
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
