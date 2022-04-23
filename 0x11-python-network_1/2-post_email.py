#!/usr/bin/python3
'''displays the body of the response.'''

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':

    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], email) as r:
        print(r.read().decode('utf-8'))
