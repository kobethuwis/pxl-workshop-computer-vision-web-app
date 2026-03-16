#!/bin/bash

MY_TAG=$1

if [ -z "$MY_TAG" ]; then
    echo "Error: No tag provided. Add an argument when executing the script to set the tag."
    exit 1
fi

# Run the Docker container
docker run -p 5000:5000 pxl-workshop-computer-vision-web-app:$MY_TAG
