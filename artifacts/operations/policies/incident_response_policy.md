---
title: Incident Response Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: cross-repository services
source_basis: NIST SP 800-61r2, Google SRE Incident Management Guide, AWS Operational Readiness
source_manifests: operations__nist_cisa.md, operations__google_sre.md, platform__aws_well_architected.md, platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Policy Statement

We commit to a standardized, policy-driven incident response approach so that every service activation can rely on deterministic actions, clearly defined roles, and automation-friendly artifacts. We treat incidents as operational learning events rather than failures.

## Policy Purpose and Scope

This policy establishes the organization's approach to preparing for, detecting, containing, eradicating, and recovering from security and operational incidents, aligned to the NIST SP 800-61r2 incident response lifecycle.

- Applies to `{{SERVICE_NAME}}` and any downstream repositories inheriting this governance baseline.
- Covers incidents classified by impact class (`{{IMPACT_CLASS}}`) and severity (`{{SEVERITY_LEVEL}}`) per the taxonomy described in this policy.
- All personnel with access to production systems must understand and follow this policy.

## NIST IR Lifecycle Phases

This policy is structured around the four NIST SP 800-61r2 phases. Each phase has entry criteria, required actions, and exit criteria.

### Phase 1 — Preparation

Preparation ensures the organization is ready to respond before incidents occur. Without preparation, every phase that follows is slower and less reliable.

**Incident Response Team (IRT):**
- Composition: `{{IRT_COMPOSITION}}` — roles include Incident Commander, Communications Lead, Operations Lead, and supporting subject-matter experts.
- Contact list location: `{{CONTACT_LIST_LOCATION}}` — must be accessible without production credentials.
- On-call rotation schedule: maintained at `{{ONCALL_SCHEDULE_LOCATION}}` and reviewed monthly.

**Tools and systems that must be ready:**
- `{{TOOL_1}}` — primary incident communication channel
- `{{TOOL_2}}` — monitoring and alerting platform
- `{{TOOL_3}}` — log aggregation and search
- `{{TOOL_N}}` — additional tools as defined by the operations team

**Preparation requirements:**
- All IRT members complete incident response training annually (`{{TRAINING_REQUIREMENT}}`).
- Playbooks exist for all services classified `{{CRITICALITY_THRESHOLD}}` or above.
- Contact list and tools are tested at least `{{PREPAREDNESS_TEST_CADENCE}}`.

### Phase 2 — Detection and Analysis

Incidents are detected through automated monitoring, user reports, or third-party notification. Accurate triage in this phase determines response urgency.

**Detection sources:**
- `{{DETECTION_SOURCE_1}}` — automated monitoring alert
- `{{DETECTION_SOURCE_2}}` — user or customer report
- `{{DETECTION_SOURCE_3}}` — security scanning or threat intelligence
- `{{DETECTION_SOURCE_N}}` — additional sources as configured

**Triage criteria:**
- Assess affected systems (`{{SYSTEMS_AFFECTED}}`), user population, and data sensitivity.
- Classify impact using the severity matrix: SEV1 (complete outage) through SEV4 (minor issue).
- Establish an incident record with `{{INCIDENT_ID}}` format immediately.

**Analysis requirements:**
- Assign an IC within `{{IC_ASSIGNMENT_SLA}}` of incident declaration.
- Document the initial hypothesis and evidence in the incident timeline.
- Preserve original evidence before any remediation actions.

### Phase 3 — Containment, Eradication, and Recovery

Containment limits the damage; eradication removes the cause; recovery restores normal operations. These steps may overlap but must each be explicitly declared complete.

**Short-term containment (`{{SHORT_TERM_CONTAINMENT}}`):**
- Immediate actions to stop ongoing harm without full root-cause analysis.
- Examples: isolate affected components, disable compromised credentials, enable read-only mode.
- Must be reversible where possible; document every change in the incident timeline.

**Evidence preservation requirement:**
- Before eradication, capture forensic evidence: logs, memory snapshots, network captures as appropriate for the incident type.
- Evidence must be stored in `{{EVIDENCE_STORAGE_LOCATION}}` and access-controlled.

**Long-term containment (`{{LONG_TERM_CONTAINMENT}}`):**
- Stabilize the system in a degraded-but-safe state while root cause is fully identified.
- Requires IC approval to transition from short-term to long-term containment.

**Eradication:**
- Identify and eliminate root cause (see root cause identification requirement in Phase 4 preparation).
- System cleaning procedure: `{{SYSTEM_CLEANING_PROCEDURE}}` — document every step taken.
- Verify eradication with at least `{{ERADICATION_VERIFICATION_STEPS}}` independent checks.

**Recovery:**
- Restore services in priority order: `{{RECOVERY_PRIORITY_ORDER}}`.
- Validation criteria before declaring recovery complete: `{{RECOVERY_VALIDATION}}`.
- Monitor for recurrence for at least `{{RECURRENCE_MONITORING_WINDOW}}` after recovery.

### Phase 4 — Post-Incident Activity

Post-incident activities ensure learning is captured and process improvements are implemented. This phase closes the feedback loop.

**Postmortem trigger:**
- SEV1: always required; draft within `{{SEV1_POSTMORTEM_DRAFT_SLA}}`.
- SEV2: required if novel cause, data impact, or process gap identified.
- SEV3: at IC discretion.

**Lessons learned process:**
- Blameless postmortem meeting within `{{POSTMORTEM_MEETING_SLA}}` of incident closure.
- Action items must be tracked in `{{ACTION_ITEM_TRACKER}}` with owners and due dates.
- Lessons learned summary shared with `{{LESSONS_LEARNED_AUDIENCE}}`.

**Policy update process:**
- If the incident reveals a gap in this policy, the IC raises a policy update request to `{{POLICY_OWNER}}` within `{{POLICY_UPDATE_SLA}}`.
- Policy changes are reviewed at the next quarterly review cycle at minimum.

## Roles and Responsibilities

- Incident Commander: `{{INCIDENT_COMMANDER}}` (authorizes status, approves escalations, and owns triage decisions).
- Communications Lead: `{{COMMUNICATIONS_LEAD}}` (coordinates stakeholder updates and external messaging).
- Operations Lead: `{{OPERATIONS_LEAD}}` (orchestrates technical recovery and runbook execution).
- Support roster entries must rotate per the on-call schedule documented at `{{ONCALL_SCHEDULE_LOCATION}}` and must keep `{{CONTACT_ALIAS}}` reachable.

## Policy Requirements

1. Respond within the response window defined by `{{RESPONSE_WINDOW_MINUTES}}`.
2. Capture actionable facts in the incident report template before any post-incident meeting.
3. Follow the incident playbook standard for investigation, communications, and service recovery playbooks.
4. Document every escalation via the escalation playbook template and tie it to affected systems (`{{SYSTEMS_AFFECTED}}`) and recovery targets (`{{RECOVERY_WINDOW_HOURS}}`).
5. Post-incident work must produce a postmortem using the reliability templates and reference the error budget policy when impact exceeds `{{ERROR_BUDGET_THRESHOLD}}`.

## Automation and AI Notes

- Use the automation validator workflow to confirm that incident artifacts include required metadata.
- Template placeholders align with the source attribution standard so AI agents can auto-fill context with `{{EVENT_ID}}`, `{{IMPACT_CLASS}}`, and `{{RECOVERY_TARGET}}`.
- Issue templates and workflows should trigger this policy enforcement as part of incident intake (see `.github/ISSUE_TEMPLATE/incident_report.yml`).

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: NIST SP 800-61r2, Google SRE Incident Management Guide, AWS Operational Readiness, Microsoft Learn continuity guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
