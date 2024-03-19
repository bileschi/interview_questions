import solution
import unittest

class TestSolution(unittest.TestCase):
  def test_normal_cases(self):
    s = solution.Solution()
    self.assertEqual(s.findMaxLength([0,1]), 2)
    self.assertEqual(s.findMaxLength([0,1,0]), 2)
    self.assertEqual(s.findMaxLength([0,1,0,0,1,1,0]), 6)
    self.assertEqual(s.findMaxLength([0,0,0,1,1,1,0]), 6)

  def test_edge_cases(self):
    s = solution.Solution()
    self.assertEqual(s.findMaxLength([]), 0)
    self.assertEqual(s.findMaxLength([0]), 0)
    self.assertEqual(s.findMaxLength([1]), 0)
    self.assertEqual(s.findMaxLength([0,0,0,0]), 0)


if __name__ == '__main__':
  unittest.main()
