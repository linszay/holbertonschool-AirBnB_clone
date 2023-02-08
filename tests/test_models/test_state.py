#!/usr/bin/python3
"""AMENITY MODULE TESTS"""
import unittest
import models
import os
import inspect
import models
from models.state import State


class TestAmenityModel(unittest.TestCase):
    """state class UNIT TESTS"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(State.__doc__) >= 1)


class TestState(unittest.TestCase):
    '''Tests for class'''

    def test_attr_str(self):
        self.assertEqual(type(State().name), str)

    def test_has_attributes(self):
        Victoria = State()
        Victoria.name = "Victoria"
        self.assertTrue('id' in Victoria.to_dict())
        self.assertTrue('created_at' in Victoria.to_dict())
        self.assertTrue('updated_at' in Victoria.to_dict())
        self.assertTrue('name' in Victoria.to_dict())

    def test_to_dict(self):
        Victoria = State()
        self.assertTrue(dict, type(Victoria.to_dict))
        self.assertEqual('to_dict' in dir(Victoria), True)


if __name__ == "__main__":
    unittest.main()
