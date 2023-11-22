#!/usr/bin/python3
"""Module that calculates area and circumference"""


class _MagicClass:
    """class _MagicClass definition"""

    def __init__(self, radius):
        """Initilizer

        Args:
            radius (int/float): radius of the circle

        Raises:
            TypeError: radius must be a number
        """
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculates Area of a circle

        Returns:
            int/float: returns the area of a circle
        """
        return 2 ** self._MagicClass__radius * math.pi

    def circumference(self):
        """Calculates Area of a circle

        Returns:
            int/float: returns the circumference of a circle
        """
        return 2 * math.pi * self._MagicClass__radius
