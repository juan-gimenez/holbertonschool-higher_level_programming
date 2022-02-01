#!/usr/bin/python3
""" JSON """
import json


def from_json_string(my_str):
    """ JSON representation"""
    a = json.loads(my_str)
    return a
