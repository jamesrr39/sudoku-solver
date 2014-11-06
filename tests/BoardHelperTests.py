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

if __name__ is '__main__':
    unittest.main()