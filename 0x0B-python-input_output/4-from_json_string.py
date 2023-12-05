#!/usr/bin/python3
"""This module defines a function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns a python object represented by a JSON string"""
    obj_rep = json.loads(my_str)
    return obj_rep
