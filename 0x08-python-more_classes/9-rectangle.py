#!/usr/bin/python3

"""A module for the rectangle class"""


class Rectangle:
    """An empty rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Class constructor

        Args:
            width (int, optional): The rectangle width. Defaults to 0.
            height (int, optional): The rectangle height. Defaults to 0.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """An instance method to calculate the rectangle area

        Returns:
            The area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """An instance method to calculate the rectangle perimeter

        Returns:
            The perimeter of the rectangle
        """

        if self.isEmpty():
            return 0

        return 2 * (self.width + self.height)

    def isEmpty(self):
        """An instance method to check whether the rectangle is empty or not"""

        if not (self.width and self.height):
            return True

        return False

    def __str__(self):
        """A pretty string representation of the rectangle"""

        rectangle_str = ""
        if self.isEmpty():
            return rectangle_str

        for length in range(self.height):
            for _ in range(self.width):
                rectangle_str += str(self.print_symbol)
            if length != self.height - 1:
                rectangle_str += '\n'

        return rectangle_str

    def __repr__(self):
        """A string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """A method to be called when a rectangle is deleted
        to print a nicely message
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2

        return rect_1

    @classmethod
    def square(cls, size=0):
        """A class method that returns a new Rectangle instance
        with width == height == size

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """

        return Rectangle(size, size)
