#!/usr/bin/python3
"""Module that defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer method for class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method for width

        Returns:
            int: value of width instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value (int): Value to be assigned to width

        Raises:
            TypeError: raised if width is not an integer
            ValueError: raised if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height

        Returns:
            int: value of height instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
            value (int): Value to be assigned to y

        Raises:
            TypeError: raised if height is not an integer
            ValueError: raised if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x

        Returns:
            int: value of x instance attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x

        Args:
            value (int): Value to be assigned to x

        Raises:
            TypeError: raised if x is not an integer
            ValueError: raised if x is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y

        Returns:
            int: value of y instance attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y

        Args:
            value (int): Value to be assigned to y

        Raises:
            TypeError: raised if y is not an integer
            ValueError: raised if y is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of a Rectangle instance

        Returns:
            int: area of a Rectangle instance
        """
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        rectangle = ''
        row = self.width
        col = self.height
        hor = self.x
        ver = self.y

        for v in range(ver):
            rectangle += '\n'
        for c in range(col):
            for h in range(hor):
                rectangle += ' '
            for r in range(row):
                rectangle += '#'
            if c != col - 1:
                rectangle += '\n'
        print(rectangle)

    def __str__(self):
        """Returns a string representation of class Rectangle

        Returns:
            str: string representation of Rectangle class instance
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Method that updates/assigns new values to attributes of
        class Rectangle or the Parent Class
        """
        if len(args) > 0:
            super().__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle

        Returns:
            dictionary: dictionary representation of a Rectangle
        """
        dict_rep = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dict_rep
