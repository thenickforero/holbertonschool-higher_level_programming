#!/usr/bin/python3
"""Script that fetches an URL and displays the value of the X-Request-Id
variable found in the header of the response.

Note: there is no URL checking in the script so take in account that
in the case of an invalid URL it will be an unexpected behaviour
and maybe it will fail.
"""
from sys import argv
from urllib.request import (urlopen, Request)

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as res:
        header = res.getheader('X-Request-Id')
        print(header)
