# Tests for leetcode problem 2641

import main
import unittest
from main import TreeNode
from typing import Optional

two = TreeNode(2)
three = TreeNode(3)
one_two_three = TreeNode(1, two, three)

def equal_trees(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
    if tree1 is None or tree2 is None:
        return tree2 is None and tree1 is None
    if tree1.val != tree2.val:
        # print(tree1.val, tree2.val)
        return False
    return equal_trees(tree1.left, tree2.left) and equal_trees(tree1.right, tree2.right)

input_one = TreeNode(5, 
                     TreeNode(4, TreeNode(1), TreeNode(10)),
                     TreeNode(9, None, TreeNode(7)))
output_one = TreeNode(0, 
                     TreeNode(0, TreeNode(7), TreeNode(7)),
                     TreeNode(0, None, TreeNode(11)))

input_two = TreeNode(3, TreeNode(1), TreeNode(2))
output_two = TreeNode(0, TreeNode(0), TreeNode(0))

input_three = TreeNode(33, 
                     TreeNode(37, None, None),
                     TreeNode(42, None, TreeNode(46)))

output_three = TreeNode(0, 
                     TreeNode(0, None, None),
                     TreeNode(0, None, TreeNode(0)))


class TestMain(unittest.TestCase):
    def test_equal_trees(self):
        self.assertTrue(equal_trees(None, None))
        self.assertTrue(equal_trees(one_two_three, one_two_three))
        self.assertFalse(equal_trees(one_two_three, two))
        self.assertFalse(equal_trees(two, one_two_three))
        self.assertTrue(equal_trees(input_one, input_one)) 


    def test_sum_at_depth(self):
        self.assertEqual(main.sum_at_depth(None), [])
        self.assertEqual(main.sum_at_depth(three), [3])
        self.assertEqual(main.sum_at_depth(one_two_three), [1, 5])


    def test_replace_value_in_tree_edges(self):
        s = main.Solution_too_much_memory()
        self.assertTrue(equal_trees(s.replaceValueInTree(None), None))
        self.assertTrue(equal_trees(s.replaceValueInTree(TreeNode(1)), TreeNode(0)))

    def test_replace_value_in_tree__case_1(self):
        s = main.Solution_too_much_memory()
        self.assertTrue(equal_trees(s.replaceValueInTree(input_one), output_one))

    def test_replace_value_in_tree__case_2(self):
        s = main.Solution_too_much_memory()
        self.assertTrue(equal_trees(s.replaceValueInTree(input_two), output_two))

    def test_replace_value_in_tree__case_3(self):
        s = main.Solution_too_much_memory()
        self.assertTrue(equal_trees(s.replaceValueInTree(input_three), output_three))

if __name__ == '__main__':
    unittest.main()
