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


"""
get the edge co-ordinates for a given square index
example:
square_index == 3
x_low: 0
x_high: 3
y_low: 3
x_high: 6
(see tests)
"""


def get_square_edge_coordinates(square_index):
    square_x_coord = square_index % 3
    square_y_coord = square_index / 3
    x_lower = 3 * square_x_coord
    x_higher = x_lower + 3
    y_lower = 3 * square_y_coord
    y_higher = y_lower + 3
    return {
        "x_high": x_higher,
        "x_low": x_lower,
        "y_high": y_higher,
        "y_low": y_lower
    };