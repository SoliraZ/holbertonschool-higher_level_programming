#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittests for the max_integer function
    """

    def test_max_integer(self):
        """Test max_integer function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 1, -23, 1]), 1)
        self.assertEqual(max_integer([1, 1, 2, 1]), 2)
        self.assertEqual(max_integer([1, -3, -2, -1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5, 4, 3, 2, 0]), 10)
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5, 4, 3, 2, -10]), 10)
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5, 4, 3, 2, -1]), 10)


if __name__ == "__main__":
    unittest.main()
