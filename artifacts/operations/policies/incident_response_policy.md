---
title: Incident Response Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: cross-repository services
source_basis: NIST SP 800-61r3, Google SRE Incident Management Guide, AWS Operational Readiness
source_manifests: operations__nist_cisa.md, operations__google_sre.md, platform__aws_well_architected.md, platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Policy Statement
We commit to a standardized, policy-driven incident response approach so that every service activation can rely on deterministic actions, clearly defined roles, and automation-friendly artifacts. We treat incidents as operational learning events rather than failures.

## Scope
- Applies to `{{SERVICE_NAME}}` and any downstream repositories inheriting this governance baseline.
- Covers incidents classified by impact class (`{{IMPACT_CLASS}}`) and severity (`{{SEVERITY_LEVEL}}`) per the taxonomy described in this policy.

## Roles & Responsibilities
- Incident Commander: `{{INCIDENT_COMMANDER}}` (authorizes status, approves escalations, and owns triage decisions).
- Communications Lead: `{{COMMUNICATIONS_LEAD}}` (coordinates stakeholder updates and external messaging).
- Operations Lead: `{{OPERATIONS_LEAD}}` (orchestrates technical recovery and runbook execution).
- Support roster entries must rotate per the on-call schedule documented elsewhere and must keep `{{CONTACT_ALIAS}}` reachable.

## Policy Requirements
1. Respond within the response window defined by `{{RESPONSE_WINDOW_MINUTES}}`.
2. Capture actionable facts in the incident report template before any post-incident meeting.
3. Follow the incident playbook standard for investigation, communications, and service recovery playbooks.
4. Document every escalation via the escalation playbook template and tie it to affected systems (`{{SYSTEMS_AFFECTED}}`) and recovery targets (`{{RECOVERY_WINDOW_HOURS}}`).
5. Post-incident work must produce a postmortem using the reliability templates and reference the error budget policy when impact exceeds `{{ERROR_BUDGET_THRESHOLD}}`.

## Automation & AI Notes
- Use the automation validator workflow to confirm that incident artifacts include required metadata.
- Template placeholders align with the source attribution standard so AI agents can auto-fill context with `{{EVENT_ID}}`, `{{IMPACT_CLASS}}`, and `{{RECOVERY_TARGET}}`.
- Issue templates and workflows should trigger this policy enforcement as part of incident intake (see `.github/ISSUE_TEMPLATE/incident_report.yml`).

## Source Attribution
- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: NIST SP 800-61r3, Google SRE Incident Management Guide, AWS Operational Readiness, Microsoft Learn continuity guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
