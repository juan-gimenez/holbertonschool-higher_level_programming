#!/usr/bin/python3
"""
github api req
"""

from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    user_passw = HTTPBasicAuth(argv[1], argv[2])
    r = get("https://api.github.com/user", auth=user_passw)
    print(r.json().get("id"))
