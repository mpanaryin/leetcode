import copy
from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Math, Matrix]

    Do not return anything, modify matrix in-place instead.
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Time complexity: O(n²)
        Space complexity: O(n²)
        """
        matrix.reverse()
        reversed_matrix_copy = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = reversed_matrix_copy[j][i]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Time complexity: O(n²)
        Space complexity: O(1)
        """
        n = len(matrix)

        # Транспонируем матрицу (swap matrix[i][j] с matrix[j][i])
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Реверс каждой строки
        for row in matrix:
            row.reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

s = Solution()
s.rotate(matrix=matrix)
