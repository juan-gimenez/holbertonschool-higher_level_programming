#!/usr/bin/python3
"""
wrap up class and subclasses
"""


class BaseGeometry():
    """class"""
    def area(self):
        """error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """subclass
    """
    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        """print str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        "area of rectangle"
        return (self.__width * self.__height)


class Square(Rectangle):
    """subclass Rectangle"""
    def __init__(self, size):
        """init"""
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", self.__size)

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """print str"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
