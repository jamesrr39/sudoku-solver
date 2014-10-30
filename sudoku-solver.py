__author__ = 'james'

from Cell import Cell

a = Cell(9)
b = Cell(None)

print a.get_is_mutable()
print b.get_is_mutable()

from Board import Board
from mocks import BoardMocks as BoardMocks

board = Board(BoardMocks.get_board_mock())
board.print_board()