#!/usr/bin/python3
"""
    This module has only a single function

    that prints a square with the character '#'

"""


def print_square(size):
    """A function that prints a square
    with the character '#'

    Args:
        @size: The length of the square
        size must be an integer and greater than or equal 0

    Raises:
        ValueError: If size is less than 0
        TypeError: If size is not an integer
        If size is a floar and is less than 0,
            it raises a TypeError exception

    Return: Nothing
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
