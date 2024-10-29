# Tests for leetcode problem 1233

import main
import unittest

class T(unittest.TestCase):
    def test_basic(self):
        s = main.SolutionOneLine()
        #s = main.Solution()
        self.assertCountEqual(s.removeSubfolders([]), [])
        self.assertCountEqual(s.removeSubfolders(["/a/b", "/a"]), ["/a"])

    def test_subtle_suffix(self):
        s = main.SolutionOneLine()
        # self.assertCountEqual(s.removeSubfolders(
        #     ["/a/b/c", "/b/c"]),
        #     ["/a/b/c", "/b/c"])
        self.assertCountEqual(s.removeSubfolders(
            ["/d/b/c/x", "/b/c", "/b/c/x/"]),
            ["/d/b/c/x", "/b/c"])
    
    def test_prefix(self):
        self.assertTrue(main.a_is_prefix_of_b("/ab","/abc/def"))


if __name__ == '__main__':
    unittest.main()
