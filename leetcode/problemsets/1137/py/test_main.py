import unittest
import main

class TestMain(unittest.TestCase):
  def test_edge(self):
    s = main.Solution()
    self.assertEqual(s.tribonacci(0), 0)
    self.assertEqual(s.tribonacci(1), 1)
    self.assertEqual(s.tribonacci(2), 1)

  def test_first_non_edge(self):
    s = main.Solution()
    self.assertEqual(s.tribonacci(3), 2)
    self.assertEqual(s.tribonacci(4), 4)

  def test_larger(self):
    s = main.Solution()
    self.assertEqual(s.tribonacci(25), 1389537)

if __name__ == '__main__':
  unittest.main()