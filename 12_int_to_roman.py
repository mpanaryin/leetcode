class Solution:
    """
    Grade[Medium]
    Topics[Hash Table, Math, String]

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
    which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX.
    There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.
    """
    chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'None', 'None']
    roman = ''
    def one_digit_converter(self, digit: int, bot_char, middle_char, top_char):
        print(bot_char, top_char, middle_char)
        if digit <= 3:
            return ''.join([bot_char for i in range(digit)])
        elif digit == 4:
            return f'{bot_char}{middle_char}'
        elif digit <= 8:
            return middle_char + ''.join([bot_char for i in range(digit-5)])
        elif digit == 9:
            return f'{bot_char}{top_char}'

    def int_to_roman(self, num: int) -> str:
        reversed_str_num = str(num)[::-1]
        chars_position = 0
        for num in reversed_str_num:
            self.roman = self.one_digit_converter(
                digit=int(num),
                bot_char=self.chars[chars_position],
                middle_char=self.chars[chars_position + 1],
                top_char=self.chars[chars_position + 2]
            ) + self.roman
            chars_position += 2
        return self.roman


class Solution2:
    def int_to_roman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

