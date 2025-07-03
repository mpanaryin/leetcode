class Solution:
    """
    Grade[Easy]
    Topics[String]

    Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a
    key for too long, resulting in a character being typed multiple times.

    Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

    You are given a string word, which represents the final output displayed on Alice's screen.

    Return the total number of possible original strings that Alice might have intended to type.

    Constraints:
        1 <= word.length <= 100
        word consists only of lowercase English letters.
    """

    def possibleStringCount(self, word: str) -> int:
        """
        Time Complexity: O(n) - Beats 99.44%
        Space Complexity: O(1) - Beats 31.83%

        Counter начинается с 1, так как возможно не было ошибок при вводе.
        Также мы не учитываем все N-подряд идущих символов, а только N-1,
        так как Alice не могла ввести лишний символ, а могла только ошибиться с количеством, таким образом при вводе
        abccc, возможные варианты abc, abcc, abccc (оригинал)
        """
        counter = 1
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                counter += 1
        return counter


s = Solution()
result = s.possibleStringCount('aaabccc')
print(result)
