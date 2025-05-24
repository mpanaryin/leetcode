from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[String, Dynamic Programming, Backtracking]

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time complexity: O(2ⁿ) (tight bound: O(4ⁿ / √n))
        Space complexity: O(4ⁿ / √n)

        ℹ️ Это количество каталановых чисел, которые описывают число правильных скобочных последовательностей.
        """
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack('', 0, 0)
        return result




s = Solution()
print(s.generateParenthesis(3))
