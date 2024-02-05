#!/usr/bin/python3
"""
    My list class
"""


class MyList(list):
    """ subclass  """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
