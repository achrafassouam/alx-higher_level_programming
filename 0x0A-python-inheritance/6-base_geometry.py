#!/usr/bin/python3
" BaseGeo class "


class BaseGeometry:
    """
    Representation of base geo
    """
    def area(self):
        raise Exception("area() is not implemented")
