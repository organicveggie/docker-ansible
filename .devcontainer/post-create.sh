#!/bin/bash

WORKSPACE_DIR=$1

GIT_CFG_SD=`git config get --all safe.directory |grep "${WORKSPACE_DIR}"`
if [[ -z $GIT_CFG_SD ]]; then
    git config --local --add safe.directory "${WORKSPACE_DIR}"
fi

set -x

python --version
pip --version

set +x