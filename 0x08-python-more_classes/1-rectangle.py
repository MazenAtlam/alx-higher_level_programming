#!/usr/bin/python3

"""A module for the rectangle class"""


class Rectangle:
    """An empty rectangle class"""

    def __init__(self, width=0, height=0):
        """Class constructor

        Args:
            width (int, optional): The rectangle width. Defaults to 0.
            height (int, optional): The rectangle height. Defaults to 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """A private instance attribute

        Width must be an integer, otherwise
        a TypeError exception will be raised with
        the message 'width must be an integer'

        If width is less than 0, a ValueError exception will be raised with
        the message 'width must be >= 0'
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """A private instance attribute

        Height must be an integer, otherwise
        a TypeError exception will be raised with
        the message 'height must be an integer'

        If height is less than 0, a ValueError exception will be raised with
        the message 'height must be >= 0'
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
