import unittest
import main

class TestMain(unittest.TestCase):
    def test_brute_force(self):
        f = main.brute_force
        self.generic_test(f)
    
    def test_v2(self):
        f = main.v2
        self.generic_test(f)
    
    def test_v3(self):
        f = main.v3
        self.generic_test(f)
    
    def test_v4(self):
        f = main.v4
        self.generic_test(f)
    
    def test_v5(self):
        f = main.v5
        self.generic_test(f)
    
    def generic_test(self, f):
        self.assertEqual(f([1], 1), 1)
        self.assertEqual(f([1, 1], 1), 3)
        self.assertEqual(f([1, 2], 1), 2)
        self.assertEqual(f([1,2,1,2,3], 2), 7)
        self.assertEqual(f([1,2,1,3,4], 3), 3)
        self.assertEqual(f([1, 1, 2, 2], 2), 4)

        self.assertEqual(f([], 3), 0)
        N = 100
        big_array_of_ones = [1] * N
        self.assertEqual(f(big_array_of_ones, 1), N * (N+1) / 2)
        self.barbell_test(f)

    def barbell_test(self, f):
        size_1 = 13
        size_2 = 19
        barbell = [1] * size_1
        barbell.append(2)
        barbell.extend([3] * size_2)
        self.assertEqual(f(barbell, 3), size_1 * size_2)


if __name__ == '__main__':
  unittest.main()
