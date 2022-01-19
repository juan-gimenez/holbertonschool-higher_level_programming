#!/usr/bin/python3
""" Square """


class Square:
    "Class"
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        "Area of the Square"
        return (self.__size ** 2)

    @property
    def size(self):
        """Size """
        return self.__size

    @size.setter
    def size(self, value):
        """value to size"""
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
