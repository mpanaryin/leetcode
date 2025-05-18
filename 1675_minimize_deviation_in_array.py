from heapq import heapify, heappop, heappush
from math import inf
from typing import List


class Solution:
    """
    Grade[Hard]
    Topics[Array, Greedy, Heap (Priority Queue), Ordered Set]

    You are given an array nums of n positive integers.

    You can perform two types of operations on any element of the array any number of times:

    If the element is even, divide it by 2.
    For example, if the array is [1,2,3,4], then you can do this operation on the last element,
    and the array will be [1,2,3,2].
    If the element is odd, multiply it by 2.
    For example, if the array is [1,2,3,4], then you can do this operation on the first element,
    and the array will be [2,2,3,4].
    The deviation of the array is the maximum difference between any two elements in the array.

    Return the minimum deviation the array can have after performing some number of operations.
    """

    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Time complexity: O(n * log(max_num))
        Space complexity: O(n)
        """
        heap = [-n if not n % 2 else -2 * n for n in set(nums)]
        heapify(heap)
        min_val = -max(heap)
        ans = inf
        while not heap[0] % 2:
            maxVal = -heappop(heap)
            heappush(heap, -maxVal // 2)
            ans = min(ans, maxVal - min_val)
            min_val = min(min_val, maxVal // 2)
        return min(-heap[0] - min_val, ans)
