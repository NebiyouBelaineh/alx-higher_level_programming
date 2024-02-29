#!/bin/bash
# Bash script that takes in a URL and displays content-length header bytes
curl -sI "$1" | grep  'Content-Length:' | cut -d ' ' -f2
