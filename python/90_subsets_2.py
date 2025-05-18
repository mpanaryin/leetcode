from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Backtracking, Bit Manipulation]

    Given an integer array nums that may contain duplicates, return all possible
    subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(2ⁿ)
        Space complexity: O(2ⁿ)
        """
        nums.sort()
        result = []

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:  # пропускаем дубликаты
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = ((),)
        for num in nums:
            for x in result:
                result += (x + (num,),)
        result = [list(res) for res in set(result)]
        return result


nums = [1, 2, 2]

s = Solution()
result = s.subsetsWithDup(nums)
print(result)
