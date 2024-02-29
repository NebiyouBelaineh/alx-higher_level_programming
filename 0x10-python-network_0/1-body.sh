#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -sw "%{http_code}" "$1" -o response.txt)
status_code=$(echo "$response" | tail -n 1)
if [ "$status_code" -eq 200 ]; then
	cat response.txt
fi
rm -f response.txt
