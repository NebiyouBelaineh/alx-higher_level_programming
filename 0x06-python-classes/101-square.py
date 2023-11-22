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
        self.size = size
        self.position = position

    def area(self):
        """Area computing method
        Returns:
            int: returns the square of the __size field
        """
        return self.__size ** 2

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

    def my_print(self):
        """Prints in stdout the square with the # character"""
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
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
            value (tuple): tuple containing position information

        Raises:
            TypeError: if value is not a tuple and if it's length is not
            TypeError: if value[0] and value[1] are not integers
            TypeError: if value contains negative numbers
        """

        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """Prints the value of an instance of the Square class"""
        new_str = ""
        if self.__size > 0:
            for row in range(self.__position[1]):
                new_str += "\n"
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    new_str += " "
                for column in range(self.__size):
                    new_str += "#"
                new_str += "\n"
        else:
            new_str += '\n'
        return new_str[:-1]
    