from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Easy]
    Topics[Stack, Tree, Depth-First Search, Binary Tree]
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        result = []

        def main_check(node):
            if node.left:
                main_check(node.left)
            result.append(node.val)
            if node.right:
                main_check(node.right)

        if root:
            main_check(root)
        return result


def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
