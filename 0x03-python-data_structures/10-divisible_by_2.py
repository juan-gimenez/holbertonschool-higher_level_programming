#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return
    tmp_list = my_list.copy()
    lentmp = len(my_list)
    for i in range(lentmp):
        if my_list[i] % 2 == 0:
            tmp_list[i] = True
        else:
            tmp_list[i] = False
    return tmp_list
