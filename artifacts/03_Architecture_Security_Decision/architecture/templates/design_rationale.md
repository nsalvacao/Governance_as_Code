---
title: Design Rationale Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: records that preserve the reasoning behind a design choice
source_basis: arc42 section 9 (architecture decisions); AWS Well-Architected design principles
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Capture the reasoning behind a design choice in a form that is reusable, reviewable, and easy to connect to the surrounding decision record. This template follows arc42 section 9 (Architecture Decisions) and AWS Well-Architected design principles.

## Template

---

### Rationale metadata

- **Rationale ID:** `{{RATIONALE_ID}}`
- **Date:** `{{RATIONALE_DATE}}`
- **Author:** `{{AUTHOR}}`
- **Related ADR:** `ADR-{{ADR_REFERENCE}}`
- **Status:** `{{STATUS}}` (draft | accepted | superseded)

---

### 1. Design context

Describe the context within which this design choice was made: `{{CONTEXT}}`. Include the system name, the feature or component under design, and any relevant prior decisions. Keep this to three sentences or fewer. This section answers "where and when did this design question arise?"

### 2. Forces at play

List the forces that create tension and must be balanced by the design. Forces include requirements, constraints, and quality attributes. Separate them into three categories:

**Requirements:**
- `{{FUNCTIONAL_REQUIREMENT}}` — describe the functional need that must be satisfied.

**Constraints:**
- `{{CONSTRAINT}}` — describe a non-negotiable limit (technology, budget, regulation, timeline).

**Quality attributes:**
- `{{QUALITY_ATTRIBUTE}}` — describe a measurable system property (e.g. latency < 200 ms, 99.9% availability, GDPR compliance).

Identifying forces explicitly is the most important step; a design choice is only justifiable if the forces it resolves are stated.

### 3. Design options considered

For each option that was seriously evaluated, provide a sub-section using the structure below. Include at least two options; include more when the decision was contested.

#### Option: `{{OPTION_NAME}}`

**Brief description:** `{{OPTION_DESCRIPTION}}`

**Forces satisfied:**
- `{{FORCE_SATISFIED}}` — explain how this option satisfies the force.

**Forces violated:**
- `{{FORCE_VIOLATED}}` — explain how this option creates tension or fails to satisfy the force.

Repeat this block for each option evaluated.

### 4. Chosen design

**Chosen design:** `{{CHOSEN_DESIGN}}`

State the selected approach in one sentence. This must map directly to one of the options listed in section 3.

### 5. Rationale

Explain which forces drove the selection of the chosen design over the alternatives. The rationale should reference forces by name rather than restating the option description. Example: "Option X was chosen because it satisfies `{{DECIDING_FORCE}}` while accepting the violation of `{{ACCEPTED_TRADE_OFF}}`."

This section answers "why this option and not the others?"

### 6. Consequences

Document the trade-offs that are explicitly accepted as a result of this design choice.

**Trade-offs accepted:**
- `{{TRADE_OFF}}` — describe the cost or limitation accepted in exchange for the benefit.

**Assumptions:**
- `{{ASSUMPTION}}` — list any assumptions this rationale depends on. If an assumption is invalidated, this design choice should be revisited.

**Monitoring signals:**
- `{{MONITORING_SIGNAL}}` — describe how the team will detect if the accepted trade-offs become unacceptable at runtime.

### 7. Related decisions

Link to other records that inform or are informed by this rationale.

- ADR reference: `ADR-{{ADR_REFERENCE}}`
- Related design rationale: `{{RELATED_RATIONALE_ID}}`
- Related architecture review: `{{RELATED_REVIEW_ID}}`

---

## Guidance

- Keep the reasoning factual and concise.
- Separate assumptions from evidence — label them clearly.
- Link to any ADR, review, or benchmark that influenced the choice.
- The forces section is mandatory; a rationale without explicit forces cannot be evaluated.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: arc42 section 9 (architecture decisions); AWS Well-Architected design principles
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
