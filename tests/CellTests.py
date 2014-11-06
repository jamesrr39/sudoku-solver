__author__ = 'james'

import unittest
from Cell import Cell


class CellTests(unittest.TestCase):

    def test_cell_eq(self):
        self.assertEqual(Cell(2), Cell(2))
        self.assertNotEqual(Cell(2), Cell(None))
        self.assertEqual(Cell(2), 2)
        self.assertEqual(Cell(None), None)
        self.assertNotEqual(Cell(2), Cell(3))

    def test_get_possible_values(self):
        row = [1, 2, 3, None, None, None, 7, None, 9]
        column = [None, None, None, None, 1, 2, 3, None, 8]
        square = [None, None, None, None, None, None, None, None, 6]
        self.assertListEqual([4, 5],Cell.get_possible_values(row, column, square))



if __name__ is '__main__':
    unittest.main()