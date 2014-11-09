__author__ = 'james'

"""
test that a set has all unique values and doesn't contain None
"""


def is_set_valid(cell_set, allow_none):
    if None in cell_set and allow_none is False:
        return False
    for index, cell in enumerate(cell_set):
        if not (cell_set.count(cell) is 1 or (cell is None and allow_none is True)):
            return False
        return True

def get_square_index(x, y):
    y_group = y / 3
    x_group = x / 3
    return (3 * y_group) + x_group