__author__ = 'james'

from Cell import Cell
import BoardHelper


class Board:

    board = []

    """
    board_list 2D list of arrays of starting grid
    """
    def __init__(self, board_matrix):
        self.board = [[Cell(cell) for cell in row] for row in board_matrix]

    def fill_in(self):
        for (row_index, row) in enumerate(self.board):
            for (column_index, cell) in enumerate(row):
                if cell.value is None:
                    square_index = self.get_square_index(column_index, row_index)
                    possible_values = cell.get_possible_values(row, self.get_column(column_index), self.get_3_by_3_square(square_index))
                    if isinstance(possible_values, list) and len(possible_values) is 1:
                        cell.set_value(possible_values[0])

    def get_column(self, column_index):
        return [item[column_index] for item in self.board]

    def get_row(self, row_index):
        return self.board[row_index]

    @staticmethod
    def get_square_index(x, y):
        y_group = y / 3
        x_group = x / 3
        return (3 * y_group) + x_group


    """
    get 3x3 squares

    index: 0-8 start from top left, go to top right, bottom left, bottom right
    """
    def get_3_by_3_square(self, index):
        square_x_coord = index % 3
        square_y_coord = index / 3
        x_lower = 3 * square_x_coord
        x_higher = x_lower + 3
        y_lower = 3 * square_y_coord
        y_higher = y_lower + 3
        return [row[x_lower:x_higher] for row in self.board[y_lower:y_higher]]


    """
    checks for:
    1. all rows containing from 1-9
    2. all columns containing from 1-9
    3. all 3x3 squares containing from 1-9
    """
    def is_valid(self):
        for row in self.board:
            if BoardHelper.is_set_valid(row) is False:
                return False
        for column_index in range(0, 8):
            if BoardHelper.is_set_valid(self.get_column(column_index)) is False:
                return False
        for square_index in range(0, 8):
            if BoardHelper.is_set_valid(self.get_3_by_3_square(square_index)) is False:
                return False
        return True

    def print_board(self):
        for row in self.board:
            print row
