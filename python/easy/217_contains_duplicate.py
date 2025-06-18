from collections import Counter, defaultdict


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Sorting]

    Given an array of integers nums and an integer target, return indices of the two
    numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order.
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n) - Beats 12.46%
        Space complexity: O(n) - Beats 10.02%
        """
        counter = Counter(nums)
        for val in counter.values():
            if val >= 2:
                return True
        return False

    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n) - Beats 14.58%
        Space complexity: O(n) - Beats 10.02%
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] == 2:
                return True
        return False
