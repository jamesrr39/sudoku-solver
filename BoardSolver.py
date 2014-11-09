__author__ = 'james'

from BoardIteration import BoardIteration


def solve(board):
    iteration = 0
    is_unsolved = True
    while is_unsolved is True:
        iteration += 1
        board_iteration = BoardIteration(board)
        board_iteration.solve()
        board = board_iteration.board
        print "squares solved: " + board_iteration.squares_solved.__str__()
        print "squares unsolved: " + board_iteration.squares_unsolved.__str__()
        if board_iteration.squares_solved is 0:
            return "unsolved after " + iteration.__str__() + " iterations"
        if board_iteration.squares_unsolved is 0:
            is_unsolved = False
    return "solved in " + iteration.__str__() + " iterations"
