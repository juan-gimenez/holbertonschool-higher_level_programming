#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    lenidx = len(my_list)
    if idx >= lenidx:
        return None
    return my_list[idx]
