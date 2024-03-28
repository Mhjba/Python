#!/usr/bin/python3
"""a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ''

    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': letter})
        json = response.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
