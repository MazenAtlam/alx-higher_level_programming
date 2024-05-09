#!/usr/bin/python3

"""This module has a class Student that defines a student
"""

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

    def to_json(self):
        """A method that retrievesa dictionary representation
        of a Student instance

        Returns:
            dict: a dictionary representation of a Student instance
        """
        return self.__dict__
