---
title: Problem Management Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: recurring problem analysis and prevention of incident recurrence
source_basis: ITIL, NIST, Google SRE
source_manifests:
  - service_mgmt__itil.md
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Problem Management Policy

This policy defines how recurring problems are identified, prioritized, diagnosed, and tracked to closure.

## Required elements

- problem statement
- affected service or asset
- suspected cause
- impact and recurrence pattern
- workaround or mitigation
- owner and review date

## Operating rules

1. Promote repeated incidents into a problem record when the same failure pattern appears more than once.
2. Separate symptoms, causes, workarounds, and permanent fixes.
3. Link problem records to incident reports, postmortems, and known error records.
4. Keep the policy public-safe and omit sensitive operational details.

## Automation guidance

- Use a consistent problem identifier so AI agents can group related incidents.
- Make recurrence and resolution status machine-readable where possible.

## Source Attribution

- Source manifests: `service_mgmt__itil.md`, `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: ITIL problem management guidance plus NIST and Google SRE operational learning practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
