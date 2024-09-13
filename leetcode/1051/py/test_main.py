import main
import unittest

class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(s.heightChecker([1,1,4,2,1,3]), 3)
        self.assertEqual(s.heightChecker([5,1,2,3,4]), 5)
        self.assertEqual(s.heightChecker([1,2,3,4,5]), 0)
    


if __name__ == '__main__':
    unittest.main()
