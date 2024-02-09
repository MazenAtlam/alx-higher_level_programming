#!/usr/bin/python3
"""
    This module has only one single function

    that prints a text with 2 new lines after

    each of these characters: '.', '?' and ':'

"""


def text_indentation(text):
    """A function that prints a text with 2 lines after each
    of these characters: '.', '?' and ':'
    There is no spaces at the beginning or at the end of each
    printed line

    Args:
        @text: The text to be printed
        text must be a string

    Raises:
        TypeError: If text is not a string

    Return: Nothing
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    replaced_txt = text
    for sign in ['.', '?', ':']:
        replaced_txt = replaced_txt.replace(sign + ' ', sign)
        replaced_txt = replaced_txt.replace(sign, sign + '\n\n')

    print(replaced_txt)
