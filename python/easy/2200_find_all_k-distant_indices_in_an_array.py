class Solution:
    """
    Grade[Easy]
    Topics[Array, Two Pointers]

    You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums
    for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

    Return a list of all k-distant indices sorted in increasing order.

    Вам дан массив целых чисел nums (с 0-индексацией), а также два целых числа: key и k.
    Определение:
    Индекс i называется k-отдалённым (k-distant), если существует хотя бы один индекс j, такой что:

    1) |i - j| <= k (расстояние между i и j не больше k)
    2) и nums[j] == key (в позиции j находится значение key)

    Ваша задача:
    Вернуть отсортированный список всех k-отдалённых индексов i в порядке возрастания.

    Constraints:
        1 <= nums.length <= 1000
        1 <= nums[i] <= 1000
        key is an integer from the array nums.
        1 <= k <= nums.length
    """

    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        Time Complexity: O(n) - Beats 100%
        Space Complexity: O(n) - Beats 46.56%
        """
        i, j = 0, 0
        length = len(nums)
        result = []
        while j < length:
            if nums[j] == key:
                while i <= j + k and i < length:
                    if abs(i - j) <= k:
                        result.append(i)
                    i += 1
            j += 1
        return result


s = Solution()
nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1

result = s.findKDistantIndices(nums, key, k)
print(result)