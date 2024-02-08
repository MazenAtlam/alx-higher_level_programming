#!/usr/bin/python3
"""
    This module has a single function

    that add two integers

"""


def add_integer(a, b=98):
    """A function that adds two integers

    Args:
        @a: first value
        @b: second value

    Return an integer: the addition of a and b"""

    if not type(a) in (int, float):
        raise TypeError('a must be an integer')

    if not type(b) in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
