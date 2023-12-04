#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int class"""


class MyInt(int):
    """Class MyInt"""
    def __init__(self, num):
        """Initalizer for class MyInt

        Args:
            num (integer): integer parameter
        """
        self.number = num

    def __eq__(self, number):
        """Returns the reversed logic of __eq__ method

        Args:
            number (integer): number

        Returns:
            boolean: True or False depedning on reverse equliaty logic
        """
        return not super().__eq__(number)

    def __ne__(self, number):
        """Returns the reversed logic of __ne__ method

        Args:
            number (integer): number

        Returns:
            boolean: True or False depedning on reverse equliaty logic
        """
        return not super().__ne__(number)
