#!/usr/bin/python3
"""
This module defines a class Square that defines a square by 0-square.py
"""


class Square:
    """ Class Square that defines a square """
    __size = None

    def __init__(self, size=0):
        if size is not None:
            self.__size = size
