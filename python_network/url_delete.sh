#!/usr/bin/bash

# Check if the frist argument exit
if [ -z "$1" ]; then
    echo "Usage: curl <url>"
    exit 1
fi

URL="$1"

BODY=$(curl -X DELETE "$URL")

echo "Body of request: $BODY"
echo 
