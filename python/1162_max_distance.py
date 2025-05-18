from typing import List


class Solution(object):
    """
    Grade[Medium]
    Topics[Array, Dynamic Programming, Breadth-First Search, Matrix]

    Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land,
    find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
    If no land or water exists in the grid, return -1.
    The distance used in this problem is the Manhattan distance:
    the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

    Вся суть решения в том, что мы закрываем вокруг земли всю воду, при этом увеличивая
    расстояние на каждой итерации по всем "землям". Новый проход будет уже по тем землям, которые мы ранее закрасили.
    И так до момента, пока не останется ни одной воды
    """

    def max_distance(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        self.land = []
        self.sea = 0
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        for r in range(self.row_len):
            for c in range(self.col_len):
                if grid[r][c] == 1:
                    self.land.append((r, c))
                else:
                    self.sea += 1
        if not self.land or not self.sea:
            return -1
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
        distance = -1
        while self.land:
            next = []
            while self.land:
                (r, c) = self.land.pop()
                for i, j in direction:
                    # Проходим по каждому направлению (влево, вправо, вниз, вверх)
                    # Каждая координата должна по итогу быть положительной, а также не уходить за
                    # пределы длины строк и столбцов (каждый за свою).
                    # Получившаяся координата должна быть 0, что означает мы нашли воду.
                    if 0 <= r + i < self.row_len and 0 <= c + j < self.col_len and grid[r + i][c + j] == 0:
                        # Закрываем воду землей, добавляя координату в хранилище,
                        # по которой мы будем двигаться, когда закончатся все текущие "земли".
                        grid[r + i][c + j] = 1
                        self.sea -= 1
                        next.append((r + i, c + j))
            distance += 1
            self.land = next
        return distance
