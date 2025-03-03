from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the subarray with the largest sum, and return its sum.
        time O(n)
        space O(n)
        """
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i - 1] + num, num)
        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
s.maxSubArray(nums)
