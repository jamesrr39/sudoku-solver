__author__ = 'james'

from Square import Square
import unittest
from mocks import BoardMocks


class BoardTests(unittest.TestCase):

    def test_validate(self):
        self.assertTrue(Square.validate([[1, 2, 3], [None, None, 7], [8, 9, 4]]))
        self.assertEqual(
            "a row should have 3 cells",
             Square.validate([[1, 2, 3], [4, 5, 6],[7, 8]])
        )
        self.assertEqual(
            "a square should have 3 rows",
            Square.validate([[1, 2, 3], [4, 6]])
        )


if __name__ is '__main__':
    unittest.main()