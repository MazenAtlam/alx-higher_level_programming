#!/usr/bin/python3
"""
    This module has a single function

    that add two integers

"""


def add_integer(a, b=98):
    """A function that adds two integers
    Floats are casted to integers

    Args:
        @a: first value
        @b: second value

    Raises: TypeError raises if a or b is not an integer or a float

    Return an integer: the addition of a and b"""

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)


if __name__ == '__main__':
    import doctest

    doctest.testfile(tests/0-add_integer.txt)
