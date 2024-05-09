#!/usr/bin/python3

"""json module used to encode and decode objects
"""
import json

"""This module has a function used to create an Object from a JSON file
"""


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file

    Args:
        filename (string): The file name

    Return:
        An object (Python data structure)
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
