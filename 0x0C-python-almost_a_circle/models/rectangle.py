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
        for a in range(self.__height):
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ print """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """updates values of rect"""
        length = len(args)
        if args is not None and length > 0:
            a = 0
            for arguments in args:
                if a == 0:
                    self.id = arguments
                elif a == 1:
                    self.width = arguments
                elif a == 2:
                    self.height = arguments
                elif a == 3:
                    self.x = arguments
                elif a == 4:
                    self.y = arguments
                    a += 1
        elif kwargs:
            for (k, val) in kwargs.items():
                if k == "id":
                    self.id = val
                elif k == "width":
                    self.width = val
                elif k == "height":
                    self.height = val
                elif k == "x":
                    self.x = val
                elif k == "y":
                    self.y = val

    def to_dictionary(self):
        """returns the dictionary representation of the Rectangle instance"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
