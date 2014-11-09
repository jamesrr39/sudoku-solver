__author__ = 'james'

from Square import Square
import BoardHelper
from Board import Board


class BoardIteration:

    squares_solved = 0
    squares_unsolved = 0
    board = []

    def __init__(self, board):
        if isinstance(board, Board):
            self.board = board
        else:
            raise TypeError("'board' should be a Board object")

    def solve(self):
        for (row_index, row) in enumerate(self.board.board):
            for (column_index, cell) in enumerate(row):
                if cell.value is None:
                    square_index = BoardHelper.get_square_index(column_index, row_index)
                    square = Square(self.board.get_3_by_3_square(square_index))
                    possible_values = cell.get_possible_values(
                        row,
                        self.board.get_column(column_index),
                        square.get_as_list()
                    )
                    if possible_values is not None:
                        if len(possible_values) is 1:
                            cell.set_value(possible_values[0])
                            self.squares_solved += 1
                        else:
                            self.squares_unsolved += 1