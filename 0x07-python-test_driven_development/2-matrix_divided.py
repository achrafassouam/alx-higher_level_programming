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

    if not isinstance(matrix, list) or not matrix[0]:
        raise TypeError(typeerror1)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(typeerror2)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
