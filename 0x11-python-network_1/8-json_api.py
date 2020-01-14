#!/usr/bin/python3
"""Script that sends a letter to a JSON API for searching data and also
checks if the response is a valid JSON response.
"""
from sys import argv
from requests import post

if __name__ == "__main__":
    letter = "" if len(argv) < 2 else argv[1]
    response = post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        valid_json = response.json()
        if not valid_json:
            print('No result')
        else:
            data = (valid_json.get('id'), valid_json.get('name'))
            print('[{}] {}'.format(*data))
    except ValueError as err:
        print('Not a valid JSON')
