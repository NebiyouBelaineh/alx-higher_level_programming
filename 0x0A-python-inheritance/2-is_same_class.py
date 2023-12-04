#!/usr/bin/python3

"""This module defines a function that checks if an object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

    Args:
        obj (object): Object to be checked if it an instance of the class
        a_class (cls): Class from which the obj is potentially an instance of
    Returns:
        bool: True if exactly an instance of the class, False otherwise
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
