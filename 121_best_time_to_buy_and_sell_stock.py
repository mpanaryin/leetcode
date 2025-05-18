import math
from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[Array, Dynamic Programming]

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and
    choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        max_profit = 0
        min_price = math.inf
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
    