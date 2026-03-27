---
title: Decision Log Standard
artifact_type: policy
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: all repositories inheriting these governance conventions
source_basis: GitHub Docs, AWS Well-Architected, Microsoft Learn
source_manifests:
  - governance__github_docs.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

This standard defines how the canonical `decision_log.md` stays coherent, traceable, and automation-ready while allowing downstream repositories to instantiate the entries they need.

## Purpose

- Keep one public, reviewable stream where accepted governance decisions accumulate.
- Surface the `DL-` identifiers that appear in the published log and link every entry to the decision or ADR that triggered it.
- Make the log consumable by humans, reusable agents, and automation tooling through consistent metadata and attribution.

## When to log a decision

1. Use the `decision_log` whenever the decision has organizational impact (governance, policy, taxonomy) and should be discoverable without interpretation.
2. Keep decisions concise; system-level rationale and context live in linked ADRs, playbooks, or postmortems.
3. Reserve ADRs for irreversible, governance-shaping, or high-risk choices; keep incremental project-level decisions in the decision log unless they change organizational standards.

## Integrity rules

- Every entry must follow the `decision_log_entry.schema.json` contract.
- IDs use the `DL-000X` format; maintain sequential numbering and reflect superseded decisions explicitly.
- Each entry records who reviewed it, the status (`draft`, `accepted`, etc.), and the next review trigger.
- Keep `source_basis` consistent with `platform__aws_well_architected.md` and `platform__microsoft_learn.md`, because they anchor the ADR and decision lifecycle language.

## Automation and AI guidance

- Agents should prefer the published schema for validation before accepting new entries.
- Emphasize fields over narrative so automation can detect the status, owner, and referenced ADR automatically.
- Downstream repos can reuse the template in `artifacts/governance/templates/decision_log_entry.md` and adapt the placeholders without changing the structural contract.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: GitHub Docs community governance guidance plus AWS/Microsoft guidance on decision records and reviews
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
