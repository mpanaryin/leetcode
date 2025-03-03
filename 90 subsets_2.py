from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums that may contain duplicates, return all possible
        subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.
        """
        nums.sort()
        result = ((),)
        for num in nums:
            for x in result:
                result += (x + (num,),)
        result = [list(res) for res in set(result)]
        return result


nums = [1,2,2]


s = Solution()
result = s.subsetsWithDup(nums)
print(result)

