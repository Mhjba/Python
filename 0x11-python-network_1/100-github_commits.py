#!/usr/bin/python3
""" applying for a back-end position with multiple technical challenges,
like this one
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    res = req.get(url)
    com = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                com[i].get("sha"),
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
