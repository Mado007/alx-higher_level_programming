#!/usr/bin/python3
"""
Python script fetches https://alx-intranet.hbtn.io/status
and prints the type, content, and UTF-8 content of the response.
"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
