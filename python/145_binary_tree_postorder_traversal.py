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

    Given the root of a binary tree, return the postorder traversal of its nodes' values.
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """

        def postorder(node: TreeNode | None, result: list):
            if node is not None:
                postorder(node.left, result)
                postorder(node.right, result)
                result.append(node.val)

        result = []
        postorder(root, result)
        return result


root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
s = Solution()
result = s.postorderTraversal(root)
print(result)
