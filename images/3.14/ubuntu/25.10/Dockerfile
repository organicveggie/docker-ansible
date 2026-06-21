FROM buildpack-deps:25.10-curl
# FROM ubuntu:25.10

# Set build-time argument for build version, with a default value
ARG IMAGE_BUILD_VERSION=v0.0.0
ENV IMAGE_BUILD_VERSION=${IMAGE_BUILD_VERSION}

ENV LANG C.UTF-8

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive


RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends software-properties-common

add-apt-repository ppa:deadsnakes/ppa
apt update
apt install \
    python3.14 \
    python3.14-dev

mkdir /tmp/python3.14-pip-install
curl https://bootstrap.pypa.io/get-pip.py -o /tmp/python3.14-pip-install/get-pip.py
python3.14 /tmp/python3.14-pip-install/get-pip.py
rm -fR /tmp/python3.14-pip-install

# Register the native Ubuntu python3 (3.13) and the new python3.14
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13) 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 2

# Force the system to use Python 3.14 non-interactively
update-alternatives --set python3 /usr/bin/python3.14
/usr/bin/python3 --version

# Clean up APT cache to reduce image size
rm -rf /var/lib/apt/lists/*
RUN_CMD_EOF

# Define image labels
LABEL org.opencontainers.image.title="organicveggie/docker-ansible" \
    org.opencontainers.image.description="Docker image for Ansible role testing with Python 3.14 on Ubuntu 25.10" \
    org.opencontainers.image.version="${IMAGE_BUILD_VERSION}" \
    org.opencontainers.image.licenses="GPL-3.0-or-later" \
    org.opencontainers.image.source="https://github.com/organicveggie/docker-ansible"

CMD ["python3.14"]