#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status'''

from urllib import request

if __name__ == '__main__':

    with request.urlopen("https://intranet.hbtn.io/status") as r:
        body_of_response = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_of_response)))
        print("\t- content: {}".format(body_of_response))
        print("\t- utf8 content: {}".format(body_of_response.decode("utf-8")))
