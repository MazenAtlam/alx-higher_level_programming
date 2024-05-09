#!/usr/bin/python3

"""A module has a function returns an object dictionary description
"""


def class_to_json(obj):
    """A function that returns a class dictionary description

    Args:
        obj (object): The object to return its dictionary description
    """

    return obj.__dict__
