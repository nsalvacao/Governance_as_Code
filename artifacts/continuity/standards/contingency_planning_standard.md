---
title: Contingency Planning Standard
artifact_type: standard
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannually
applies_to: contingency planning
source_basis: NIST SP 800-34 Rev. 1
source_manifests: operations__nist_cisa.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Purpose

This standard defines the requirements for developing, testing, and maintaining contingency plans for all systems in scope. Per NIST SP 800-34 Rev. 1 sections 3–6, contingency planning is the coordinated strategy for recovering or maintaining operations of mission-critical information systems after a disruption. Replace `{{OWNER_NAME}}` with the accountable team or role.

## Contingency Planning Phases

NIST SP 800-34 Rev. 1 organizes contingency planning into five phases; all plans must address each phase explicitly:

1. **Prevention** — controls and redundancies implemented before a disruption to reduce likelihood and impact. Document prevention controls in `{{PREVENTION_CONTROLS_REF}}`.
2. **Detection** — mechanisms that identify a disruption and initiate the notification chain. Detection criteria must be unambiguous and measurable.
3. **Response** — immediate actions taken after detection to limit damage, protect data, and mobilize the recovery team. The response phase ends when the damage assessment is complete and the plan is formally activated.
4. **Recovery** — execution of recovery procedures to restore system functionality to the minimum acceptable level (per BIA RTO). Recovery ends when the system meets the agreed minimum service threshold.
5. **Reconstitution** — restoration of the system to full normal operations, including validation, deactivation of alternate processing arrangements, and lessons-learned capture.

## Plan Types and Applicability

Organizations must select the appropriate plan type(s) based on the system tier and recovery scenario; each acronym is defined below. Select applicable plan types using `{{PLAN_TYPES_APPLICABLE}}`:

| Plan Type | Full Name | Scope |
|---|---|---|
| BCP | Business Continuity Plan | Organization-wide continuity of mission-essential functions during a prolonged disruption |
| ISCP | Information System Contingency Plan | Recovery of a specific information system's hardware, software, and data |
| COOP | Continuity of Operations Plan | Continuation of essential functions at an alternate facility for up to 30 days |
| DRP | Disaster Recovery Plan | IT infrastructure recovery following a major disruption (subset of BCP) |
| CIRP | Cyber Incident Response Plan | Response and recovery specific to cybersecurity incidents |

A single system may require multiple plan types. The BIA system tier `{{SYSTEM_TIER}}` determines which plan types are mandatory.

## Contingency Plan Structure Requirements

Every contingency plan produced under this standard must include the following sections in order; omitted sections must be documented with a rationale:

1. **Supporting information** — plan identification, system description, applicable laws and regulations, and a list of key assumptions `{{ASSUMPTION_N}}`.
2. **Concept of operations** — overview of how the plan will be activated and executed, including the command structure and authority chain `{{ACTIVATION_AUTHORITY}}`.
3. **Notification and activation phase** — step-by-step procedure for detecting a disruption, notifying the recovery team, assessing damage, and making the formal activation decision.
4. **Recovery phase** — detailed recovery procedures organized by priority tier, alternative processing site information `{{ALT_SITE}}`, and minimum resource requirements from the BIA.
5. **Reconstitution phase** — validation criteria `{{VALIDATION_CRITERIA}}` for confirming full restoration, procedures for deactivating alternate arrangements, and lessons-learned process.
6. **Plan appendices** — contact lists, equipment inventories, backup procedures, and any supporting reference material.

## Testing Requirements

All contingency plans must be tested according to the schedule below; test results must be documented in the exercise drill record template. Testing cadences are set by system tier and plan type:

| Test Type | Description | Required Cadence |
|---|---|---|
| Tabletop exercise | Discussion-based walkthrough of plan scenarios with key personnel | `{{TABLETOP_CADENCE}}` |
| Functional exercise | Activation of partial plan components in a controlled environment | `{{FUNCTIONAL_CADENCE}}` |
| Full-scale exercise | Complete activation of the plan, including alternate site and all recovery steps | `{{FULL_SCALE_CADENCE}}` |

Testing must verify that RTO and RPO targets from the BIA can be met. Failures to meet objectives must generate corrective action items tracked to closure.

## Maintenance Requirements

Contingency plans must be reviewed and updated on the schedule `{{ANNUAL_REVIEW_DATE}}` and after any of the following events: a plan activation, a significant change to the system, an organizational change affecting the recovery team, or a test that reveals material gaps. The plan version and change history must be maintained. The plan owner `{{OWNER_NAME}}` is responsible for ensuring the plan reflects the current system state.

## Training Requirements

All personnel with roles in contingency plan execution must complete initial training before being assigned to a recovery team role and annual refresher training thereafter. Training must cover plan activation procedures, individual role responsibilities, and communication protocols. Training completion must be documented and retained for `{{TRAINING_RECORD_RETENTION}}`. New personnel must be trained within `{{NEW_HIRE_TRAINING_WINDOW}}` of assignment.

## Source Attribution

- Source manifests: `operations__nist_cisa.md`
- Primary source basis: NIST SP 800-34 Rev. 1 sections 3–6
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
