# Tests for leetcode problem 1233

import main
import unittest

class T(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertCountEqual(s.removeSubfolders([]), [])
        self.assertCountEqual(s.removeSubfolders(["/a/b", "/a"]), ["/a"])
    
    def test_prefix(self):
        self.assertTrue(main.a_is_prefix_of_b(["", "a"], ["", "a", "b"]))


if __name__ == '__main__':
    unittest.main()
