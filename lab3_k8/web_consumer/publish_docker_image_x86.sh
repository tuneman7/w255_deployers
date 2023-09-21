#!/bin/bash
source ./env.sh
find . -type d -name __pycache__ -exec rm -r {} \+
rm -rf ./myproj
. build_docker.sh
docker login
docker tag ${IMAGE_NAME} donirwinberkeley/${IMAGE_NAME}:x86_latest
docker push donirwinberkeley/${IMAGE_NAME}:x86_latest
