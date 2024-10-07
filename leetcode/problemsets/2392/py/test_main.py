import main
import unittest

class TestMain(unittest.TestCase):
    def test_tests_run(self):
        s = main.Solution()
        print("Tests run")
        self.assertTrue(True)

    def xtest_valid_conditions(self):
        s = main.Solution()
        self.assertTrue(s.validConditions([], 10))
        self.assertTrue(s.validConditions([[1, 2]], 2))
        self.assertTrue(s.validConditions([[1, 2], [2, 3], [2, 4]], 10))
        self.assertTrue(s.validConditions([[1, 2], [2, 3], [3, 4]], 10))
        self.assertTrue(s.validConditions([[4, 3], [3, 2], [2, 1]], 10))
                        
    def xtest_valid_conditions_bad(self):
        s = main.Solution()
        # condition greater than k
        self.assertFalse(s.validConditions([[1, 3]], 2))
        self.assertFalse(s.validConditions([[3, 1]], 2))
        # condition less than 1
        self.assertFalse(s.validConditions([[1, 2], [0, 2]], 10))
        self.assertFalse(s.validConditions([[1, 2], [2, 0]], 10))
        # bad partial ordering
        self.assertFalse(s.validConditions([[1, 2], [2, 3], [3, 1]], 10))

    def test_valid_conditions_bad(self):
        s = main.Solution()
        self.assertFalse(s.validConditions([[1, 2], [2, 3], [3, 1]], 10))
                        
                        

if __name__ == '__main__':
    unittest.main()
