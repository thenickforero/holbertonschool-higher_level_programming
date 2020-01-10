#!/bin/bash
# Bash script to get the body of a response only if it's status code is 200 OK and also follows all redirects until it reaches the final server.
curl -sfGL "$1"
