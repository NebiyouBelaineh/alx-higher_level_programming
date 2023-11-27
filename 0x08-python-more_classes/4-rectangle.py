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
        self.width = width
        self.height = height

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

    def area(self):
        """Returns the area of a rectangle

        Returns:
            int: area of a rectangle(product of height and width)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle

        Returns:
            int: preimeter of a rectangle(sum of all 4 sides)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def draw(self):
        """Draws a rectangle with the width and height dimension

        Returns:
            str: string filled with '#' and '\n'
        """
        rectangle = ''
        row = self.__width
        col = self.__height
        if row == 0 or col == 0:
            return rectangle

        for c in range(col):
            for r in range(row):
                rectangle += '#'
            if c != col - 1:
                rectangle += '\n'
        return rectangle

    def __str__(self):
        """Returns a string with a representaion of the class Rectangle

        Returns:
            string: string representaion of class Rectangle
        """
        return self.draw()

    def __repr__(self):
        """Returns the representation of class Rectangle"""
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return "Rectangle(" + w + ", " + h + ")"
