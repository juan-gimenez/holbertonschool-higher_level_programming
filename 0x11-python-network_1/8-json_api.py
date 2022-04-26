#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
from requests import post

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    req = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_todic = r.json()
        # the response body is properly JSON formatted and not empty
        if len(r_todic.keys()) > 0:
            print("[{}] {}".format(r_todic.get('id'), r_todic.get('name')))
        else:
            # the JSON is empty
            print("No result")
    except:
        print("Not a valid JSON")
