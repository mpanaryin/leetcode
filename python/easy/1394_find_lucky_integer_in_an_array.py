from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Counting]

    Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

    Return the largest lucky integer in the array. If there is no lucky integer return -1.

    Constraints:
        1 <= arr.length <= 500
        1 <= arr[i] <= 500
    """

    def findLucky(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n) - Beats 100%
        Space Complexity: O(n) - Beats 50.63%
        """
        max_value = -1
        counter = Counter(arr)
        for key, value in counter.items():
            if key == value:
                max_value = max(max_value, key)
        return max_value


arr = [1, 2, 2, 3, 3, 3]
s = Solution()
result = s.findLucky(arr)
print(result)
