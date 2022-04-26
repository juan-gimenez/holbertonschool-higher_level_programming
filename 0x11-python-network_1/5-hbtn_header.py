#!/usr/bin/python3
""" value of X-Request-Id"""

import sys
import requests

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get("X-Request-Id")))
