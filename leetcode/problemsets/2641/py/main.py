# Solution to leetcode problem 2641
#
#
# Given the root of a binary tree, replace the value of each node in the tree
# with the sum of all its cousins' values.
#
# Two nodes of a binary tree are cousins if they have the same depth with
# different parents.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from dataclasses import dataclass
from typing import Dict, List, Optional
from collections import defaultdict

@dataclass
class TreeNode:
    val: int = 0
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

DBPRINT = False

def dbprint(*args, **kwargs):
    if DBPRINT:
        print(*args, **kwargs)
    else:
        pass

def sum_at_depth(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    sums = defaultdict(int)
    _sum_at_depth_helper(root, 0, sums)
    max_depth = max(sums.keys())
    l = [0] * (max_depth + 1)
    for k in sums.keys():
        l[k] = sums[k]
    return l


def _sum_at_depth_helper(root: Optional[TreeNode], this_depth: int, sums: Dict[int, int]):
    if root is None:
        return
    sums[this_depth] += root.val
    if root.left:
        _sum_at_depth_helper(root.left, this_depth+1, sums)
    if root.right:
        _sum_at_depth_helper(root.right, this_depth+1, sums)


class Solution_too_much_memory:
    # Note that an inplace version of this is also works, but still fails the
    # memory boundary.  The issue is probably with the number of recursive calls
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Given the root of a binary tree, replace the value of each node in the tree
        # with the sum of all its cousins' values.
        #
        # Two nodes of a binary tree are cousins if they have the same depth with
        # different parents.
        #
        # The value at each node should be the sum of the values at the same depth
        # minus its own value and it's siblings' values.
        if root == None:
            return None
        new_root = TreeNode(0)
        sad = sum_at_depth(root)
        dbprint(f'{sad=}')
        def _replaceValueInTreeHelper(old_root: TreeNode, new_root: TreeNode, sad: List[int]) -> None:
            if old_root == None:
                return
            dbprint(f"at {old_root.val=}")
            # Handles the two children of this root.  Replaces thier values
            # with the sum at their depth minus their sums.
            if old_root.left == None and old_root.right == None:   
                # This node has no children - there is nothing to do.
                return
            new_kids_val = sad[1]
            left_kid_val = 0
            right_kid_val = 0
            # Compute kids value
            if old_root.left:
                left_kid_val = old_root.left.val
            if old_root.right: 
                right_kid_val = old_root.right.val
            new_kids_val = sad[1] - left_kid_val - right_kid_val
            if old_root.left:
                dbprint(f" minting new left {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}")
                new_root.left = TreeNode(new_kids_val)
            if old_root.right:
                dbprint(f" minting new right {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}")
                new_root.right = TreeNode(new_kids_val)
            # Kids are handled.  Take care of grandkids.
            _replaceValueInTreeHelper(old_root.left, new_root.left, sad[1:])
            _replaceValueInTreeHelper(old_root.right, new_root.right, sad[1:])
        
        _replaceValueInTreeHelper(root, new_root, sad)
        return new_root


class Solution:
    # Inplace version of the above.  replaces recursion with a stack.
    #
    # Note that in place solutions are more difficult to test as they
    # overwrite the test data with the results.
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Given the root of a binary tree, replace the value of each node in the tree
        # with the sum of all its cousins' values.
        #
        # Two nodes of a binary tree are cousins if they have the same depth with
        # different parents.
        #
        # The value at each node should be the sum of the values at the same depth
        # minus its own value and it's siblings' values.
        if root == None:
            return None
        new_root = root
        root.val = 0
        sad = sum_at_depth(root)
        dbprint(f'{sad=}')
        queue = [(root, 1)]

        def _replaceValueInTreeHelper(old_root: TreeNode, depth: int) -> None:
            if old_root == None:
                return
            dbprint(f"at {old_root.val=}")
            # Handles the two children of this root.  Replaces thier values
            # with the sum at their depth minus their sums.
            if old_root.left == None and old_root.right == None:   
                # This node has no children - there is nothing to do.
                return
            left_kid_val = 0
            right_kid_val = 0
            # Compute kids value
            if old_root.left:
                left_kid_val = old_root.left.val
            if old_root.right: 
                right_kid_val = old_root.right.val
            new_kids_val = sad[depth] - left_kid_val - right_kid_val
            if old_root.left:
                dbprint(f" minting new left {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}")
                old_root.left.val = new_kids_val
                queue.append((old_root.left, depth+1))
            if old_root.right:
                dbprint(f" minting new right {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}")
                old_root.right.val = new_kids_val
                queue.append((old_root.right, depth+1))

        while queue:
            node, depth = queue.pop(0)
            _replaceValueInTreeHelper(node, depth)
        return new_root
