__author__ = 'james'


class Board:

    board = []

    """
    board_list 2D list of arrays of starting grid
    """
    def __init__(self, board_matrix):
        self.board = board_matrix


    def fill_in(self):
        # todo
        return

    def get_column(self, column_index):
        return [item[column_index] for item in self.board]

    """
    get 3x3 squares

    index: start from top left, go to top right, bottom left, bottom right
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
            if self.is_set_valid(row) is False:
                return False
        for column_index in range(0, 8):
            if self.is_set_valid(self.get_column(column_index)) is False:
                return False
        for square_index in range(0, 8):
            if self.is_set_valid(self.get_3_by_3_square(square_index)) is False:
                return False
        return True

    """
    test that a set has all unique values and doesn't contain None
    """
    @staticmethod
    def is_set_valid(set):
        print set
        if None in set:
            return False
        for index, cell in enumerate(set):
            if set.count(cell) > 1:
                return False
            return True

    def print_board(self):
        for row in self.board:
            print row
