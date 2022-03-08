#!/usr/bin/python3
"""
class base
"""
import csv
import json


class Base:
    """ base class """

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

    def from_json_string(json_string):
        """JSON string representation"""
        if json_string is None:
            return []
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """Returns an inst"""
        if cls.__name__ == "Square":
            d = cls(1)
        elif cls.__name__ == "Rectangle":
            d = cls(1, 1)
            d.update(**dictionary)
            return d

    def save_to_file_csv(cls, list_objs):
        """Saves to csv """
        r = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_fcsv:
            write_csv = csv.DictWriter(save_fcsv, r[0].keys())
            write_csv.writeheader()
            write_csv.writerows(r)
