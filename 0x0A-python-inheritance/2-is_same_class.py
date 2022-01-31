#!/usr/bin/python3
"""
checks if is an instance
"""


def is_same_class(obj, a_class):
    """ if obj is an instance return true
    else false
    """
    return (type(obj) is a_class)
