#!/usr/bin/python3
"""This module defines a function that returns the JSON representation of an
object(string)"""


def to_json_string(my_obj):
    import json
    """Returns the JSON representation of an object in the form of a
    string"""
    json_rep = json.dumps(my_obj)
    return json_rep
