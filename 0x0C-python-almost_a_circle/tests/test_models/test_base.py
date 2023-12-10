#!/usr/bin/python3
"""Unittest module for base.py"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def testBase(self):
        """Testing base class"""
        result = self.b1.id
        self.assertEqual(result, 1)
        result = self.b2.id
        self.assertEqual(result, 2)
        result = self.b3.id
        self.assertEqual(result, 3)
        result = self.b4.id
        self.assertEqual(result, 12)
        result = self.b5.id
        self.assertEqual(result, 4)

    def tearDown(self):
        self.b1.id = None
        self.b2.id = None
        self.b3.id = None
        self.b4.id = None
        self.b5.id = None
        Base._Base__nb_objects = 0
