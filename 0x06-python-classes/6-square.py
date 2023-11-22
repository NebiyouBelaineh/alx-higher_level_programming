#!/usr/bin/python3
"""This module is used to create a class named Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initilizes Square attributes

        Args:
            size (int, optional): _description_. Defaults to 0.
            position (tuple, optional): _description_. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """Prints # to stdout if size is > 0, newline if size is 0
            If __position[1] > 0, then space is not printed
        """
        if self.__size == 0:
            print()
        else:
            for h in range(1, self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Position Setter method

        Returns:
            tuple: returns the position field
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter function

        Args:
            value (_type_): _description_

        Raises:
            TypeError: if value is not a tuple and if it's length is not
            TypeError: if value[0] and value[1] are not integers
            TypeError: if value contains negative numbers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
