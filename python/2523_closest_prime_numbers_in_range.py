import math


class Solution:
    """
    Grade[Medium]
    Topics[Math, Number Theory]

    Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right .
    Both num1 and num2 are prime numbers.
    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
    Return the positive integer array ans = [num1, num2].
    If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value.
    If no such numbers exist, return [-1, -1].

    Constraints:
    1 <= left <= right <= 10^6
    """

    def sieve_of_eratosthenes(self, n: int) -> list[int]:
        """
        Решето Эратосфена - алгоритм создания простых чисел:
        1. Создаётся список чисел от 2 до n.
        2. Первое число (2) считается простым, после чего все его кратные удаляются из списка.
        3. Затем берётся следующее оставшееся число (оно гарантированно простое), и его кратные также вычеркиваются.
        4. Процесс продолжается до тех пор, пока не будут обработаны все числа до n.
        Time complexity: O(n log log n)
        """
        dp = [True] * (n + 1)
        dp[0] = dp[1] = False
        p = 2
        # Текущий цикл удалит все не простые числа
        while p * p <= n:
            if dp[p]:
                for i in range(p * p, n + 1, p):
                    dp[i] = False
            p += 1
        return [i for i, prime in enumerate(dp) if prime]

    def closestPrimes(self, left: int, right: int) -> list[int]:
        nums = self.sieve_of_eratosthenes(right)
        smallest_int = math.inf
        smallest_d: dict[int, tuple[int, int]] = {}
        for i in range(len(nums) - 1):
            if nums[i] >= left:
                res = nums[i + 1] - nums[i]
                if smallest_int > res:
                    smallest_int = res
                    smallest_d[res] = (nums[i], nums[i + 1])
        return smallest_d.get(smallest_int, (-1, -1))


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
r = s.closestPrimes(84084, 407043)
print(r)
