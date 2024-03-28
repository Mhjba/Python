#!/usr/bin/python3
"""a URL, sends a request to the URL
and displays the body of the response.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    res = req.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
