#!/usr/bin/python3
"""
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ open and rewrite a file """
    with open(filename, 'a', encoding="UTF8") as f:
        f.write(text)
        return len(text)
