#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """ class Myint swaper"""
    def __eq__(self, sign):
        """ swaps equal with not equal"""
        return int.__ne__(self, sign)

    def __ne__(self, sign):
        """ swaps not equal with equal"""
        return int.__eq__(self, sign)
