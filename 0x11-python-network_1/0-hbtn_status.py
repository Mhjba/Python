#!/usr/bin/python3
"""that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    pack = response.read()

print("Body response:")
print(f"    - type: {type(pack)}")
print(f"    - content: {pack}")
print(f"    - utf8_content : {pack.decode('utf-8')}")
