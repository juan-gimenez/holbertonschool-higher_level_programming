#!/usr/bin/python3
"""class"""


class Square:
    """create the Square"""
    def __init__(self, size=0):
        self.size = size

        @origin
        def size(self):
            """size origin"""
            return self.__size

        @size.set
        def size(self, value):
            """sett to size"""
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def area(self):
            return(self.__size ** 2)

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for x in range(self.__size):
                    prit("#" * self.__size)
