#!/usr/bin/python3
"""This module defines an class named Rectangle
    """


class Rectangle:
    """class named rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor function

        Args:
            width (int, optional): first param. Defaults to 0.
            height (int, optional): second param. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property getter function for width of the rectangle

        Returns:
            int: value of the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter function

        Args:
            value (int): Value of the width of rectangle

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter function for height of the rectangle

        Returns:
            int: value of the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter function

        Args:
            value (int): Value of the height of rectangle

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
