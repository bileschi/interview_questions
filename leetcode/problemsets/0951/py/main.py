# Solution to leetcode problem 0951

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# Return true if flipping the LR children of graph from root1 can make it
# identical to the graph from root2.
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        # Any of:
        # 1. left-left & right-right
        # 2. left-right & right-left
        return (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.right, root2.right)
        ) or (
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        )
