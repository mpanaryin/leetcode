from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, String, Backtracking, Depth-First Search, Matrix]

    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
    or vertically neighboring. The same letter cell may not be used more than once.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time complexity: O(m × n × 4^L)
        Space complexity: O(L)
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"  # mark as visited

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            board[r][c] = tmp  # backtrack
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        def find_next_letter(row_index, colum_index, letter_index, result):
            if result[0]:
                return True
            to_left = True
            to_right = True
            to_upper = True
            to_down = True
            next_letter_index = letter_index + 1
            if next_letter_index == word_len + 1:
                result[0] = True
                return True

            if row_index == 0:
                # Вверх не ходим
                to_upper = False
            if row_index == board_row_count - 1:
                # Вниз не ходим
                to_down = False
            if colum_index == 0:
                # Влево не ходим
                to_left = False
            if colum_index == board_column_count - 1:
                # Вправо не ходим
                to_right = False

            if to_right:
                if board[row_index][colum_index + 1] == word[letter_index] and \
                        (row_index, colum_index + 1) not in passed_cells[:letter_index - 1]:
                    del passed_cells[letter_index:]
                    passed_cells.append((row_index, colum_index + 1))
                    find_next_letter(row_index, colum_index + 1, next_letter_index, result)

            if to_down:
                if board[row_index + 1][colum_index] == word[letter_index] and \
                        (row_index + 1, colum_index) not in passed_cells[:letter_index - 1]:
                    del passed_cells[letter_index:]
                    passed_cells.append((row_index + 1, colum_index))
                    find_next_letter(row_index + 1, colum_index, next_letter_index, result)

            if to_left:
                if board[row_index][colum_index - 1] == word[letter_index] and \
                        (row_index, colum_index - 1) not in passed_cells[:letter_index - 1]:
                    del passed_cells[letter_index:]
                    passed_cells.append((row_index, colum_index - 1))
                    find_next_letter(row_index, colum_index - 1, next_letter_index, result)

            if to_upper:
                if board[row_index - 1][colum_index] == word[letter_index] and \
                        (row_index - 1, colum_index) not in passed_cells[:letter_index - 1]:
                    del passed_cells[letter_index:]
                    passed_cells.append((row_index - 1, colum_index))
                    find_next_letter(row_index - 1, colum_index, next_letter_index, result)

            return False
        total_chars = sum([len(row) for row in board])
        if total_chars < len(word):
            return False
        result = [False]
        board_row_count = len(board) # Количество строк
        board_column_count = len(board[0]) # Количество столбцов
        first_letter = word[0]
        word_len = len(word)
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == first_letter:
                    print('VALUE: ', value)
                    passed_cells = [(i,j)]
                    if find_next_letter(i, j, 1, result):
                        return True
        return result[0]

board = [["a","a"],["A","A"]]
word = "aaa"

s = Solution()
result = s.exist(board, word)
print(result)