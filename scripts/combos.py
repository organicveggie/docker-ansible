#!/usr/bin/env python3
"""Single source of truth for the python/OS build matrix.

Consumed by generate-dockerfiles.py, compute_tags.py, and
update_readme_tags.py so the set of supported combinations only needs
to change in one place.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class OSName(StrEnum):
    DEBIAN = "debian"
    UBUNTU = "ubuntu"


class OSRelease(StrEnum):
    BOOKWORM = "bookworm"
    TRIXIE = "trixie"
    NOBLE = "24.04"
    QUESTING = "25.10"
    RESOLUTE = "26.04"


OS_RELEASE_MAP: dict[OSRelease, OSName] = {
    OSRelease.BOOKWORM: OSName.DEBIAN,
    OSRelease.TRIXIE: OSName.DEBIAN,
    OSRelease.NOBLE: OSName.UBUNTU,
    OSRelease.QUESTING: OSName.UBUNTU,
    OSRelease.RESOLUTE: OSName.UBUNTU,
}

# Ubuntu codename alias for tags like "0.2-py3.12-noble". Debian releases
# have no alias tag.
OS_RELEASE_ALIAS: dict[OSRelease, str | None] = {
    OSRelease.BOOKWORM: None,
    OSRelease.TRIXIE: None,
    OSRelease.NOBLE: "noble",
    OSRelease.QUESTING: "questing",
    OSRelease.RESOLUTE: "resolute",
}

# Display label for the README tags table.
OS_RELEASE_LABEL: dict[OSRelease, str] = {
    OSRelease.BOOKWORM: "Bookworm",
    OSRelease.TRIXIE: "Trixie",
    OSRelease.NOBLE: "24.04",
    OSRelease.QUESTING: "25.10",
    OSRelease.RESOLUTE: "26.04",
}

OS_DEFAULT_PYTHON_VERSION: dict[OSRelease, str] = {
    OSRelease.BOOKWORM: "3.11",
    OSRelease.TRIXIE: "3.14",
    OSRelease.NOBLE: "3.12",
    OSRelease.QUESTING: "3.13",
    OSRelease.RESOLUTE: "3.14",
}

PYTHON_VERSIONS: list[str] = ["3.12", "3.13", "3.14"]

OS_RELEASES: list[OSRelease] = [
    OSRelease.BOOKWORM,
    OSRelease.TRIXIE,
    OSRelease.NOBLE,
    OSRelease.QUESTING,
    OSRelease.RESOLUTE,
]

# The (python, os_release) combo that also receives bare tags with no
# python/os suffix (e.g. "0.2.0", "latest").
CANONICAL_PYTHON = "3.14"
CANONICAL_OS_RELEASE = OSRelease.TRIXIE


@dataclass(frozen=True)
class Combo:
    python: str
    os_release: OSRelease

    @property
    def os_name(self) -> OSName:
        return OS_RELEASE_MAP[self.os_release]

    @property
    def alias(self) -> str | None:
        return OS_RELEASE_ALIAS[self.os_release]

    @property
    def label(self) -> str:
        return OS_RELEASE_LABEL[self.os_release]

    @property
    def is_canonical(self) -> bool:
        return (
            self.python == CANONICAL_PYTHON
            and self.os_release == CANONICAL_OS_RELEASE
        )


def all_combos() -> list[Combo]:
    return [
        Combo(python=python, os_release=os_release)
        for python in PYTHON_VERSIONS
        for os_release in OS_RELEASES
    ]
