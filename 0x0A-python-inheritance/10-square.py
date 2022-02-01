#!/usr/bin/python3
"""
class BaseGeometry
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """subclass of class Rectangle"""
    def __init__(self, size):
        """init square"""
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", self.__size)

    def area(self):
        """area of square"""
        return (self.__size * self.__size)
