from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according
        to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
        """
        def elements_checker(nums: list):
            for num, count in Counter(nums).items():
                if num != '.' and count != 1:
                    return False
            return True

        sqr1 = []
        sqr2 = []
        sqr3 = []
        for i in range(9):
            row_nums = []
            column_nums = []
            for j in range(9):  # Проверка столбцов
                row_num = board[i][j] # Заполняем строки
                column_num = board[j][i] # Заполняем столбцы
                if row_num != '.':
                    row_nums.append(row_num)
                if column_num != '.':
                    column_nums.append(column_num)

            if not elements_checker(row_nums) or not elements_checker(column_nums):
                return False

            if len(sqr1) < 9:
                sqr1.extend(board[i][:3])
            else:
                if not elements_checker(sqr1):
                    return False
                sqr1 = board[i][:3]

            if len(sqr2) < 9:
                sqr2.extend(board[i][3:6])
            else:
                if not elements_checker(sqr2):
                    return False
                sqr2 = board[i][3:6]

            if len(sqr3) < 9:
                sqr3.extend(board[i][6:9])
            else:
                if not elements_checker(sqr3):
                    return False
                sqr3 = board[i][6:9]
        if not (elements_checker(sqr1) and elements_checker(sqr2) and elements_checker(sqr3)):
            return False

        return True


class Solution2:
    def isValidSudoku(self, board):
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)

board = [
    [".",".",".",".",".",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    ["9","3",".",".","2",".","4",".","."],
    [".",".","7",".",".",".","3",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".","3","4",".",".",".","."],
    [".",".",".",".",".","3",".",".","."],
    [".",".",".",".",".","5","2",".","."]]
s = Solution()
result = s.isValidSudoku(board)
print(result)
