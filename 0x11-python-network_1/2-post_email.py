#!/usr/bin/python3
""" a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.parse as parse
import urllib.request as req
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode("utf-8")

    request = req.Request(url, data)
    with req.urlopen(request) as response:
        print(response.read().decode("utf-8"))
