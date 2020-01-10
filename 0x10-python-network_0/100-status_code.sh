#!/bin/bash
# Bash script that prints the HTTP Status code of a certain service/connection.
curl -s -o /dev/null -w "%{http_code}" "$1"
