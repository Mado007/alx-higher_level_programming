#!/usr/bin/python3

"""Take the URL and send request to it and display value of `X-Request-Id`"""

import urllib.request
import sys

def hbtn_header(url):
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        request_id = headers['X-Request-Id']
        print(request_id)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        hbtn_header(url)
    else:
        print('Usage: ./1-hbtn_header.py <url>')
