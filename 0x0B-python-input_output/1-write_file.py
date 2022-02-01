#!/usr/bin/python3
""" write a file"""


def write_file(filename="", text=""):
    """ write a file"""
    with open(filename, 'w') as file:
        writef = file.write(text)
        return writef
