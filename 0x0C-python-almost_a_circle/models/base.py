#!/usr/bin/python3
"""This module contains the class Base which is the base of all classes"""
import json
import random


class Base:
    """class Base with iniitilizer method and a private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = (cls.__name__+".json")
        with open(filename, "w", encoding='utf-8') as file:
            if list_objs is None:
                file.write(Base.to_json_string([]))
            else:
                dict_rep = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dict_rep))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # Dummy instance created
        dummy_instance = cls(1, 2, 3)
        # Don't forget to use ** with dictionary values ;)
        dummy_instance.update(**dictionary)
        return dummy_instance
