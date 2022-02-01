#!/usr/bin/python3
""" append file """


def append_write(filename="", text=""):
    """ append a file """
    with open(filename, 'a') as file:
        appendf = file.write(text)
        return appendf
