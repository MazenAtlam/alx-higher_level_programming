#!/usr/bin/python3

"""json module used to encode and decode objects
"""
import json

"""This module has a function used to
return an object (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (string): A JSON string to be converted to
            its python object representation

    Return:
        An object (Python data structure)
    """
    return json.loads(my_str)
