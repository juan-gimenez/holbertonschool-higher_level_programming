#!/usr/bin/python3
""" class to json func"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary of object"""
        a = {}
        if type(attrs) is list:
            for b in attrs:
                if type(b) is not str:
                    return self.__dict__
                if b in self.__dict__:
                    a[aux] = self.__dict__[b]
            return a
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes"""
        for a in json:
            self.__dict__[a] = json[a]
