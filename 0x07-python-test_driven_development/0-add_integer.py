#!/usr/bin/python3
""" sum of two ints """


def add_integer(a, b=98):
    """
    function that adds 2 integers.
    """
    """ isinstance to check if int """
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    b = int(b)
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    a = int(a)

    return a + b
