#!/usr/bin/python3
"""This module defines a class called Rectangle that inherits from
BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle is a class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initilizer method for class Rectangle

        Args:
            width (int): first parameter
            height (int): second parameter
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a rectangle

        Returns:
            integer: product of width and height
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of class Rectangle

        Args:
            width (integer): width parameter
            height (integer): height parameter

        Returns:
            string: string representation of the class
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
