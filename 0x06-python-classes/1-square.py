#!/usr/bin/python3

"""
This module has a square class that defines a square

Attributes: Nothing

Todo: * define a square
"""


class Square:
    """Square class that defines a square


Attributes: size (private attribute)
"""

    def __init__(self, size):
        """An __init__ method that used to assign attributes


Args: size (int): Length of the square
"""

        self.__size = size
