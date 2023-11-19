from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Given the root of a binary tree and an integer targetSum,
        return true if the tree has a root-to-leaf path such that adding up all the values
        along the path equals targetSum.

        A leaf is a node with no children.
        """
        def path_sum(node: TreeNode, current_sum: int = 0):
            if node and not self.result:
                if not node.left and not node.right:
                    if targetSum == current_sum + node.val:
                        self.result = True
                if node.left:
                    path_sum(node.left, current_sum + node.val)
                if node.right:
                    path_sum(node.right, current_sum + node.val)

        self.result = False
        path_sum(root)
        return self.result


s = Solution()
result = s.hasPathSum(
    root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))),
    targetSum=27
)
print(result)



