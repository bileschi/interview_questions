import main
import unittest


class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(
            6,
            s.findSpecialInteger([1,2,2,6,6,6,6,7,10]))
        self.assertEqual(
            1,
            s.findSpecialInteger([1, 1]))



if __name__ == "__main__":
    unittest.main()
