from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers, Greedy]

    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains
    the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    """
    def max_area(self, height: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
