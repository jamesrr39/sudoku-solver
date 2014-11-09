__author__ = 'james'

from Board import Board
from mocks import BoardMocks
import BoardSolver


board = Board(BoardMocks.get_board_mock())
board.print_board()
print "\n\n"
print BoardSolver.solve(board)
print "\n\n"
board.print_board()