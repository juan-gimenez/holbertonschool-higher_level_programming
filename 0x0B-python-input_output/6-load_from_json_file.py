#!/usr/bin/python3
""" Json """
import json


def load_from_json_file(filename):
    """ read a f"""
    with open(filename, 'r') as f:
        a = json.load(f)
        return a
