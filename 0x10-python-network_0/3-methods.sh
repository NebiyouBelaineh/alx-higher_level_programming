#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI 0.0.0.0:5000/route_4 | grep -i "Allow" | awk '{for (i=2; i<=NF; i++) printf "%s%s", $i, (i<NF ? " " : "\n")}'
