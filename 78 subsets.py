from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements, return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.
        """
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res


nums = [1,2,3]


s = Solution()
print(s.subsets(nums))
