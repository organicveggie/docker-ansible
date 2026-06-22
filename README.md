# docker-ansible

[![Build Status](https://github.com/organicveggie/docker-ansible/actions/workflows/docker.yml/badge.svg)](https://github.com/organicveggie/docker-ansible/actions/workflows/docker.yml) [![License](https://img.shields.io/github/license/organicveggie/docker-ansible)](https://github.com/organicveggie/docker-ansible/blob/master/LICENSE)

Docker containers for [Ansible](https://docs.ansible.com) playbook and role testing.

# Container Images

## Support Matrix

* **Python:** `3.12`, `3.13`, `3.14`
* **OS:**
  * **Debian:** `Bookworm`, `Trixie`
  * **Ubuntu:** `24.04`, `25.10`, `26.04`
* **Architectures:** ([more info](https://github.com/docker-library/official-images#architectures-other-than-amd64))
  * `amd64`, `arm64v8`

| Python | OS     | Release  | Tags               |
|:------ | ------ | -------- | ------------------ |
| 3.12   | Debian | Bookworm | `-py3.12-bookworm` |
| 3.12   | Debian | Trixie   | `-py3.12-trixie`   |
| 3.12   | Ubuntu | 24.04    | `-py3.12-24.04`    |
| 3.12   | Ubuntu | 25.10    | `-py3.12-25.10`    |
| 3.12   | Ubuntu | 26.04    | `-py3.12-26.04`    |
| 3.13   | Debian | Bookworm | `-py3.13-bookworm` |
| 3.13   | Debian | Trixie   | `-py3.13-trixie`   |
| 3.13   | Ubuntu | 24.04    | `-py3.13-24.04`    |
| 3.13   | Ubuntu | 25.10    | `-py3.13-25.10`    |
| 3.13   | Ubuntu | 26.04    | `-py3.13-26.04`    |
| 3.14   | Debian | Bookworm | `-py3.14-bookworm` |
| 3.14   | Debian | Trixie   | `-py3.14-trixie`   |
| 3.14   | Ubuntu | 24.04    | `-py3.14-24.04`    |
| 3.14   | Ubuntu | 25.10    | `-py3.14-25.10`    |
| 3.14   | Ubuntu | 26.04    | `-py3.14-26.04`    |

## Tags

| Python | OS     | Release  | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:------ | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.12   | Debian | Bookworm | [`0.2.0-py3.12-bookworm`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/bookworm/Dockerfile), [`0.2-py3.12-bookworm`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/bookworm/Dockerfile), [`0-py3.12-bookworm`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/bookworm/Dockerfile), [`py3.12-bookworm-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/bookworm/Dockerfile) |
| 3.12   | Debian | Trixie   | [`0.2-py3.12-trixie`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/trixie/Dockerfile), [`0-py3.12-trixie`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/trixie/Dockerfile), [`py3.12-trixie-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/trixie/Dockerfile)                 | 
| 3.12   | Ubuntu | 24.04    | [`0.2.0-py3.12-24.04`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`0.2-py3.12-24.04`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`0-py3.12-24.04`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`py3.12-24.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`0.2.0-py3.12-noble`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`0.2-py3.12-noble`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`0-py3.12-noble`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`py3.12-noble-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile)                                                                                                                                                                                                                                                                                                                                                                  |
| 3.12   | Ubuntu | 25.10    | [`0.2.0-py3.12-25.10`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`0.2-py3.12-25.10`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`0-py3.12-25.10`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`py3.12-25.10-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`0.2.0-py3.12-questing`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`0.2-py3.12-questing`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`0-py3.12-questing`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`py3.12-questing-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile)                                                                                                                                                                                                                                                                                                                                                      |
| 3.12   | Ubuntu | 26.04    | [`0.2.0-py3.12-26.04`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`0.2-py3.12-26.04`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`0-py3.12-26.04`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`py3.12-26.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`0.2.0-py3.12-resolute`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`0.2-py3.12-resolute`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`0-py3.12-resolute`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`py3.12-resolute-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile)                                                                                                                                                                                                                                                                                                                                                      |
| 3.13   | Debian | Bookworm |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.13   | Debian | Trixie   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.13   | Ubuntu | 24.04    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.13   | Ubuntu | 25.10    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.13   | Ubuntu | 26.04    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.14   | Debian | Bookworm |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.14   | Debian | Trixie   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.14   | Ubuntu | 24.04    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.14   | Ubuntu | 25.10    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3.14   | Ubuntu | 26.04    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Python 3.12

* [`0.2.0-py3.12-bookworm, 0.2-py3.12-bookworm, 0-py3.12-bookworm, py3.12-bookworm-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/bookworm/Dockerfile)
* [`0.2.0-py3.12-trixie, 0.2-py3.12-trixie, 0-py3.12-trixie, py3.12-trixie-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/debian/trixie/Dockerfile)
* [`0.2.0-py3.12-24.04, 0.2-py3.12-24.04, 0-py3.12-24.04, py3.12-24.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/24.04/Dockerfile)
* [`0.2.0-py3.12-25.10, 0.2-py3.12-25.10, 0-py3.12-25.10, py3.12-25.10-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/25.10/Dockerfile)
* [`0.2.0-py3.12-26.04, 0.2-py3.12-26.04, 0-py3.12-26.04, py3.12-26.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.12/ubuntu/26.04/Dockerfile)

### Python 3.13

* [`0.2.0-py3.13-bookworm, 0.2-py3.13-bookworm, 0-py3.13-bookworm, py3.13-bookworm-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.13/debian/bookworm/Dockerfile)
* [`0.2.0-py3.13-trixie, 0.2-py3.13-trixie, 0-py3.13-trixie, py3.13-trixie-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.13/debian/trixie/Dockerfile)
* [`0.2.0-py3.13-24.04, 0.2-py3.13-24.04, 0-py3.13-24.04, py3.13-24.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.13/ubuntu/24.04/Dockerfile)
* [`0.2.0-py3.13-25.10, 0.2-py3.13-25.10, 0-py3.13-25.10, py3.13-25.10-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.13/ubuntu/25.10/Dockerfile)
* [`0.2.0-py3.13-26.04, 0.2-py3.13-26.04, 0-py3.13-26.04, py3.13-26.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.13/ubuntu/26.04/Dockerfile)


### Python 3.14

* [`0.2.0-py3.14-bookworm, 0.2-py3.14-bookworm, 0-py3.14-bookworm, py3.14-bookworm-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.14/debian/bookworm/Dockerfile)
* [`0.2.0-py3.14-trixie, 0.2-py3.14-trixie, 0-py3.14-trixie, py3.14-trixie-latest, 0.1.0, 0.1, 0, latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.14/debian/trixie/Dockerfile)
* [`0.2.0-py3.14-24.04, 0.2-py3.14-24.04, 0-py3.14-24.04, py3.14-24.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.14/ubuntu/24.04/Dockerfile)
* [`0.2.0-py3.14-25.10, 0.2-py3.14-25.10, 0-py3.14-25.10, py3.14-25.10-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.14/ubuntu/25.10/Dockerfile)
* [`0.2.0-py3.14-26.04, 0.2-py3.14-26.04, 0-py3.14-26.04, py3.14-26.04-latest`](https://github.com/organicveggie/docker-ansible/blob/main/images/3.14/ubuntu/26.04/Dockerfile)

# Usage

## Docker

```shell
$ docker pull ghcr.io/organicveggie/docker-ansible:py3.12-bookworm-latest
```

## Molecule

```yaml
platforms:
  - name: instance
    image: "ghcr.io/organicveggie/docker-ansible:0.2-py3.12-24.04"
    command: ${MOLECULE_DOCKER_COMMAND:-""}
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    privileged: true
    pre_build_image: true

```
