---
title: Business Impact Analysis Standard
artifact_type: standard
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannually
applies_to: continuity planning
source_basis: NIST SP 800-34 Rev. 1
source_manifests: operations__nist_cisa.md, platform__aws_well_architected.md, operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

This standard defines when and how a Business Impact Analysis (BIA) must be performed as a prerequisite to contingency planning. Per NIST SP 800-34 Rev. 1 section 2.2, the BIA is the foundational input that drives all recovery targets and system tier assignments across the contingency planning lifecycle. Replace `{{OWNER_NAME}}` with the accountable team or role.

## Scope of BIA in the Contingency Planning Lifecycle

The BIA establishes the business criticality baseline from which all contingency plans, recovery objectives, and resource allocations derive. It must be completed before drafting any contingency plan (BCP, ISCP, COOP, DRP, or CIRP) and must be refreshed whenever system scope or business context changes materially. The BIA scope covers all systems and functions identified in `{{SCOPE_STATEMENT}}`.

## When BIA Is Required

A BIA is required in the following circumstances; document the triggering condition using `{{BIA_TRIGGER}}`:

- Initial system authorization or registration in the system inventory.
- Significant change to system functionality, architecture, or data classification.
- Change in system categorization (e.g., FIPS 199 impact level adjustment).
- Annual review cycle per `{{REVIEW_CADENCE}}`.
- Post-incident findings that reveal unanalyzed critical dependencies.
- Organizational restructuring that alters mission ownership.

System categorization changes are the most common trigger. The BIA drives the system tier `{{SYSTEM_TIER}}` (e.g., Tier 1 Mission Critical, Tier 2 Essential, Tier 3 Supporting), which in turn determines the required depth and testing frequency for associated contingency plans.

## Required BIA Outputs

Every completed BIA must produce the following outputs; incomplete BIAs must not be used to set contractual or regulatory recovery commitments:

1. **Mission-critical function list** — an enumerated list of all functions performed by or dependent on the system, with a criticality designation for each.
2. **Recovery Time Objective (RTO) per function** — the maximum acceptable duration from disruption to restoration of minimum acceptable service levels; expressed as `{{RTO}}`.
3. **Recovery Point Objective (RPO) per function** — the maximum acceptable data loss measured in time; expressed as `{{RPO}}`.
4. **Maximum Tolerable Downtime (MTD) per function** — the absolute outer bound beyond which business impact becomes unacceptable regardless of workarounds; MTD must be greater than or equal to RTO.
5. **Resource dependency map** — all people, infrastructure, data, and third-party services required to sustain each function.
6. **Recovery priority ranking** — ordered list of functions for recovery sequencing.

## BIA Methodology Steps

Follow these steps in order; each step produces a documented artifact that feeds the next:

1. **Identify critical functions** — interview stakeholders and review system documentation to enumerate all business functions supported by `{{SYSTEM_NAME}}`. Assign a preliminary criticality level to each.
2. **Identify supporting resources** — for each function, list hardware, software, data, personnel, facilities, and external dependencies. Capture these in the resource dependency matrix.
3. **Determine outage impacts** — for each function and each resource, assess the financial, operational, regulatory, and reputational impact of a sustained outage. Use quantified estimates where available (e.g., `{{FINANCIAL_IMPACT_PER_HOUR}}`).
4. **Establish recovery time objectives** — derive RTO, RPO, and MTD for each function based on the impact assessment. Shorter objectives require more investment; document the rationale for each value.
5. **Identify recovery priorities** — rank functions and resources in the order they must be restored to achieve minimum viable operations, then full operations.
6. **Document and review** — produce the BIA report using the BIA template, obtain sign-off from `{{BIA_APPROVER}}`, and store the approved version in `{{BIA_REPOSITORY_PATH}}`.

## System Categorization Impact

The BIA output directly maps to the system tier assignment `{{SYSTEM_TIER}}`, which governs the required plan type, testing frequency, and minimum staffing for recovery operations. Tier 1 systems (MTD < 24 hours) require full contingency plan suites and quarterly exercises. Tier 2 systems (MTD 24–72 hours) require BCP and ISCP with semi-annual exercises. Tier 3 systems (MTD > 72 hours) require at minimum an ISCP with annual tabletop exercises.

## Review Cadence

BIAs must be reviewed on the schedule `{{REVIEW_CADENCE}}` and upon any triggering event listed above. The review must confirm that all RTO, RPO, and MTD values remain accurate and that no new critical dependencies have been added. Document the review outcome and any changes in the BIA version history.

## BIA Template Reference

Use the canonical BIA template at `artifacts/07_Operations_Incidents_Continuity/continuity/templates/business_impact_analysis.md` for all new BIA documents. The template enforces the required output structure and placeholder conventions.

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `platform__aws_well_architected.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-34 Rev. 1 section 2.2
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
