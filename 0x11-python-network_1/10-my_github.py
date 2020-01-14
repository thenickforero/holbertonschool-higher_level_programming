#!/usr/bin/python3
"""Script that requests the Github API to display your id
using your credentials as auth ( username and email).
"""
from sys import argv
from requests import get

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    auth_credentials = ["", ""]
    if len(argv) > 1 and len(argv) <= 3:
        auth_credentials = tuple(auth_credentials[:3 - len(argv)] + argv[1:3])

    response = get(url, auth=auth_credentials)
    data = response.json()

    print(data.get('id', 'None'))
