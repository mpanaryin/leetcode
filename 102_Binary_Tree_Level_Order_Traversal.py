from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal of its nodes' values.
        (i.e., from left to right, level by level).
        """
        def left_to_right_traversal(node: TreeNode | None, current_level: int):
            if node:
                try:
                    level_order[current_level].append(node.val)
                except IndexError:
                    level_order.append([node.val])
            else:
                return
            current_level += 1
            left_to_right_traversal(node.left, current_level)
            left_to_right_traversal(node.right, current_level)

        level_order = []
        left_to_right_traversal(root, 0)
        return level_order


s = Solution()
result = s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(result)





