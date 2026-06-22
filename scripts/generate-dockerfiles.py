#!/usr/bin/env python3
from __future__ import annotations

import argparse
from enum import StrEnum
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "images"
DEFAULT_TEMPLATE = IMAGES_DIR / "Dockerfile.default.j2"
CUSTOM_TEMPLATE = IMAGES_DIR / "Dockerfile.custom.j2"


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
    OSRelease.BOOKWORM: "3.11",
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
    parser = argparse.ArgumentParser(
        description="Generate Dockerfiles from a Jinja2 template."
    )
    parser.add_argument(
        "--default-template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help=f"Path to Jinja2 default template (default: {DEFAULT_TEMPLATE})",
    )
    parser.add_argument(
        "--custom-template",
        type=Path,
        default=CUSTOM_TEMPLATE,
        help=f"Path to Jinja2 custom template (default: {CUSTOM_TEMPLATE})",
    )
    return parser.parse_args()


def generate(default_template_path: Path, custom_template_path: Path) -> None:
    env = Environment(loader=FileSystemLoader(str(default_template_path.parent)))
    default_template = env.get_template(default_template_path.name)
    custom_template = env.get_template(custom_template_path.name)

    for python_version, os_releases in VERSIONS.items():
        py_major, py_minor = python_version.split(".")
        for os_release in os_releases:
            os_name = OS_RELEASE_MAP[os_release]
            out_dir = IMAGES_DIR / python_version / os_name / os_release
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / "Dockerfile"

            if OS_DEFAULT_PYTHON_VERSION[os_release] == python_version:
                template = default_template
                template_path = default_template_path
            else:
                template = custom_template
                template_path = custom_template_path

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
            print(
                f"wrote {out_path.relative_to(REPO_ROOT)} from {template_path.relative_to(REPO_ROOT)}"
            )


def main() -> None:
    args = parse_args()
    generate(args.default_template, args.custom_template)


if __name__ == "__main__":
    main()
