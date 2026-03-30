---
title: Audit Trail Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: risk-platform
review_cadence: quarterly
applies_to: decisions, changes, exceptions, and governance records
source_basis: NIST auditability and traceability guidance
source_manifests:
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Policy Statement

All material decisions, configuration changes, exceptions, and risk-acceptance actions MUST generate a permanent, tamper-evident audit record in accordance with SOX Section 404, ISO/IEC 27001:2022 Annex A.8.15, and NIST SP 800-92 log management guidelines.

## Scope

This policy applies to:

| Record Category | Examples | Retention Owner |
|---|---|---|
| Governance decisions | ADRs, exception approvals, change records | `{{GOVERNANCE_RECORD_OWNER}}` |
| Infrastructure changes | Deployments, config modifications, access grants | `{{PLATFORM_RECORD_OWNER}}` |
| Security events | Authentication attempts, privilege escalation, policy changes | `{{SECURITY_RECORD_OWNER}}` |
| Risk and compliance | Risk register updates, audit findings, deviation records | `{{RISK_RECORD_OWNER}}` |
| Financial / SOX-relevant | Any change touching financial systems or controls | `{{FINANCE_RECORD_OWNER}}` |

## Audit Record Requirements

Each audit record MUST contain:

| Field | Requirement |
|---|---|
| Record ID | Unique, immutable, system-generated |
| Timestamp | UTC, machine-readable (ISO 8601), `{{TIMESTAMP_PRECISION}}` precision |
| Actor | Authenticated identity (`{{IDENTITY_SOURCE}}` — e.g., SSO, service account) |
| Action | Verb + object (e.g., "approved exception EX-042", "deployed v1.3.0 to production") |
| Affected resource | Path, ARN, or canonical identifier |
| Outcome | Success / Failure / Partial |
| Justification reference | Link to approving ticket, ADR, or change record |
| Previous state | Snapshot or hash of state before change (where applicable) |

## Log Retention

| Record Category | Retention Period | Storage Tier | Immutability |
|---|---|---|---|
| Security audit logs | `{{SECURITY_LOG_RETENTION}}` (e.g., 7 years for SOX) | `{{SECURITY_LOG_STORAGE}}` | Write-once, read-many (WORM) |
| Access logs | `{{ACCESS_LOG_RETENTION}}` | `{{ACCESS_LOG_STORAGE}}` | `{{ACCESS_LOG_IMMUTABILITY}}` |
| Change records | `{{CHANGE_LOG_RETENTION}}` | `{{CHANGE_LOG_STORAGE}}` | Append-only |
| Risk and exception records | `{{RISK_LOG_RETENTION}}` | `{{RISK_LOG_STORAGE}}` | `{{RISK_LOG_IMMUTABILITY}}` |

Retention clock starts at: `{{RETENTION_START_EVENT}}` (e.g., record creation date).

## Access Controls

- Audit logs MUST NOT be modifiable by the actor whose actions they record.
- Log access requires `{{LOG_ACCESS_ROLE}}` role; read-only by default.
- Log deletion requires approval from `{{LOG_DELETION_AUTHORITY}}` and generates its own audit event.
- Export of bulk audit logs requires approval from `{{BULK_EXPORT_AUTHORITY}}`.

## Review and Alerting

| Review Type | Frequency | Owner | Action if Anomaly Detected |
|---|---|---|---|
| Automated integrity check | `{{INTEGRITY_CHECK_FREQUENCY}}` | `{{SIEM_TOOL}}` | Alert `{{SECURITY_ALERT_CONTACT}}` |
| Privileged action review | `{{PRIVILEGED_REVIEW_CADENCE}}` | `{{PRIVILEGED_REVIEWER}}` | Escalate to `{{ESCALATION_CONTACT}}` |
| Quarterly compliance audit | Quarterly | `{{COMPLIANCE_AUDITOR}}` | File corrective action in `{{CORRECTIVE_ACTION_REGISTER}}` |
| Annual external audit | Annual | `{{EXTERNAL_AUDITOR}}` | Report to `{{AUDIT_COMMITTEE}}` |

## Non-repudiation

Audit records for the following actions MUST carry a cryptographic signature or equivalent non-repudiation mechanism:

- `{{NON_REPUDIATION_ACTION_1}}` (e.g., production deployments)
- `{{NON_REPUDIATION_ACTION_2}}` (e.g., privilege escalation approvals)
- `{{NON_REPUDIATION_ACTION_3}}` (e.g., exception approvals above `{{EXCEPTION_RISK_THRESHOLD}}` risk level)

Signing mechanism: `{{SIGNING_MECHANISM}}` (e.g., GPG commit signing, OIDC token, AWS CloudTrail digest).

## Source Attribution

- Source manifests: operations__nist_cisa.md
- Primary source basis: NIST auditability and traceability guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
