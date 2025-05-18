from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[Array, Matrix]

    You are given an m x n integer grid accounts where accounts[i][j]
    is the amount of money the i'th customer has in the j'th bank. Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts.
    The richest customer is the customer that has the maximum wealth.

    Constraints:
    m == accounts.length
    n == accounts[i].length
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100
    """

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Time complexity = O(n * m)
        Space complexity = O(n)
        """
        return max([sum(i) for i in accounts])

    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        """
        Time complexity = O(n * m)
        Space complexity = O(1)
        """
        if not accounts:
            return 0
        maximum = sum(accounts[0])
        for i in accounts:
            if _maximum := sum(i) > maximum:
                maximum = _maximum
        return maximum


accounts1 = [[1, 2, 3], [3, 2, 1]]
accounts2 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

s = Solution()
result = s.maximumWealth2(accounts2)
print(result)
