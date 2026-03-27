---
title: Architectural Decision Record Standard
artifact_type: policy
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: all architecture and delivery decisions that threaten irreversible outcomes
source_basis: AWS Well-Architected ADR process; Microsoft Learn release and incident reviews; GitHub Docs governance guidance
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

This standard explains when an ADR is required, how it differs from the decision log, and how to author an ADR that stays automation-friendly and reuse-ready.

## ADR versus Decision Log

- **ADR**: captures the full context, options considered, trade-offs, and technical consequences of a hard-to-reverse decision (architecture, platform, delivery contracts, automation safety). Each ADR follows the template in `artifacts/governance/templates/architecture_decision_record.md` and is the single source for the working rationale.
- **Decision log**: publishes the distilled acceptance outcome once the ADR (or other governance process) is approved. Decision log entries point back to one or more ADRs for context and keep the public corpus lightweight.
- Always link the ADR ID inside the decision log template under `Linked ADR`. Automation can then follow the link to fetch the reasoning, review status, and superseded history.

## When to author an ADR

1. The decision will change an organizational standard, baseline, automation contract, or release pathway.
2. The decision will be difficult to reverse without significant effort (e.g., pipeline rewrites, baseline migrations).
3. The decision may span teams, tooling, or automation surfaces rather than a single sprint deliverable.
4. Avoid capturing easily reversed or single-repo choices in ADRs; keep those decisions in the decision log unless they touch governance or automation baselines.

## Structure and automation expectations

- Always use `{{UPPER_SNAKE_CASE}}` placeholders for fields agents must populate.
- Sections follow the template in `artifacts/governance/templates/architecture_decision_record.md`: `Context`, `Decision`, `Consequences`, `Validation`, `Review notes`.
- Include metadata for owner, status, review cadence, and publication status.
- Mark each ADR with a `Status` (`proposed`, `accepted`, `superseded`) and update `updated` with the current date.
- After acceptance, append the entry to `decision_log.md` and keep the ADR immutable thereafter; new facts require a superseding ADR.

## Automation guidance

- Agents ingest the schema from `artifacts/governance/schemas/decision_log_entry.schema.json` to validate decision log entries after referencing ADR metadata.
- Use the ADR template to feed release automation, compliance checkers, and knowledge graphs with structured context and consequences.
- Document attachments (links to runbooks, readiness reviews, evaluation suites) should reside in the ADR body so AI assistants can reference them without editing the decision log.

## Source Attribution

- Source manifests: platform__aws_well_architected.md, platform__microsoft_learn.md, governance__github_docs.md
- Primary source basis: AWS and Microsoft architectural decision guidance plus GitHub governance norms
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
