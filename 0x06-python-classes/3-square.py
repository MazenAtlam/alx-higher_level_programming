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

    def __init__(self, size=0):
        """An __init__ method that used to assign attributes


Args: size (int): Length of the square
"""

        if type(size) != int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size


    def area(self):
        """A puplic method that gets the current square area


Args: Nothing

Returns: The current square area
"""

        return size**2
