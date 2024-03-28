#!/usr/bin/python3
"""a URL and an email address, sends a POST request
to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    res = req.post(url, data=value)
    print(res.text)
