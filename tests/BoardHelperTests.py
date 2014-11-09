__author__ = 'james'

import BoardHelper
import unittest


class BoardHelperTests(unittest.TestCase):

    def test_is_set_valid(self):
        self.assertTrue(BoardHelper.is_set_valid([1, 2, 3, 4, 5, 6, 7, 8, 9], False))
        self.assertFalse(BoardHelper.is_set_valid([2, 2, 3, 4, 5, 6, 7, 8, 9], False))
        self.assertFalse(BoardHelper.is_set_valid([1, 2, 3, 4, 5, None, 7, 8, 9], False))
        self.assertTrue(BoardHelper.is_set_valid([1, 2, 3, 4, 5, None, None, 8, 9], True))
        self.assertTrue(BoardHelper.is_set_valid([2, 9, 3, 4, 5, 6, 7, 8, 1], False))
        self.assertFalse(BoardHelper.is_set_valid([4, 2, 3, 4, 5, 6, 7, 8, 9], False))

    def test_get_square_index(self):
        self.assertEqual(3, BoardHelper.get_square_index(2, 4))
        self.assertEqual(5, BoardHelper.get_square_index(6, 3))
        self.assertEqual(8, BoardHelper.get_square_index(8, 8))

if __name__ is '__main__':
    unittest.main()