# Tests for leetcode problem 0951

import main
import unittest

class TestMain(unittest.TestCase):
    def test_edge(self):
        s = main.Solution()
        self.assertTrue(s.flipEquiv([], []))
    


if __name__ == '__main__':
    unittest.main()
