# Tests for leetcode problem 2684

import main
import unittest

class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(s.maxMoves([[1, 1], [1, 1]]), 0)
        self.assertEqual(s.maxMoves([[1, 2], [1, 2]]), 1)
        self.assertEqual(s.maxMoves([[1, 2], [1, 1]]), 1)

    def test_ex_1(self):
        s = main.Solution()
        self.assertEqual(s.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]), 3)

    def test_ex_2(self):
        s = main.Solution()
        self.assertEqual(s.maxMoves([[3,2,4],[2,1,9],[1,1,7]]), 0)

    def test_ex_3(self):
        s = main.Solution()
        self.assertEqual(s.maxMoves([[ 2, 4, 3, 5],
                                     [ 5, 4, 9, 3],
                                     [ 3, 4, 2,11],
                                     [10, 9,13,15]]), 3)

if __name__ == '__main__':
    unittest.main()
