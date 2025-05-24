from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Medium]
    Topics[Tree, Depth-First Search, Breadth-First Search, Binary Tree]

    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.
    """

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        def traversal(node: TreeNode, level: int):
            if node:
                if level == len(result):
                    result.append(node.val)
                traversal(node.right, level + 1)
                traversal(node.left, level + 1)

        result = []
        traversal(root, 0)
        return result


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
s = Solution()
result = s.rightSideView(root)
print(result)
