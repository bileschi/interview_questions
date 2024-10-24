# Tests for leetcode problem 0951

import main
import unittest
from main import TreeNode

def tree_from_list(l):
    if not l:
        return None
    root = TreeNode(l[0])
    q = [root]
    i = 1
    while i < len(l):
        node = q.pop(0)
        if l[i] is not None:
            node.left = TreeNode(l[i])
            q.append(node.left)
        i += 1
        if i < len(l) and l[i] is not None:
            node.right = TreeNode(l[i])
            q.append(node.right)
        i += 1
    return root

class TestMain(unittest.TestCase):
    def test_edge(self):
        s = main.Solution()
        self.assertTrue(s.flipEquiv(None, None))
        self.assertFalse(s.flipEquiv(None, TreeNode(0)))    

    def test_example(self):
        s = main.Solution()
        self.assertTrue(
            s.flipEquiv(
                tree_from_list([1,2,3,4,5,6,None,None,None,7,8]),
                tree_from_list([1,3,2,None,6,4,5,None,None,None,None,8,7])))


if __name__ == '__main__':
    unittest.main()
