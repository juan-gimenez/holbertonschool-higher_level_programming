#!/usr/bin/python3
"""script that adds all arguments to a Python list"""
from sys import argv
import os.path

if __name__ == '__main__':

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_json_file = __import__('6-load_from_json_file').load_from_json_file

    argmts = []
    add = "add_item.json"
    if os.path.exists(add):
        argmts = load_json_file(add)
    save_to_json_file(argmts + argv[1:], add)
