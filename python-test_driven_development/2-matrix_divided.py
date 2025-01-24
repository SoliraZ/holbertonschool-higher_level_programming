#!/usr/bin/python3
"""
This module provides a function to
divide all elements of a matrix by a given divisor.
Functions:
    matrix_divided(matrix, div): Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.
    Returns:
        list of lists of float.
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is zero.
    """
    float_or_int = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
