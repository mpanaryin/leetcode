from typing import List


class Solution:
    """
    Grade[Hard]
    Topics[Array, Binary Search, Divide and Conquer]

    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Time complexity: O((m + n) * log(m + n))
        Space complexity: O(m + n)
        """
        new_nums = sorted(nums1+nums2)
        total_len = len(new_nums)
        middle_index = (total_len - 1) // 2
        if total_len % 2 == 0:
            return sum(new_nums[middle_index:middle_index + 2]) / 2
        return new_nums[middle_index]
