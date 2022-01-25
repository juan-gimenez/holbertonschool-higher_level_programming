#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle():
    """Class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __repr__(self):
        """ repr rect"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """ str"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return (rectangle)
        for a in range(self.__height):
            for b in range(self.__width):
                rectangle += "#"
            if a != (self.__height - 1):
                rectangle += "\n"
        return (rectangle)

    def area(self):
        """ returns the area"""
        self.area = self.__width * self.__height
        return (self.area)

    def perimeter(self):
        """ calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        p = (self.__width * 2) + (self.__height * 2)
        return p

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
