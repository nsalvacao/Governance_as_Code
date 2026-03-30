---
title: Decision Log Standard
artifact_type: standard
status: public
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: public decision logs used by this repository and downstream repositories
source_basis: GitHub Docs decision record practices and repository governance conventions
source_manifests:
  - governance__github_docs.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Purpose

Define how decisions are recorded and managed as knowledge artifacts in `{{REPOSITORY_NAME}}`. This standard treats decision records not merely as audit trail items but as organizational memory — reusable knowledge that reduces cognitive debt and prevents the rediscovery of solved problems.

## Decision Records as Organizational Memory

Decisions are a primary source of organizational knowledge. When decisions go unrecorded:

- Teams repeat the same exploratory work in future discussions.
- New members cannot understand why the system is shaped as it is.
- Cognitive debt accumulates: the gap between the system as documented and the system as built widens over time.
- Agents and automation tools lack the structured context they need to operate safely.

Every decision that materially affects `{{REPOSITORY_NAME}}` — its structure, its processes, its tooling, or its governance — must be recorded in the appropriate decision record format. "We discussed it in a meeting" is not an acceptable substitute.

## Decision Record Types

Not all decisions have the same scope or longevity. This standard recognizes three types:

### Architectural Decision Records (ADRs)

- **Scope**: technical architecture, system design, tooling selection, interface contracts
- **When to use**: when a decision shapes the structure or behavior of the system in a way that is costly to reverse
- **Storage location**: `{{ADR_STORAGE_LOCATION}}` (e.g., `docs/adr/` or `artifacts/08_Knowledge_Documentation_Continuous_Improvement/records/`)
- **Format**: ADR format (context, decision, consequences, status)
- **Lifecycle**: proposed → accepted → superseded/deprecated

### Governance Decision Log Entries

- **Scope**: process changes, ownership changes, policy updates, standards revisions
- **When to use**: when a decision affects how the team operates or how the repository is governed
- **Storage location**: `{{GOVERNANCE_LOG_LOCATION}}` (e.g., `decision_log.md` at repository root)
- **Format**: log entry with stable identifier, date, decision summary, rationale, and status
- **Lifecycle**: active → archived (when superseded or no longer relevant)

### Operational Decision Points

- **Scope**: runtime choices encoded in runbooks and operational procedures
- **When to use**: when an operator must choose between actions based on system state
- **Storage location**: embedded in the relevant runbook at `{{RUNBOOK_LOCATION}}`
- **Format**: inline decision point with conditions, options, and expected outcomes
- **Lifecycle**: tied to the owning runbook's lifecycle

## Knowledge Extraction from Decisions

Decision records must be written so that the following elements can be extracted and reused:

| Element | What to capture | Where it is stored |
|---|---|---|
| Context | The situation, constraints, and pressures that made the decision necessary | `{{KNOWLEDGE_STORE}}` |
| Trade-offs | Alternatives considered and why they were not chosen | `{{KNOWLEDGE_STORE}}` |
| Lessons | What was learned that could inform future decisions | `{{KNOWLEDGE_STORE}}` |
| Assumptions | Conditions that were assumed to be true at decision time | In the decision record itself |
| Trigger | The event or question that forced the decision | In the decision record itself |

Knowledge extracted from decisions is stored in `{{KNOWLEDGE_STORE}}` and indexed for search. Extraction may be manual or automated via `{{EXTRACTION_AUTOMATION_HOOK}}`.

## Decision Search and Discoverability

Decision records are only valuable if they can be found. Apply the following tagging and search conventions:

### Tagging conventions

Every decision record must be tagged with at least one tag from each of the following dimensions:

- **Domain tag**: `{{TAG_1}}` (e.g., `security`, `infrastructure`, `process`, `tooling`)
- **Status tag**: `{{TAG_2}}` (e.g., `active`, `superseded`, `proposed`)
- **Impact tag**: `{{TAG_3}}` (e.g., `breaking`, `additive`, `cosmetic`)

Additional free-form tags are permitted. Tag vocabulary is maintained at `{{TAG_VOCABULARY_LOCATION}}`.

### Search criteria

When searching for relevant decisions, use the following criteria:

1. By domain: find all decisions tagged `{{SEARCH_DOMAIN}}`
2. By date range: find decisions made between `{{START_DATE}}` and `{{END_DATE}}`
3. By status: find all `active` decisions that have not been superseded
4. By keyword: full-text search across decision summaries and context fields
5. By affected component: `{{COMPONENT_SEARCH_CRITERION}}`

## Decision Lifecycle in Knowledge Management

Decision records transition through states. Each state transition has implications for how the knowledge is managed.

| State | Meaning | Knowledge action |
|---|---|---|
| **Proposed** | Decision is under discussion; outcome not yet determined | Tag as proposed; do not reference from other documents yet |
| **Active** | Decision is accepted and in effect | Publish to knowledge store; link from relevant standards and runbooks |
| **Archived** | Decision has been superseded or the context no longer applies | Move to archive at `{{ARCHIVE_LOCATION}}`; update all inbound links to point to the superseding decision |
| **Superseded** | A newer decision explicitly replaces this one | Record the superseding decision ID in the record; keep the record readable for historical context |

Knowledge extracted from active decisions must be reviewed when the decision is archived or superseded. If the extracted knowledge remains valid despite the decision change, it is retained and updated. If it is invalidated, it is removed or marked as historical.

## Anti-Patterns

Avoid the following patterns that degrade decision knowledge quality:

1. **Undocumented verbal decisions**: decisions made in meetings, chat, or ad-hoc conversations that are never written down. These decisions are invisible to new team members and automation tools.
2. **Decision drift**: a decision record that no longer reflects the actual state of the system because it was never updated after the decision was revised. Keep records current or mark them as superseded.
3. **Over-broad decisions**: a single decision record that covers too many topics. Split into focused records with clear scope boundaries.
4. **Missing rationale**: a decision record that states the outcome but not the reasoning. The "why" is the most valuable part of a decision record for future readers.
5. **Orphaned records**: decision records that are not linked from any standard, runbook, or architectural document. Orphaned records are not discoverable and will not be maintained.

## Automation Hooks

Decision records are machine-readable knowledge artifacts. The following automation hooks consume decision records in `{{REPOSITORY_NAME}}`:

- **Agent context injection**: agents load active decision records tagged `{{AGENT_RELEVANT_TAG}}` as context before operating on the system. Hook: `{{AGENT_CONTEXT_HOOK}}`.
- **Staleness detection**: a scheduled check flags decision records that have been in `active` state for more than `{{STALENESS_THRESHOLD}}` without review. Hook: `{{STALENESS_CHECK_HOOK}}`.
- **Supersession propagation**: when a decision is marked superseded, automation notifies owners of documents that link to it. Hook: `{{SUPERSESSION_HOOK}}`.
- **Knowledge extraction pipeline**: on merge of a decision record, a pipeline extracts tagged elements into `{{KNOWLEDGE_STORE}}`. Hook: `{{EXTRACTION_HOOK}}`.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: GitHub Docs decision record practices and repository governance conventions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
