---
title: "{{ADR_TITLE}}"
artifact_type: architectural_decision_record
status: public-draft
visibility: public
classification: public
owner: "{{OWNER}}"
review_cadence: "{{REVIEW_CADENCE}}"
applies_to: "{{APPLIES_TO}}"
source_basis: MADR 3.x (adr.github.io/madr) — Markdown Architectural Decision Records
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
adr_id: "ADR-{{ADR_SEQUENCE}}"
decision_date: "{{ADR_DATE}}"
decision_log_link: "{{DECISION_LOG_LINK}}"
supersedes: "{{SUPERSEDES}}"
---

# {{ADR_TITLE}}

<!-- Replace {{ADR_TITLE}} with a short imperative noun phrase, e.g. "Use PostgreSQL as primary data store". -->

- Status: `{{STATUS}}` <!-- proposed | accepted | deprecated | superseded by [ADR-N](path/adr-N.md) -->
- Date: `{{DECISION_DATE}}`
- Deciders: `{{DECIDERS}}` <!-- List all people or roles involved in the decision. -->
- Tags: `{{TAGS}}` <!-- Comma-separated labels, e.g. database, security, cost. -->

## Context and Problem Statement

{{CONTEXT_AND_PROBLEM_STATEMENT}}

<!-- Describe the architectural or technical challenge that forces a decision. Include the forces at play (functional, non-functional, organizational). State why the decision is needed now and what happens if it is not made. -->

## Decision Drivers

<!-- List the quality attributes, constraints, and forces that most influence the choice. Each driver should be testable or observable. -->

* {{DRIVER_1}}
* {{DRIVER_2}}
* {{DRIVER_3}}

## Considered Options

<!-- Name all options that were seriously evaluated. Each option listed here must have a corresponding Pros and Cons subsection below. -->

* {{OPTION_1}}
* {{OPTION_2}}
* {{OPTION_3}}

## Decision Outcome

Chosen option: "{{CHOSEN_OPTION}}", because {{JUSTIFICATION}}.

<!-- State why this option best satisfies the decision drivers compared to the alternatives. Be specific about the trade-offs accepted. -->

### Positive Consequences

<!-- List the improvements, capabilities, or risk reductions that result from this choice. -->

* {{POSITIVE_CONSEQUENCE_1}}
* {{POSITIVE_CONSEQUENCE_2}}

### Negative Consequences

<!-- List the trade-offs, technical debt, or risks introduced by this choice. These must be consciously accepted. -->

* {{NEGATIVE_CONSEQUENCE_1}}
* {{NEGATIVE_CONSEQUENCE_2}}

## Pros and Cons of the Options

<!-- Provide at least one "Good, because …" and one "Bad, because …" bullet for every option listed in Considered Options. -->

### {{OPTION_1}}

<!-- Brief description of this option. -->

* Good, because {{PRO_1}}
* Good, because {{PRO_2}}
* Bad, because {{CON_1}}
* Bad, because {{CON_2}}

### {{OPTION_2}}

<!-- Brief description of this option. -->

* Good, because {{PRO_1}}
* Good, because {{PRO_2}}
* Bad, because {{CON_1}}
* Bad, because {{CON_2}}

### {{OPTION_3}}

<!-- Brief description of this option. -->

* Good, because {{PRO_1}}
* Bad, because {{CON_1}}
* Bad, because {{CON_2}}

## Source Attribution

- Source manifests: platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: MADR 3.x (adr.github.io/madr) — Markdown Architectural Decision Records
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
