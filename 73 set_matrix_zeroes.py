from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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



matrix = [[1,1,1],[1,0,1],[1,1,1]]

s = Solution()
s.setZeroes(matrix)
print(matrix)