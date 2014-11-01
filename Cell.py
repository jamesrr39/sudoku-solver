__author__ = 'james'


class Cell:

    mutable = False
    value = None

    def __init__(self, value):
        if value is None:
            self.mutable = True

    def get_is_mutable(self):
        return self.mutable

    def set_value(self, value):
        if self.mutable is True:
            self.value = value
            return True
        else:
            return False

    def __str__(self):
        return self.value + "a"