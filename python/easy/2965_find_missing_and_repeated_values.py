class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Math, Matrix]

    You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2].
    Each integer appears exactly once except a which appears twice and b which is missing.
    The task is to find the repeating and missing numbers a and b.

    Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

    Constraints:

    2 <= n == grid.length == grid[i].length <= 50
    1 <= grid[i][j] <= n * n
    For all x that 1 <= x <= n * n there is exactly one x that is not equal to any of the grid members.
    For all x that 1 <= x <= n * n there is exactly one x that is equal to exactly two of the grid members.
    For all x that 1 <= x <= n * n except two of them there is exatly one pair of i, j
    that 0 <= i, j <= n - 1 and grid[i][j] == x.
    """

    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)

        Создадим список длины n*n+1 с пустыми значениями и будем его заполнять значениями из grid.
        Так как всё будет отсортировано, то пустое значение - это пропуск,
        а не соответствие индекса - это дойное значение.
        """
        doubled = missing = None
        dp = [0] * (len(grid) * len(grid) + 1)
        for i in grid:
            for j in i:
                dp[j] += j

        for i, num in enumerate(dp):
            if i > num:
                missing = i
            elif i < num:
                doubled = i

            if missing and doubled:
                break

        return [doubled, missing]


grid1 = [[1, 3], [2, 2]]
grid2 = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
grid3 = [[2, 2], [3, 4]]
s = Solution()
result = s.findMissingAndRepeatedValues(grid3)
print('result', result)
