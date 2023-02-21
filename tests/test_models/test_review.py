#!/usr/bin/python3
"""CITY MODULE TESTS"""
import unittest
import models
import os
import inspect
from datetime import datetime
from models.city import City


class TestCityModel(unittest.TestCase):
    """review UNIT TESTS"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)


class TestState(unittest.TestCase):

    def test_attr_str(self):
        self.assertEqual(type(Review().place_id), str)
        self.assertEqual(type(Review().user_id), str)
        self.assertEqual(type(Review().text), str)

    def test_has_attributes_in_to_dict(self):
        """check if attr is in to_dict"""
        review = Review()
        review.place_id = "melb"
        review.user_id = "jacq"
        review.text = "hello"
        self.assertTrue('id' in review.to_dict())
        self.assertTrue('created_at' in review.to_dict())
        self.assertTrue('updated_at' in review.to_dict())
        self.assertTrue('place_id' in review.to_dict())
        self.assertTrue('user_id' in review.to_dict())
        self.assertTrue('text' in review.to_dict())

    def test_to_dict(self):
        review = Review()
        self.assertTrue(dict, type(review.to_dict))
        self.assertEqual('to_dict' in dir(review), True)


if __name__ == "__main__":
    unittest.main()
