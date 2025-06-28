import heapq
from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Sorting, Heap (Priority Queue)]

    You are given an integer array nums and an integer k.
    You want to find a subsequence of nums of length k that has the largest sum.

    Return any such subsequence as an integer array of length k.

    A subsequence is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.

    Constraints:
        1 <= nums.length <= 1000
        -10^5 <= nums[i] <= 10^5
        1 <= k <= nums.length
    """

    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        Time Complexity: O(n log k) - Beats 48.81%
        Space Complexity: O(n) - Beats 32.14%
        """
        result = []
        max_values = heapq.nlargest(k, nums)
        counter = Counter(max_values)
        for num in nums:
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        return result

    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        Time Complexity: O(n log n) - Beats 33.73%
        Space Complexity: O(n) - Beats 12.57%
        """
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        # sort by numerical value in descending order
        vals.sort(key=lambda x: -x[1])
        # select the first k elements and sort them in ascending order by index
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]  # target subsequence
        return res

    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        Time Complexity: O(n log n) - Beats 91.93%
        Space Complexity: O(n) - Beats 54.89%
        """
        # Pair with indices
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        # Sort by value descending
        nums_with_indices.sort(key=lambda x: -x[0])
        # Take top k and sort by original index
        top_k = sorted(nums_with_indices[:k], key=lambda x: x[1])
        # Extract values
        return [num for num, _ in top_k]


s = Solution()
nums = [2, 1, 3, 3]
k = 2

result = s.maxSubsequence(nums, k)
print(result)