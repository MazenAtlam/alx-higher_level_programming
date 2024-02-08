#!/usr/bin/python3
"""

    This module has only one single function

    that prints the name passed to it
"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first_name> <last_name>

    Args:
        @first_name: The first name
        @last_name: The last name

    Raises:
        TyprError: If first_name is not a string, or
                If last_name is not a string

    Return: Nothing
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
