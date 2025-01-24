#!/usr/bin/python3
"""
This module provides a function to add two integers.

Functions:
    add_integer(a, b=98): Returns the integer addition of a and b.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number to add. Must be an integer or float.
        b (int, float): The second number to add. Must be an integer or float.

    Returns:
        int: The sum of a and b, cast to an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
