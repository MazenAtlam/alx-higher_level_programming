#!/usr/bin/python3

"""A module that defines a square

    Attributes: Nothing

    Todo:
        * define a square
        * calculate the area of the square
        * print the square at certain position
"""


class Square:
    """A class that is used to define the square

        Attributes:
            size (int): A private attribute to store the length of the square
            position (tuple): A private attribute where the square is located
    """

    def __init__(self, size=0, position=(0, 0)):
        """A special method to intialize the attributes' values
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """A getter&setter proerty of the size private attribute

            Raises:
                TyprError: If the size is not an integer
                ValueError: If the size is less than zero
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
        """A getter&setter property of the position private attribute

            Raises:
                TypeError: If position is not a tuple of 2 positive integers
        """

        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or type(value[0]) is not int or \
        type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integer')

        self.__position = value

    def area(self):
        """A method that computes the area of the square

        Return: The area of the square
        """

        return size * size

    def __str__(self):
        """A method to print the square at certain position
        """

        data = ''
        if self.size == 0:
            data += '\n'
        else:
            for i in range(self.position[1]):
                data += '\n'
            for i in range(self.size):
                for j in range(self.position[0]):
                    data += ' '
                for k in range(self.size):
                    data += '#'
                if i != self.size - 1:
                    data += '\n'

        return data
