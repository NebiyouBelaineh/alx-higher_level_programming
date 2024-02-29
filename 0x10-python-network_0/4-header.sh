#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL and sends header variable X-School-User-Id  with the value 98
curl -sH "X-School-User-Id: 98" "$1"
