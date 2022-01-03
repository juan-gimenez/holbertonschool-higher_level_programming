#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    newlist = my_list
    if idx < 0:
        return newlist
    lenidx = len(my_list)
    if idx >= lenidx:
        return newlist
    newlist[idx] = element
    return newlist
