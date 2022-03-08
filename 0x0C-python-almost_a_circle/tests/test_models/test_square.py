"""Unitfor Square """
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests Square
    """
    def test(self):
        """Square size"""
        Base._Base__nb_objects = 0
        s1 = Square(3)
        self.assertEqual(s1.size, 3)

    def test_zero(self):
        """zero case"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
            self.assertEqual(e, "width must be > 0")

    def test_negative(self):
        """negative """
        with self.assertRaises(ValueError) as e:
            s1 = Square(-5)
            self.assertEqual(e, "width must be > 0")

    def test_string(self):
        """string"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("string")
            self.assertEqual(e, "width must be an integer")

    def test_list(self):
        """list"""
        with self.assertRaises(TypeError) as e:
            s1 = Square([1, 2, 3, 4])
            self.assertEqual(e, "width must be an integer")

    def test_dict(self):
        """dict"""
        with self.assertRaises(TypeError) as e:
            s1 = Square({"h": 1, "i": 2})
            self.assertEqual(e, "width must be an integer")

    def test_tuple(self):
        """tuple"""
        with self.assertRaises(TypeError) as e:
            s1 = Square((2, 3, 2, 4))
            self.assertEqual(e, "width must be an integer")

    def test_float(self):
        """float"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(3.50)
            self.assertEqual(e, "width must be an integer")
