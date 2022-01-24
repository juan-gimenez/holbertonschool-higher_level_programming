#!/usr/bin/python3
def print_square(size):

    if (type(size) != float or type(size) != int) or size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for a in range(size):
            for b in range(size):
                print("#", end="")
            print()
