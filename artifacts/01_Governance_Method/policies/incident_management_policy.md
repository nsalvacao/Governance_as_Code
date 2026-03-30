---
title: Incident Management Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident handling and escalation
source_basis: NIST SP 800-61r3, Google SRE incident management guidance, AWS operational readiness guidance
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Policy Statement

Define a deterministic incident-management model that makes roles, severity, escalation, and recovery decisions explicit. All teams operating services within scope of `{{OWNER_NAME}}` must follow this policy for any event that disrupts or risks disrupting service availability, integrity, or confidentiality.

## Policy Scope

This policy applies to `{{SCOPE_SERVICES}}` and all personnel involved in designing, operating, or supporting those services. It covers all incident types from initial detection through resolution and post-incident review. Exceptions require written approval from `{{POLICY_OWNER}}`.

## Severity Levels

Severity classification drives response urgency, escalation, and postmortem requirements. Assign the highest applicable level at declaration time; downgrade as facts emerge.

| Severity | Definition | Response SLA |
|----------|-----------|--------------|
| SEV1 | `{{SEV1_DEFINITION}}` — complete outage or data loss affecting all users | `{{SEV1_TTR_TARGET}}` |
| SEV2 | `{{SEV2_DEFINITION}}` — significant degradation affecting a major feature or user segment | `{{SEV2_TTR_TARGET}}` |
| SEV3 | `{{SEV3_DEFINITION}}` — partial impact on a non-critical path; workaround available | `{{SEV3_TTR_TARGET}}` |
| SEV4 | `{{SEV4_DEFINITION}}` — minor issue with negligible user impact; handled in normal work queue | `{{SEV4_TTR_TARGET}}` |

Severity is declared by the first responder and ratified by the Incident Commander. Reclassification must be logged with justification.

## Incident Commander Role

The Incident Commander (IC) owns the incident from declaration to closure. Every declared incident must have exactly one IC at all times.

**Responsibilities:**
- Declares the incident and assigns initial severity.
- Drives resolution by coordinating the Operations Lead and Communications Lead.
- Holds final decision authority (`{{IC_AUTHORITY}}`) on escalation, rollback, and customer notification timing.
- Maintains incident channel discipline: all updates flow through the IC or a delegate.
- Initiates and chairs the postmortem when required.

**Qualification:** The IC must have completed IC training `{{IC_TRAINING_REQUIREMENT}}` and appear on the current on-call rotation.

## Communications Lead Role

The Communications Lead manages all external and stakeholder communications during an active incident.

**Responsibilities:**
- Drafts and publishes status page updates and customer-facing messages.
- Ensures internal stakeholders (`{{STAKEHOLDER_LIST}}`) receive updates at the cadence defined in the incident communications plan.
- Owns the communication log for the incident record.
- Coordinates with legal and support teams before public disclosure of security-related incidents.

## Operations Lead Role

The Operations Lead executes hands-on remediation under IC direction.

**Responsibilities:**
- Follows the relevant service playbook and runbook steps.
- Coordinates technical responders and assigns investigation tasks.
- Reports status and blockers to the IC at every update interval.
- Documents all changes made during the incident in the incident timeline.

## Escalation Policy

Escalation triggers must be checked at every status update cycle.

| Severity | Escalation Target | Trigger |
|----------|------------------|---------|
| SEV1 | `{{SEV1_ESCALATION}}` | Auto-escalate at declaration; no manual gate |
| SEV2 | `{{SEV2_ESCALATION}}` | Escalate if uncontained after `{{SEV2_ESCALATION_WINDOW}}` |
| SEV3 | `{{SEV3_ESCALATION}}` | IC discretion; escalate if scope grows |
| SEV4 | Normal ticket queue | No escalation required |

The IC must notify the escalation target immediately; waiting for situation clarity is not acceptable for SEV1.

## IC Handoff Procedure

Incidents lasting longer than `{{MAX_IC_DURATION}}` must rotate the IC role to prevent fatigue errors.

**Handoff criteria (`{{HANDOFF_CRITERIA}}`):**
1. Incoming IC reviews the incident channel and current status summary.
2. Outgoing IC verbally confirms open actions, current hypothesis, and next decision point.
3. Handoff is logged in the incident channel with timestamp and both IC names.
4. No handoff during an active remediation step — wait for a safe checkpoint.

## Postmortem Requirements

| Severity | Postmortem Required |
|----------|---------------------|
| SEV1 | Always; must be published within `{{SEV1_POSTMORTEM_SLA}}` |
| SEV2 | Required if the incident was novel, caused unexpected data impact, or revealed a process gap |
| SEV3 | At IC discretion; encouraged when root cause is unclear |
| SEV4 | Not required |

Postmortems must be blameless, link to the incident report and timeline, and produce at least one tracked action item. See the postmortem template for structure.

## SLA for Incident Resolution

Time-to-Resolve (TTR) targets begin at incident declaration, not at detection.

| Severity | TTR Target |
|----------|-----------|
| SEV1 | `{{SEV1_TTR_TARGET}}` |
| SEV2 | `{{SEV2_TTR_TARGET}}` |
| SEV3 | `{{SEV3_TTR_TARGET}}` |
| SEV4 | `{{SEV4_TTR_TARGET}}` |

Misses against TTR targets must be documented in the incident report and reviewed during the next operational review cycle.

## Policy Enforcement

Compliance is verified quarterly by `{{POLICY_REVIEWER}}` using the incident record audit process. Non-compliance is escalated to `{{COMPLIANCE_ESCALATION_TARGET}}`.

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md, platform__aws_well_architected.md
- Primary source basis: NIST SP 800-61r3, Google SRE incident management guidance, AWS operational readiness guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
