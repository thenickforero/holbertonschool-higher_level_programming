#!/usr/bin/python3
"""Script that fetches an URL and displays the content of the response body
but also handles HTTP Errors printing the error code.

Note: there is no URL checking in the script so take in account that
in the case of an invalid URL it will be an unexpected behaviour
and maybe it will fail.
"""
from sys import argv
from requests import get

if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.content.decode('utf-8'))

