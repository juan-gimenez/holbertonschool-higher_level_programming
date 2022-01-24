#!/usr/bin/python3
"""say my name - mr white """


def say_my_name(first_name, last_name=""):
    """
    Function that prints the first and second name
    Must be say_my_name_(str, str):

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
