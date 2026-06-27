#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from combos import OS_DEFAULT_PYTHON_VERSION, PYTHON_APT_REF, all_combos

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "images"
DEFAULT_TEMPLATE = IMAGES_DIR / "Dockerfile.default.j2"
CUSTOM_TEMPLATE = IMAGES_DIR / "Dockerfile.custom.j2"


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

    for combo in all_combos():
        py_major, py_minor = combo.python.split(".")
        out_dir = IMAGES_DIR / combo.python / combo.os_name.value / combo.os_release.value
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "Dockerfile"

        if OS_DEFAULT_PYTHON_VERSION[combo.os_release] == combo.python:
            template = default_template
            template_path = default_template_path
        else:
            template = custom_template
            template_path = custom_template_path

        out_path.write_text(
            template.render(
                python_version=combo.python,
                python_major_version=py_major,
                python_minor_version=py_minor,
                os_default_python=OS_DEFAULT_PYTHON_VERSION[combo.os_release],
                os_name=combo.os_name.value,
                os_release=combo.os_release.value,
                python_apt_ref=PYTHON_APT_REF[combo.os_release],
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
