#!/usr/bin/python3
"""This module defines a function that returns True if the object is an
instance of a class that inherited (directly or indirectly) from the
specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj (Object): object to be checked for inheritance
        a_class (cls): Class the object potentially inherits from

    Returns:
        bool: True if it inherits directly or indiirectly, False otherwise
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
