#!/usr/bin/python3
"""a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""

from sys import argv
import requests as req


if __name__ == "__main__":
    url = argv[1]

    res = req.get(url)
    print(res.headers.get("X-Request-Id"))
