import itertools
from collections import defaultdict


class Solution:
    """
    Grade[Easy]
    Topics[Array]

    Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
    where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

    Constraints:
        1 <= nums.length <= 100
        1 <= nums[i], k <= 100
    """

    def countPairs(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(N^2) - Beats 49.67%
        Space Complexity: O(1) - Beats 32.33%
        """
        counter = 0
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] == nums[j] and i * j % k == 0:
                    counter += 1
        return counter

    def countPairs(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(N^2) worst case - Beats 95.00%
        Space Complexity: O(N) - Beats 12.50%
        """
        d = defaultdict(list)
        counter = 0
        for ind, num in enumerate(nums):
            d[num].append(ind)

        for indexes in d.values():
            for pair in list(itertools.combinations(indexes, 2)):
                if pair[0] * pair[1] % k == 0:
                    counter += 1
        return counter


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
s = Solution()
result = s.countPairs(nums, k)
print(result)
