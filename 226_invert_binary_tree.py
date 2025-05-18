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

    Given the root of a binary tree, invert the tree, and return its root.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
