import solution
import unittest

class TestSolution(unittest.TestCase):
    def test_normal_cases(self):
        for input, expected in (
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([-1, 1, 2, -1, -4], [[-1, -1, 2]]),
            ([-2, -1, -1, 0, 1, 1, 2],
             [[-1, -1, 2], [-2, 1, 1],[-1, 0, 1], [-2, 0, 2]]),
            ([0, 0, 0], [[0, 0, 0]]),
            ([0, 0, 0, 0], [[0, 0, 0]])):
            with self.subTest(input=input, expected=expected):
                actual = solution.Solution().threeSum(input)
                self.assertCountEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()