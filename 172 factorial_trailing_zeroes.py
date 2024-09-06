import sys
from functools import lru_cache

sys.set_int_max_str_digits(0)

class Solution:
    """
    Given an integer n, return the number of trailing zeroes in n!.

    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
    """
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            """
            Тут мог бы быть такой код:
            return 1 if n == 0 else n * factorial(n - 1)

            Но будет ошибка с лимитом рекурсии
            """
            result = 1
            while n > 0:
                result *= n
                print(result)
                n -= 1
            return result

        num = factorial(n)
        str_num = str(num)
        zeros = 0
        if str_num.endswith('0'):
            for num in reversed(str_num):
                if num == '0':
                    zeros += 1
                else:
                    return zeros
        return zeros

    def trailingZeroes2(self, n: int) -> int:
        """
        The code below presents an Easy Python solution with clear syntax. The algorithm works as follows:

        The numbers of "zeros" in "n!" can be traced by decomposing the multiplication "n * (n-1) * ..."
        into a prime factorization with the format:
        n! = 2^a * 3^b * 5^c, ...
        In this factorization, the number of "zeros" in "n!" would correspond to the highest number of "10's"
        that we can form. Since "10 = 5 * 2", the number of zeros would be "10's = min(a,c) ".

        While we should consider tracking 2^a and 5^c separately, we can note that 50% of integer numbers are
        even (multiples of 2), whereas only 20% are multiples of 5.

        As a result, we can conclude that we add a zero to our factorial every time we multiply by 5...

        Some numbers can multiply by 5 more than once, such as 5^2 = 25 or 5^3 = 125. We can consider these
        cases by adding a loop to account for all multiples of 5^x.
        Since 5^x grows exponentially, we achieve an algorithm with Log(n) time complexity.

        I hope the explanation was helpful. This is a very interesting problem.
        """
        x = 5
        result = 0
        while x <= n:
            result += n // x
            x *= 5
        return result


n = 5
s = Solution()
result = s.trailingZeroes(n)
print(result)