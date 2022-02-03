#!/usr/bin/python3
"""
class
"""

Base = __import__("base.py").Base


class Rectangle(Base):
    """init"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        if type(widht) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """property"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """property"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
