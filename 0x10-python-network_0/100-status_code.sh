#!/bin/bash
#  Bash script that sends a request to a URL and displays only the status code of the response
curl -sw "%{http_code}" "$1" | grep -oE '[0-9]+' |tr -d '\n'
