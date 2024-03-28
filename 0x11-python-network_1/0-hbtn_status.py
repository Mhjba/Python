#!/usr/bin/python3
""" that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        pack = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(pack)))
        print('\t- content: {}'.format(pack))
        print('\t- utf8 content: {}'.format(pack.decode("utf-8")))
