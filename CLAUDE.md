# Claude Code Repository Onboarding Guide

Use this file as the repository-wide operational guide for Claude Code contributing to this repository.

## Project Intent

This repository is the public, live instance of a central governance system and, in parallel, a reusable artifact library.

Contribution success depends on preserving this split:
- root files and `/.github/` implement this repository instance;
- `artifacts/` provides reusable templates, standards, schemas, scripts, and workflow definitions for downstream repositories.

The main delivery objective is deterministic, auditable governance contributions with low validation and CI failure risk.

## Priority & Conflict Handling

Resolve instructions in this order:
1. Explicit user/task instruction (current session)
2. Path-scoped instructions (if present)
3. Repository-wide instructions (this file)
4. Organization/personal defaults

Follow the most specific applicable rule.

If ambiguity remains, choose the safest minimal change and state assumptions in the PR summary.

When rules conflict, preserve repository correctness and deterministic validation over convenience edits.

## Critical Rules (MUST / NEVER / SHOULD)

### MUST

- Keep the instance-vs-template boundary:
  - edit root and `/.github/` only when changing this repository's behavior;
  - edit `artifacts/` for reusable governance assets.
- Keep all reusable artifacts under `artifacts/<dimension>/<artifact-type>/` (except allowed dimension `README.md` files).
- Preserve provenance:
  - Markdown artifacts require frontmatter + `## Source Attribution`;
  - GitHub-native files require `Source Attribution` comments.
- Keep README catalog links resolvable to real artifact paths.
- Run deterministic validation locally before proposing merge: `python3 scripts/validate_governance_artifacts.py`
- Use `python3` (not `python`) — the environment only exposes `python3`.

### NEVER

- Never add unresolved placeholders to root instance documents.
- Never break canonical GitHub-native locations (`.github/ISSUE_TEMPLATE/`, `.github/workflows/`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/CODEOWNERS`).
- Never claim command/platform support as verified without execution evidence.
- Never place volatile operational snapshots (temporary statuses, transient counts, sprint notes) in core governance files.
- Never run `scripts/sync_catalog_links.py` without a dedicated branch — it mutates `README.md`.

### SHOULD

- Prefer small, auditable changes with clear scope (`instance`, `artifact library`, or `both`).
- Update `decision_log.md` for structural or policy-level changes.
- Keep scripts and workflows aligned (local validator and CI wrapper must stay equivalent).
- Use existing artifact patterns before introducing new structures.
- Check `artifacts/conventions/schemas/frontmatter.schema.json` before writing new artifact frontmatter.

### Failure-First Aid (3-step emergency block)

1. Re-run minimal validation subset:
   - `python3 scripts/validate_governance_artifacts.py`
   - `python3 scripts/validate_governance_artifacts.py --report-only`
2. Verify manifest/path/frontmatter/schema synchronization:
   - check frontmatter contract keys;
   - confirm `README.md` catalog links resolve to real paths;
   - confirm artifact path depth (`artifacts/<dimension>/<artifact-type>/`) and GitHub-native Source Attribution markers.
3. If behavior is not reproducible, downgrade the claim/command status to `[UNVERIFIED]` and reference the relevant source-of-truth link.

## Repository Map (Where to change what)

| Path | Role | Change Here When | High-Risk Notes |
|---|---|---|---|
| `README.md` | Canonical public map + repository overview | Updating public corpus map, navigation, or canonical links | Catalog rows and canonical links are validator-gated (expected 103 rows) |
| `decision_log.md` | Official accepted decisions | Structural, policy, or model decisions are accepted | Inconsistent decision wording can create downstream ambiguity |
| `GOVERNANCE.md` | Instance governance behavior | Changing maintenance/lifecycle rules for this repository | Must remain instance-specific, not template-like |
| `CONTRIBUTING.md` | Contribution contract | Adjusting contribution process or expectations | Must remain aligned with validator and PR template |
| `SECURITY.md` | Security reporting process | Updating vulnerability disclosure and scope text | Must keep private-first reporting guidance |
| `SUPPORT.md` | Clarification route | Updating support vs issue/PR boundaries | Keep routing crisp to avoid noisy issue intake |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR intake enforcement surface | Changing required PR evidence/checklist | Template and contribution rules must stay synchronized |
| `.github/ISSUE_TEMPLATE/*.yml` | Structured issue intake | Changing bug/change/incident/investigation intake forms | Form drift can break governance workflow expectations |
| `.github/workflows/validate-governance-artifacts.yml` | CI validation gate | Changing validation trigger paths/job behavior | Must keep local and CI validation semantics aligned |
| `scripts/validate_governance_artifacts.py` | Deterministic validator | Updating frontmatter, traceability, layout, or catalog checks | Breaking checks can silently lower governance guarantees |
| `scripts/sync_catalog_links.py` | Catalog canonical-link sync utility | Updating README canonical artifact mapping logic | Missing mappings abort execution; always use in isolated branch |
| `artifacts/README.md` | Reusable library index | Updating library structure or dimension semantics | Keep dimension-first model explicit |
| `artifacts/<dimension>/*` | Reusable standards/policies/templates/schemas/scripts/workflows | Adding or updating reusable assets for downstream repos | Respect frontmatter contract and dimension/type placement |
| `artifacts/conventions/schemas/frontmatter.schema.json` | Metadata contract reference | Evolving metadata model for reusable artifacts | Contract drift impacts authoring consistency |
| `artifacts/conventions/workflows/validate-governance-artifacts.yml` | Reusable workflow definition | Updating downstream reusable validation workflow | Keep equivalence with instance workflow intent |
| `artifacts/conventions/scripts/validate_governance_artifacts.py` | Reusable validator script counterpart | Updating reusable validator implementation | Keep behavior compatible with instance validator expectations |
| `.private/` | Non-public working material, drafts, rationale | Internal notes and analysis not intended for publication | Contents must not leak into public corpus |

## Internal Tooling & Approved Workflow Systems

These systems govern how contributions are shaped, validated, and merged.

| System | Role Classification | What it controls | What breaks if ignored | Defined at | How to validate compliance |
|---|---|---|---|---|---|
| Deterministic governance validator | `validation gatekeeper` | Frontmatter keys, Source Attribution presence, artifact layout, catalog link integrity | CI failures, broken traceability, invalid artifact topology, missing catalog integrity | `scripts/validate_governance_artifacts.py` | `python3 scripts/validate_governance_artifacts.py` → clean exit |
| CI validation workflow | `workflow orchestrator` | Merge-gating execution of deterministic validator on relevant path changes | Broken changes can merge without validation; PR confidence drops | `.github/workflows/validate-governance-artifacts.yml` | Confirm workflow file points to validator and relevant paths |
| Catalog link synchronization utility | `internal toolkit` | Deterministic generation/update of README canonical artifact links from mapping table | Catalog drift, broken/missing canonical links, mapping incompleteness | `scripts/sync_catalog_links.py` | Run in isolated branch, inspect README diff |
| Frontmatter contract schema | `internal toolkit` | Canonical metadata contract for reusable artifacts (12 required keys) | Inconsistent metadata across artifacts and weaker machine-readability | `artifacts/conventions/schemas/frontmatter.schema.json` | `python3 -m json.tool artifacts/conventions/schemas/frontmatter.schema.json > /dev/null` |
| Public document map tables | `workflow orchestrator` | Canonical indexing of reusable governance corpus by dimension | Contributors cannot reliably find canonical artifacts; map/asset divergence | `README.md` (sections `## 1.` to `## 10.`) | Ensure each row has valid canonical artifact link under `artifacts/` |
| GitHub issue/PR intake templates | `workflow orchestrator` | Structured intake for bugs, change requests, incidents, investigations, and PR evidence | Low-quality or missing contribution context; triage inconsistency | `.github/ISSUE_TEMPLATE/*.yml`, `.github/PULL_REQUEST_TEMPLATE.md` | Check templates remain present, parseable, and aligned with contribution rules |
| Decision log contract | `reference-only` | Accepted structural principles and precedence for repository behavior | Conflicting interpretations, duplicated policy logic, unstable contribution decisions | `decision_log.md` | Confirm new structural changes are reflected as accepted decisions |

## Build, Test, Lint & CI Validation

Local validation uses the Python standard library only — no external test runner is required.

### Command Validation Matrix

| Command | Purpose | Preconditions | Expected Result | Common Failure | Recovery | Status | Portability | Last Validated | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| `python3 scripts/validate_governance_artifacts.py` | Run deterministic governance validation | Python 3 available; run at repository root | `Validator: OK (no issues found).` and exit `0` | Missing Source Attribution/frontmatter keys, bad catalog links, wrong artifact layout | Fix reported file/path issues and rerun | `VERIFIED` | `Linux` | `2026-03-27` | Executed in terminal during guide generation; exit 0 confirmed |
| `python3 scripts/validate_governance_artifacts.py --report-only` | Report issues without failing pipeline locally | Python 3 available; run at repository root | Findings printed; exit `0` even with findings | Assumed pass/fail semantics misunderstood | Use non-report mode to enforce exit status before merge | `[UNVERIFIED]` | `Linux` | `unknown` | Flag observed in script source; not executed from this session |
| `python3 -m py_compile scripts/validate_governance_artifacts.py scripts/sync_catalog_links.py` | Syntax-check governance automation scripts | Python 3 available | No output and exit `0` | Syntax/import errors | Fix script syntax and rerun | `VERIFIED` | `Linux` | `2026-03-27` | Executed in terminal during guide generation |
| `python3 -m json.tool artifacts/conventions/schemas/frontmatter.schema.json > /dev/null` | Validate frontmatter schema JSON syntax | Python 3 available | Exit `0` with no stderr | Invalid JSON formatting | Correct schema JSON and rerun | `[UNVERIFIED]` | `Linux` | `unknown` | Script inspected; artifact existence confirmed but not executed |
| `git --no-pager status --short` | Quick pre/post-change workspace sanity check | Git worktree available | Clean or expected scoped changes | Unexpected unrelated modifications | Isolate branch scope and re-check before commit | `VERIFIED` | `Linux` | `2026-03-27` | Executed in terminal during guide generation |
| `python3 scripts/sync_catalog_links.py` | Update README canonical artifact link column from mapping | Mapping dictionary complete; run from repository root; use isolated branch | README canonical-link column updated consistently | Missing row mapping raises `SystemExit` | Add missing mappings in `CATALOG_LINKS`, rerun, review diff | `NOT-RUN` | `Linux` | `unknown` | Script inspected; intentionally not executed to avoid unsolicited README mutation |
| `Validate Governance Artifacts` workflow job | CI gate for governance changes | Push/PR touching configured paths | Validator runs on `ubuntu-latest` and gates merge | Workflow path filters mismatch or validator failure in CI | Align changed paths and fix validator findings; re-run CI | `[UNVERIFIED]` | `CI-only` | `unknown` | Verified workflow definition in `.github/workflows/validate-governance-artifacts.yml` |

### CI/CD Mapping

- Merge gate: `.github/workflows/validate-governance-artifacts.yml`
- Trigger scope: changes in `artifacts/**`, `.github/**`, `scripts/**`, and root governance docs (`README.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `SECURITY.md`, `decision_log.md`)
- Local replication: `python3 scripts/validate_governance_artifacts.py` before PR

## Architecture & High-Risk Areas

### Operational Components

1. Repository instance layer — `README.md`, root governance docs, `.github/*`
2. Reusable artifact library — `artifacts/<dimension>/<artifact-type>/`
3. Deterministic validation layer — `scripts/validate_governance_artifacts.py`
4. CI orchestration layer — `.github/workflows/validate-governance-artifacts.yml`
5. Catalog synchronization toolkit — `scripts/sync_catalog_links.py`
6. Decision authority layer — `decision_log.md`
7. Private working material — `.private/` (non-public; must not leak)

### High-Risk Change Zones

- **Validator logic**: small rule changes affect all contribution outcomes across every artifact.
- **README catalog structure**: row-count (`103 expected`) and canonical-link integrity are enforced by validator.
- **Instance/template boundary**: incorrect placement causes semantic drift and governance confusion.
- **Source Attribution contract**: missing markers break traceability guarantees in both Markdown and YAML files.
- **GitHub-native intake assets**: malformed or deleted templates reduce triage and change quality.
- **Schema/contract drift**: metadata consistency degrades if `frontmatter.schema.json`, docs, and validator diverge.
- **`python3` vs `python`**: environment exposes `python3` only — scripts must be run with `python3`.

## Known Gotchas & Recovery

1. **`python` not found — use `python3`**
   - Diagnosis: `python: command not found` error when running scripts.
   - Recovery: replace `python` with `python3` in all local commands.
   - Prevention: always use `python3` in this WSL environment.

2. **Edited the wrong layer (instance vs reusable)**
   - Diagnosis: change is in root/`.github/` but intended for downstream reuse.
   - Recovery: move/update equivalent content under `artifacts/` and keep root instance minimal.
   - Prevention: classify change scope before editing (`instance`, `artifact library`, `both`).

3. **Missing `## Source Attribution` in Markdown or marker comment in GitHub-native files**
   - Diagnosis: validator reports missing Source Attribution on affected file.
   - Recovery: add attribution in canonical format and rerun validator.
   - Prevention: copy attribution pattern from neighboring validated files.

4. **Frontmatter key drift**
   - Diagnosis: validator reports missing canonical keys on artifacts.
   - Recovery: add required keys: `title`, `artifact_type`, `status`, `visibility`, `classification`, `owner`, `review_cadence`, `applies_to`, `source_basis`, `source_manifests`, `alignment_mode`, `updated`.
   - Prevention: start from an existing validated artifact or reference `frontmatter.schema.json`.

5. **README catalog canonical link mismatch**
   - Diagnosis: validator reports missing/invalid canonical artifact links or wrong row count.
   - Recovery: fix table link target; if many rows drifted, use sync utility in a controlled branch.
   - Prevention: avoid manual bulk-editing catalog tables without mapping review.

6. **Artifact path depth violation**
   - Diagnosis: validator flags artifact not under `artifacts/<dimension>/<artifact-type>/`.
   - Recovery: relocate file to compliant path and update references.
   - Prevention: create new files directly in the correct dimension/type folder.

7. **`scripts/sync_catalog_links.py` exits due to missing mapping**
   - Diagnosis: script aborts with "Missing catalog link mapping for row".
   - Recovery: add missing key to `CATALOG_LINKS` dict in the script, rerun, review output.
   - Prevention: keep mapping updated whenever new catalog row labels are introduced.

8. **CI passes locally but not in GitHub Actions**
   - Diagnosis: local `python3 scripts/validate_governance_artifacts.py` passes; CI still fails.
   - Recovery: inspect workflow run logs, check path filters, replicate failing file set locally.
   - Prevention: include CI workflow changes and validator changes in the same validation pass.

## Fast-Path: Common Contribution Flow

1. Determine change scope: `instance` / `artifact library` / `both`.
2. Locate authoritative path(s) from the Repository Map above.
3. Apply minimal, boundary-safe edits — prefer editing existing files over creating new ones.
4. Run local deterministic validation:
   - `python3 scripts/validate_governance_artifacts.py`
5. If changed scripts or schema, also run:
   - `python3 -m py_compile scripts/validate_governance_artifacts.py scripts/sync_catalog_links.py`
6. Prepare PR using `.github/PULL_REQUEST_TEMPLATE.md` — state scope, validation evidence, and downstream impact.
7. Merge only after CI validation gate passes.

## Sources of Truth

- Repository overview and canonical public map: `README.md`
- Accepted structural principles: `decision_log.md`
- Repository governance behavior: `GOVERNANCE.md`
- Contribution contract: `CONTRIBUTING.md`
- Security reporting rules: `SECURITY.md`
- Support routing: `SUPPORT.md`
- Deterministic validator: `scripts/validate_governance_artifacts.py`
- Catalog sync toolkit: `scripts/sync_catalog_links.py`
- CI gate workflow: `.github/workflows/validate-governance-artifacts.yml`
- Reusable library index: `artifacts/README.md`
- Frontmatter schema contract reference: `artifacts/conventions/schemas/frontmatter.schema.json`
- Copilot agent guide (equivalent, Copilot-targeted): `.github/copilot-instructions.md`

## Validation Metadata

- Complexity Mode: `standard`
- Generated On: `2026-03-27`
- Verification Coverage: `3 VERIFIED / 3 [UNVERIFIED] / 1 NOT-RUN`
- Internal Systems Coverage: `7 detected / 7 documented`
- Staleness Check: `PASS`

- Known Gaps:
  - `--report-only` flag validated via source inspection only, not execution (`[UNVERIFIED]`).
  - `frontmatter.schema.json` JSON syntax assumed valid (validator passes, file confirmed to exist); not directly syntax-checked in this session (`[UNVERIFIED]`).
  - CI workflow execution not run from this environment (`[UNVERIFIED]` CI-only rows).
  - Catalog sync script not executed to avoid unsolicited README mutation (`NOT-RUN`).

- How to close gaps:
  - Run `python3 scripts/validate_governance_artifacts.py --report-only` on a repo with a known issue and confirm exit 0 behavior.
  - Run `python3 -m json.tool artifacts/conventions/schemas/frontmatter.schema.json > /dev/null` and record result.
  - Push to a test branch touching a validator-scoped path and capture CI run logs.
  - Execute `python3 scripts/sync_catalog_links.py` in an isolated branch and inspect resulting diff.

- Top-5 Conformance Checks: `PASS`
  - Mandatory sections present and in required order: `PASS`
  - Command table schema complete (all required columns): `PASS`
  - Tri-state status usage and evidence per row: `PASS`
  - Internal tooling/workflow systems documented with roles + impact: `PASS`
  - Volatile snapshots excluded from core content: `PASS`

---

Trust this guide first. Search only when information is missing, outdated, or proven incorrect during execution.
