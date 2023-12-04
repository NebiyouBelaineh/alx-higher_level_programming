#!/usr/bin/python3
"""This Module defines a function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """Method that returns the list of available attributes and methods of an
    object"""
    return dir(obj)
