#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status and
prints information about the body of the response retrieved.
"""
from urllib.request import (urlopen, Request)


if __name__ == "__main__":

    req = Request('https://intranet.hbtn.io/status')
    with urlopen(req) as response:
        data = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf8 content: {}'.format(data.decode('utf-8')))
