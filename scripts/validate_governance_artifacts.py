#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Sequence, Tuple


REQUIRED_FRONTMATTER_KEYS = [
    "title",
    "artifact_type",
    "status",
    "visibility",
    "classification",
    "owner",
    "review_cadence",
    "applies_to",
    "source_basis",
    "source_manifests",
    "alignment_mode",
    "updated",
]

FRONTMATTER_PATHS = [Path("artifacts")]
ROOT_MARKDOWN_PATHS = [
    Path("README.md"),
    Path("GOVERNANCE.md"),
    Path("CONTRIBUTING.md"),
    Path("CODE_OF_CONDUCT.md"),
    Path("SUPPORT.md"),
    Path("SECURITY.md"),
    Path("decision_log.md"),
    Path("CLAUDE.md"),
    Path("GEMINI.md"),
    Path("sources/README.md"),
]
SUPPLEMENTAL_MARKDOWN_DIRS = [Path("sources/manifests")]
GITHUB_META_PATHS = [
    Path(".github/ISSUE_TEMPLATE"),
    Path(".github/PULL_REQUEST_TEMPLATE.md"),
    Path(".github/CODEOWNERS"),
    Path(".github/workflows"),
    Path(".github/commands"),
    Path(".github/copilot-instructions.md"),
]
ARTIFACT_META_PATHS = [Path("artifacts")]
SCHEMA_PATHS = [Path("artifacts")]
PUBLIC_MANIFEST_DIR = Path("sources/manifests")
LICENSE_PATH = Path("LICENSE")

CATALOG_SECTION_PATTERN = re.compile(r".*<b>(\d+)\..*")
MARKDOWN_LINK_PATTERN = re.compile(r"\]\(\./([^)]+)\)")
LOCAL_PATH_PATTERN = re.compile(r"(/mnt/[^\s)]+|(?<![A-Za-z])[A-Za-z]:[\\/][^\s)]*)")
ISSUE_TEMPLATE_BAD_LABELS_PATTERN = re.compile(r"^labels:\s*\n\s*-\s*type\s*:", re.MULTILINE)
MANIFEST_NAME_PATTERN = re.compile(r"[\w-]+__[\w-]+\.md")


def iter_markdown_paths() -> Iterable[Path]:
    for base in FRONTMATTER_PATHS:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if path.name == "PULL_REQUEST_TEMPLATE.md":
                continue
            yield path


def iter_root_markdown_paths() -> Iterable[Path]:
    for path in ROOT_MARKDOWN_PATHS:
        if path.exists():
            yield path
    for base in SUPPLEMENTAL_MARKDOWN_DIRS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            yield path


def iter_comment_paths() -> Iterable[Path]:
    for base in GITHUB_META_PATHS:
        if base.suffix in {".md", ".toml"} or base.name == "CODEOWNERS":
            if base.exists():
                yield base
            continue
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix in {".yml", ".yaml", ".toml"}:
                yield path


def iter_artifact_meta_paths() -> Iterable[Path]:
    for base in ARTIFACT_META_PATHS:
        if not base.exists():
            continue
        for path in base.rglob("*.yml"):
            yield path
        for path in base.rglob("PULL_REQUEST_TEMPLATE.md"):
            yield path
        for path in base.rglob("CODEOWNERS"):
            yield path


def iter_schema_paths() -> Iterable[Path]:
    for base in SCHEMA_PATHS:
        if not base.exists():
            continue
        for path in base.rglob("*.json"):
            yield path


def parse_frontmatter(text: str) -> Tuple[dict[str, object], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, None
    fm_lines: list[str] = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        fm_lines.append(line.rstrip("\n"))
    else:
        return {}, None

    fm_data: dict[str, object] = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            fm_data[key] = value
            i += 1
            continue
        items: list[str] = []
        i += 1
        while i < len(fm_lines):
            nested = fm_lines[i].strip()
            if nested.startswith("- "):
                items.append(nested[2:].strip())
                i += 1
                continue
            if nested == "":
                i += 1
                continue
            break
        fm_data[key] = items
    body = "\n".join(lines[len(fm_lines) + 2 :])
    return fm_data, body


def has_source_attribution(text: str) -> bool:
    return "Source Attribution" in text


def normalize_manifest_refs(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        refs = MANIFEST_NAME_PATTERN.findall(value)
        if refs:
            return refs
        return [item.strip() for item in re.split(r"[, ]+", value) if item.strip().endswith(".md")]
    return []


def validate_manifest_refs(fm_data: dict[str, object]) -> list[str]:
    refs = normalize_manifest_refs(fm_data.get("source_manifests", []))
    if not refs:
        return ["missing resolvable source manifest references"]
    missing = [ref for ref in refs if not (PUBLIC_MANIFEST_DIR / ref).exists()]
    if missing:
        return [f"missing public source manifests: {', '.join(missing)}"]
    return []


def check_markdown(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    fm_data, _ = parse_frontmatter(content)
    problems: list[str] = []
    if not fm_data:
        return ["missing frontmatter"]
    missing = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in fm_data]
    if missing:
        problems.append(f"missing frontmatter keys: {', '.join(missing)}")
    problems.extend(validate_manifest_refs(fm_data))
    if not has_source_attribution(content):
        problems.append("missing '## Source Attribution'")
    if LOCAL_PATH_PATTERN.search(content):
        problems.append("contains local machine path reference")
    return problems


def check_root_markdown(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    problems: list[str] = []
    if not content.strip():
        return ["empty public markdown file"]
    fm_data, _ = parse_frontmatter(content)
    if fm_data:
        missing = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in fm_data]
        if missing:
            problems.append(f"missing frontmatter keys: {', '.join(missing)}")
        if "source_manifests" in fm_data:
            problems.extend(validate_manifest_refs(fm_data))
    if not has_source_attribution(content):
        problems.append("missing '## Source Attribution'")
    if LOCAL_PATH_PATTERN.search(content):
        problems.append("contains local machine path reference")
    return problems


def check_comment_file(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    problems: list[str] = []
    if "Source Attribution" not in content:
        problems.append("missing 'Source Attribution' marker")
    if LOCAL_PATH_PATTERN.search(content):
        problems.append("contains local machine path reference")
    if path.parent.name == "ISSUE_TEMPLATE" and path.suffix in {".yml", ".yaml"}:
        if ISSUE_TEMPLATE_BAD_LABELS_PATTERN.search(content):
            problems.append("issue template uses invalid labels mapping format")
    return problems


def check_schema_file(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    try:
        json.loads(content)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc.msg}"]
    problems: list[str] = []
    if "source_manifests" not in content:
        problems.append("missing 'source_manifests' reference")
    if "alignment_mode" not in content:
        problems.append("missing 'alignment_mode' reference")
    return problems


def run_checks(paths: Iterable[Path], checker) -> list[Tuple[Path, Sequence[str]]]:
    failures: list[Tuple[Path, Sequence[str]]] = []
    for path in paths:
        problems = checker(path)
        if problems:
            failures.append((path, problems))
    return failures


def check_license_exists() -> list[Tuple[Path, Sequence[str]]]:
    if LICENSE_PATH.exists():
        return []
    return [(LICENSE_PATH, ["missing LICENSE file"])]


def check_artifact_layout() -> list[Tuple[Path, Sequence[str]]]:
    failures: list[Tuple[Path, Sequence[str]]] = []
    artifacts_root = Path("artifacts")
    if not artifacts_root.exists():
        return failures
    for path in artifacts_root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(artifacts_root)
        if len(relative.parts) == 1 and path.name == "README.md":
            continue
        if len(relative.parts) == 2 and path.name == "README.md":
            continue
        if len(relative.parts) < 3:
            failures.append((path, ["artifact file must live under artifacts/<dimension>/<artifact-type>/ unless it is a dimension README"]))
    return failures


def check_duplicate_artifact_names() -> list[Tuple[Path, Sequence[str]]]:
    failures: list[Tuple[Path, Sequence[str]]] = []
    by_name: dict[str, list[Path]] = defaultdict(list)
    for path in Path("artifacts").rglob("*.md"):
        by_name[path.name].append(path)
    for name, paths in sorted(by_name.items()):
        if name == "README.md":
            continue
        if len(paths) > 1:
            rendered = ", ".join(sorted(path.as_posix() for path in paths))
            failures.append((paths[0], [f"duplicate artifact filename detected: {name} -> {rendered}"]))
    return failures


def check_readme_catalog_links() -> list[Tuple[Path, Sequence[str]]]:
    readme = Path("README.md")
    lines = readme.read_text(encoding="utf-8").splitlines()
    failures: list[Tuple[Path, Sequence[str]]] = []
    current_section = ""
    in_catalog_table = False
    row_count = 0

    for line in lines:
        if CATALOG_SECTION_PATTERN.match(line):
            current_section = line.strip()
            in_catalog_table = False
            continue
        if current_section and line.startswith("| Document | Nature | Public role | Primary source basis"):
            in_catalog_table = True
            continue
        if in_catalog_table and line.startswith("|---"):
            continue
        if in_catalog_table and line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                failures.append((readme, [f"catalog row in '{current_section}' is missing the canonical artifact column: {line}"]))
                continue
            document = cells[0]
            if document == "Document":
                continue
            row_count += 1
            links = MARKDOWN_LINK_PATTERN.findall(cells[4])
            if not links:
                failures.append((readme, [f"catalog row '{document}' is missing a valid relative artifact link"]))
                continue
            target_link = next((link for link in links if link.endswith(".md")), links[0])
            target = Path(target_link)
            if not target.exists():
                failures.append((readme, [f"catalog row '{document}' points to a missing artifact: {target}"]))
                continue
            if target.parts[0] != "artifacts":
                failures.append((readme, [f"catalog row '{document}' must point into artifacts/: {target}"]))
                continue
            relative = target.relative_to("artifacts")
            if len(relative.parts) < 3:
                failures.append((readme, [f"catalog row '{document}' must point to artifacts/<dimension>/<artifact-type>/, got: {target}"]))
            if target.name == "incident_management_policy.md" and "Playbook" in document:
                failures.append((readme, [f"catalog row '{document}' points to a policy instead of the playbook artifact"]))
            continue
        if in_catalog_table and not line.startswith("|"):
            in_catalog_table = False

    if row_count != 103:
        failures.append((readme, [f"expected 103 catalog rows with canonical links, found {row_count}"]))
    return failures


def gather_all_checks() -> list[Tuple[Path, Sequence[str]]]:
    failures: list[Tuple[Path, Sequence[str]]] = []
    failures.extend(run_checks(iter_markdown_paths(), check_markdown))
    failures.extend(run_checks(iter_root_markdown_paths(), check_root_markdown))
    failures.extend(run_checks(iter_comment_paths(), check_comment_file))
    failures.extend(run_checks(iter_artifact_meta_paths(), check_comment_file))
    failures.extend(run_checks(iter_schema_paths(), check_schema_file))
    failures.extend(check_license_exists())
    failures.extend(check_artifact_layout())
    failures.extend(check_duplicate_artifact_names())
    failures.extend(check_readme_catalog_links())
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate frontmatter and traceability for governance artifacts.")
    parser.add_argument("--report-only", action="store_true", help="Print findings without changing the exit status.")
    args = parser.parse_args()
    failures = gather_all_checks()
    if not failures:
        print("Validator: OK (no issues found).")
        return 0
    for path, problems in failures:
        print(f"{path}:")
        for problem in problems:
            print(f"  - {problem}")
    if args.report_only:
        print("Validator: issues reported in report-only mode.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
