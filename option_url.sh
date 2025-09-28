#!/usr/bin/bash

# Check if the second argument was passed
if [ -z "$1"]; then
    echo "Usage: curl <url>"
    exit 1
fi

URL="$1"

BODY=$(curl -X OPTION "$1")

echo "Body of url: $BODY"