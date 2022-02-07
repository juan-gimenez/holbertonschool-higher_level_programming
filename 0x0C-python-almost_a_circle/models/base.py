#!/usr/bin/python3
"""
class base
"""

import json
class Base:
    """ base
    """
    __n_objects = 0

    def __init__(self, id=None):
        """class constructor
        """
        if id is not None:
            self.id = id

        else:
            Base.__n_objects += 1
            self.id = Base.__n_objects

    def to_json_string(list_dictionaries):
        """ returns a json str"""
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ json representation to a file """
        if list_objs is not None:
            if type(cls) == Square:
                op = "Square.json"
            else:
                op = "Rectangle.json"
            with open(op, 'w+') as f:
                for a in range(len(list_objs)):
                    f.write(self.to_json_string(list_objs[a]))
        else:
            with open(op, 'w+') as f:
                f.write(self.to_json_string(list()))
