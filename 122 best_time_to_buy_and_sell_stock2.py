import math
from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Dynamic Programming, Greedy]

    You are given an integer array prices where prices[i] is the price of a given stock on the i`th day.

    On each day, you may decide to buy and/or sell the stock.
    You can only hold at most one share of the stock at any time.
    However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        prices_length = len(prices)
        current_stock = None
        profit = 0
        for i, price in enumerate(prices):
            # Расчёт для последней итерации
            if i == prices_length - 1:
                if current_stock is not None:
                    profit += price - current_stock
                    return profit
                else:
                    break
            # Определяем какую акцию купить
            if current_stock is None and price < prices[i + 1]:
                current_stock = price
            # Фиксируем прибыль
            if current_stock is not None and price > current_stock and prices[i + 1] < price:
                profit += price - current_stock
                current_stock = None

        return profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]
prices4 = [2, 1, 2, 0, 1]
prices5 = [2, 1, 2, 1, 0, 1, 2]
s = Solution()
result = s.maxProfit(prices5)
print(result)
