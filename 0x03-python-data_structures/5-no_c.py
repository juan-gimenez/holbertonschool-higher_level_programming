#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for x in my_string:
        if x != 'C' and x != 'c':
            n_str += x
    return n_str
