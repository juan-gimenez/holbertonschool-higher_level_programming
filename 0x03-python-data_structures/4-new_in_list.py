#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list[:]
    lenidx = len(my_list)
    if idx >= 0 and idx < lenidx:
        newlist[idx] = element
        return newlist
    return my_list
