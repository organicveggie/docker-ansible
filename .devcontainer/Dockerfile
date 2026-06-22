FROM python:3.12-bookworm

# Create a non-root user with UID 1000 and GID 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Set build-time argument for build version, with a default value
ARG IMAGE_BUILD_VERSION=v0.0.0-unknown
ENV IMAGE_BUILD_VERSION=${IMAGE_BUILD_VERSION}

# Setup the devcontainer user and permissions
RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends sudo

# Create the devcontainer user and add to sudoers
groupadd --gid $USER_GID $USERNAME 
useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME 
chmod 0440 /etc/sudoers.d/$USERNAME

# Ensure bash is set as the default shell for the devcontainer user
chsh -s /bin/bash $USERNAME
RUN_CMD_EOF

# Install Docker CLI, buildx, and other necessary tools
RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    gnupg \
    libonig-dev \
    openssh-client \
    rsync \
    vim

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian trixie stable" \
       > /etc/apt/sources.list.d/docker.list

apt-get update
apt-get install -y --no-install-recommends \
    docker-ce-cli \
    docker-buildx-plugin

# Clean up APT cache to reduce image size
rm -rf /var/lib/apt/lists/*
RUN_CMD_EOF

# Set the active user for subsequent commands
USER $USERNAME

COPY requirements.txt /tmp/requirements.txt
RUN <<RUN_CMD_EOF
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r /tmp/requirements.txt
RUN_CMD_EOF

WORKDIR /workspaces
