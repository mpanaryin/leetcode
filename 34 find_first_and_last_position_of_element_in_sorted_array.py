from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in non-decreasing order,
        find the starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.
        """
        indexes = []
        for i, num in enumerate(nums):
            if num == target:
                indexes.append(i)
        if not indexes:
            return [-1, -1]
        return [indexes[0], indexes[-1]]


s = Solution()
result = s.searchRange()
print(result)