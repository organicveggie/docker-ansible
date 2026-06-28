#!/usr/bin/env python3
"""Regenerate the Tags table in README.md for a released version.

Run after a `vX.Y.Z` git tag is pushed (see the `update-readme` job in
.github/workflows/docker.yml). Replaces everything between the
TAGS:START/TAGS:END markers in README.md with a freshly computed table.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from combos import all_combos
from compute_tags import release_tags

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
DOCKERFILE_URL = (
    "https://github.com/organicveggie/docker-ansible/blob/main/images/{python}/{os_name}/{os_release}/Dockerfile"
)

START_MARKER = "<!-- TAGS:START -->"
END_MARKER = "<!-- TAGS:END -->"


def render_table(version: str) -> str:
    header = (
        "| Python | OS     | Release  | Tags |\n"
        "|:------ | ------ | -------- | ---- |"
    )
    rows = [header]
    for combo in all_combos():
        url = DOCKERFILE_URL.format(
            python=combo.python, os_name=combo.os_name.value, os_release=combo.os_release.value
        )
        tags = ", ".join(f"[`{tag}`]({url})" for tag in release_tags(version, combo))
        os_label = "Debian" if combo.os_name.value == "debian" else "Ubuntu"
        rows.append(f"| {combo.python}   | {os_label} | {combo.label}    | {tags} |")
    return "\n".join(rows)


def update_readme(version: str) -> None:
    text = README_PATH.read_text()
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    if not pattern.search(text):
        raise SystemExit(f"Markers {START_MARKER!r}/{END_MARKER!r} not found in {README_PATH}")

    replacement = f"{START_MARKER}\n{render_table(version)}\n{END_MARKER}"
    README_PATH.write_text(pattern.sub(replacement, text))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Regenerate README.md's Tags table.")
    parser.add_argument("--version", required=True, help='Git tag, e.g. "v0.2.0" or "0.2.0"')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    update_readme(args.version.removeprefix("v"))


if __name__ == "__main__":
    main()
