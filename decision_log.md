---
title: Decision Log
artifact_type: evidence
status: discovery
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: continuous
applies_to: repository-wide governance decisions
source_basis: GitHub Docs community governance guidance plus AWS and Microsoft decision-record practices
source_manifests:
  - governance__github_docs.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Decision Log

Status: public canonical, in discovery
Last updated: 2026-03-27

## DL-0001 - Foundational explicit truths about the repository

- Date: 2026-03-27
- Status: Accepted
- Context: Truths identified during the reading of the foundational documents and confirmed as correct.

### Decision

The following foundational truths are hereby recorded:

1. This repository exists to be the central governance node and the single source of truth for methodology, documentation, and cross-cutting automation.
2. Its purpose is to define the organizational system through handbooks, policies, templates, schemas, and reusable workflows, not merely to archive passive documentation.
3. Satellite repositories should consume, instantiate, and reference what is defined here, avoiding local structural reinvention.
4. The documentation architecture should be driven by objective triggers so that documentation arises from real work rather than abstract bureaucracy.
5. The intended documentation system is a knowledge graph in which experiments, incidents, and changes feed analysis, decision-making, operations, and the knowledge base.
6. A central objective is to build auditable organizational memory, reduce cognitive debt, and let each project inherit maturity with low startup cost.
7. Documentation must be treated as infrastructure: structured, parameterized, validatable, automatable, and subject to enforcement.
8. The repository's current state is still mostly conceptual definition and discovery; the target architecture described in the documents is not yet implemented in full.

## DL-0002 - Accepted foundational inferences

- Date: 2026-03-27
- Status: Accepted
- Context: Strong inferences derived from the system-level reading of the documents and validated as correct.

### Decision

The following foundational inferences are hereby recorded:

1. Canonical documentation should behave as operational infrastructure, not as passive text.
2. Centralization is a deliberate mechanism for fighting organizational entropy.
3. Project repositories should be light on governance and rich in factual instances.
4. Documentation should only arise from objective and verifiable triggers.
5. Experiment-based learning and incident-based learning have equal legitimacy in the system.
6. Every document should have explicit provenance and traceable upstream and downstream relationships.
7. Governance should be applied within the normal delivery flow, including PRs, validations, and automation.
8. The documentation system is designed for a dual audience: humans and agents/systems.
9. The methodology defined here should behave like a reusable organizational product.
10. The real output is not just documentation, but composed and reusable organizational memory.
11. Organizational consistency takes precedence over local structural autonomy when the two conflict.
12. Formalization is used as a tool to reduce future friction, not to increase bureaucracy.

## DL-0003 - Publication and curation model

- Date: 2026-03-27
- Status: Accepted
- Context: Definition of the boundary between the public corpus and unpublished working material.

### Decision

1. This repository should be curated to be publishable by default.
2. The public corpus should favor reusable methodology, governance structures, taxonomies, criteria, generic templates, and publication-ready artifacts.
3. Working material, drafts, supplemental rationale, and context not intended for publication should be kept outside the public corpus.

## DL-0004 - Treatment of the initial source documents

- Date: 2026-03-27
- Status: Accepted
- Context: Decision on the status of the foundational documents used during the initial discovery phase.

### Decision

1. `documentacao_central.md`, `mapa_documentacao.md`, and `racional.md` are now treated as draft source documents.
2. These documents should be kept in an ignored area of the repository and used as raw material for later public, canonical documents.
3. Relevant content may be consolidated, rewritten, and published later in new pieces that are suitable for the public corpus.

## DL-0005 - Public and private decision records

- Date: 2026-03-27
- Status: Accepted
- Context: Separation between the public decision record and supplemental non-public rationale.

### Decision

1. `decision_log.md` is the default public record.
2. The public record should use publication-ready wording and avoid parallel intents, supplemental rationale, or sensitive context.
3. Supplemental rationale may be kept in a private Git-ignored record, named `decision_log_private.md` or equivalent.
4. When dual records exist, the public document represents the official formulation and the private document represents only supplemental context.

## DL-0006 - Document classification grid

- Date: 2026-03-27
- Status: Accepted
- Context: Initial definition of the classification policy for the document corpus.

### Decision

1. The document classification grid may be public.
2. The classification system should support, at minimum, states equivalent to public, public-redacted, and private.
3. A later phase will define an automatic mechanism to inject that classification into document frontmatter.

## DL-0007 - Selective applicability across repositories

- Date: 2026-03-27
- Status: Accepted
- Context: Clarification on how the governance system should apply across current and future repositories.

### Decision

1. It is assumed that not every current or future repository will require every document in the overall corpus.
2. Document applicability should be determined case by case according to the nature, risk, maturity, and operating model of each repository.
3. The governance system should therefore support selective instantiation rather than universal mandatory instantiation.

## DL-0008 - Centralization of reusable governance assets

- Date: 2026-03-27
- Status: Accepted
- Context: Clarification on where reusable governance artifacts must live and how they should be designed.

### Decision

1. All reusable governance assets should live in this repository.
2. This includes, at minimum, templates, schemas, scripts, reusable workflows, automation logic, and any other reusable governance mechanism.
3. These assets should be designed from the start for reuse through placeholders, variables, and explicit parameterization.
4. They should be designed to take advantage of GitHub-native mechanisms wherever useful, including Actions, variables, environments, secrets, and related automation surfaces.
5. The target operating model is maximum automation and intelligence with minimum manual intervention.

## DL-0009 - Automation-first execution for systems and AI agents

- Date: 2026-03-27
- Status: Accepted
- Context: Clarification that the decision log should guide both human collaborators and AI agents.

### Decision

1. The decision log is intended to guide both human collaborators and AI agents working in or from this repository.
2. Reusable governance artifacts should therefore be explicit enough to indicate what to instantiate, how to instantiate it, and under which conditions it applies.
3. Automation and agent workflows should prefer repository-defined rules, reusable assets, and parameterized entry points over ad hoc manual execution.
4. When automation is feasible through reusable repository mechanisms, that path is preferred over bespoke per-repository manual handling.

## DL-0010 - First-wave public foundation bundle

- Date: 2026-03-27
- Status: Accepted
- Context: Definition of the first public implementation wave for the repository.

### Decision

1. The first wave establishes the public foundation of the system through conventions, governance entry surfaces, decision and ADR standards, reliability artifacts, incident-response artifacts, continuity artifacts, and a deterministic validation layer.
2. Each first-wave family should ship as a reusable bundle where relevant, combining policies, standards, templates, schemas, and GitHub-native files rather than isolated prose.
3. The first wave is intentionally baseline-oriented: it enables consistent instantiation and later automation waves without requiring every downstream repository to adopt every artifact immediately.

## DL-0011 - Canonical metadata and traceability contract

- Date: 2026-03-27
- Status: Accepted
- Context: Need for a single metadata and provenance contract across the first-wave public corpus.

### Decision

1. Public Markdown artifacts should use a canonical frontmatter contract centered on title, artifact type, status, visibility, classification, ownership, review cadence, applicability, source basis, source manifests, alignment mode, and updated date.
2. Every public artifact must expose traceable provenance.
3. Markdown documents and templates should use a `## Source Attribution` section.
4. GitHub-native files that should not use frontmatter must expose equivalent traceability through comments.
5. `source_manifests` should be represented as a YAML list by default, with compatibility for legacy string-based forms where needed.

## DL-0012 - GitHub-native placement and deterministic validation

- Date: 2026-03-27
- Status: Accepted
- Context: Need to ensure the first-wave corpus behaves predictably on GitHub and can be checked automatically.

### Decision

1. GitHub-native files should live in their canonical repository paths, especially `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/CODEOWNERS`, and `.github/workflows/`.
2. The first wave includes a deterministic validator implemented with the Python standard library and a matching GitHub Actions workflow.
3. The validator must check both frontmatter-based artifacts and comment-attributed GitHub-native files.
4. Human contributors and AI agents are expected to use the validator before considering first-wave changes ready for merge.

## DL-0013 - Repository instance versus reusable artifact split

- Date: 2026-03-27
- Status: Accepted
- Context: The first-wave implementation initially mixed repository-specific files with placeholder-based reusable content, which made the semantics of the public corpus unclear.

### Decision

1. Files at the repository root and under `/.github/` are the concrete instance of this repository and must not carry unresolved placeholders.
2. Reusable counterparts for those document classes must live in the artifact library under `artifacts/`.
3. Downstream repositories should instantiate reusable assets from the artifact library rather than copying root instance files.

## DL-0014 - Dimension-first artifact library

- Date: 2026-03-27
- Status: Accepted
- Context: The previous type-first top-level structure (`docs/`, `templates/`, `policies/`, `schemas/`) did not map intuitively to the dimensional structure defined in the public document map.

### Decision

1. Reusable assets are now organised under `artifacts/<dimension>/<artifact-type>/`.
2. Dimensions should align with the public document map wherever practical.
3. The library structure should make it obvious which category an artifact belongs to before the reader needs to care about file type.

## DL-0015 - One catalog entry, at least one reusable artifact

- Date: 2026-03-27
- Status: Accepted
- Context: Clarification on the expected completion model for the public document catalog embedded in the README.

### Decision

1. Each document entry listed in the ten dimensional tables of the README must, in the final system, link to a corresponding reusable artifact.
2. The minimum target is therefore at least one reusable artifact per catalog entry.
3. The total number of reusable artifacts may exceed the number of catalog entries where the system benefits from additional schemas, explanatory standards, rationale documents, scenario-specific variants, or multiple implementation forms.
4. The folder structure must be designed for that end state from the start, so that the final corpus remains intuitive even as the number of artifacts grows beyond the base catalog count.

## DL-0016 - README as canonical public artifact index

- Date: 2026-03-27
- Status: Accepted
- Context: The catalog wave turns the README from a descriptive map into the public navigational index of the reusable corpus.

### Decision

1. The ten dimensional tables in `README.md` are the canonical public index of the reusable governance corpus.
2. Every catalog row must expose a final canonical primary artifact link.
3. That link must resolve to a real reusable artifact under `artifacts/`.
4. Deterministic validation must fail when a row is missing its canonical link or when the linked target does not exist.

## DL-0017 - Canonical bridge artifacts are allowed

- Date: 2026-03-27
- Status: Accepted
- Context: Some existing reusable assets are supportive or implementation-specific but not sufficiently explicit to serve directly as the public canonical target for a README row.

### Decision

1. A catalog row may point to a bridge artifact created specifically to represent that document class more clearly in the public library.
2. Bridge artifacts are valid when they improve navigability, naming clarity, or dimensional alignment.
3. Bridge artifacts must remain reusable, source-attributed, and publication-safe.
4. The existence of a bridge artifact does not invalidate older supporting artifacts in neighboring dimensions when those still serve implementation or supporting purposes.

## DL-0018 - Public provenance manifests

- Date: 2026-03-28
- Status: Accepted
- Context: Public documents and reusable artifacts claim traceable provenance, but that provenance must be publicly inspectable rather than implicit or private-only.

### Decision

1. Source manifests referenced in public files must resolve to public, sanitized manifest documents.
2. Public source manifests are published under `sources/manifests/`.
3. Private research material may remain richer and more exploratory, but public provenance must be sufficient to verify the declared source basis and authority.
4. Public-facing attribution should link to the published manifest whenever practical.

## DL-0019 - Public versus private agent guidance

- Date: 2026-03-28
- Status: Accepted
- Context: Some agent- and automation-oriented documents exposed implementation detail and internal operating tone that are not appropriate for the public presentation of the repository.

### Decision

1. Public agent guidance must remain minimal, institutional, and contribution-oriented.
2. Detailed operational instructions, orchestration notes, and internal execution heuristics belong in non-public material.
3. Public AI automation surfaces should describe intent, trust boundaries, and contribution expectations without exposing unnecessary internal process detail.

## DL-0020 - Canonical single-source rule for duplicate artifact families

- Date: 2026-03-28
- Status: Accepted
- Context: Some public artifact families evolved into parallel variants with the same semantic role, creating ambiguity about the canonical source of truth.

### Decision

1. For each semantic document role, the public corpus should expose one canonical reusable artifact.
2. Duplicate public artifacts with the same semantic role must be consolidated, archived, or reclassified as supporting material.
3. The README catalog must link only to the canonical artifact for each document role.

## DL-0021 - Public-readiness before structural simplification

- Date: 2026-03-28
- Status: Accepted
- Context: The current numbered structure can still be opened publicly if its semantics, attribution, and validation are sound, even if deeper structural simplification is still desirable later.

### Decision

1. Public-readiness hardening takes precedence over a broader tree refactor.
2. The numbered dimension structure remains in place for the current remediation wave.
3. Structural simplification toward a flatter `dimension -> artifact-type` model remains a later optimization rather than a prerequisite for publication safety.

## DL-0022 - MIT formalization

- Date: 2026-03-28
- Status: Accepted
- Context: The public repository already claimed MIT licensing and needed that claim to be made legally and operationally explicit.

### Decision

1. The repository now ships with a formal MIT `LICENSE` file.
2. Public license claims must link directly to that file.
3. If future licensing changes are needed, public claims must change atomically with the legal artifact.

## Source Attribution

- Source manifests: [`governance__github_docs.md`](./sources/manifests/governance__github_docs.md), [`platform__aws_well_architected.md`](./sources/manifests/platform__aws_well_architected.md), [`platform__microsoft_learn.md`](./sources/manifests/platform__microsoft_learn.md)
- Primary source basis: GitHub Docs community governance guidance plus AWS and Microsoft decision-record practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
