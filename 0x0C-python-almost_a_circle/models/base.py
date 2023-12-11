#!/usr/bin/python3
"""This module contains the class Base which is the base of all classes"""
import json
import csv
import turtle


class Base:
    """class Base with iniitilizer method and a private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer method for class Base

        Args:
            id (int, optional): id number for all objects from Base or
            inherit from Base. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): contains a list of objects to be saved to a
            file
        """
        filename = (cls.__name__+".json")
        with open(filename, "w", encoding='utf-8') as file:
            if list_objs is None:
                file.write(Base.to_json_string([]))
            else:
                dict_rep = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dict_rep))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation

        Args:
            json_string (str): JSON string representation of an object

        Returns:
            list: list of objects
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Returns:
            object: an instance of the calling class with updated attributes
            from dictionary
        """
        # Dummy instance created
        dummy_instance = cls(1, 2, 3)
        # Don't forget to use ** with dictionary values ;)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances from a file

        Returns:
            list: list of instances from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_json = cls.from_json_string(file.read())
                list_output = []
                # goes through list of json/dict values
                for lj in list_json:
                    # creates an instance object of containing the json/dict
                    # values
                    lj_obj = cls.create(**lj)
                # appends the created object
                    list_output.append(lj_obj)
                return list_output
        except FileNotFoundError as fne:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that serializes in CSV saves to file

        Args:
            list_objs (list): list objects to be saved in a csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
                return
            if filename == "Rectangle.csv":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for lo in list_objs:
                list_objs_dict_rep = lo.to_dictionary()
                csvwriter.writerow(list_objs_dict_rep)

    @classmethod
    def load_from_file_csv(cls):
        """Class method that loads and deserilizes in CSV from a file

        Returns:
            list: list of instance of the calling class loaded from a
            CSV file
        """
        list_objs = []
        list_output = []
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, newline='') as csvfile:
                if filename == "Rectangle.csv":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                csvreader = csv.DictReader(csvfile, fieldnames=fieldnames)

                for cr in csvreader:
                    dict_rep = {}
                    for key, value in cr.items():
                        dict_rep[key] = int(value)
                    list_objs.append(dict_rep)

                for lo in list_objs:
                    obj = cls.create(**lo)
                    list_output.append(obj)
                return list_output
        except FileNotFoundError as fne:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method in class Base that draws all Rectangles and Squares

        Args:
            list_rectangles (list): Contains a list of rectangles to be drawn
            list_squares (list): Contains a list of squares to be drawn
        """
        neba = turtle.Turtle()

        neba.shape("square")
        neba.screen.bgcolor("#9ED2BE")
        neba.pensize(6)

        neba.color("#FFA559", "#072541")
        for lr in list_rectangles:
            neba.showturtle()
            neba.screen.delay(50)
            neba.up()
            neba.goto(lr.x, lr.y)
            neba.down()
            # Move and Turn
            for turn in range(2):
                # Increase scale for better visibility
                neba.forward(lr.width * 2)
                neba.left(90)
                # Increase scale for better visibility
                neba.forward(lr.height * 2)
                neba.left(90)
            neba.hideturtle()

        neba.color("#2D4356", "#C51605")
        neba.shape("circle")
        for lq in list_squares:
            neba.showturtle()
            neba.screen.delay(50)
            neba.up()
            neba.goto(lq.x, lq.y)
            neba.down()
            # Move and Turn
            for turn in range(2):
                # Increase scale for better visibility
                neba.forward(lq.width * 2)
                neba.left(90)
                # Increase scale for better visibility
                neba.forward(lq.height * 2)
                neba.left(90)
            neba.hideturtle()
        # Thank your reviewer
        neba.showturtle()
        neba.up()
        neba.hideturtle()
        neba.goto(0, -100)
        neba.color("#900C3F")
        neba.down()
        neba.write("Thank you for the review, Have a great day!",
                   align="center", font=("Arial", 24, "bold"))
        neba.up()
        turtle.exitonclick()
