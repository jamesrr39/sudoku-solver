__author__ = 'james'


class Cell:

    mutable = False

    def __init__(self, value):
        if value is None:
            self.mutable = True

    def get_is_mutable(self):
        return self.mutable

