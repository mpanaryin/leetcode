from functools import cache


class Solution:
    """
    Grade[Medium]
    Topics[Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree]

    Given an integer n, return the number of structurally unique BST's
    (binary search trees) which has exactly n nodes of unique values from 1 to n.
    """

    def numTrees(self, n: int) -> int:
        """
        Time complexity: O(n²)
        Space complexity: O(n)
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


class Solution2:

    @cache
    def numTrees(self, n: int) -> int:
        """
        Функция использует рекурсию для вычисления количества уникальных бинарных деревьев с n узлами.
        Она делает это, перебирая все возможные корневые узлы, от 1 до n, и для каждого корневого узла вычисляет
        количество уникальных левых и правых поддеревьев, а затем умножает их количество, так как количество
        всех возможных деревьев с заданным корнем будет равно произведению количества левых и правых поддеревьев.

        Формула для количества уникальных бинарных деревьев с n узлами включает в себя суммирование для всех возможных
        корневых узлов:
        numTrees(n) = sum(numTrees(i-1) * numTrees(n-i) for i in range(1, n+1))

        Где i - это номер корневого узла, и мы рекурсивно вызываем numTrees для левого поддерева
        с i-1 узлами и для правого поддерева с n-i узлами. Затем мы умножаем результаты этих рекурсивных вызовов
        и суммируем результаты для всех возможных корневых узлов.

        Time complexity: O(n²)
        Space complexity: O(n)
        """
        if n <= 1: return 1
        return sum(self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1))
