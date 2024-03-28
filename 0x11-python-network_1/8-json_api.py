#!/usr/bin/python3
"""a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    data = {"q": letter}

    res = req.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        j = res.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j("id"), j("name")))
    except ValueError:
        print("Not a valid JSON")
