#!/usr/bin/python3
"""
This module defines a class Square that defines a square by 1-square.py
"""


class Square:
    """ Class Square that defines a square """
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
