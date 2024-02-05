#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt is a rebel. It inherits from int but inverts == and !=
    """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
