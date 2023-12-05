#!/usr/bin/python3
"""This module defines a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file using
    JSON representation"""
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)
