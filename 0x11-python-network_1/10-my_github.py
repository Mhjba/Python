#!/usr/bin/python3
""" a gitHub credentials (username and password)
and uses the GitHub API to display your id
"""

from requests.auth import HTTPBasicAuth
import requests as req
from sys import argv


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = req.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
