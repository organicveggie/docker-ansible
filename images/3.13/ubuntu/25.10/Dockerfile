FROM buildpack-deps:25.10

# Set build-time argument for build version, with a default value
ARG IMAGE_BUILD_VERSION=v0.0.0
ENV IMAGE_BUILD_VERSION=${IMAGE_BUILD_VERSION}

ENV LANG=C.UTF-8

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive



RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
    python3-dev \
    python3-setuptools \
    python3-pip \
    python3-yaml \
RUN_CMD_EOF

RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
    iproute2 \
    libffi-dev \
    libssl-dev \
    libyaml-dev \
    libonig-dev \
    locales \
    rsyslog \
    systemd \
    systemd-cron \
    sudo

# Clean up APT cache to reduce image size
apt-get clean
rm -fR /var/lib/apt/lists/*
rm -fR /usr/share/doc
rm -fR /usr/share/man

# Remove useless Python environment warning flag.
rm -rf /usr/lib/python3.12/EXTERNALLY-MANAGED
RUN_CMD_EOF

RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf

# Fix potential UTF-8 errors with ansible-test.
RUN locale-gen en_US.UTF-8

# Install Ansible via Pip
RUN --mount=type=bind,source=images/requirements.txt,target=/tmp/requirements.txt <<RUN_CMD_EOF
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r /tmp/requirements.txt
RUN_CMD_EOF

COPY images/initctl_faker .
RUN <<RUN_CMD_EOF
chmod +x initctl_faker
rm -fr /sbin/initctl
ln -s /initctl_faker /sbin/initctl
RUN_CMD_EOF

# Install Ansible inventory file.
RUN <<RUN_CMD_EOF
mkdir -p /etc/ansible
echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts
RUN_CMD_EOF

# Remove unnecessary getty and udev targets that result in high CPU usage when using
# multiple containers with Molecule (https://github.com/ansible/molecule/issues/1104)
RUN <<RUN_CMD_EOF
rm -f /lib/systemd/system/systemd*udev*
rm -f /lib/systemd/system/getty.target
RUN_CMD_EOF

# Define image labels
LABEL org.opencontainers.image.authors="Sean Laurent" \
    org.opencontainers.image.base.name="buildpack-deps:25.10-curl" \
    org.opencontainers.image.description="Docker image for Ansible role testing with Python 3.13 on Ubuntu 25.10" \
    org.opencontainers.image.licenses="GPL-3.0-or-later" \
    org.opencontainers.image.source="https://github.com/organicveggie/docker-ansible" \
    org.opencontainers.image.title="organicveggie/docker-ansible" \
    org.opencontainers.image.version="${IMAGE_BUILD_VERSION}"

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/lib/systemd/systemd"]
# ENTRYPOINT ["python3.13"]