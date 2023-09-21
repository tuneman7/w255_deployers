#!/bin/bash
source ./env.sh

#get these values from the env bash file
# IMAGE_NAME=w255_l3_api_web_consumer
# APP_NAME=w255_l3_api_web_consumer
# DOCKER_FILE=Dockerfile.api_consumer



find . -type d -name __pycache__ -exec rm -r {} \+

#docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

echo "docker stop ${APP_NAME}"
docker stop ${APP_NAME}
echo "docker rm ${APP_NAME}"
docker rm ${APP_NAME}

#build docker from the docker file
echo "docker build -t ${IMAGE_NAME} -f ${DOCKER_FILE}" 
docker build -t ${IMAGE_NAME} -f ${DOCKER_FILE} .


