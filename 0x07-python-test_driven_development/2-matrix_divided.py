#!/usr/bin/python3
"""
    This module has a single function

    that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places

    Args:
        @matrix: A list of lists of integers or floats
        @div: A number (integer or float)

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats, or
            if any row the matrix does not have the same size of other rows, or
            if div is not a number
        ZeroDivisionError: if div is equal to 0

    Return: A new matrix
    """

    result = []

    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    for item in matrix:
        if type(item) is not list:
            raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
        size = len(item)
        if size != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        row = []
        for element in item:
            if type(element) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
            row.append(round(element / div, 2))
        result.append(row)

    return result
