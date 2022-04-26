#!/usr/bin/python3
''' displays the body of the response depending on error.'''

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(quest.status_code))
    else:
        print(r.text)
