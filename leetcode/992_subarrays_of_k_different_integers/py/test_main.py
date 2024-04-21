import unittest
import main

class TestMain(unittest.TestCase):
    def test_brute_force(self):
        f = main.brute_force
        self.generic_test(f)
    
    def test_v2(self):
        f = main.v2
        self.generic_test(f)
    
    def generic_test(self, f):
        self.assertEqual(f([1,2,1,2,3], 2), 7)
        self.assertEqual(f([1,2,1,3,4], 3), 3)
        self.assertEqual(f([], 3), 0)
        N = 100
        big_array_of_ones = [1] * N
        self.assertEqual(f(big_array_of_ones, 1), N * (N+1) / 2)



if __name__ == '__main__':
  unittest.main()
