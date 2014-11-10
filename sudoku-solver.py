__author__ = 'james'

from Board import Board
from mocks import BoardMocks
import BoardSolver
import logging
import json

log_level = "INFO"


def file_get_contents(file_path):
    file = open(file_path, "r")
    data = file.read()
    file.close()
    return data


def solve_board(board):
    if not isinstance(board, Board):
        raise TypeError("solve_board needs a Board object passed in")
    print "\n" + board.to_string() + "\n"
    BoardSolver.solve(board)
    print "\n" + board.to_string() + "\n"


numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % log_level)
logging.basicConfig(level=numeric_level)

#solve_board(Board(BoardMocks.get_board_mock()))
solve_board(Board(json.loads(file_get_contents('mocks/very-difficult.json'))))

