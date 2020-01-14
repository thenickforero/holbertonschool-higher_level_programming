#!/usr/bin/python3
"""Script that sends a search request to the Star Wars API
and also prints the number of results
and the name of every character from the results
it prints all the result without taking in account the pagination.
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    query = "" if len(argv) < 2 else argv[1]

    response = get(url, params={'search': query})
    data = response.json()

    results_count = data.get('count')
    print('Number of results: {}'.format(results_count))

    if results_count > 0:
        while True:
            characters = data.get('results')
            for char in characters:
                print(char.get('name'))
            if data.get('next'):
                response = get(data.get('next'))
                data = response.json()
            else:
                break
