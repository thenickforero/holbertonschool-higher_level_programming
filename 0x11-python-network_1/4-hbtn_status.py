#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status and
prints information about the body of the response retrieved.
"""
from requests import get


if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    data = response.content.decode(response.encoding)
    print('Body response:')
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
