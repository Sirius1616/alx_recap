#!/usr/bin/bash

# Check if the second argument was passed
if [ -z "$1"]; then
    echo "Usage: curl <ur>"
    exit 1
fi

URL="$1"

BODY="$"