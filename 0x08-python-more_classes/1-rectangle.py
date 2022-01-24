#!/usr/bin/python3
"""
task 0
"""


class Rectangle:
    """class Rectangle"""
    pass


def __init__(self, width=0, height=0):
    """ attrib """
    if type(width) is not int:
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")
    self.__width = width
    if type(height) is not int:
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
    self.__height = height


@property
def height(self):
    """ property height"""
    return self.__height


@height.setter
def height(self, value):
    """ set the height"""
    if type(value) is not int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value


@property
def width(self):
    """property width"""
    return self.__width


@width.setter
def width(self, value):
    """set the widht"""
    if type(value) != int:
        raise TypeError("must be an integer")
    if value < 0:
        raise ValueError("must be >= 0")
    self.__width = value
