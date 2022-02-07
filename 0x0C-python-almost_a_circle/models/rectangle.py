#!/usr/bin/python3
"""
class
"""

from models.base import Base


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
        if type(width) is not int:
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

    def area(self):
        """ returns the area"""
        return(self.__width * self.__height)

    def display(self):
        """ display """
        if self.width == 0 or self.height == 0:
            return (rectangle)
        for y in range(self.y):
            print()
        for a in range(self.__height):
            for space in range(self.x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str """
        strid = "(" + str(self.id) + ") "
        strxy = str(self.__x) + '/' + str(self.__y)
        strwyh = str(self.__width) + '/' + str(self.__height)
        return ("[Rectangle] " + strid + strxy + " - " + strwyh)

    def update(self, *args, **kwargs):
        """updates values of rect"""
        lenghtargs = len(args)
        dictionaryofargs = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args is not None:
            if lenghtargs < 6:
                for a in range(lenghtargs):
                    setattr(self, dictionaryofargs[a], args[a])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns a dictionary of rectangle"""
        d = {'id': self.id,
             'width': self.width,
             'height': self.height,
             'x': self.x,
             'y': self.y, }
        return d
