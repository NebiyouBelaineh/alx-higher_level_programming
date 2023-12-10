#!/usr/bin/python3
"""This module defines a class Square that inherits from
class Rectangle"""
import unittest
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer method for class Square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of class Square"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, super().x, super().y, super().width))

    @property
    def size(self):
        """Getter method for width/height, i.e size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for width/height, i.e size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method updates/assigns new values to attributes of parent classes"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        dict_rep = {
             "id": self.id,
             "size": self.width,
             "x": self.x,
             "y": self.y
         }
        return dict_rep
