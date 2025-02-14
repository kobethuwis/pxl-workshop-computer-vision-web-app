#!/bin/bash

MY_TAG=$1

# Build the Docker image
docker build -t pxl-workshop-computer-vision-web-app:$MY_TAG -f ./deployment/Dockerfile .