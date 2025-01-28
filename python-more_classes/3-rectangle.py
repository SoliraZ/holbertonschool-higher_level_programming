#!/usr/bin/python3
"""
This module defines a class Rectangle
that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ Class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0, my_string=""):
        self.width = width
        self.height = height
        self.my_string = my_string

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        my_string = ""
        for i in range(self.height):
            j = 0
            for j in range(self.width):
                my_string += '#'
            if not i == self.height - 1:
                my_string += '\n'
        return (my_string)
