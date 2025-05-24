from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Hash Table, String, Backtracking]

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations
    that the number could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.

    Логика решения: решение "в тупую". Так как мы знаем что максимум 4 цифры,
    то создадим под каждую N-ое количество списков и просто пройдем по всем, собрав все комбинации
    """
    phone_buttons = {
        1: [],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time complexity: O(3ⁿ × 4ᵐ)
        Space complexity: O(3ⁿ × 4ᵐ)
        """
        abc = []
        result = []
        for digit in digits:
            abc.append(self.phone_buttons.get(int(digit)))

        abc_len = len(abc)
        if len(abc) == 1:
            return abc[0]
        elif abc_len == 2:
            lst1 = abc[0]
            lst2 = abc[1]
            for l1 in lst1:
                for l2 in lst2:
                    result.append(l1 + l2)
        elif abc_len == 3:
            lst1 = abc[0]
            lst2 = abc[1]
            lst3 = abc[2]
            for l1 in lst1:
                for l2 in lst2:
                    for l3 in lst3:
                        result.append(l1 + l2 + l3)
        elif abc_len == 4:
            lst1 = abc[0]
            lst2 = abc[1]
            lst3 = abc[2]
            lst4 = abc[3]
            for l1 in lst1:
                for l2 in lst2:
                    for l3 in lst3:
                        for l4 in lst4:
                            result.append(l1 + l2 + l3 + l4)
        return result


class Solution2:
    """
    Усовершенствуем решение. С предыдущего решения мы понимаем, что нам надо создать рекурсию,
    которая сможет проходить по всем спискам при этом перебирая буквы.

    Это и делаем: проходим по каждой букве, при этом запоминая, какие буквы уже были до этого склеивая строку.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        phone_buttons = {
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        res = []
        if len(digits) == 0:
            return res

        self.dfs(digits, 0, phone_buttons, '', res)
        return res

    def dfs(self, digits, index, phone_buttons, path, res):
        if index >= len(digits):
            return res.append(path)
        string_list = phone_buttons.get(int(digits[index]))  # список букв под номером
        for char in string_list:
            # Начинаем заполнять с первой буквы, прибавляя остальные через рекурсию
            self.dfs(digits, index + 1, phone_buttons, path + char, res)
