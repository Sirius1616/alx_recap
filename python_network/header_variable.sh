#!/usr/bin/bash

# Check if second argument was passed
if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

URL="$1"

if [ "$URL" != "http*://*"]; then
    URL="https://$URL"
fi

DATA="{'email': 'johnezekiel130@gmail.com'}"

BODY=$(curl -X GET -H "Content-Type: application/json" -d "$DATA" "$URL")


echo "Body of request: $BODY"