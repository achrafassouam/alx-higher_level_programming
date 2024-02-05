#!/usr/bin/python3
"""
a function that returns True if the object is an instance

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance or subclass of a_class.

    Args:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if obj is an instance of a_class or a subclass of a_class,
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    for cls in obj.__class__.__mro__:
        if cls is a_class:
            return True
        return False
