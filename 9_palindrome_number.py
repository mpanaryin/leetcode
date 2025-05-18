class Solution:
    """
    Grade[Medium]
    Topics[Math]

    Given an integer x, return true if x is a palindrome, and false otherwise.
    """
    def is_palindrome(self, x: int) -> bool:
        """
        Time complexity: O(log₁₀ n)
        Space complexity: O(log₁₀ n)
        """
        return str(x) == str(x)[::-1]
