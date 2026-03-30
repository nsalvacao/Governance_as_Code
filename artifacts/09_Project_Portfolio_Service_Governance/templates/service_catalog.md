---
title: Service Catalog / Service Portfolio Record
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: service offerings and portfolio records
source_basis: ITIL
source_manifests:
  - service_mgmt__itil.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Service Catalog / Service Portfolio Record

## Purpose

Provide the authoritative inventory of services offered, their ownership, scope, and status (ITIL 4 Service Catalog Management practice).

## Catalog Metadata

| Field | Value |
|---|---|
| Catalog Owner | `{{CATALOG_OWNER}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Review Cadence | `{{REVIEW_CADENCE}}` |
| Catalog Location | `{{CATALOG_URL}}` |

## Service Catalog Entry

_One entry per service. Add rows as needed._

| Field | Value |
|---|---|
| Service ID | `{{SERVICE_ID}}` |
| Service Name | `{{SERVICE_NAME}}` |
| Service Description | `{{SERVICE_DESCRIPTION}}` |
| Service Type | `{{SERVICE_TYPE}}` (Business Service / Technical Service / Infrastructure Service) |
| Service Owner | `{{SERVICE_OWNER}}` |
| Service Manager | `{{SERVICE_MANAGER}}` |
| Consumer Group | `{{CONSUMER_GROUP}}` |
| Status | `{{SERVICE_STATUS}}` (Pipeline / Active / Deprecated / Retired) |

## Service Details

**Value proposition**: `{{SERVICE_VALUE_PROPOSITION}}`

**Service hours**: `{{SERVICE_HOURS}}` (e.g., 24×7, Business hours Mon–Fri `{{HOURS_TIMEZONE}}`)

**Planned maintenance windows**: `{{MAINTENANCE_WINDOWS}}`

## Service Level Reference

| SLA / Agreement Type | Reference | Target |
|---|---|---|
| SLA | `{{SLA_LINK}}` | Availability: `{{AVAILABILITY_TARGET}}`%, MTTR: `{{MTTR_TARGET}}` |
| OLA | `{{OLA_LINK}}` | `{{OLA_TARGET}}` |

## Dependencies

| Dependency | Type | Criticality | Owner | Impact if Unavailable |
|---|---|---|---|---|
| `{{DEPENDENCY_1}}` | `{{DEP_1_TYPE}}` | `{{DEP_1_CRITICALITY}}` | `{{DEP_1_OWNER}}` | `{{DEP_1_IMPACT}}` |
| `{{DEPENDENCY_2}}` | `{{DEP_2_TYPE}}` | `{{DEP_2_CRITICALITY}}` | `{{DEP_2_OWNER}}` | `{{DEP_2_IMPACT}}` |

## Service Access and Request

| Method | Details | Link |
|---|---|---|
| Self-service portal | `{{SELF_SERVICE_DESCRIPTION}}` | `{{SELF_SERVICE_URL}}` |
| Service request form | See service request model | `{{REQUEST_MODEL_LINK}}` |
| Emergency contact | `{{EMERGENCY_CONTACT}}` | `{{EMERGENCY_LINK}}` |

## Linked Records

| Record Type | Link |
|---|---|
| Configuration / CMDB Record | `{{CMDB_RECORD_LINK}}` |
| Service Request Model | `{{REQUEST_MODEL_LINK}}` |
| Known Errors (active) | `{{KNOWN_ERRORS_LINK}}` |
| SLA Document | `{{SLA_LINK}}` |
| Runbook | `{{RUNBOOK_LINK}}` |
| Incident Playbook | `{{PLAYBOOK_LINK}}` |

## Lifecycle History

| Date | Change | Changed By |
|---|---|---|
| `{{ENTRY_CREATED_DATE}}` | Service entry created | `{{CATALOG_OWNER}}` |
| `{{LAST_REVIEW_DATE}}` | Annual review completed | `{{REVIEWER}}` |

## Source Attribution

- Source manifests: `service_mgmt__itil.md`
- Primary source basis: ITIL service catalog and service portfolio guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
