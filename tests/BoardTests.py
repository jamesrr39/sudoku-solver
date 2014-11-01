__author__ = 'james'

from Board import Board
import unittest
from mocks import BoardMocks

class BoardTests(unittest.TestCase):
    def test_is_set_valid(self):
        self.assertTrue(Board.is_set_valid([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(Board.is_set_valid([2, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(Board.is_set_valid([1, 2, 3, 4, 5, None, 7, 8, 9]))
        self.assertTrue(Board.is_set_valid([2, 9, 3, 4, 5, 6, 7, 8, 1]))
        self.assertFalse(Board.is_set_valid([4, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_get_column(self):
        board = Board(BoardMocks.get_board_mock())
        column = board.get_column(7)
        self.assertListEqual(column,[None, 8, None, None, None, None, 7, None, None])


    def test_get_3_x_3_grid(self):
        board = Board(BoardMocks.get_board_mock())
        square = board.get_3_by_3_square(2)
        print square
        self.assertListEqual(square,[[None, None, None], [None, 8, None], [None, None, None]])



if __name__ is '__main__':
    unittest.main()