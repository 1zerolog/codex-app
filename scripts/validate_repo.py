#!/usr/bin/env python3
"""Validate the Codex Labkit repository layout."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KEBAB_CASE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_required_files(errors: list[str]) -> None:
    required = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "AGENTS.md",
        "skills/README.md",
        "plugins/README.md",
        "docs/architecture.md",
    ]
    for relpath in required:
        if not (ROOT / relpath).is_file():
            fail(f"Missing required file: {relpath}", errors)


def validate_skills(errors: list[str]) -> None:
    for skill_file in sorted((ROOT / "skills").glob("*/SKILL.md")):
        folder = skill_file.parent.name
        if not KEBAB_CASE.match(folder):
            fail(f"Skill folder is not kebab-case: {folder}", errors)

        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"Skill is missing YAML frontmatter: {skill_file.relative_to(ROOT)}", errors)
            continue

        frontmatter_end = text.find("\n---\n", 4)
        if frontmatter_end == -1:
            fail(f"Skill frontmatter is not closed: {skill_file.relative_to(ROOT)}", errors)
            continue

        frontmatter = text[4:frontmatter_end]
        if "name:" not in frontmatter:
            fail(f"Skill frontmatter missing name: {skill_file.relative_to(ROOT)}", errors)
        if "description:" not in frontmatter:
            fail(f"Skill frontmatter missing description: {skill_file.relative_to(ROOT)}", errors)


def validate_plugins(errors: list[str]) -> None:
    for plugin_dir in sorted((ROOT / "plugins").iterdir()):
        if not plugin_dir.is_dir():
            continue
        if not KEBAB_CASE.match(plugin_dir.name):
            fail(f"Plugin folder is not kebab-case: {plugin_dir.name}", errors)

        manifest = plugin_dir / ".codex-plugin" / "plugin.json"
        if not manifest.is_file():
            fail(f"Plugin missing manifest: {plugin_dir.relative_to(ROOT)}", errors)
            continue

        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"Invalid plugin manifest JSON: {manifest.relative_to(ROOT)}: {exc}", errors)
            continue

        for key in ("name", "version", "description"):
            if not data.get(key):
                fail(f"Plugin manifest missing {key}: {manifest.relative_to(ROOT)}", errors)


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    validate_skills(errors)
    validate_plugins(errors)

    if errors:
        print("Codex Labkit validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Codex Labkit validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
