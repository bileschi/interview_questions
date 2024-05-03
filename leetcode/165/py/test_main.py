import main
import unittest

class TestMain(unittest.TestCase):
    def test_normal_cases(self):
        s = main.Solution()
        self.assertEqual(0, s.compareVersion("1.01", "1.001"))
        self.assertEqual(0, s.compareVersion("1.0", "1.0.0"))
        self.assertEqual(-1, s.compareVersion("0.1", "1.1"))
        
if __name__ == '__main__':
    unittest.main()