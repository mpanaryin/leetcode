from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table]

    You are given an integer array nums and an integer k.

    An integer h is called valid if all values in the array that are strictly greater than h are identical.

    For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10,
    but 5 is not a valid integer.

    You are allowed to perform the following operation on nums:

    Select an integer h that is valid for the current values in nums.
    For each index i where nums[i] > h, set nums[i] to h.
    Return the minimum number of operations required to make every element in nums equal to k.
    If it is impossible to make all elements equal to k, return -1.

    Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 100
        1 <= k <= 100
    """

    def minOperations(self, nums: list[int], k: int) -> int:
        """Первое решение, думал что количество элементов влияет на количество операций"""
        if k > min(nums):
            return -1
        result = 0
        counter = Counter(nums)
        for num in reversed(sorted(counter)):
            if num != k:
                result += 1
        return result

    def minOperations(self, nums: list[int], k: int) -> int:
        """Второе решение, понял что количество элементов не важно, важно лишь количество уникальных"""
        nums_set = set(nums)
        min_num = min(nums_set)

        if k > min_num:
            return -1

        if min_num == k:
            return len(nums_set) - 1

        return len(nums_set)


nums = [5, 2, 5, 4, 5]
k = 2
s = Solution()
result = s.minOperations(nums, k)
print(result)
