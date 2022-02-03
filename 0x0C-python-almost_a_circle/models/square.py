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
        return super()self.height

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value
