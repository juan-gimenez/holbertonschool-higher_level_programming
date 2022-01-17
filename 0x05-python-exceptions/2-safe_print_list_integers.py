#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int = 0
    for y in range(0, x):
        try:
            print(end="{:d}".format(my_list[y]))
            int += 1
        except (ValueError, TypeError):
            pass
    print()
    return int
