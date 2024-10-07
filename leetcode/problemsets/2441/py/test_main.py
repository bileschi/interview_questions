import main
import unittest

class TestMain(unittest.TestCase):
    def test_brute(self):
        s = main.Solution()
        self.assertEqual(3, s.findMaxK([-1,2,-3,3]))
        self.assertEqual(7, s.findMaxK( [-1,10,6,7,-7,1]))
        self.assertEqual(-1, s.findMaxK([-10,8,6,7,-2,-3]))


    # def test_v2(self):
    #     s = main.Solution()
    #     f = s.compareV2
    #     self.generic_test(f)

    # def test_v3(self):
    #     s = main.Solution()
    #     f = s.compareV3
    #     self.generic_test(f)

    # def generic_test(self, f):
    #     self.assertEqual(0, f("1.01", "1.001"))
    #     self.assertEqual(0, f("1.0", "1.0.0"))
    #     self.assertEqual(-1, f("0.1", "1.1"))
    #     self.assertEqual(1, f("3.0.4.10", "3.0.4.2"))
    #     self.assertEqual(1, f("1.0.1", "1"))
    #     self.assertEqual(-1, f("1", "1.1"))

if __name__ == '__main__':
    unittest.main()