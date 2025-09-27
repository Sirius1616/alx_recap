#!/bin/bash

# Check if URL was provided
if [-z "$1"] then
    echo "Usage: $0 <url>"
    exit 1
fi


URL="$1"

# Fetch the body using curl
BODY=$(curl -s "$URL")

# Print the body
echo "Body of the URL: "
echo "$BODY"

# Print the length of the body
echo
echo "Length of body: ${#BODY}"