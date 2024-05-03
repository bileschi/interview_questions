import main
import unittest

class TestMain(unittest.TestCase):
    def test_normal_cases(self):
        s = main.Solution()
        self.assertTrue(s.isPalindrome(1))
        self.assertTrue(s.isPalindrome(121))
        self.assertFalse(s.isPalindrome(12))
        self.assertFalse(s.isPalindrome(-121))
        
if __name__ == '__main__':
    unittest.main()