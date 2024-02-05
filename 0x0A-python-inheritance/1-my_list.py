#!/usr/bin/python3
""" My list class """


class MyList(list):
    """ subclass  """
    def print_sorted(self):
        print (sorted(self))
