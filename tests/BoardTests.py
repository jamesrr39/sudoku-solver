__author__ = 'james'

from Board import Board
import unittest
from mocks import BoardMocks


class BoardTests(unittest.TestCase):

    def test_get_column(self):
        board_mock = BoardMocks.get_board_mock()
        column_index = 7
        board = Board(board_mock)
        column = board.get_column(column_index)
        self.assertListEqual(column, [
            board_mock[0][column_index],
            board_mock[1][column_index],
            board_mock[2][column_index],
            board_mock[3][column_index],
            board_mock[4][column_index],
            board_mock[5][column_index],
            board_mock[6][column_index],
            board_mock[7][column_index],
            board_mock[8][column_index]
        ])

    def test_get_3_x_3_grid(self):
        board_mock = BoardMocks.get_board_mock()
        board = Board(board_mock)
        square = board.get_3_by_3_square(2)
        self.assertEqual(square.__len__(), 3)
        for (index, row) in enumerate(square):
            self.assertListEqual(row,[
                board_mock[index][6],
                board_mock[index][7],
                board_mock[index][8]
            ])

    def test_get_square_index(self):
        self.assertEqual(3, Board.get_square_index(2, 4))
        self.assertEqual(5, Board.get_square_index(6, 3))
        self.assertEqual(8, Board.get_square_index(8, 8))

if __name__ is '__main__':
    unittest.main()