#!/usr/bin/python3
"""
 a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    All elements of the matrix should be divided by div
    rounded to 2 decimal places

    1: check if matrix is a list of lists of integers or floats
    2: check if div is a number (integer or float) and not equal to 0

    Return: new matrix
    """

    typeerror1 = "matrix must be a matrix (list of lists) of integers/floats"
    typeerror2 = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError(typeerror1)
    previous = len(matrix[0])

    for count, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(typeerror1)
        if len(row) != previous:
            raise TypeError(typeerror2)
        previous = len(row)
        new_matrix.append(row[:])
        for val, item in enumerate(row):
            if not isinstance(item, (int, float)):
                raise TypeError(wrong_type)
            new_matrix[count][val] = round(item / div, 2)

    return new_matrix
