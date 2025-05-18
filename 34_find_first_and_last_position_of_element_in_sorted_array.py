from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Binary Search]

    Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity: O(log n)
        Space complexity: O(n)
        """

        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1

            return idx

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)

        return [left, right]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
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
