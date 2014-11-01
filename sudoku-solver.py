__author__ = 'james'

from Board import Board
from mocks import BoardMocks

board = Board(BoardMocks.get_board_mock())
board.print_board()