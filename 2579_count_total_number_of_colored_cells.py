class Solution:
    """
    Grade[Medium]
    Topics[Math]

    There exists an infinitely large two-dimensional grid of uncolored unit cells.
    You are given a positive integer n, indicating that you must do the following routine for n minutes:

    At the first minute, color any arbitrary unit cell blue.
    Every minute thereafter, color blue every uncolored cell that touches a blue cell.
    Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

    Constraints:
    1 <= n <= 10^5
    """

    def coloredCells(self, n: int) -> int:
        """
        1. Мы всегда рассматриваем квадрат (1 + (2 * (n - 1))).
        2. На каждой итерации размер закрашенных ячеек увеличивается на 2 и касается граней квадрата.
        Остальная форма остаётся лесенкой.

        Мое решение такое: м
        1. Мы считаем количество ячеек креста по формуле row_count * 2 - 1,
        где row_count текущий размер грани, а минус 1, так как всегда пересечение по центру.
        2. Далее нам необходимо посчитать сколько ячеек добавилось в промежуток между любой из двух граней креста,
        например верхней и левой (назовём их углом). Так как таких угла будет 4, то потом это перемножаем.
        Расчет основан на количестве добавляемых закрашенных ячеек на каждой итерации.
        Начиная с 3ей итерации появляется 1 закрашенная ячейка, а после они увеличиваются на 2 с каждой новой итерацией.
        """
        # Расчет креста
        row_count = (1 + (2 * (n - 1)))
        total = row_count * 2 - 1
        angle_cell_count = 0
        for i in range(1, n + 1):
            # Расчет угла
            if i >= 3:
                # Количество новых ячеек на каждой итерации в рамках одного угла
                angle_cell_count += i - 2
        total += (angle_cell_count * 4)
        return total

    def colored_cells(self, n: int) -> int:
        """
        Идеальное упакованное решение:
        Мы начинаем с одной синей клетки, а затем последовательно добавляем кратные 4:
        сначала 4 × 1, затем 4 × 2, затем 4 × 3, и так далее, продолжая n - 1шаги.
        Это означает, что общее количество следует за суммой:
        1 + (4×1) + (4×2)+...+(4×(n−1))
        """
        return 1 + n * (n - 1) * 2


s = Solution()
result = s.coloredCells(5)
print('result', result)
