#!/usr/bin/python3
"""a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = req.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        j = res.json()
        if j == {}:
            print("[{}] {}".format(j("id"), j("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
