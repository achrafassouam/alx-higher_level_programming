#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ open a file and prints it to stdout """
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read())
