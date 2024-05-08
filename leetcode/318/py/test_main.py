import main
import unittest


class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(16, s.maxProduct(words=["abcw","baz","foo","bar","xtfn","abcdef"]))
        self.assertEqual(4, s.maxProduct(words=["a","ab","abc","d","cd","bcd","abcd"]))
        self.assertEqual(0, s.maxProduct(words=["a","aa","aaa","aaaa"]))

if __name__ == "__main__":
    unittest.main()
