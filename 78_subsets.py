from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Backtracking, Bit Manipulation]

    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(2ⁿ × n)
        Space complexity: O(2ⁿ × n)
        """
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res


nums = [1, 2, 3]

s = Solution()
print(s.subsets(nums))
