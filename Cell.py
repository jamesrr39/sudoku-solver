__author__ = 'james'


class Cell:

    value = None

    def __init__(self, value):
        self.set_value(value)

    def set_value(self, value):
        if value is not None:
            self.value = value

    @staticmethod
    def get_possible_values(row, column, square):
        possible_values = range(1, 10)
        for unique_set in [row, column, square]:
            for cell in unique_set:
                if cell is not None and cell in possible_values:
                    possible_values.remove(cell)
        return possible_values

    def __getitem__(self):
        return self.value

    def __repr__(self):
        return "N" if self.value is None else self.value.__str__()

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.value == other.value
        else:
            return self.value == other