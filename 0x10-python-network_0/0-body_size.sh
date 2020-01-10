#!/bin/bash
# Bash script to print the size of the body of the response in bytes.
curl "$1" -s | wc -c
