#!/bin/bash
# Bash script to send a JSON HTTP POST request on a certain URL/server with the content of a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
