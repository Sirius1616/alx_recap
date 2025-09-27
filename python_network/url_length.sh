#!/usr/bin/bash

# Check for the the second argument exist
if [ -z "$1" ]; then
    echo "Usage: curl <url>"
    exit 1
fi

URL="$1"


# Assign scheme if scheme was not provided
if [ "$URL" != "http*://*"]; then
    URL="https://$URL"
fi

BODY=$(curl -X GET "$URL")

echo "Body of the URL: "
echo "$BODY"

echo 
echo "Length of body: ${#BODY}"