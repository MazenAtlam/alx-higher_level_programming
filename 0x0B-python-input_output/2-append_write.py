#!/usr/bin/python3

"""This module have a function used to
append a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """A funcion that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str, optional): The name of the text file. Defaults to "".
        text (str, optional): The string to be appended. Defaults to "".

    Return:
        The number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        no_of_chars = file.write(text)

    return no_of_chars
