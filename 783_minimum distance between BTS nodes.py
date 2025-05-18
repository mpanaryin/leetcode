import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Easy]
    Topics[Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree]

    Given the root of a Binary Search Tree (BST),
    return the minimum difference between the values of any two different nodes in the tree.
    """
    pre = -math.inf
    res = math.inf

    def minDiffInBST(self, root: Optional[TreeNode]) -> float:
        """
        Опишу этот алгоритм: мы проходим по левым узлам до конечного.
        Дойдя до конечного, мы с конца начинаем выполнять оценку узлов (так работает рекурсия).
        Тут же после оценки мы залетаем в правый узел и оцениваем его тем же алгоритмом
        """
        print('Мы начали c root: {}'.format(root.val if root else None))
        if root is None:
            return

        self.minDiffInBST(root.left)
        # evaluate and set the current node as the node previously evaluated
        print(f'Минимум между {self.res} и {root.val} - {self.pre}')
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        print('root val: ', root.val)
        print("self.res: ", self.res)
        print("self.pre: ", self.pre)
        print('~~~~~~')

        self.minDiffInBST(root.right)
        return self.res


root = TreeNode(90, TreeNode(69, TreeNode(49, None, TreeNode(52)), TreeNode(89)))

s = Solution()
result = s.minDiffInBST(root=root)
print(result)
