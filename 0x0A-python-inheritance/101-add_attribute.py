#!/usr/bin/python3
"""This module defines a function that adds attribute if it's possible"""


def add_attribute(obj, attribute_name, attribute_value):
    """Function that adds an attribute if it is possible"""
    # Return whether the object has an attribute with the given name.
    if hasattr(obj, "__dict__"):
        obj.__setattr__(attribute_name, attribute_value)
    else:
        raise TypeError("can't add new attribute")
