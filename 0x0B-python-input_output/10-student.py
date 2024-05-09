#!/usr/bin/python3

"""This module has a class Student that defines a student
"""

def is_str_list(a_list):
    """A function that checks if a list contains only strings

    Args:
        list (list): _description_

    Returns:
        _type_: _description_
    """
    for element in a_list:
            if not isinstance(element, str):
                return False
    return True


class Student:
    """A class Student that defines a student

    Attributes:
        first_name (string): The student first name
        last_name (string): The student last name
        age (int): The student age
    """

    def __init__(self, first_name, last_name, age):
        """Intializing instance attributes

        Args:
            first_name (string): The student first name
            last_name (string): The student last name
            age (int): The student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that retrievesa dictionary representation
        of a Student instance

        - If attrs is a list of strings,
            only attribute names contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved

        Returns:
            dict: a dictionary representation of a Student instance
        """
        attrs_dict = dict()
        if not attrs or isinstance(attrs, list) == False:
            return self.__dict__

        if is_str_list(attrs):
            for key, value in self.__dict__.items():
                if key in attrs:
                    attrs_dict.update({key: value})
            return attrs_dict

        return self.__dict__
