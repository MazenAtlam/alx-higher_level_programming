#!/usr/bin/python3

"""This module have a function used to
read a text file (UTF8) and print it to stdout
"""


def read_file(filename=""):
    """A funcion that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): The name of the text file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        file_text = file.read()

    print(file_text)
