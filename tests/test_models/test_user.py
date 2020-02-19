#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test user"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Alejo"
        cls.user.last_name = "Lopez"
        cls.user.email = "alejolo311@gmamil.com"
        cls.user.password = "thisisthepass"

    @classmethod
    def teardown(cls):
        """teardonw"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_00(self):
        """chekcing the attrs"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_01(self):
        """is a subclass"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_02(self):
        """types"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_03(self):
        """dict"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_04(self):
        """save"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)
