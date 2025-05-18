from heapq import heappush, heappop
from typing import List


class Solution:
    """
    Grade[Hard]
    Topics[Array, Greedy, Sorting, Heap (Priority Queue)]

    Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
    LeetCode would like to work on some projects to increase its capital before the IPO.
    Since it has limited resources, it can only finish at most k distinct projects before the IPO.
    Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

    You are given n projects where the ith project has a pure profit profits[i] and a minimum
    capital of capital[i] is needed to start it.

    Initially, you have w capital. When you finish a project, you will obtain its pure profit and
    the profit will be added to your total capital.

    Pick a list of at most k distinct projects from given projects to maximize your final capital,
    and return the final maximized capital.

    The answer is guaranteed to fit in a 32-bit signed integer.
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        # heapq is a min heap, but we need a max heap
        # so we will store negated elements
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # push a negated element
                heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            # pop a negated element
            w += -heappop(q)
        return w
