#!/usr/bin/python3
"""that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    pack = response.read()
    print('Body response:')
    print('\t- type: {type(pack)}')
    print('\t- content: {pack}')
    print('\t- utf8 content: {pack.decode("utf-8")}')
