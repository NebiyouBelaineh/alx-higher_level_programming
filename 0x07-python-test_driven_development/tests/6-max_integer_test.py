#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class contains tests for max_integer() function
    The following methods are prepared to test edge cases for max_integer:
    """
    def testPositive(self):
        """Test for positive numbers in a list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        # test for large number
        self.assertEqual(max_integer([999999999999, 500222222222222222222000,
                                      322222220]), 500222222222222222222000)

    def testNegative(self):
        """Test for negative numbers in a list
        """
        # test for negative number
        self.assertEqual(max_integer([-1, -6, -99, -200]), -1)

        self.assertEqual(max_integer([-999999999999, -500222222222222222222000,
                                      -322222220]), -322222220)

    def testFloat(self):
        """Test for floating point numbers
        """
        # test for floating point in a list
        self.assertEqual(max_integer([1.3, 0.66, 22.4, 4848.20, -22.4]),
                         4848.20)

    def testEmptyParm(self):
        """Test for empty parameter
        """
        # test for empty parameter
        self.assertEqual(max_integer(), None)

    def testSameNumbers(self):
        """Test for same numbers in a list
        """
        # test for same/equal numbers
        self.assertEqual(max_integer([5, 5, 5, 5, 5, 5, 5, 5, 5]), 5)

    def testNonList(self):
        """Test for non list datatypes passed to max_integer()
        """
        # test for string input
        self.assertEqual(max_integer("ABC"), 'C')
        self.assertEqual(max_integer(""), None)
        # test for tuples
        self.assertEqual(max_integer((1, 5, 22, 9)), 22)
        # test for multiple parameter over the requirement
        self.assertRaises(TypeError, max_integer, 1, 2, 3)

    def testMixedList(self):
        """Test for mixed values passed to max_integer in alist
        """
        # test mixed elements in list
        self.assertRaises(TypeError, max_integer, [11, '12', 13, '14', 15])

    def testDocString(self):
        """Test for document fullfillment for 6-max_integer module
        """
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def testFunctionDoc(self):
        """Test for document fullfillment max_integer function
        """
        self.assertTrue(len(max_integer.__doc__) > 1)


if __name__ == '__main__':
    unittest.main()
