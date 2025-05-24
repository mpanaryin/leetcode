from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Bit Manipulation, Counting]

    You are given an integer array nums consisting of 2 * n integers.

    You need to divide nums into n pairs such that:

    Each element belongs to exactly one pair.
    The elements present in a pair are equal.
    Return true if nums can be divided into n pairs, otherwise return false.

    Constraints:
    nums.length == 2 * n
    1 <= n <= 500
    1 <= nums[i] <= 500
    """

    def divideArray(self, nums: list[int]) -> bool:
        """
        Time Complexity: O(n) - проходимся 2 раза, первый раз по массиву заполняя dict, второй по dict
        Space Complexity: O(n) - нужно где-то хранить dict с элементами
        """
        counter = Counter(nums)
        for key, value in counter.items():
            if value % 2 != 0:
                return False
        return True


nums = [3, 2, 3, 2, 2, 2]
nums = [1, 2, 3, 4]
s = Solution()
result = s.divideArray(nums)
print(result)
print(nums)
