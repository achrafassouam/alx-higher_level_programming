#!/usr/bin/python3
'''
    Rectangle Class
'''
from models.base import Base


class Rectangle(Base):
    '''
        initialization of Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            return width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' set width '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        ''' return height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' set height '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        ''' return x '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' set x '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        ''' return y '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' set y '''
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        ''' return area '''
        return (self.width * self.height)

    def display(self):
        ''' print the rectangle '''
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        ''' updating str '''
        return (
            "[Rectangle] ({})".format(self.id) +
            " {}/{}".format(self.x, self.y) +
            " - {}/{}".format(self.width, self.height)
        )

    def update(self, *args, **kwargs):
        ''' updating the args '''
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        ''' returning a dictionaty of the square '''
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }

    def setter_validation(self, name, value):
        ''' returing the raised errors '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))
