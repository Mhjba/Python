#!/usr/bin/python3
"""a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    q = "" if len(argv) == 1 else argv[1]
    payload = {"q": q}

    response = req.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = response.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
