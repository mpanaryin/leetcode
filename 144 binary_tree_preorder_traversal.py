from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        Given the root of a binary tree, return the preorder traversal of its nodes' values.
        """
        def preorder(node: TreeNode | None, result: list):
            if node is not None:
                result.append(node.val)
                preorder(node.left, result)
                preorder(node.right, result)

        result = []
        preorder(root, result)
        return result



root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
s = Solution()
result = s.preorderTraversal(root)
print(result)
