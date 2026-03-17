#!/bin/bash

MY_TAG=$1

if [ -z "$MY_TAG" ]; then
    echo "Error: No tag provided. Add an argument when executing the script to set the tag."
    exit 1
fi

#TODO: Run the Docker container
