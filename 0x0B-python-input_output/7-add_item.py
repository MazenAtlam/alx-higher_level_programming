#!/usr/bin/python3

"""This module adds all arguments to a Python list,
and then save them to a file called 'add_item.json'

Modules used:
    sys - to take the arguments passed after run the script
"""
import sys


def append_list(original, new):
    """A function used to append a list in an original list

    Args:
        original (list): The list to be updated
        new (list): The list to be appended
    """
    for item in new:
        original.append(item)


def main():
    """main - Start of the program
    """
    filename = "add_item.json"
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        args = list(load_from_json_file(filename))
    except Exception:
        args = []
    append_list(args, list(sys.argv[1:]))
    save_to_json_file(args, filename)


main()
