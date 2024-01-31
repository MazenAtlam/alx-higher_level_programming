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

        self.__size = size

    @property
    def size(self):
        """A property for the private attribute 'size' as getter
and setter methods that returns the value of size


If size is not an integer, it will raise a TypeError with massage
'size must be an integer'
If size is less than 0, it will raise a ValueError with massage
'size must be >= 0'
"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """A puplic method that gets the current square area


Args: Nothing

Returns: The current square area
"""

        return self.__size**2
