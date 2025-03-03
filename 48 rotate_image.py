import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.
        """
        matrix.reverse()
        reversed_matrix_copy = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = reversed_matrix_copy[j][i]


matrix = [[1,2,3],[4,5,6],[7,8,9]]


s = Solution()
s.rotate(matrix=matrix)

