#!/usr/bin/python3
"""
function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Return a + b
    if a and b aren't integer or float :
        raise : TypeError
        message : a or b must be an integer
    a and b must be first casted to integers if they are float
    """

    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        return (int(a) + int(b))
    except Exception as e:
        raise e
