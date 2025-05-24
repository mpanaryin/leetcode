from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Medium]
    Topics[Array, Hash Table, Divide and Conquer, Tree, Binary Tree]

    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
    inorder is the inorder traversal of the same tree, construct and return the binary tree.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))  # find root
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])  # рекурсивное построение левых ветвей
            root.right = self.buildTree(preorder, inorder[ind + 1:])  # рекурсивное построение правых ветвей
            return root
