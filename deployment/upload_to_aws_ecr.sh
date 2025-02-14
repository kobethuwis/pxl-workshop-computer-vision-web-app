#!/bin/bash

MY_TAG=$1
AWS_REGION=$(aws configure get region)
ECR_REPOSITORY_NAME=pxl-workshop-computer-vision-web-app
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)

# Authenticate Docker to the Amazon ECR registry
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Tag the Docker image
docker tag $ECR_REPOSITORY_NAME:$MY_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY_NAME:$MY_TAG

# Push the Docker image to the ECR repository
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY_NAME:$MY_TAG
