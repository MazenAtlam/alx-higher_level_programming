#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """A subclass test from ``unittest.TestCase``
    that tests the behaviour of the function ``max_integer(list=[])``
    that finds and returns the max integer in a list of integers
    
    If the list is empty, the function returns None

    Args: Nothing

    Attributes:
    """

    def test_list(self):
        """A method to test the argument ``list``"""

        self.assertIsNone(max_integer())
        self.assertEqual(max_integer([99]), 99)
        self.assertEqual(max_integer([49, 51, 60]), 60)
        self.assertEqual(max_integer([-10, -5, -9]), -5)
        self.assertEqual(max_integer([4, -5, 0]), 4)

        with self.assertRaises(TypeError):
            max_integer(9)
            max_integer({8, 7, 3, 0})
            max_integer(["C is fun", 100, 500])
            max_integer([4, 6, 0, True])
            max_integer([2, 0.71, 89, 5.6])
            max_integer([[48, 89, 94], [18, 16, 58]])
            max_integer(None)
            max_integer([(5, 8), (6, 4)])
            max_integer("ALX")


if __name__ == "__main__":
    unittest.main()
