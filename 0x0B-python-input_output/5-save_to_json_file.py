#!/usr/bin/python3

"""json module used to encode and decode objects
"""
import json

"""This module has a function used to
write an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """A function that returns the JSON representation of an object as a string

    Args:
        my_obj (object): An object to be converted to the JSON representation
        filename (string): The name of the file

    Return:
        Nothing
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
