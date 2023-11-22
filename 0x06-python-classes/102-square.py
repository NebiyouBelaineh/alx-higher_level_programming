#!/usr/bin/python3
"""This module is used to create a class named Square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """
        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Size getter method
        Returns:
            int: returns the __size field
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter method

        Args:
            value (int): value to set for __size field
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area computing method
        Returns:
            int: returns the square of the __size field
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return (self.area() >= other.area())
