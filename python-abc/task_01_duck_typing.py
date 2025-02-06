#!/usr/bin/python3
""" Task 01: Duck Typing """


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Class Shape that defines a shape """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ Class Circle that defines a circle """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return ((self.radius * self.radius) * pi)

    def perimeter(self):
        return (2 * pi * self.radius)


class Rectangle(Shape):
    """ Class Rectangle that defines a rectangle """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return ((self.width + self.height) * 2)


def shape_info(info):
    """ Function to print the area and perimeter of a shape """
    print("Area: {}".format(info.area()))
    print("Perimeter: {}".format(info.perimeter()))
