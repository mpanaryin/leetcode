class Solution:
    """
    Grade[Easy]
    Topics[Math, Greedy]

    You are given an integer num. You know that Danny Mittal will sneakily remap one of the
    10 possible digits (0 to 9) to another digit.

    Return the difference between the maximum and minimum values Danny can make by remapping exactly one digit in num.

    Notes:

    When Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of d1 in num with d2.
    Danny can remap a digit to itself, in which case num does not change.
    Danny can remap different digits for obtaining minimum and maximum values respectively.
    The resulting number after remapping can contain leading zeroes.
    We mentioned "Danny Mittal" to congratulate him on being in the top 10 in Weekly Contest 326.

    Логика решения: минимальное значение всегда будет достигнуто результатом замены первого символа на 0.
    Чтобы определить максимальное нам придётся проходить по первым элементам и искать место, где нет 9.
    Если мы его находим, то заменяем. Иначе возвращаем изначальное число, которе равно N-ое кол-во "9".
    """

    def min_max_difference(self, num: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        str_num = str(num)
        min_value = str_num.replace(str_num[0], '0')
        max_value = None
        for digit in str_num:
            if digit == '9':
                continue
            for i in reversed(range(0, 10)):
                if i >= int(digit):
                    max_value = str_num.replace(digit, str(i))
                    break
            if max_value is not None:
                break
        if max_value is None:
            max_value = str_num
        result = int(max_value) - int(min_value)
        return result
