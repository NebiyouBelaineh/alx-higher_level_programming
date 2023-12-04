#!/usr/bin/python3
"""This module defines a class called BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry that contains a method area()"""
    def area(self):
        """Raises an Exception with the message
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value if it is an integer or not

        Args:
            name (string): first parameter
            value (int): second parameter

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than or equal to Zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
