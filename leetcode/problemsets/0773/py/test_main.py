# Tests for leetcode problem 0773

import main
import unittest

class TestMain(unittest.TestCase):
    def test_basic__eq_num_moves(self):
        s = main.Solution()
        self.assertEqual(s.slidingPuzzle([[1,2,3], [4,0,5]]), 1)
        self.assertEqual(s.slidingPuzzle([[4,1,2], [5,0,3]]), 5)

    def test_no_solution__eq_neg_1(self):
        s = main.Solution()
        self.assertEqual(s.slidingPuzzle([[1,2,3], [5,4,0]]), -1)

    def test_invalid_board__eq_neg_1(self):
        s = main.Solution()
        invalid_boards = [
            [[1,2,3], [4,5,6]],  # too many numbers
            [[1,2,3], [4,5]],    # too few numbers
            [[1,2,0], [4,5,0]],  # too many zeros
            [[1,2], [4,5]],      # invalid board
            [[1,2], [4,5,0]]     # invalid board
        ]
        for board in invalid_boards:
            self.assertEqual(s.slidingPuzzle(board), -1)

    def test_get_possible_moves_1(self):
        start = (1, 2, 3, 0, 4, 5)
        moves = main._get_possible_moves(start)
        expected = [
            (0, 2, 3, 1, 4, 5),
            (1, 2, 3, 4, 0, 5)
        ]
        self.assertCountEqual(moves, expected)

    def test_get_possible_moves_2(self):
        start = (1, 0, 3, 4, 5, 6)
        moves = main._get_possible_moves(start)
        expected = [
            (1, 5, 3, 4, 0, 6),
            (0, 1, 3, 4, 5, 6),
            (1, 3, 0, 4, 5, 6)
        ]
        self.assertCountEqual(moves, expected)

    def test_precompute_states(self):
        states = main._precompute_states()
        # only half the permutations are reachable.
        self.assertEqual(len(states), 360)

if __name__ == '__main__':
    unittest.main()
