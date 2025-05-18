from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Hash Table, Matrix]

    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

    You must do it in place.
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Time complexity: O(m × n)
        Space complexity: O(m + n)
        """
        i_set = set()  # rows with 0
        j_set = set()  # columns with 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    i_set.add(i)
                    j_set.add(j)

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i in i_set or j in j_set:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Time complexity: O(m × n)
        Space complexity: O(1)
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

s = Solution()
s.setZeroes(matrix)
print(matrix)
