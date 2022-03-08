#!/usr/bin/python3
"""unitest for rectangle"""

import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingRectangle(unittest.TestCase):
    """class to Test Rectangle"""

    def test0(self):
        """test of Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r0 = Rectangle(4)

    def test1(self):
        """test of Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle("word", 3)

    def test2(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r2 = Rectangle([4, 7], 3)

    def test3(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle((4, 3), 4)

    def test4(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r4 = Rectangle({'d': 2}, 9)

    def test5(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 3)

    def test6(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r6 = Rectangle(-2, 4)

    def test7(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r7 = Rectangle(2.5, 4)

    def test7(self):
        """test Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r7 = Rectangle(4, "hi")
