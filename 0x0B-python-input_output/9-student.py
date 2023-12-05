#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of an instance of class
        Student

        Returns:
            dict: dictionary representation of an instance of class Student
        """
        return self.__dict__
