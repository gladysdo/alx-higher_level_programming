#!/usr/bin/python3
# Script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
