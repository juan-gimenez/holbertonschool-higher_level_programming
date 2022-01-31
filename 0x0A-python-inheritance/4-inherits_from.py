#!/usr/bin/python3
"""
checks if is an instance
"""


def inherits_from(obj, a_class):
    """ checks if subclass and not class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
