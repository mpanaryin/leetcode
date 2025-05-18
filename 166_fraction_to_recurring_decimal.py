from decimal import Decimal, getcontext


class Solution:
    """
    Grade[Medium]
    Topics[Hash Table, Math, String]

    Given two integers representing the numerator and denominator of a fraction,
    return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    If multiple answers are possible, return any of them.

    It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
    """

    def max_repeating_period(self, a: int, b: int):
        # Обработка отрицательных чисел
        a = abs(a)
        b = abs(b)
        # Убираем общий делитель числителя и знаменателя
        while b % 2 == 0:
            b //= 2
        while b % 5 == 0:
            b //= 5
        # Если b становится 1, значит период отсутствует
        if b == 1:
            return 0
        # Иначе находим минимальное k, для которого 10^k ≡ 1 (mod b)
        k = 1
        remainder = 10 % b
        while remainder != 1:
            remainder = (remainder * 10) % b
            k += 1

        return k

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        Time complexity: O(k)
        Space complexity: O(k)
        """
        getcontext().prec = 1000000
        numerator = Decimal(numerator)
        denominator = Decimal(denominator)
        result = numerator / denominator
        if numerator % denominator == 0:
            return str(int(result))

        period = self.max_repeating_period(numerator, denominator)
        if period == 0:
            return f"{result:.999999f}".rstrip('0').rstrip('.')

        # Определяем количество знаков после запятой
        integer, remainder = f"{result:.999999f}".split(".")
        for i in range(len(remainder) - 1):
            if remainder[i:i + period] == remainder[i + period:i + period + period]:
                return f'{integer}.{remainder[0:i]}({remainder[i:i + period]})'


n1 = 1
d1 = 2

n2 = 4
d2 = 333

n3 = 2
d3 = 1

n4 = 1
d4 = 17

n5 = 1
d5 = 214748364

n5 = 1
d5 = 2147483648

s = Solution()
result = s.fractionToDecimal(n5, d5)
print(result)
