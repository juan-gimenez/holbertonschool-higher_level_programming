#!/usr/bin/python3
"third square"


class Square:
    """ Square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
            pass
        elif size < 0:
            raise ValueError("size must be >= 0")
        pass
        else:
            self.__size = size

    def area(self):
        return ((self.__size) ** 2)
