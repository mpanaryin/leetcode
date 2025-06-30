from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Sliding Window, Sorting, Counting]

    We define a harmonious array as an array where the difference
    between its maximum value and its minimum value is exactly 1.

    Given an integer array nums, return the length of its longest
    harmonious subsequence among all its possible subsequences.

    Constraints:
        1 <= nums.length <= 2 * 10^4
        -10^9 <= nums[i] <= 10^9
    """

    def findLHS(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n) - Beats 32.85%
        Space Complexity: O(n) - Beats 5.28%
        """
        counter = Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda x: x[0])
        max_result = 0
        for i in range(len(sorted_counter) - 1):
            if sorted_counter[i + 1][0] - sorted_counter[i][0] <= 1:
                max_result = max(max_result, sorted_counter[i + 1][1] + sorted_counter[i][1])
        return max_result

    def findLHS(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n) - Beats 32.85%
        Space Complexity: O(n) - Beats 5.28%
        """
        counter = Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda x: x[0])
        max_result = 0
        for i in range(len(sorted_counter) - 1):
            if sorted_counter[i + 1][0] - sorted_counter[i][0] <= 1:
                max_result = max(max_result, sorted_counter[i + 1][1] + sorted_counter[i][1])
        return max_result

    def findLHS(self, nums: list[int]) -> int:
        """
        Оптимизированный вариант:
        Time Complexity: O(n) - Beats 68.28%
        Space Complexity: O(n) - Beats 21.92%
        """
        frequency_map = Counter(nums)
        max_result = 0

        for num in frequency_map:
            if num + 1 in frequency_map:
                current_length = frequency_map[num] + frequency_map[num + 1]
                max_result = max(max_result, current_length)

        return max_result

    def findLHS(self, nums: list[int]) -> int:
        """
        Оптимизированный вариант по памяти:
        Time Complexity: O(n) - Beats 27.20%
        Space Complexity: O(n) - Beats 93.48%
        """
        nums.sort()
        j = 0
        max_result = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                max_result = max(max_result, i - j + 1)
        return max_result


s = Solution()
nums = [1, 3, 2, 2, 5, 2, 3, 7]

result = s.findLHS(nums)
print(result)
