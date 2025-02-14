#!/bin/bash

AWS_ACCESS_KEY_ID=$1
AWS_SECRET_ACCESS_KEY=$2
AWS_REGION=eu-west-1

# Configure AWS CLI with provided credentials
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region $AWS_REGION

# Verify AWS credentials
aws sts get-caller-identity &> /dev/null

if [ $? -eq 0 ]; then
    echo "AWS config succeeded"
else
    echo "AWS config failed"
fi
