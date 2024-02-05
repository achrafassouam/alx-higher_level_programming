#!/usr/bin/python3
"""
    a functions that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """
    Args: obj

    Return: A list of strings, where each string
        is the name of an attribute or method of the object.
    """
    return (dir(obj))
