#!/usr/bin/python3
"""
peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """gets the pick of a list of ints"""
    if list_of_integers is not None:
        list_of_integers.sort()
        # return first int of sorted
        return list_of_integers[-1]
