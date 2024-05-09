#!/usr/bin/python3

"""This module is to gets the Pascal triangle of a number
"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing the Pascal triangle of a number

    Args:
        n (int): A number to represent the Pascal triangle of it

    Return:
        A list of lists of integers or empty list if n is less than or equal 0
    """
    p_triangle = []
    if n > 0:
        p_triangle = [[1]]
        for i in range(1, n):
            triangle_i = [1]
            for j in range(1, i):
                triangle_i.append(p_triangle[i - 1][j - 1] + p_triangle[i - 1][j])
            triangle_i.append(1)
            p_triangle.append(triangle_i)

    return p_triangle
