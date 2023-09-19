#!/bin/bash
deactivate
rm -rf ./w210_web
IMAGE_NAME=w210_web_aplication
APP_NAME=w210_web_aplication
DOCKER_FILE=Dockerfile.210proj

docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

echo "docker stop ${APP_NAME}"
docker stop ${APP_NAME}
echo "docker rm ${APP_NAME}"
docker rm ${APP_NAME}

#build docker from the docker file
echo "docker build -t ${IMAGE_NAME} -f ${DOCKER_FILE}" 
docker build -t ${IMAGE_NAME} -f ${DOCKER_FILE} .
echo "docker run --name ${APP_NAME} -p  80:80 ${IMAGE_NAME}"
docker run --name ${APP_NAME} -p  80:80 ${IMAGE_NAME} 
