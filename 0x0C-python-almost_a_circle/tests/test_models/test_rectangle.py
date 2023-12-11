#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys
import os


class TestRectangleClass(unittest.TestCase):
    """Test Case class for Class Rectangle"""

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 0, 0, 12)
        self.r3 = Rectangle(2, 1)
        self.r4 = Rectangle(4, 6, 2, 1, 12)
        self.r5 = Rectangle(2, 1, 1, 1)
        self.r6 = Rectangle(3, 5, 1)
        Base._Base__nb_objects = 0

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3
        del self.r4
        del self.r5
        del self.r6
        Base._Base__nb_objects = 0

    def testIds(self):
        """Testing IDs with integer inputs"""
        result = self.r1.id
        self.assertEqual(result, 1)
        result = self.r2.id
        self.assertEqual(result, 12)

    def testNonIntWidth(self):
        """Testing TypeError exception with non-integer Width inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle('ten', 5)
        with self.assertRaises(TypeError):
            result = Rectangle([10], 5)
        with self.assertRaises(TypeError):
            result = Rectangle((10, 2), 5)
        with self.assertRaises(TypeError):
            result = Rectangle({}, 5)
        with self.assertRaises(TypeError):
            result = Rectangle(10.5, 5)

    def testNonIntHeight(self):
        """Testing TypeError exception with non-integer Height inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, '5')
        with self.assertRaises(TypeError):
            result = Rectangle(10, [5])
        with self.assertRaises(TypeError):
            result = Rectangle(10, (5, 2))
        with self.assertRaises(TypeError):
            result = Rectangle(10, {})
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5.5)

    def testNonIntX(self):
        """Testing TypeError exception with non-integer X inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, '5')
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, [5])
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, (5, 2))
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, {})
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, 5.5)

    def testNonIntY_str(self):
        """Testing TypeError exception with non-integer Y inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, 0, '5')

    def testNonIntY_list(self):
        """Testing TypeError exception with non-integer Y inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, 0, [5])

    def testNonIntY_tuple(self):
        """Testing TypeError exception with non-integer Y inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, 0, (5, 2))

    def testNonIntY_dict(self):
        """Testing TypeError exception with non-integer Y inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, 0, {})

    def testNonIntY_float(self):
        """Testing TypeError exception with non-integer Y inputs"""
        with self.assertRaises(TypeError):
            result = Rectangle(10, 5, 0, 5.5)

    def testGetterWidth(self):
        """Testing Getter method for Width"""
        self.assertEqual(10, self.r1.width)
        self.assertEqual(10, self.r2.width)

    def testGetterHeight(self):
        """Testing Getter method for Height"""
        self.assertEqual(2, self.r1.height)
        self.assertEqual(2, self.r2.height)

    def testGetterX(self):
        """Testing Getter method for x"""
        self.assertEqual(0, self.r2.x)

    def testGetterY(self):
        """Testing Getter method for x"""
        self.assertEqual(0, self.r2.y)

    def testWidth_Less(self):
        """Testing width <= 0"""
        with self.assertRaises(ValueError):
            result = Rectangle(-10, 5, 1, 1)

    def testHeight_Less(self):
        """Testing height <= 0"""
        with self.assertRaises(ValueError):
            result = Rectangle(10, -5, 1, 5)

    def testX_Less(self):
        """Testing x < 0"""
        with self.assertRaises(ValueError):
            result = Rectangle(10, 5, -1, 5)

    def testY_Less(self):
        """Testing y < 0"""
        with self.assertRaises(ValueError):
            result = Rectangle(10, 5, 1, -1)

    def test_area(self):
        """Testing area output"""
        result = self.r1.width * self.r1.height
        self.assertEqual(result, 20)

    def test_initilizer_method_missing_args(self):
        """Testing area output"""
        with self.assertRaises(TypeError):
            self.r1 = Rectangle(1)

    def test_display(self):
        """Testing display output"""
        cap_output = StringIO()
        sys.stdout = cap_output
        result = self.r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), "##\n")

    def test__str__(self):
        """Testing __str__ method"""
        result = self.r4.__str__()
        self.assertEqual(result, "[Rectangle] (12) 2/1 - 4/6")

    def test_display_1(self):
        """Testing display method with x and y support"""
        cap_output = StringIO()
        sys.stdout = cap_output
        result = self.r5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), "\n ##\n")

    def test_update_normal_inputs_id(self):
        """Testing update method using variable argument
        with normal inputs"""
        # test update with id
        result = self.r5.update(89)
        self.assertEqual(self.r5.id, 89)

    def test_update_normal_inputs_width(self):
        """Testing update method using variable argument
        with normal inputs"""
        # test update() with width
        result = self.r2.update(89, 2)
        self.assertEqual(self.r2.width, 2)

    def test_update_normal_inputs_height(self):
        """Testing update method using variable argument
        with normal inputs"""
        # test update () with height
        result = self.r2.update(89, 2, 3)
        self.assertEqual(self.r2.height, 3)

    def test_update_normal_inputs_x(self):
        """Testing update method using variable argument
        with normal inputs"""
        # test update () with x
        result = self.r2.update(89, 2, 3, 4)
        self.assertEqual(self.r2.x, 4)

    def test_update_normal_inputs_y(self):
        """Testing update method using variable argument
        with normal inputs"""
        # test update () with y
        result = self.r2.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r2.y, 5)

    def test_update_negative_y(self):
        """Testing update() with negative  inputs"""
        # test update () with negative values
        with self.assertRaises(ValueError):
            result = self.r2.update(89, 2, 3, 4, -5)

    def test_update_negative_x(self):
        """Testing update() with negative  inputs"""
        with self.assertRaises(ValueError):
            result = self.r2.update(89, 2, 3, -4, 5)

    def test_update_negative_height(self):
        """Testing update() with negative  inputs"""
        with self.assertRaises(ValueError):
            result = self.r2.update(89, 2, -3, 4, 5)

    def test_update_negative_width(self):
        """Testing update() with negative  inputs"""
        with self.assertRaises(ValueError):
            result = self.r2.update(89, -2, 3, 4, 5)

        # ID negative is not specified to be be a non integer
        # and perhaps not a non integer
        # with self.assertRaises(ValueError):
        #     result = self.r2.update(-89, 2, 3, 4, 5)

    # May not be needed since inputs are tested individually and exceptions
    # are handled
    def test_update_non_integer_float_y(self):
        """Testing update() with non integers"""
        with self.assertRaises(TypeError):
            result = self.r2.update(89, 2, 3, 4, 5.1)

    def test_update_non_integer_float_x(self):
        """Testing update() with non integers"""
        with self.assertRaises(TypeError):
            result = self.r2.update(89, 2, 3, 4.2, 5)

    def test_update_non_integer_tuple(self):
        """Testing update() with non integers"""
        with self.assertRaises(TypeError):
            result = self.r2.update(89, 2, (3, 3), 4, 5)

    def test_update_non_integer_dict(self):
        """Testing update() with non integers"""
        with self.assertRaises(TypeError):
            result = self.r2.update(89, 2, 3, {4}, 5)

    def test_update_non_integer_str(self):
        """Testing update() with non integers"""
        with self.assertRaises(TypeError):
            result = self.r2.update(89, '2', 3, 4, 5)

    def test_update_kwargs_id(self):
        """Testing update() with kwargs"""
        result = self.r5.update(id=4)
        self.assertEqual(4, self.r5.id)

    def test_update_kwargs_width(self):
        """Testing update() with kwargs"""
        result = self.r5.update(width=9)
        self.assertEqual(9, self.r5.width)

    def test_update_kwargs_height(self):
        """Testing update() with kwargs"""
        result = self.r2.update(height=1)
        self.assertEqual(1, self.r2.height)

    def test_update_kwargs_x(self):
        """Testing update() with kwargs"""
        result = self.r2.update(x=22)
        self.assertEqual(22, self.r2.x)

    def test_update_kwargs_y(self):
        """Testing update() with kwargs"""
        result = self.r1.update(y=8)
        self.assertEqual(8, self.r1.y)

    def test_to_dictionary(self):
        """Testing method to_dictionary()"""
        result = self.r4.to_dictionary()
        self.assertEqual(result, {"id": 12, "width": 4, "height": 6, "x": 2,
                                  "y": 1})

    def testToJson_str(self):
        """Testing Base method to_json_string()"""
        _result = """[{"id": 12, "width": 4, "height": 6, "x": 2, "y": 1}]"""
        dict_rep = self.r4.to_dictionary()
        result = Base.to_json_string([dict_rep])
        self.assertEqual(result, _result)

    def testToJson_str_none(self):
        """Testing Base method to_json_string()"""
        # test with None
        _result = "[]"
        result = Base.to_json_string(None)
        self.assertEqual(result, _result)

    def testToJson_str_empty_list(self):
        """Testing Base method to_json_string()"""
        # test with empty list
        _result = "[]"
        list_rep = []
        result = Base.to_json_string([])
        self.assertEqual(result, _result)

    def test_save_to_file_None(self):
        """Testing save_to_file() method from Base class with Class Rectangle
        with None input"""
        _result = "[]\n"
        Rectangle.save_to_file(None)
        try:
            with open("Rectangle.json", "r") as file:
                cap_output = StringIO()
                sys.stdout = cap_output
                print(file.read())
                sys.stdout = sys.__stdout__
                self.assertEqual(cap_output.getvalue(), _result)
        except FileNotFoundError as fne:
            pass

    def test_save_to_file(self):
        """Testing save_to_file() method from Base class with Class Rectangle
        with list_objs input"""
        _result = """[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},\
 {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]\n"""
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        Rectangle.save_to_file([self.r1, self.r2])
        try:
            with open("Rectangle.json", "r") as file:
                cap_output = StringIO()
                sys.stdout = cap_output
                print(file.read())
                sys.stdout = sys.__stdout__
                self.assertEqual(cap_output.getvalue(), _result)
        except FileNotFoundError as fne:
            pass

    def test_from_json_string(self):
        """Testing from_json_string() Base class method with class Rectangle"""
        list_input = [
                        {'id': 89, 'width': 10, 'height': 4},
                        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        result = Rectangle.from_json_string(json_list_input)
        _result = [{'height': 4, 'width': 10, 'id': 89}, {'height': 7,
                                                          'width': 1, 'id': 7}]
        self.assertEqual(result, _result)

    def test_create(self):
        """Testing create() method in base class"""
        _result = "[Rectangle] (4) 1/0 - 3/5\n"
        # test with ID not defined
        dict_rep_r6 = self.r6.to_dictionary()
        cap_output = StringIO()
        sys.stdout = cap_output
        result = Rectangle.create(**dict_rep_r6)
        print(result)
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), _result)

    def test_create_predefined_ID(self):
        """Testing create() method in base class"""
        # test with predefined ID
        _result = "[Rectangle] (12) 0/0 - 10/2\n"
        dict_rep_r2 = self.r2.to_dictionary()
        cap_output = StringIO()
        sys.stdout = cap_output
        result = Rectangle.create(**dict_rep_r2)
        print(result)
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_output.getvalue(), _result)

    def test_load_from_file(self):
        """Testing load_from_file method in Base class"""
        # Test when the file does not exist
        filename = "Rectangle.json"
        if os.path.exists(filename):
            # Delete the file
            os.remove(filename)

        _result = []
        result = Rectangle.load_from_file()
        self.assertEqual(result, _result)

    def test_load_from_file_csv_withFile(self):
        """Testing load_from_file method in Base class"""
        # Test when file exists
        _result = [self.r3, self.r4]
        result = Rectangle.load_from_file()
        res_list = []
        _res_list = []
        if len(_result) == len(result):
            for i in range(len(_result)):
                res_list.append(result[i])
                _res_list.append(_result[i])

        self.assertEqual(_res_list, res_list)

    def test_load_from_file_csv_noFile(self):
        """Testing load_from_file method in Base class"""
        # Test when the file does not exist
        filename = "Rectangle.csv"
        if os.path.exists(filename):
            # Delete the file
            os.remove(filename)

        _result = []
        result = Rectangle.load_from_file_csv()
        self.assertEqual(result, _result)

    def test_load_from_file_csv_withFile(self):
        """Testing load_from_file method in Base class"""
        # Test when file exists
        _result = [self.r3, self.r4]
        result = Rectangle.load_from_file_csv()
        res_list = []
        _res_list = []
        if len(_result) == len(result):
            for i in range(len(_result)):
                res_list.append(result[i])
                _res_list.append(_result[i])
        self.assertEqual(_res_list, res_list)
