__author__ = 'james'

from Square import Square
import BoardHelper
from Board import Board
import logging
from Cell import Cell

logger = logging.getLogger(__name__)


class BoardIteration:

    squares_solved = 0
    squares_unsolved = 0
    board = []

    def __init__(self, board):
        if isinstance(board, Board):
            self.board = board
        else:
            raise TypeError("'board' should be a Board object")


    """
    looks at the values of the other cells and sees if there are any that are not filled
    """
    def simple_solve(self):
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
                            cell.possible_values = possible_values
                            self.squares_unsolved += 1

    """
    looks at the possible values of the other cells in the unique sets and calculates any that could be shared between 2 cells
    """
    def complex_solve(self):
        for (row_index, row) in enumerate(self.board.board):
            for (column_index, cell) in enumerate(row):
                if not isinstance(cell, Cell):
                    raise TypeError("not a cell")
                square_index = BoardHelper.get_square_index(column_index, row_index)
                square = Square(self.board.get_3_by_3_square(square_index))
                unique_sets = [
                    self.board.get_row(row_index),
                    self.board.get_column(column_index),
                    square.get_as_list()
                ]
                print isinstance(unique_sets[2][5],Cell)
                for (k,unique_set) in enumerate(unique_sets):
                    for (j, cell) in enumerate(unique_set):
                        if not isinstance(cell, Cell):
                            raise TypeError("k " + k.__str__() + " not a cell")
                        logger.info(cell.possible_values)
                        #print eachcell.possible_values
                    # todo
                    #for cell in unique_set:
                        #if cell is not None:




