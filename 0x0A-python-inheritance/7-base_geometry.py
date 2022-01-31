#!/usr/bin/python3
"""
class
"""


class BaseGeometry():
    """ method """
    def area(self):
        """raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ int validator """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(name) is not str:
            raise TypeError("name must be a string")
