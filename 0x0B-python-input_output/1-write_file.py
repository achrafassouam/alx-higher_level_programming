#!/usr/bin/python3
"""
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """ open and rewrite a file """
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)
        return len(text)
