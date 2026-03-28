---
title: Service Configuration / Asset Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: service configuration and asset traceability
source_basis: ITIL
source_manifests:
  - service_mgmt__itil.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Service Configuration / Asset Record

## Purpose

Track the configuration items (CIs) and managed assets supporting a service, providing traceability for change management and incident diagnosis (ITIL 4 Configuration Management / CMDB).

## CI / Asset Metadata

| Field | Value |
|---|---|
| CI ID | `{{CI_ID}}` (e.g., CI-2026-0042) |
| CI Name | `{{CI_NAME}}` |
| CI Type | `{{CI_TYPE}}` (Application / Infrastructure / Network / Service / Document / Process) |
| Status | `{{CI_STATUS}}` (Ordered / In Test / Live / Retired / Decommissioned) |
| Environment | `{{CI_ENVIRONMENT}}` (Production / Staging / Development / DR) |
| Owner | `{{CI_OWNER}}` |
| Managed By | `{{CI_MANAGED_BY}}` |
| Record Created | `{{RECORD_CREATED_DATE}}` |
| Last Reviewed | `{{LAST_REVIEWED_DATE}}` |

## Configuration Attributes

| Attribute | Value |
|---|---|
| Version / Build | `{{CI_VERSION}}` |
| Hostname / Identifier | `{{CI_HOSTNAME}}` |
| Location | `{{CI_LOCATION}}` (physical: `{{PHYSICAL_LOCATION}}` / cloud: `{{CLOUD_REGION}}`) |
| IP Address / Endpoint | `{{CI_ENDPOINT}}` |
| Operating System / Platform | `{{CI_PLATFORM}}` |
| Vendor | `{{CI_VENDOR}}` |
| Support Contract | `{{SUPPORT_CONTRACT_REF}}` |
| License Information | `{{LICENSE_INFO}}` |

## Configuration Baseline

**Baseline version**: `{{BASELINE_VERSION}}`

**Baseline date**: `{{BASELINE_DATE}}`

**Baseline hash / digest**: `{{BASELINE_HASH}}`

Description of baseline configuration: `{{BASELINE_DESCRIPTION}}`

## Relationships and Dependencies

| Relationship Type | Related CI / Service | CI ID | Impact Direction |
|---|---|---|---|
| `{{REL_TYPE_1}}` (e.g., Depends on) | `{{RELATED_CI_1}}` | `{{RELATED_CI_1_ID}}` | `{{IMPACT_DIRECTION_1}}` |
| `{{REL_TYPE_2}}` (e.g., Supports) | `{{RELATED_CI_2}}` | `{{RELATED_CI_2_ID}}` | `{{IMPACT_DIRECTION_2}}` |
| `{{REL_TYPE_3}}` (e.g., Hosted on) | `{{RELATED_CI_3}}` | `{{RELATED_CI_3_ID}}` | `{{IMPACT_DIRECTION_3}}` |

Relationship types: Depends on / Supports / Hosted on / Component of / Connects to / Backs up

## Change History

| Date | Change Description | Change ID | Changed By |
|---|---|---|---|
| `{{CHANGE_DATE_1}}` | `{{CHANGE_DESC_1}}` | `{{CHANGE_ID_1}}` | `{{CHANGED_BY_1}}` |

## Linked Records

| Record Type | Link |
|---|---|
| Service Catalog Entry | `{{SERVICE_CATALOG_LINK}}` |
| Incident History | `{{INCIDENT_HISTORY_LINK}}` |
| Change Records | `{{CHANGE_RECORDS_LINK}}` |
| Problem Records | `{{PROBLEM_RECORDS_LINK}}` |

## Source Attribution

- Source manifests: `service_mgmt__itil.md`
- Primary source basis: ITIL configuration and asset management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
