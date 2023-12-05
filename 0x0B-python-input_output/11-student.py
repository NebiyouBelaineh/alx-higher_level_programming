#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of an instance of class
        Student

        Args:
            attrs (list, optional): list of attributes to return as dictionary
            Defaults to None.

        Returns:
            dict: dictionary
        """
        if isinstance(attrs, list) and all(type(t) for t in attrs):
            ret_dict = {}
            for i in attrs:
                if getattr(self, i, None):
                    if i in self.__dict__:
                        ret_dict[i] = self.__dict__[i]
            return ret_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of othe Student instance

        Args:
            json (json): json text which is a dictionary
        """
        for key, values in json.items():
            setattr(self, key, values)
