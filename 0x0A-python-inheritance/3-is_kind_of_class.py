#!/usr/bin/python3
"""This module defines a function that checks if the Object is an
instance of or if the object is an instance of a class that inherited
from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the Object is an instance of or if the
    object is an instance of a class that inherited from, the specified class,
    or False otherwise

    Args:
        obj (Object): object to be checked
        a_class (cls): class that has a potential instance obj

    Returns:
        bool: True if obj is an instance of a_class, False otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
