#!/usr/bin/python3
"""
   matrix
"""


def matrix_divided(matrix, div):

    """
    divides elements of a matrix (list of lists)
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    listone = []
    for x in matrix:
        if type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
          of integers/floats")

        if len(x) != len(matrix[0]):
            raise TypeError("Each row of the matrix \
        must have the same size")

        listscnd = []
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix mut be a matrix (list of lists) of \
            integers/floats")

                listscnd.append(round(y / div, 2))
        listone.append(listscnd)
    return listone
