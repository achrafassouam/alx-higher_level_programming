#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in matrix:
        new_matrix.append(list(map(lambda num: num ** 2, num)))
    return new_matrix
