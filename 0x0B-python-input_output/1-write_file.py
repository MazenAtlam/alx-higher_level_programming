#!/usr/bin/python3

"""This module have a function used to write a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str, optional): The name of the text file. Defaults to "".
        text (str, optional): The string to be written. Defaults to "".
    
    Return:
        The number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        no_of_chars = file.write(text)

    return no_of_chars
