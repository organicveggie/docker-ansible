#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import requests
from jinja2 import Environment, FileSystemLoader

from combos import OS_DEFAULT_PYTHON_VERSION, PYTHON_APT_REF, all_combos

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "images"
DEFAULT_TEMPLATE = IMAGES_DIR / "Dockerfile.default.j2"
CUSTOM_TEMPLATE = IMAGES_DIR / "Dockerfile.custom.j2"

_digest_cache: dict[str, str] = {}


def fetch_image_digest(image: str, tag: str) -> str:
    """Return the manifest list digest for image:tag from Docker Hub."""
    cache_key = f"{image}:{tag}"
    if cache_key in _digest_cache:
        return _digest_cache[cache_key]

    namespace = image if "/" in image else f"library/{image}"

    token_resp = requests.get(
        "https://auth.docker.io/token",
        params={"service": "registry.docker.io", "scope": f"repository:{namespace}:pull"},
        timeout=30,
    )
    token_resp.raise_for_status()
    token = token_resp.json()["token"]

    manifest_resp = requests.head(
        f"https://registry-1.docker.io/v2/{namespace}/manifests/{tag}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": ",".join([
                "application/vnd.oci.image.index.v1+json",
                "application/vnd.docker.distribution.manifest.list.v2+json",
            ]),
        },
        timeout=30,
    )
    manifest_resp.raise_for_status()
    digest = manifest_resp.headers["Docker-Content-Digest"]
    _digest_cache[cache_key] = digest
    return digest


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

        is_default = OS_DEFAULT_PYTHON_VERSION[combo.os_release] == combo.python
        if is_default:
            template = default_template
            template_path = default_template_path
        else:
            template = custom_template
            template_path = custom_template_path

        buildpack_deps_digest = fetch_image_digest("buildpack-deps", combo.os_release.value)

        if is_default:
            if combo.os_name.value == "debian":
                final_image = "debian"
                final_tag = f"{combo.os_release.value}-slim"
            else:
                final_image = combo.os_name.value
                final_tag = combo.os_release.value
            extra_vars: dict[str, str] = {
                "base_image_digest": fetch_image_digest(final_image, final_tag),
            }
        else:
            extra_vars = {
                "buildpack_deps_curl_digest": fetch_image_digest(
                    "buildpack-deps", f"{combo.os_release.value}-curl"
                ),
            }

        out_path.write_text(
            template.render(
                python_version=combo.python,
                python_major_version=py_major,
                python_minor_version=py_minor,
                os_default_python=OS_DEFAULT_PYTHON_VERSION[combo.os_release],
                os_name=combo.os_name.value,
                os_release=combo.os_release.value,
                python_apt_ref=PYTHON_APT_REF[combo.os_release],
                buildpack_deps_digest=buildpack_deps_digest,
                **extra_vars,
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
