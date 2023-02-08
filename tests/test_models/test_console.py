#!/usr/bin/python3
"""Unit Tests"""


import unittest
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """console UNIT TESTS"""

    def test_bas_mod_crt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def test_bas_mod_upd(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_uwu_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_ini_tim(self):
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_dict(self):
        bm1 = BaseModel()
        dict = bm1.to_dict()
        self.assertIsInstance(dict, dict)
        self.assertIsInstance(dict["updated_at"], str)
        self.assertIsInstance(dict["created_at"], str)

    def test_str_met(self):
        bm1 = BaseModel()
        self.assertIn(bm1.id, str(bm1))
