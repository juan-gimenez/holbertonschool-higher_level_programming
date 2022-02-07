#!/usr/bin/python3
"""
class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """ crepr of square """
        strsq1 = "[Square] "
        strsq2 = "(" + str(self.id) + ") "
        strsq3 = str(self.x) + "/" + str(self.y)
        return (strsq1 + strsq2 + strsq3 + " " + str(self.width))

    def update(self, *args, **kwargs):
        """updates values of square"""
        length = len(args)
        dictionaryofatrrib = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args:
            if length < 5:
                for a in range(length):
                    setattr(self, dictionaryofatrrib[a], args[a])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        "returns the dictionary representation of a Square"
        d = {'id': self.id,
             'size': self.width,
             'x': self.x,
             'y': self.y, }
        return d
