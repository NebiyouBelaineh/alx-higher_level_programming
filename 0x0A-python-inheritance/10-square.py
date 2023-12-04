#!/usr/bin/python3
"""This module defines a class named Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """Initilizer function for Square class

        Args:
            size (integer): size of a square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the area of a square

        Returns:
            integer: area of a square
        """
        return (self.__size ** 2)
