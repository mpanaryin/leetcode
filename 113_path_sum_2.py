from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of
        the node values in the path equals targetSum. Each path should be returned as a list of the node values,
        not node references.

        A root-to-leaf path is a path starting from the root and ending at any leaf node.
        A leaf is a node with no children.
        """
        def path_sum(node: TreeNode, values: list | None = None):
            if node:
                # Создание или дополнение словаря текущей нодой
                if not values:
                    values = [node.val]
                else:
                    values.append(node.val)
                values_right = values.copy()
                # Итоговая проверка, когда мы дошли до leaf
                if not node.left and not node.right:
                    if targetSum == sum(values):
                        self.result.append(values)
                # Рекурсия для заполнения остальных нод
                if node.left:
                    path_sum(node.left, values)
                if node.right:
                    path_sum(node.right, values_right)

        self.result = []
        path_sum(root)
        return self.result


s = Solution()
result = s.pathSum(
    root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))),
    targetSum=27
)
print(result)