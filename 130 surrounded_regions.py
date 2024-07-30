class Solution:
    """
    You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.
    Region: To form a region connect every 'O' cell.
    Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
    A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.
    """

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j):
            """
            Проверяем, есть ли O на краю.
            Если да, то также ищем её соседей и меняем на T (temp)
            """
            try:
                if board[i][j] == 'O':
                    board[i][j] = 'T'
                    dfs(i + 1, j)
                    dfs(i - 1, j)
                    dfs(i, j + 1)
                    dfs(i, j - 1)
            except IndexError:
                pass

        in_row_count = len(board[-1])
        in_column_count = len(board)
        # По горизонтали верх
        for i in range(in_row_count):
            dfs(0, i)
        print('~~~~~')
        # По горизонтали низ
        for i in range(in_row_count):
            dfs(in_column_count - 1, i)
        print('~~~~~')
        # По вертикали лево
        for i in range(in_column_count):
            dfs(i, 0)
        print('~~~~~')
        # По вертикали права
        for i in range(in_column_count):
            dfs(i, in_row_count - 1)

        for i, row in enumerate(board):
            for j, let in enumerate(row):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i, row in enumerate(board):
            for j, let in enumerate(row):
                if board[i][j] == 'T':
                    board[i][j] = 'O'





board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
s = Solution()
s.solve(board)
print(board)
