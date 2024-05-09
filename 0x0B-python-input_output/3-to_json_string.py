#!/usr/bin/python3

"""json module used to encode and decode objects
"""
import json

"""This module has a function used to
return the JSON representation of an object as a string
"""


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object as a string

    Args:
        my_obj (object): An object to be converted to the JSON representation

    Return:
        The JSON representation of an object as a string
    """
    return json.dumps(my_obj)
