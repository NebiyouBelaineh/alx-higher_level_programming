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
