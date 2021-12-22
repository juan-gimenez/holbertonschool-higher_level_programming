#!/usr/bin/python3
def uppercase(str):
    for toupp in str:
        toupp = ord(toupp)
        if toupp > 96 and toupp < 123:
            toupp = toupp - 32
        print("{:c}".format(toupp), end='')
    print()
