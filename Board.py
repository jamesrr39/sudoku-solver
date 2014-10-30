__author__ = 'james'


class Board:

    board = []

    def __init__(self):

        for rows in range(0, 8, 1):
            self.board.append([None, None, None, None, None, None, None, None, None])
            self.fill_in()

    def fill_in(self):
        return

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
        # todo - columns and 3x3 groups

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
