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

    def __init__(self, size=0, position=(0, 0)):
        """An __init__ method that used to assign attributes


Args: size (int): Length of the square
"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """A property for the private attribute 'position' as getter
and setter methods that returns the value of position


If position is not a tuple of 2 positive integers,
it will raise a TypeError with massage
'position must be a tuple of 2 positive integers'
"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) > 2 or
                type(value[0]) is not int or value[0] < 0 or
                type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """A puplic method that gets the current square area


Args: Nothing

Returns: The current square area
"""

        return self.__size**2

    def my_print(self):
        """A puplic method that prints the square with the character #
If size is equal to 0, print an empty line

Args: Nothing

Returns: Nothing
"""

        if self.__size is 0:
                print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
