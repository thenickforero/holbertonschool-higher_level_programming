#!/usr/bin/python3
"""Script that fetches an URL and displays the content of the response body
but also handles HTTP Errors printing the error code.

Note: there is no URL checking in the script so take in account that
in the case of an invalid URL it will be an unexpected behaviour
and maybe it will fail.
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import (urlopen, Request)

if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as res:
            data = res.read()
            print(data.decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
