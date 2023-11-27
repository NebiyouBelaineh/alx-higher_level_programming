#!/usr/bin/python3
"""This module defines a class named Rectangle
    """


class Rectangle:
    """Class representing properties of a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor function

        Args:
            width (int, optional): first param. Defaults to 0.
            height (int, optional): second param. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Prints string when deleting an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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
            str: string filled with print_symbol and '\n'
        """
        rectangle = ''
        row = self.__width
        col = self.__height
        if row == 0 or col == 0:
            return rectangle

        for c in range(col):
            for r in range(row):
                rectangle += str(self.print_symbol)
            if c != col - 1:
                rectangle += '\n'
        return rectangle

    def bigger_or_equal(rect_1, rect_2):
        """Returns rect_1 if it is bigger or equal to rect_2, othewise rect_2 is returned

        Args:
            rect_1 (Rectangle): rectangle 1 from Rectangle class
            rect_2 (Rectangle): rectangle 2 from Rectangle class

        Raises:
            TypeError: raised if rect_1 is not an instance of Rectangle class
            TypeError: raised if rect_2 is not an instance of Rectangle class

        Returns:
            Rectangle: returns the bigger or equal rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

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
