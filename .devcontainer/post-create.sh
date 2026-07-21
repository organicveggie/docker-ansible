#!/bin/sh

WORKSPACE_DIR=$1

set -x

git config --local --add safe.directory "${WORKSPACE_DIR}"
gpg --import /home/vscode/.gnupg/git-public-key.asc

python --version
pip --version

set +x