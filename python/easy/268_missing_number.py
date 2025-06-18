class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting]

    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    def missingNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n) - Beats 63.85%
        Space complexity: O(n) - Beats 52.11%
        """
        return sum([i for i in range(1, len(nums) + 1)]) - sum(nums)
