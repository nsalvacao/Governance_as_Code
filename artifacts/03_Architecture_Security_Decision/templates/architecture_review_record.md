---
title: Architecture Review Record Template
artifact_type: template
status: public
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: formal architecture review outcomes and review evidence
source_basis: arc42 architecture documentation (arc42.org); AWS Well-Architected Framework review practices
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Purpose

Capture the outcome of an architecture review so the review can be repeated, audited, and connected to the underlying decision. This template is aligned with the arc42 documentation structure and the six AWS Well-Architected pillars.

## Template

---

### Review metadata

- **Review date:** `{{REVIEW_DATE}}`
- **Review type:** `{{REVIEW_TYPE}}` (initial | periodic | triggered-by-change)
- **System name:** `{{SYSTEM_NAME}}`
- **Reviewed artifact or scope:** `{{REVIEWED_ARTIFACT}}`
- **Reviewers:** `{{REVIEWERS}}`
- **Review facilitator:** `{{FACILITATOR}}`
- **ADR or change trigger:** `{{TRIGGER_REFERENCE}}`

---

### 1. System scope

Briefly describe what `{{SYSTEM_NAME}}` does, its external interfaces, and the boundaries of this review. One to three sentences. Reference the authoritative system description document if one exists.

### 2. Architecture goals and constraints

List the non-negotiable constraints (regulatory, compliance, organisational) and the primary quality goals that the architecture must satisfy. Each constraint should be stated as a testable condition: `{{CONSTRAINT_DESCRIPTION}}`. Each goal should be ranked by importance: `{{QUALITY_GOAL}}`.

### 3. Solution strategy

Summarise the key architectural decisions that define this system's approach. Each entry should reference the corresponding ADR: `{{KEY_DECISION}}` → `ADR-{{ADR_REFERENCE}}`. Include technology choices, deployment model, and integration pattern if they are not obvious from context.

### 4. Building block view

Describe the top-level decomposition of the system into components. For each component, state its responsibility and its main interfaces.

| Component | Responsibility | Key interfaces |
|---|---|---|
| `{{COMPONENT_NAME}}` | `{{COMPONENT_RESPONSIBILITY}}` | `{{COMPONENT_INTERFACES}}` |

Add rows as needed. For systems with multiple decomposition levels, describe the first level here and reference detailed diagrams if available.

### 5. Runtime view

Describe the most important scenarios showing how the building blocks collaborate at runtime. Focus on scenarios that carry architectural risk or that have been the subject of past incidents.

**Scenario:** `{{SCENARIO_NAME}}`
Steps: `{{SCENARIO_STEPS}}`
Key observations: `{{SCENARIO_OBSERVATIONS}}`

Add a scenario block for each significant runtime interaction.

### 6. Deployment view

Describe how the system is deployed across infrastructure nodes. Include environment names (`{{ENVIRONMENT_NAME}}`), runtime platforms, and network topology at the level needed to understand operational risk.

### 7. Cross-cutting concepts

Document shared architectural approaches that apply across multiple building blocks. Examples: logging strategy, error handling policy, authentication mechanism, data encoding standards, caching patterns. Each concept: `{{CONCEPT_NAME}}` — `{{CONCEPT_DESCRIPTION}}`.

### 8. Quality requirements — AWS Well-Architected pillars

Map review findings to the six AWS Well-Architected pillars. For each pillar, note the current state, findings, and recommended actions.

| Pillar | Current state | Findings | Recommended actions |
|---|---|---|---|
| Operational Excellence | `{{OE_STATE}}` | `{{OE_FINDINGS}}` | `{{OE_ACTIONS}}` |
| Security | `{{SEC_STATE}}` | `{{SEC_FINDINGS}}` | `{{SEC_ACTIONS}}` |
| Reliability | `{{REL_STATE}}` | `{{REL_FINDINGS}}` | `{{REL_ACTIONS}}` |
| Performance Efficiency | `{{PERF_STATE}}` | `{{PERF_FINDINGS}}` | `{{PERF_ACTIONS}}` |
| Cost Optimization | `{{COST_STATE}}` | `{{COST_FINDINGS}}` | `{{COST_ACTIONS}}` |
| Sustainability | `{{SUS_STATE}}` | `{{SUS_FINDINGS}}` | `{{SUS_ACTIONS}}` |

### 9. Architecture risks and technical debt

List known risks and deferred work. Each entry should have an owner and a target resolution date.

| Risk / debt item | Severity (H/M/L) | Owner | Target date |
|---|---|---|---|
| `{{RISK_DESCRIPTION}}` | `{{RISK_SEVERITY}}` | `{{RISK_OWNER}}` | `{{RISK_TARGET_DATE}}` |

### 10. Review outcome

State the overall verdict and required follow-up actions.

- **Overall verdict:** `{{VERDICT}}` (approved | approved-with-conditions | requires-rework)
- **Required changes before next release:** `{{REQUIRED_CHANGES}}`
- **Conditions (if conditional approval):** `{{CONDITIONS}}`
- **Follow-up review date:** `{{FOLLOW_UP_DATE}}`
- **Decision:** `{{DECISION}}`

---

## Guidance

- Keep the result factual and bounded to what was reviewed.
- Link to the ADR or design rationale that triggered the review.
- Each building block entry should be independently understandable — avoid acronyms without expansion.
- The AWS WA pillar table must be completed for every review, even if some pillars are marked as out-of-scope for this review cycle.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: arc42 architecture documentation (arc42.org); AWS Well-Architected Framework review practices
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
