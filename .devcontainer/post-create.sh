#!/bin/sh

WORKSPACE_DIR=$1
HOME_DIR="/home/vscode"

set -x

git config --local --add safe.directory "${WORKSPACE_DIR}"
gpg --import ${HOME_DIR}/.gnupg/git-public-key.asc

python --version
pip --version

set +x