from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array]

    Given a circular array nums, find the maximum absolute difference between adjacent elements.

    Note: In a circular array, the first and last elements are adjacent.
    """

    def maxAdjacentDistance(self, nums: list[int]) -> int:
        """
        Time complexity: O(n) - Beats 100%
        Space complexity: O(n) - Beats 11%
        :param nums:
        :return:
        """
        return max([abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)] + [abs(nums[0] - nums[-1])])


s = Solution()
result = s.maxAdjacentDistance([1, 2, 4])
print(result)
