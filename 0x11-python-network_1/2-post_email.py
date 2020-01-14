#!/usr/bin/python3
"""Script that fetches an URL and sends an email as data using a POST request

Note: there is no parameter checking in the script so take in account that
in the case of an invalid URL/email it will be an unexpected behaviour
and maybe it will fail.
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import (urlopen, Request)
if __name__ == "__main__":
    (url, email) = argv[1:3]
    data = urlencode({'email': email})
    req = Request(url, data.encode('ascii'))
    with urlopen(req) as res:
        data = res.read()
        print(data.decode('utf-8'))
