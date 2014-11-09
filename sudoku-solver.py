__author__ = 'james'

from Board import Board
from mocks import BoardMocks
import BoardSolver


max_iterations = 100

board = Board(BoardMocks.get_board_mock())
board.print_board()
print "\n\n"
BoardSolver.solve(board, max_iterations)
print "\n\n"
board.print_board()