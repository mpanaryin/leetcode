from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
        """
        def traversal(node):
            return ([node.val] + traversal(node.left) + traversal(node.right)) if node else [None]

        p_traversal = traversal(p)
        q_traversal = traversal(q)
        if p_traversal == q_traversal:
            return True
        return False


p = TreeNode(1, TreeNode(2), None)
q = TreeNode(1, None, TreeNode(2))

s = Solution()
s.isSameTree(p, q)
