#!/usr/bin/python3
"""
    a function that inserts a line of text to a file
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ x """
    with open(filename, "r+") as f:
        lines = f.readlines()
        updated_lines = []
        for line in lines:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)
        f.seek(0)
        f.writelines(updated_lines)
