FROM buildpack-deps:24.04-curl
# FROM ubuntu:24.04

# Set build-time argument for build version, with a default value
ARG IMAGE_BUILD_VERSION=v0.0.0
ENV IMAGE_BUILD_VERSION=${IMAGE_BUILD_VERSION}

ENV LANG C.UTF-8

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive




# Define image labels
LABEL org.opencontainers.image.title="organicveggie/docker-ansible" \
    org.opencontainers.image.description="Docker image for Ansible role testing with Python 3.12 on Ubuntu 24.04" \
    org.opencontainers.image.version="${IMAGE_BUILD_VERSION}" \
    org.opencontainers.image.licenses="GPL-3.0-or-later" \
    org.opencontainers.image.source="https://github.com/organicveggie/docker-ansible"

CMD ["python3.12"]