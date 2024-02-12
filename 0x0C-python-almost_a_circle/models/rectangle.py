#!/usr/bin/python3
"""
    Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
        initialization of Rectangle class
        Inherits from:
            Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    """ Returning private attribute """
    def width(self):
        return self.__width

    @width.setter
    """ Setting private attribute """
    def width(self, value):
        self.setter_validation("width", value)
        self.__width = value

    @property
    """ Returning private attribute """
    def height(self):
        return self.__height

    @height.setter
    """ Setting private attribute """
    def height(self, value):
        self.setter_validation("height", value)
        self.__height = value

    @property
    """ Returning private attribute """
    def x(self):
        return self.__x

    @x.setter
    """ Setting private attribute """
    def x(self, value):
        self.setter_validation("x", value)
        self.__x = value

    @property
    """ Returning private attribute """
    def y(self):
        return self.__y

    @y.setter
    """ Setting private attribute """
    def y(self, value):
        self.setter_validation("y", value)
        self.__y = value

    @staticmethod
    def setter_validation(self, name, value):
        """ setter for validations raise """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))
