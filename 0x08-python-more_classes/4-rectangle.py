#!/usr/bin/python3

""" a class representing a Rectangle """


class Rectangle:
    """
    Construct a new Rectangle with the specified width and height.

    Args:
        width (int) and height (int). Defaults to 0.
    Raises:
        TypeError if args aren't int type
        ValueError if args are les then 0.
    Area:
        returns the area of the rectangle
    Perimeter:
        return the perimeter of the rectangle
        if one of the args is equal to 0, the perimeter is 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append(self.__width * "#")
        return "\n".join(rect)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
