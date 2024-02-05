#!/usr/bin/python3
"""
 a function that returns True if the object is an instance of a class
 hat inherited (directly or indirectly) from the specified class
 otherwise False
"""


def inherits_from(obj, a_class):
    """
    Checks if an object inherits from a given class.

    Args:
    obj: The object to check inheritance for.
    a_class: The class to check if obj inherits from.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
