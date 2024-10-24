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
from collections import defaultdict, deque


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


DBPRINT = False


def dbprint(*args, **kwargs):
    if DBPRINT:
        print(*args, **kwargs)
    else:
        pass


def sum_at_depth(root: Optional[TreeNode]) -> List[int]:
    # Performs a DFS to fill a list summing the values at each depth.
    # Uses a helper function with a more convenient signature for recursion.
    if root is None:
        return []
    sums = defaultdict(int)
    _sum_at_depth_helper(root, 0, sums)
    max_depth = max(sums.keys())
    l = [0] * (max_depth + 1)
    for k in sums.keys():
        l[k] = sums[k]
    return l


def _sum_at_depth_helper(
    root: Optional[TreeNode], this_depth: int, sums: Dict[int, int]
):
    # Helper function for sum_at_depth
    if root is None:
        return
    sums[this_depth] += root.val
    if root.left:
        _sum_at_depth_helper(root.left, this_depth + 1, sums)
    if root.right:
        _sum_at_depth_helper(root.right, this_depth + 1, sums)


class Solution_too_much_memory:
    # Note that an inplace version of this is also works, but still fails the
    # memory boundary in leetcoade.  The issue not the duplication of the tree,
    # but probably with the number of recursive calls blowing out the stack.
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
        dbprint(f"{sad=}")

        def _replaceValueInTreeHelper(
            old_root: TreeNode, new_root: TreeNode, sad: List[int]
        ) -> None:
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
                dbprint(
                    f" minting new left {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}"
                )
                new_root.left = TreeNode(new_kids_val)
            if old_root.right:
                dbprint(
                    f" minting new right {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}"
                )
                new_root.right = TreeNode(new_kids_val)
            # Kids are handled.  Take care of grandkids.
            _replaceValueInTreeHelper(old_root.left, new_root.left, sad[1:])
            _replaceValueInTreeHelper(old_root.right, new_root.right, sad[1:])

        _replaceValueInTreeHelper(root, new_root, sad)
        return new_root


class Solution2:
    # Inplace version of the above. Replaces recursion with a stack.
    #
    # Note that in place solutions are more difficult to test as they
    # overwrite the test data with the results.
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Given the root of a binary tree, replace the value of each node in the
        # tree with the sum of all its cousins' values.
        #
        # Two nodes of a binary tree are cousins if they have the same depth
        # with different parents.
        #
        # The value at each node should be the sum of the values at the same
        # depth minus its own value and it's siblings' values.
        if root == None:
            return None
        new_root = root
        root.val = 0
        sad = sum_at_depth(root)
        dbprint(f"{sad=}")
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
                dbprint(
                    f" minting new left {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}"
                )
                old_root.left.val = new_kids_val
                queue.append((old_root.left, depth + 1))
            if old_root.right:
                dbprint(
                    f" minting new right {sad[1]=}, {left_kid_val=}, {right_kid_val=}, {new_kids_val=}"
                )
                old_root.right.val = new_kids_val
                queue.append((old_root.right, depth + 1))

        while queue:
            node, depth = queue.pop(0)
            _replaceValueInTreeHelper(node, depth)
        return new_root


class Solution3:
    # Improvement over `Solution` that removes the helper function and
    # some unnecessary variables.
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        q = deque()  # (node, siblings_sum)
        q.append((root, root.val + 0))  # root has zero siblings

        while q:
            # At this point in the code, all the nodes in the queue are at the
            # same depth.
            n_at_this_depth = len(q)
            level_sum = 0
            for node, _ in q:
                level_sum += node.val

            # For every element in this depth:
            #   0. Remove it from the queue.
            #   1. Replace its value with (level_sum - siblings_sum).
            #   2. Calculate the sum of its children.
            #   3. Enclude the children in the queue.
            for _ in range(n_at_this_depth):
                node, siblings_sum = q.popleft()
                dbprint(
                    f"Changing node {node.val=} to {level_sum=} - {siblings_sum=} ({level_sum-siblings_sum})"
                )

                node.val = level_sum - siblings_sum
                children_sum = 0
                if node.left:
                    children_sum += node.left.val
                if node.right:
                    children_sum += node.right.val
                if node.left:
                    dbprint(
                        f" Enquing left node ({node.val=}, {children_sum=})"
                    )
                    q.append((node.left, children_sum))
                if node.right:
                    dbprint(
                        f" Enquing right node ({node.val=}, {children_sum=})"
                    )
                    q.append((node.right, children_sum))
        return root