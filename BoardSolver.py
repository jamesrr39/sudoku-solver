__author__ = 'james'

from BoardIteration import BoardIteration
import logging

logger = logging.getLogger("BoardSolver")


def solve(board):
    iteration = 0
    is_unsolved = True
    while is_unsolved is True:
        iteration += 1
        board_iteration = BoardIteration(board)
        board_iteration.simple_solve()
        board = board_iteration.board
        logger.info("iteration #" + iteration.__str__())
        logger.info("squares solved: " + board_iteration.squares_solved.__str__())
        logger.info("squares unsolved: " + board_iteration.squares_unsolved.__str__())
        logger.debug("\n" + board.to_string())
        if board_iteration.squares_solved is 0:
            logger.warn("unsolved after " + iteration.__str__() + " iterations")
            board_iteration.complex_solve()
            return False
        if board_iteration.squares_unsolved is 0:
            is_unsolved = False
    logger.info("solved in " + iteration.__str__() + " iterations")
    return True
