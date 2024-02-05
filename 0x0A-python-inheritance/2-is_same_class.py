#!/usr/bin/python3
"""
Class
"""


def is_same_class(obj, a_class):
    """
    check if an object is an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
