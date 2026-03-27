---
title: Incident Playbook Standard
artifact_type: standard
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident responders
source_basis: Google SRE Incident Management Guide, NIST SP 800-61r3
source_manifests: operations__google_sre.md, operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Standard Overview
Playbooks must be modular, short-lived, and automatable. Each playbook adheres to the `{{IMPACT_CLASS}}` taxonomy and references the relevant incident report, timeline, escalation, and service recovery templates.

## Playbook Structure
1. **Trigger** – specify `{{TRIGGER_EVENT}}` and detection source.
2. **Roles** – list the Incident Commander, Communications Lead, and Operations Lead with their contact placeholders.
3. **Impact** – record the impact class, severity, and affected systems.
4. **Investigation steps** – include automation hooks (scripts, queries) that can be invoked to gather facts.
5. **Communications** – link to the `incident_communications.md` template for external/internal messages.
6. **Escalation** – cite the escalation template for decision thresholds and approvers.
7. **Recovery** – describe recovery targets, runbook steps, and mitigation tactics tied to the service recovery template.
8. **Learning** – define follow-up actions and link to the postmortem process.

## Automation Guidance
- Each playbook must expose inputs compatible with GitHub Actions or AI assistants (e.g., `{{INCIDENT_ID}}`, `{{COMM_CHANNEL}}`, `{{ESCALATION_THRESHOLD}}`).
- Use the automation validator to ensure the playbook file includes frontmatter metadata and source attribution.

## Source Attribution
- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide, NIST SP 800-61r3
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
