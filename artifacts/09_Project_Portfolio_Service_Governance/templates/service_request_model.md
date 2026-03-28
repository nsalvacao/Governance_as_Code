---
title: Service Request Model / Request Catalog
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: repeatable service requests and fulfillment paths
source_basis: ITIL
source_manifests:
  - service_mgmt__itil.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Service Request Model / Request Catalog

## Purpose

Define a repeatable service request type with its eligibility criteria, fulfillment workflow, and SLA (ITIL 4 Service Request Management practice — Request Catalog entry).

## Request Model Metadata

| Field | Value |
|---|---|
| Request Model ID | `{{REQUEST_MODEL_ID}}` |
| Request Type Name | `{{REQUEST_TYPE_NAME}}` |
| Service | `{{SERVICE_NAME}}` (as in Service Catalog `{{SERVICE_CATALOG_LINK}}`) |
| Model Owner | `{{MODEL_OWNER}}` |
| Version | `{{MODEL_VERSION}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Status | `{{MODEL_STATUS}}` (Active / Deprecated / Draft) |

## Request Description

**What the request provides**: `{{REQUEST_DESCRIPTION}}`

**Typical use cases**:
- `{{USE_CASE_1}}`
- `{{USE_CASE_2}}`

**What this request does NOT cover**: `{{OUT_OF_SCOPE}}`

## Eligibility

| Criterion | Requirement |
|---|---|
| Who can request | `{{ELIGIBLE_REQUESTERS}}` (e.g., all employees / team members with role `{{REQUIRED_ROLE}}`) |
| Prerequisites | `{{PREREQUISITES}}` (e.g., manager approval, security training completed) |
| Restrictions | `{{RESTRICTIONS}}` |

## Fulfillment Workflow

| Step | Action | Owner | Automation Level | SLA |
|---|---|---|---|---|
| 1 | Request received and acknowledged | `{{INTAKE_OWNER}}` | `{{INTAKE_AUTOMATION}}` | Within `{{ACK_SLA}}` |
| 2 | Eligibility check | `{{ELIGIBILITY_CHECKER}}` | `{{ELIGIBILITY_AUTOMATION}}` | Within `{{ELIGIBILITY_SLA}}` |
| 3 | Approval (if required): `{{APPROVAL_CONDITION}}` | `{{APPROVER}}` | `{{APPROVAL_AUTOMATION}}` | Within `{{APPROVAL_SLA}}` |
| 4 | Fulfillment: `{{FULFILLMENT_ACTION}}` | `{{FULFILLMENT_OWNER}}` | `{{FULFILLMENT_AUTOMATION}}` | See SLA below |
| 5 | Verification and closure | `{{VERIFICATION_OWNER}}` | `{{VERIFICATION_AUTOMATION}}` | Within `{{CLOSURE_SLA}}` |

## Approval Requirements

| Approval Type | Required When | Approver | Escalation if Not Received |
|---|---|---|---|
| `{{APPROVAL_TYPE_1}}` | `{{APPROVAL_CONDITION_1}}` | `{{APPROVER_1}}` | Escalate to `{{ESCALATION_1}}` after `{{ESCALATION_TIMEOUT_1}}` |
| `{{APPROVAL_TYPE_2}}` | `{{APPROVAL_CONDITION_2}}` | `{{APPROVER_2}}` | Escalate to `{{ESCALATION_2}}` after `{{ESCALATION_TIMEOUT_2}}` |

## Service Level

| Metric | Target |
|---|---|
| Acknowledgement | Within `{{ACK_SLA}}` of request submission |
| Standard fulfillment | Within `{{STANDARD_FULFILLMENT_SLA}}` of approval |
| Urgent fulfillment | Within `{{URGENT_FULFILLMENT_SLA}}` — requires `{{URGENT_TRIGGER}}` |
| Availability of request channel | `{{REQUEST_CHANNEL_AVAILABILITY}}` |

## Information Required from Requester

| Field | Required? | Guidance |
|---|---|---|
| `{{REQUIRED_FIELD_1}}` | Yes | `{{FIELD_1_GUIDANCE}}` |
| `{{REQUIRED_FIELD_2}}` | Yes | `{{FIELD_2_GUIDANCE}}` |
| `{{OPTIONAL_FIELD_1}}` | No | `{{OPTIONAL_FIELD_1_GUIDANCE}}` |

## Automation Notes

- Automation level: `{{OVERALL_AUTOMATION_LEVEL}}` (Manual / Semi-automated / Fully automated)
- Automated steps: `{{AUTOMATED_STEPS}}`
- Tool / integration: `{{AUTOMATION_TOOL}}`
- Human-in-the-loop gates: `{{HUMAN_GATES}}`

## Source Attribution

- Source manifests: `service_mgmt__itil.md`
- Primary source basis: ITIL request fulfillment guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
