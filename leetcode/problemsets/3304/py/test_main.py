# Tests for leetcode problem 3304

import main
import unittest

class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(s.kthCharacter(5), "b")
        self.assertEqual(s.kthCharacter(10), "c")
    


if __name__ == '__main__':
    unittest.main()
