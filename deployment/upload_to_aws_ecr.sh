#!/bin/bash

MY_TAG=$1
AWS_REGION=$(aws configure get region)
ECR_REPOSITORY_NAME=pxl-workshop-computer-vision-web-app
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)

#TODO: Authenticate Docker to the Amazon ECR registry


#TODO: Tag the Docker image


#TODO: Push the Docker image to the ECR repository

