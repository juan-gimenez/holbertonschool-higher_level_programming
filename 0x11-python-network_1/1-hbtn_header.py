#!/usr/bin/python3
'''displays the value of the X-Request-Id.'''

from urllib import request
from sys import argv
if __name__ == '__main__':
    with request.urlopen(argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
