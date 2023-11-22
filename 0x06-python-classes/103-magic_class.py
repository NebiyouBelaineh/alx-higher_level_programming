#!/usr/bin/python3
"""Module that calculates area and circumference"""


import math


class MagicClass:
    """class MagicClass definition"""

    def __init__(self, radius=0):
        """Initilizer

        Args:
            radius (int or float): radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates Area of a circle

        Returns:
            int/float: returns the area of a circle
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates Area of a circle

        Returns:
            int/float: returns the circumference of a circle
        """
        return (2 * math.pi * self.__radius)
