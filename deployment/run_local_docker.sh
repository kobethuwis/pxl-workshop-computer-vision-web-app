#!/bin/bash

MY_TAG=$1

# Run the Docker container
docker run -p 5000:5000 pxl-workshop-computer-vision-web-app:$MY_TAG
