#!/usr/bin/env python3
"""Compute the release tags for one (python, OS release) combo.

Mirrors the merge job in .github/workflows/docker.yml: the workflow's
tag trigger (`v[0-9]+.[0-9]+.[0-9]+`) only ever matches stable
versions, so there is no pre-release case to handle here.
"""
from __future__ import annotations

import argparse

from combos import Combo, OSRelease


def release_tags(version: str, combo: Combo) -> list[str]:
    """Tags for `version` (e.g. "0.2.0", no leading "v") on this combo."""
    major, minor, _ = version.split(".", 2)
    major_minor = f"{major}.{minor}"
    suffix = f"py{combo.python}-{combo.os_release.value}"

    def namespace(suf: str) -> list[str]:
        return [f"{version}-{suf}", f"{major_minor}-{suf}", f"{major}-{suf}", f"{suf}-latest"]

    tags = namespace(suffix)
    if combo.alias:
        tags += namespace(f"py{combo.python}-{combo.alias}")
    if combo.is_canonical:
        tags += [version, major_minor, major, "latest"]
    return tags


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print release tags for one combo.")
    parser.add_argument("--version", required=True, help='Version without "v" prefix, e.g. "0.2.0"')
    parser.add_argument("--python", required=True, dest="python_version")
    parser.add_argument("--os-release", required=True, choices=[r.value for r in OSRelease])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    combo = Combo(python=args.python_version, os_release=OSRelease(args.os_release))
    print("\n".join(release_tags(args.version, combo)))


if __name__ == "__main__":
    main()
