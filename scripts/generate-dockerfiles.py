#!/usr/bin/env python3
from __future__ import annotations

import argparse
from enum import StrEnum
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = REPO_ROOT / "Dockerfile.template.j2"
IMAGES_DIR = REPO_ROOT / "images"


class OSRelease(StrEnum):
    BOOKWORM = "bookworm"
    TRIXIE = "trixie"
    NOBLE = "24.04"
    QUESTING = "25.10"
    RESOLUTE = "26.04"
    STONKING = "26.10"


class OSName(StrEnum):
    DEBIAN = "debian"
    UBUNTU = "ubuntu"


OS_RELEASE_MAP: dict[OSRelease, OSName] = {
    OSRelease.BOOKWORM: OSName.DEBIAN,
    OSRelease.TRIXIE: OSName.DEBIAN,
    OSRelease.NOBLE: OSName.UBUNTU,
    OSRelease.QUESTING: OSName.UBUNTU,
    OSRelease.RESOLUTE: OSName.UBUNTU,
    OSRelease.STONKING: OSName.UBUNTU,
}


OS_DEFAULT_PYTHON_VERSION: dict[OSRelease, str] = {
    OSRelease.BOOKWORM: "3.12",
    OSRelease.TRIXIE: "3.14",
    OSRelease.NOBLE: "3.12",
    OSRelease.QUESTING: "3.13",
    OSRelease.RESOLUTE: "3.14",
    OSRelease.STONKING: "3.14",
}


VERSIONS: dict[str, list[OSRelease]] = {
    "3.14": [
        OSRelease.BOOKWORM,
        OSRelease.TRIXIE,
        OSRelease.NOBLE,
        OSRelease.QUESTING,
        OSRelease.RESOLUTE,
        OSRelease.STONKING,
    ],
    "3.13": [
        OSRelease.BOOKWORM,
        OSRelease.TRIXIE,
        OSRelease.NOBLE,
        OSRelease.QUESTING,
        OSRelease.RESOLUTE,
        OSRelease.STONKING,
    ],
    "3.12": [
        OSRelease.BOOKWORM,
        OSRelease.TRIXIE,
        OSRelease.NOBLE,
        OSRelease.QUESTING,
        OSRelease.RESOLUTE,
        OSRelease.STONKING,
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Dockerfiles from a Jinja2 template.")
    parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help=f"Path to Jinja2 template (default: {DEFAULT_TEMPLATE})",
    )
    return parser.parse_args()


def generate(template_path: Path) -> None:
    env = Environment(loader=FileSystemLoader(str(template_path.parent)))
    template = env.get_template(template_path.name)

    for python_version, os_releases in VERSIONS.items():
        py_major, py_minor = python_version.split('.')
        for os_release in os_releases:
            os_name = OS_RELEASE_MAP[os_release]
            out_dir = IMAGES_DIR / python_version / os_name / os_release
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / "Dockerfile"
            out_path.write_text(
                template.render(
                    python_version=python_version,
                    python_major_version=py_major,
                    python_minor_version=py_minor,
                    os_default_python=OS_DEFAULT_PYTHON_VERSION[os_release],
                    os_name=os_name.value,
                    os_release=os_release.value,
                )
            )
            print(f"wrote {out_path.relative_to(REPO_ROOT)}")


def main() -> None:
    args = parse_args()
    generate(args.template)


if __name__ == "__main__":
    main()
