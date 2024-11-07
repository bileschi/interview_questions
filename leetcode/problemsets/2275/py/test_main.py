# Tests for leetcode problem 2275

import main
import unittest

class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(s.largestCombination([16,17,71,62,12,24,14]), 4)
        self.assertEqual(s.largestCombination([8, 8]), 2)

if __name__ == '__main__':
    unittest.main()
