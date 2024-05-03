import main
import unittest

class TestMain(unittest.TestCase):
    def test_normal_cases(self):
        s = main.Solution()
        self.assertTrue(s.isPalindrome(1))
        self.assertTrue(s.isPalindrome(121))
        self.assertFalse(s.isPalindrome(12))
        self.assertFalse(s.isPalindrome(-121))

    def test_no_string_cases(self):
        s = main.Solution()
        self.assertTrue(s.isPalindromeNoString(1))
        self.assertTrue(s.isPalindromeNoString(121))
        self.assertFalse(s.isPalindromeNoString(12))
        self.assertFalse(s.isPalindromeNoString(-121))
        
if __name__ == '__main__':
    unittest.main()