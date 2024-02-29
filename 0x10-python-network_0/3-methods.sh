#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i "Allow" | awk '{for (i=2; i<=NF; i++) printf "%s%s", $i, (i<NF ? " " : "\n")}'| tr -d '\r'
