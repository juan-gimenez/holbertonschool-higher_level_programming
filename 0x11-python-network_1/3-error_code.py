#!/usr/bin/python3
'''manage urllib.error.HTTPError exceptions'''

from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
