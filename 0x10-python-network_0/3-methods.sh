#!/bin/bash
# Bash script to print the allowed HTTP methods of a certain server using a specific custom header in the response body.
curl -sI "$1" | grep Allow | cut -f2- -d " "
