from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Medium]
    Topics[Tree, Breadth-First Search, Binary Tree]

    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
    (i.e., from left to right, then right to left for the next level and alternate between).

    Решение: мы будем проходить просто по дереву и собирать по всем уровням элементы слева направо,
    запоминая, что это за уровень. Всё кладём в elements_dict.
    После проходим по полученному defaultdict и меняем направление элементов, в случае, если
    уровень их нахождения нечетный
    """
    level = 0

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        elements_dict = defaultdict(list)
        elements = []
        self.collector(root, self.level, elements_dict)
        for index, value in elements_dict.items():
            if not index % 2:
                elements.append(value)
            else:
                value.reverse()
                elements.append(value)
        return elements

    def collector(self, root, level, elements_dict):
        if root is None:
            return
        if self.level < level:
            self.level = level
        elements_dict[level].append(root.val)
        self.collector(root.left, level + 1, elements_dict)
        self.collector(root.right, level + 1, elements_dict)
