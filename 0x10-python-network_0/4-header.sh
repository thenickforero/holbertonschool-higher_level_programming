#!/bin/bash
# Bash script to get the body of a response from a server who checks a custom HTTP header in the request.
curl -s "$1" -H 'X-HolbertonSchool-User-Id:98'
