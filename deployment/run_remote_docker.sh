#!/bin/bash

MY_TAG=$1

if [ -z "$MY_TAG" ]; then
    echo "Error: No tag provided. Add an argument when executing the script to set the tag."
    exit 1
fi

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
AWS_REGION=$(aws configure get region)

# Run the Docker container
docker run -p 5000:5000 $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/pxl-workshop-computer-vision-web-app:$MY_TAG
