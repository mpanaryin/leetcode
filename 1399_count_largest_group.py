from collections import Counter


class Solution:
    """
    Grade[Easy]

    You are given an integer n.

    Each number from 1 to n is grouped according to the sum of its digits.

    Return the number of groups that have the largest size.

    Constraints:
        1 <= n <= 10^4
    """

    def countLargestGroup(self, n: int) -> int:
        """
        Time Complexity: O(N) - Beats 66.25%
        Space Complexity: O(N) - Beats 90.25%
        """
        counter = Counter()
        for num in range(1, n+1):
            total = self._digit_sum(num)
            counter[total] += 1
        max_in_group = max(counter.values())
        return sum([1 for k, v in counter.items() if v == max_in_group])

    def _digit_sum(self, num):
        """
        Вычислит сумму цифр числа
        ЗНАЧИТЕЛЬНО лучше sum([int(x) for x in str(num)])
        """
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total


n = 24
s = Solution()
result = s.countLargestGroup(n)
print(result)
