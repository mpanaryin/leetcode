from functools import cache


class Solution:
    """
    Grade[Medium]
    Topics[Array, Dynamic Programming]

    Given a triangle array, return the minimum path sum from top to bottom.

    For each step, you may move to an adjacent number of the row below. More formally,
    if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
    Обязательно к изучению:
    https://leetcode.com/problems/triangle/solutions/2146264/c-python-simple-solution-w-explanation-recursion-dp/
    """
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        @cache
        def dfs(i, j):
            if i == len(triangle):
                return 0

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)

            return min(lower_left, lower_right)

        return dfs(0, 0)


triangle = [[-1], [2, 3], [1, -1, -3]]
s = Solution()
result = s.minimumTotal(triangle)
print(result)
