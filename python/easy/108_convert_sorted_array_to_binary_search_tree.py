from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Easy]
    Topics[Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree]

    Given an integer array nums where the elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Time complexity: O(n)
        Space complexity: O(log n)
        """
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1:])
        )

