import main
import unittest


class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertListEqual(
            ["Gold Medal","Silver Medal","Bronze Medal","4","5"],
            s.findRelativeRanks([5,4,3,2,1]))
        self.assertListEqual(
            ["Gold Medal","5","Bronze Medal","Silver Medal","4"],
            s.findRelativeRanks([10,3,8,9,4]))



if __name__ == "__main__":
    unittest.main()
