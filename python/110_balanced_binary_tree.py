from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Easy]
    Topics[Tree, Depth-First Search, Binary Tree]

    Given a binary tree, determine if it is height-balanced.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(h)
        """
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1
