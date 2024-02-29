#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
# 	The size must be displayed in bytes
# 	You have to use curl
URL=$1
curl -sI "$URL" | grep  'Content-Length:' | cut -d ' ' -f2