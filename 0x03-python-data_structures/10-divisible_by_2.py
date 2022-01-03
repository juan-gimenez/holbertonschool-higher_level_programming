#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return
    tmp_list = my_list.copy()
    lentmp = len(tmp_list)
    for i in range(lentmp):
        if tmp_list[i] % 2 != 0:
            tmp_list[i] = False
        else:
            tmp_list[i] = True
        return tmp_list
