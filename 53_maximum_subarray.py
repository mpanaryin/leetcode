from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[String]

    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n) ❗
        """
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i - 1] + num, num)
        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
s.maxSubArray(nums)
