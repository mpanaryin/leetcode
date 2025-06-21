from collections import Counter


class Solution:
    """
    Grade[Medium]
    Topics[Hash Table, String, Greedy, Sorting, Counting]

    You are given a string word and an integer k.

    We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

    Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.

    Return the minimum number of characters you need to delete to make word k-special.

    Constraints:
        1 <= word.length <= 10^5
        0 <= k <= 10^5
        word consists only of lowercase English letters.
    """

    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Time Complexity: O(n^2), где n максимум 26 - Beats 72.87%
        Space Complexity: O(n), где n максимум 26 - Beats 100%

        Логика решения: ищем символ с наименьшей частотой после операции удаления.
        Затем все символы с частотой менее, чем у этого символа будут удалены.
        Все символы с частотой более чем у символа + k будут уменьшены до этого значения.

        Можем перебрать все вариации построив hash map, так как у нас всего 26 уникальных значений.
        """
        counter = Counter(word)
        result = len(word)
        for i in counter.values():
            deleted = 0
            for j in counter.values():
                # Основная логика выбора "символа с наименьшей частотой после операции удаления"
                if i > j:
                    deleted += j
                elif j > i + k:
                    deleted += j - (i + k)
            result = min(result, deleted)
        return result


s = Solution()
word = "dabdcbdcdcd"
k = 2
result = s.minimumDeletions(word, k)
print(result)
