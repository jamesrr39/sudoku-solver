__author__ = 'james'

from Cell import Cell

a = Cell(9)
b = Cell(None)

print a.get_is_mutable()
print b.get_is_mutable()

from Board import Board

board = Board()
board.print_board()