#!/usr/bin/python3
""" Defile a class -> Square """


class Square:
    """ Representing the class Square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        esle:
            self.__size = size
