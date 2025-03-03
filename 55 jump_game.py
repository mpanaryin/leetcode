from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.
        """
        max_reach_index = 0
        for i, num in enumerate(nums):
            if max_reach_index == i and num == 0 and i != len(nums) - 1:
                return False
            max_reach_index = max(i + num, max_reach_index)
        return True

nums = [3,2,1,0,4]
s = Solution()
result = s.canJump(nums)
print(result)