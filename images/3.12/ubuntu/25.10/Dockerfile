# ==========================================
# Stage 1: Version Resolver (Always runs, but tiny)
# ==========================================
FROM buildpack-deps:25.10 AS version-resolver
RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y curl
rm -rf /var/lib/apt/lists/*
RUN_CMD_EOF

# Resolve the version and save it to a file
RUN <<RUN_CMD_EOF
set -eux
LATEST_PY=$(curl -s https://www.python.org/ftp/python/ | grep -o '3\.12\.[0-9]\+/' | cut -d '/' -f1 | sort -V | tail -n1)
echo "${LATEST_PY}" > /tmp/python_version
RUN_CMD_EOF

# ==========================================
# Stage 2: Build Environment
# ==========================================
FROM buildpack-deps:25.10 AS builder

ENV LANG=C.UTF-8

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive


RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libbz2-dev \
    libdb5.3-dev \
    libexpat1-dev \
    libffi-dev \
    libgdbm-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libuuid1 \
    software-properties-common \
    zlib1g-dev
RUN_CMD_EOF

# Resolve, download, and compile the latest Python 3.12.x
COPY --from=version-resolver /tmp/python_version /tmp/python_version
RUN <<RUN_CMD_EOF
set -eux
VERSION=$(cat /tmp/python_version)
echo "Building Python ${VERSION}..."
curl -O "https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tar.xz"
tar -xf "Python-${VERSION}.tar.xz"
cd "Python-${VERSION}"

# Configure with a custom prefix to make copying easy in the next stage
./configure --enable-loadable-sqlite-extensions \
    --enable-optimizations \
    --enable-option-checking=fatal \
    --prefix=/opt/python3.12 \
    --with-ensurepip=install

make -j$(nproc)
make install
RUN_CMD_EOF

RUN <<RUN_CMD_EOF
# Install required libraries for installing Ansible
apt-get install -y --no-install-recommends \
    libffi-dev \
    libonig-dev \
    libssl-dev \
    libyaml-dev
rm -rf /var/lib/apt/lists/*
RUN_CMD_EOF

ENV PYTHON_PATH=/opt/python3.12/bin/python3.12

# Install Ansible via Pip
RUN --mount=type=bind,source=images/requirements.txt,target=/tmp/requirements.txt <<RUN_CMD_EOF
${PYTHON_PATH} -m pip install --no-cache-dir --upgrade pip
${PYTHON_PATH} -m pip install --no-cache-dir -r /tmp/requirements.txt
RUN_CMD_EOF

# ==========================================
# Stage 3: Final Lightweight Runtime Image
# ==========================================
FROM buildpack-deps:25.10-curl

# Set build-time argument for build version, with a default value
ARG IMAGE_BUILD_VERSION=v0.0.0
ENV IMAGE_BUILD_VERSION=${IMAGE_BUILD_VERSION}

ENV LANG=C.UTF-8

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive


RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
    iproute2 \
    libffi8 \
    liblzma5 \
    libonig5 \
    libreadline8 \
    libsqlite3-0 \
    libssl3 \
    libbz2-1.0 \
    lsb-release \
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
RUN_CMD_EOF

ENV PYTHON_PATH=/opt/python3.12

# Copy the entire compiled Python directory from the builder stage
COPY --from=builder ${PYTHON_PATH} ${PYTHON_PATH}

# Create the symlinks to the custom Python installation into the system PATH
RUN <<RUN_CMD_EOF
ln -sf ${PYTHON_PATH}/bin/python3.12 /usr/local/bin/python3.12
ln -sf ${PYTHON_PATH}/bin/pip3.12 /usr/local/bin/pip3
ln -sf /usr/local/bin/python3.12 /usr/local/bin/python3

ln -sf ${PYTHON_PATH}/bin/ansible /usr/local/bin/ansible

python3 --version
pip3 --version
ansible --version
RUN_CMD_EOF

RUN <<RUN_CMD_EOF
# Remove useless Python environment warning flag.
rm -rf /usr/lib/python3.13/EXTERNALLY-MANAGED

sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf

# Fix potential UTF-8 errors with ansible-test.
locale-gen en_US.UTF-8
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
    org.opencontainers.image.description="Docker image for Ansible role testing with Python 3.12 on Ubuntu 25.10" \
    org.opencontainers.image.licenses="GPL-3.0-or-later" \
    org.opencontainers.image.source="https://github.com/organicveggie/docker-ansible" \
    org.opencontainers.image.title="organicveggie/docker-ansible" \
    org.opencontainers.image.version="${IMAGE_BUILD_VERSION}"

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
CMD ["/lib/systemd/systemd"]