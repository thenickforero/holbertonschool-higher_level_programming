#!/bin/bash
# Bash script to send a delete request to a certain server / url and also displays the body of the response.
curl -s "$1" -X DELETE
