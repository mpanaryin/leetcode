from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Medium]
    Topics[Tree, Depth-First Search, Binary Search Tree, Binary Tree]

    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(h)
        """

        def is_valid_node(node, min_val, max_val):
            if not node:
                return True  # Пустое поддерево считается допустимым BST

            if min_val is not None and node.val <= min_val:  # Проверяется только для правых
                return False
            if max_val is not None and node.val >= max_val:  # Проверяется только для левых
                return False

            return (is_valid_node(node.left, min_val, node.val) and
                    is_valid_node(node.right, node.val, max_val))

        return is_valid_node(root, None, None)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(8, TreeNode(9), TreeNode(7)))
s = Solution()
print(s.isValidBST(root))
