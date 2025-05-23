# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Easy]
    Topics[Tree, Depth-First Search, Breadth-First Search, Binary Tree]
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.
    """
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(h)
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
