__author__ = 'james'

from Board import Board
import unittest


class BoardTests(unittest.TestCase):
    def test_is_set_valid(self):
        self.assertTrue(Board.is_set_valid([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(Board.is_set_valid([2, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(Board.is_set_valid([1, 2, 3, 4, 5, None, 7, 8, 9]))
        self.assertTrue(Board.is_set_valid([2, 9, 3, 4, 5, 6, 7, 8, 1]))
        self.assertFalse(Board.is_set_valid([4, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_get_3_x_3_grid(self):
        board = Board()



if __name__ is '__main__':
    unittest.main()