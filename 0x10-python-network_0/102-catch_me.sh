#!/bin/bash
# Bash script to make a specific request to get a specific response from the server
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "origin:HolbertonSchool"
