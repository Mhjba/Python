#!/usr/bin/python3
"""that fetches https://alx-intranet.hbtn.io/status"""

import requests as req


if __name__ == "__main__":
    response = req.get("https://alx-intranet.hbtn.io/status")
    res = response.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
