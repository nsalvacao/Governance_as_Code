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

## Standard Overview
Contingency plans must exist for critical systems identified in the BIA and describe recovery actions when standard incident responses are insufficient.

## Plan Components
1. **Critical scenarios** – `{{SCENARIO_NAME}}`
2. **Activation criteria** – thresholds for invoking the plan, referencing severity and impact placeholders.
3. **Recovery posture** – alternative resources, failover routes, and manual workarounds.
4. **Command structure** – link to the incident coordination and escalation templates.
5. **Communications** – tie to the incident communications template for stakeholder updates.

## Automation Guidance
- Plans should reference automation scripts stored in `scripts/` or `.github/workflows/`.
- Include `{{AUTOMATION_TRIGGERS}}` so AI agents can surface the correct plan during automation runs.

## Source Attribution
- Source manifests: `operations__nist_cisa.md`
- Primary source basis: NIST SP 800-34 Rev. 1
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
