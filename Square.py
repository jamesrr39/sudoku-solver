__author__ = 'james'


from Cell import Cell


class Square:

    square = []

    """
    square: 2D array
    """
    def __init__(self, square):
        validation_result = Square.validate(square)
        if validation_result is True:
            self.square = square
        else:
            raise Exception(validation_result)

    """
     validates the square is a 3x3 square containing 1-9 and none
    """
    @staticmethod
    def validate(square):
        if len(square) is not 3:
            return "a square should have 3 rows"
        for row in square:
            if len(row) is not 3:
                return "a row should have 3 cells"
            for cell in row:
                value = cell.value
                if value is not None and value not in range(1, 10):
                    return "the cell should be None or between 1 and 9 (inclusive). Actual value: " + value.__str__()
        return True

    def get_as_list(self):
        square_list = []
        for row in self.square:
            square_list.extend(row)
        return square_list