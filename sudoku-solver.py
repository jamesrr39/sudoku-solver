__author__ = 'james'

from Board import Board
from mocks import BoardMocks
import BoardSolver
import logging

log_level = "INFO"

numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % log_level)
logging.basicConfig(level=numeric_level)

board = Board(BoardMocks.get_board_mock())
board.print_board()
print "\n\n"
BoardSolver.solve(board)
print "\n\n"
board.print_board()