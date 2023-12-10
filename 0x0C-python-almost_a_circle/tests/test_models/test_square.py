#!/usr/bin/python3
"""Unittest for Square Class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestSquareClass(unittest.TestCase):
    """Test case for class for Class Square"""

    def setUp(self):
        """setUp method"""
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)
        self.s4 = Square(4, 1, 1, 20)

    def tearDown(self):
        Base._Base__nb_objects = 0
        del self.s1
        del self.s2
        del self.s3
        del self.s4

    def testSquare_size(self):
        """Testing Square class with Height and Width it inherits
        from parent class Rectangle outputs"""
        # Test width
        result = self.s1.width
        self.assertEqual(result, 5)
        # Test height
        result = self.s1.height
        self.assertEqual(result, 5)

    def testSquare_area(self):
        """Testing area() method from parent class"""
        result = self.s1.area()
        self.assertEqual(result, 25)

    def testSquare_str(self):
        """Testing __str__ method for class square"""
        result = self.s4.__str__()
        self.assertEqual("[Square] (20) 1/1 - 4", result)

    def testSquare_display(self):
        """Testing display() method inherited from parent class"""
        cap_output = StringIO()
        sys.stdout = cap_output
        result = self.s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), "  ##\n  ##\n")

    def testSquare_setter(self):
        """Testing setter and getter methods for class Square"""
        self.s1.size = 10
        self.assertEqual(10, self.s1.size)
        result = self.s2.size
        self.assertEqual(result, 2)

    def testSquare_update(self):
        """Testing update() method"""
        # update id
        self.s4.update(22)
        result = self.s4.id
        self.assertEqual(result, 22)
        # update size
        self.s4.update(22, 4)
        result = self.s4.size
        self.assertEqual(result, 4)
        # update x
        self.s4.update(22, 4, 4)
        result = self.s4.x
        self.assertEqual(result, 4)
        # update y
        self.s4.update(22, 4, 4, 5)
        result = self.s4.y
        self.assertEqual(result, 5)

    def test_update_negative(self):
        """Testing update() with negative  inputs"""
        # test update () with negative values
        with self.assertRaises(ValueError):
            result = self.s2.update(89, 2, 3, -4)

        with self.assertRaises(ValueError):
            result = self.s2.update(89, 2, -3, 4)

        with self.assertRaises(ValueError):
            result = self.s2.update(89, -2, 3, 4)

    def test_update_non_integer(self):
        """Testing update() with non integers"""
        with self.assertRaises(TypeError):
            result = self.s3.update(89, 2, 3, 5.1)

        with self.assertRaises(TypeError):
            result = self.s3.update(89, 2, 4.2, 5)

        with self.assertRaises(TypeError):
            result = self.s3.update(89, (3, 3), 4, 5)

        with self.assertRaises(TypeError):
            result = self.s3.update(89, 2, 3, {4})

        with self.assertRaises(TypeError):
            result = self.s3.update(89, '2', 4, 5)

    def test_update_kwargs(self):
        """Testing update() with kwargs"""

        result = self.s2.update(id=4)
        self.assertEqual(4, self.s2.id)

        result = self.s2.update(size=9)
        self.assertEqual(9, self.s2.size)

        result = self.s2.update(x=22)
        self.assertEqual(22, self.s2.x)

        result = self.s2.update(y=8)
        self.assertEqual(8, self.s2.y)

    def testSquare_toDict(self):
        """Testing to_dictionary() method in Square class"""
        result = self.s4.to_dictionary()
        self.assertEqual(result, {"id": 20, "size": 4, "x": 1, "y": 1})

    def testToJson_str(self):
        """Testing Base method to_json_string()"""
        _result = """[{"id": 20, "size": 4, "x": 1, "y": 1}]"""
        dict_rep = self.s4.to_dictionary()
        result = Base.to_json_string([dict_rep])
        self.assertEqual(result, _result)
        # test with None
        _result = "[]"
        result = Base.to_json_string(None)
        self.assertEqual(result, _result)
        # test with empty list
        _result = "[]"
        list_rep = []
        result = Base.to_json_string(list_rep)
        self.assertEqual(result, _result)

    def test_save_to_file_None(self):
        """Testing save_to_file() method from Base class with Class Square
        with None input"""
        _result = "[]\n"
        Square.save_to_file(None)
        try:
            with open("Square.json", "r") as file:
                cap_output = StringIO()
                sys.stdout = cap_output
                print(file.read())
                sys.stdout = sys.__stdout__
                self.assertEqual(cap_output.getvalue(), _result)
        except FileNotFoundError as fne:
            pass

    def test_save_to_file(self):
        """Testing save_to_file() method from Base class with Class Square
        with list_objs input"""
        _result = """[{"id": 3, "size": 3, "x": 1, "y": 3}, {"id": 20, "size": 4, "x": 1, "y": 1}]\n"""
        Square.save_to_file([self.s3, self.s4])
        try:
            with open("Square.json", "r") as file:
                cap_output = StringIO()
                sys.stdout = cap_output
                print(file.read())
                sys.stdout = sys.__stdout__
                self.assertEqual(cap_output.getvalue(), _result)
        except FileNotFoundError as fne:
            pass

    def test_from_json_string(self):
        """Testing from_json_string() Base class method with class Square"""
        list_input = [
        {'id': 89, 'size': 4, 'x': 5, 'y': 6}, 
        {'id': 7, 'size': 7, 'x': 3, 'y': 4}
        ]
        json_list_input = Square.to_json_string(list_input)
        result = Square.from_json_string(json_list_input)
        _result = [{'size': 4, 'id': 89, 'x': 5, 'y': 6}, {'size': 7, 'id': 7, 'x': 3, 'y': 4}]
        self.assertEqual(result, _result)

    def test_create(self):
        """Testing create() method in base class"""
        _result = "[Square] (20) 1/1 - 4\n"
        # test with ID not defined
        dict_rep_s4 = self.s4.to_dictionary()
        cap_output = StringIO()
        sys.stdout = cap_output
        result = Square.create(**dict_rep_s4)
        print(result)
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), _result)
        # test with predefined ID
        # self.s3 = Square(3, 1, 3)
        _result = "[Square] (3) 1/3 - 3\n"
        dict_rep_s3 = self.s3.to_dictionary()
        cap_output = StringIO()
        sys.stdout = cap_output
        result = Square.create(**dict_rep_s3)
        print(result)
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), _result)

